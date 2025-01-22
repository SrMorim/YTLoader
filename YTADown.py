import yt_dlp

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
        print("Download de áudio concluído!")
    except Exception as e:
        print("Ocorreu um erro:", e)

# Exemplo de uso
url = "https://www.youtube.com/watch?v=r3EbvPCRpSY"  # Substitua com uma URL real do vídeo
baixar_audio(url)