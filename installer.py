#!/usr/bin/env python3
import os
import sys
import subprocess

def install_required_library():
    try:
        import yt_dlp  # Tenta importar para verificar se está instalada
    except ImportError:
        print("Biblioteca 'yt_dlp' não encontrada. Instalando...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "--break-system-packages"])
            print("Biblioteca 'yt_dlp' instalada com sucesso!")
        except subprocess.CalledProcessError as e:
            print("Erro ao instalar a biblioteca 'yt_dlp':", e)
            sys.exit(1)

def create_launcher():
    # Obtém o caminho absoluto do YTLoader.py
    script_path = os.path.abspath("YTLoader.py")
    if not os.path.exists(script_path):
        print("Arquivo YTLoader.py não encontrado no diretório atual.")
        sys.exit(1)
    
    if os.name == "nt":
        # Para Windows: cria um arquivo em lote (BAT)
        launcher_content = f'@echo off\r\n"{sys.executable}" "{script_path}" %*\r\n'
        # Tenta encontrar uma pasta que esteja no PATH (usaremos a pasta Scripts do Python)
        scripts_dir = os.path.join(os.path.dirname(sys.executable), "Scripts")
        if not os.path.isdir(scripts_dir):
            scripts_dir = os.path.dirname(sys.executable)
        launcher_path = os.path.join(scripts_dir, "YTLoader.bat")
    else:
        # Para sistemas Unix-like (Linux/macOS): cria um script shell
        launcher_content = f'#!/bin/bash\n"{sys.executable}" "{script_path}" "$@"\n'
        # Se o usuário for root, utiliza /usr/local/bin, senão, ~/.local/bin
        if os.geteuid() == 0:
            launcher_dir = "/usr/local/bin"
        else:
            launcher_dir = os.path.expanduser("~/.local/bin")
            os.makedirs(launcher_dir, exist_ok=True)
        launcher_path = os.path.join(launcher_dir, "YTLoader")
    
    try:
        with open(launcher_path, "w", encoding="utf-8") as f:
            f.write(launcher_content)
        if os.name != "nt":
            os.chmod(launcher_path, 0o755)
        print(f"Launcher criado com sucesso em: {launcher_path}")
        print("Agora você pode executar o programa digitando 'YTLoader' no terminal.")
    except Exception as e:
        print("Erro ao criar o launcher:", e)
        sys.exit(1)

def main():
    install_required_library()
    create_launcher()

if __name__ == "__main__":
    main()
