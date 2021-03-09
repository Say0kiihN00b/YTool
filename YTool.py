import pytube
from os import system

system("clear")
url = input("Qual video sera instalado?")
yt = pytube.YouTube(url)

print(f"O video {yt.title} esta sendo instalado")
video = yt.streams.first()
video.download()
