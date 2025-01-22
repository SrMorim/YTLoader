import yt_dlp

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
        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro:", e)

# Exemplo de uso
url = "https://www.youtube.com/watch?v=G0WXGGtqQj4"  # Substitua com uma URL real do vídeo
baixar_video(url)

