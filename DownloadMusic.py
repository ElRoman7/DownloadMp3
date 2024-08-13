import os
import yt_dlp
from tkinter import Tk, filedialog

default_path = "D:/Musica/"

def download_video_as_mp3(url, download_path=default_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("El archivo ha sido descargado y convertido a MP3.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def get_download_path():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(initialdir=default_path, title="Selecciona la carpeta de descarga")
    return folder_selected if folder_selected else default_path

if __name__ == "__main__":
    change_path = input(f"¿Quieres descargar los archivos en una ubicación diferente a '{default_path}'? (S/N): ").strip().lower()
    
    if change_path == 's':
        download_path = get_download_path()
    else:
        download_path = default_path

    while True:
        url = input("Introduce la URL del video de YouTube (o escribe 'salir' para terminar): ").strip()
        
        if url.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        download_video_as_mp3(url, download_path)
        
        print("\n---\n")
