import yt_dlp
import os
import sys

#Menu
def mainmenu():
     while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
        ┌────────────────────────────────┐
        │░█░█░▀█▀░█░░░█▀█░█▀█░█▀▄░█▀▀░█▀▄│
        │░░█░░░█░░█░░░█░█░█▀█░█░█░█▀▀░█▀▄│
        │░░▀░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀│
        └────────────────────────────────┘
        Link: {url}
        ''')
        option = input("[1]Vídeo + Audio\n[2]Vídeo\n[3]Audio\n[4]Nova URL\n[x]Exit\n>>> ")
        
        if option == "1":
            baixar_video_audio(url)
            break
        elif option == "2":
            baixar_video(url)
            break
        elif option == "3":
            baixar_audio(url)
            break
        elif option == "4":
            novaurl()
            break
        elif option == "x":
            print("bye...")
            break

#Funções
def baixar_video_audio(url):
    if "youtube.com" not in url and "youtu.be" not in url:
        print("URL inválida! Por favor, insira uma URL válida do YouTube.")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Tenta baixar a melhor combinação de vídeo e áudio, ou o melhor único se necessário
        'merge_output_format': 'mp4',          # Formato final do arquivo mesclado
        'outtmpl': '%(title)s.%(ext)s',         # Nomeia o arquivo com o título do vídeo
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        input("Download de vídeo completo (vídeo mesclado com áudio) concluído!")
    except Exception as e:
        input("Ocorreu um erro:", e)
    
    mainmenu()

def baixar_video(url):
    if "youtube.com" not in url and "youtu.be" not in url:
        print("URL inválida! Por favor, insira uma URL válida do YouTube.")
        return
    
    ydl_opts = {
        'format': 'bestvideo',  # Apenas o melhor vídeo disponível
        'outtmpl': '%(title)s.%(ext)s'  # Nomeia o arquivo com o título do vídeo
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        input("Download concluído!")
    except Exception as e:
        input("Ocorreu um erro:", e)
    
    mainmenu()

def baixar_audio(url):
    if "youtube.com" not in url and "youtu.be" not in url:
        print("URL inválida! Por favor, insira uma URL válida do YouTube.")
        return
    
    ydl_opts = {
        'format': 'bestaudio',  # Apenas o melhor áudio disponível
        'outtmpl': '%(title)s.%(ext)s',  # Nomeia o arquivo com o título do vídeo
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Formato do áudio (pode ser mp3, wav, etc.)
            'preferredquality': '192',  # Qualidade do áudio
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        input("Download de áudio concluído!")
    except Exception as e:
        input("Ocorreu um erro:", e)
    
    mainmenu()

def novaurl():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        global url
        
        print("""
        ░█░░░▀█▀░█▀█░█░█
        ░█░░░░█░░█░█░█▀▄
        ░▀▀▀░▀▀▀░▀░▀░▀░▀
        """)
        url = input("Cole o link: ")
        mainmenu()
        break

if __name__ == "__main__":
    #-=INFO=-#
    url = ""
    try:
        url = sys.argv[1]
        mainmenu()
    except Exception:
        novaurl()




