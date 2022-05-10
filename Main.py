import Song as s
import User as u
import SongCollection as sc
import UserCollection as uc
try:
    # Apertura Archivos
    songs=open("Songs.csv","r")
    users=open("Users.csv","r")

    # Creación de Objetos SongCollection y UserCollection
    songList=sc.SongCollection()
    userList=uc.UserCollection()

    # Lectura de lineas archivos Songs.csv
    songLine=songs.readline()
    songLine=songs.readline()

    while songLine!="":
        data=songLine.split(";")
        # Creando objetos de tipo Song
        song=s.Song(data[0], data[1], data[2], data[3], int(data[4][:-1]))
        songList.add(song)
        songLine=songs.readline()

    # Lectura de lineas archivos Users.csv
    userLine=users.readline()
    userLine=users.readline()

    while userLine!="":
        # Creando objetos de tipo User
        user=u.User(userLine[:-1])
        userList.add(user)
        userLine=users.readline()

    # Cierre de Archivos
    songs.close()
    users.close()
except:
    print("Error")

print("\n\nLista de Canciones\n")
songList.play()

print("\n\nLista de Usuarios\n")
userList.print()

print("\n\nEliminacion de Usuarios\n")
print(userList.remove("Bruise"))
print(userList.remove("Kenny"))

userList.addUserSong("Lynch", "La bamba", songList)
userList.addUserSong("Lynch", "Jump", songList)
userList.addUserSong("Aspect", "Jump", songList)
userList.addUserSong("Aspect", "Beat It", songList)
userList.addUserSong("Kraken", "Beat It", songList)
userList.addUserSong("Kraken", "Stairway To Heaven", songList)
userList.addUserSong("Psycho", "Hotel California", songList)

print("\n\nAgregando Canciones a Un Usuario Eliminado\n")
userList.addUserSong("Bruise", "Hey Jude", songList)

print("\n\nAgregando Canciones que no Existen\n")
userList.addUserSong("Kraken", "One", songList)

print("\n\nReproduciendo Lista de Canciones de Usuario\n")
userList.playUserList("Kraken")

print("\n\nEliminando Cancion\n")
songList.remove("Beat It", userList)

print("\n\nReproduciendo Lista de Canciones Luego de Eliminación\n")
userList.playUserList("Kraken")