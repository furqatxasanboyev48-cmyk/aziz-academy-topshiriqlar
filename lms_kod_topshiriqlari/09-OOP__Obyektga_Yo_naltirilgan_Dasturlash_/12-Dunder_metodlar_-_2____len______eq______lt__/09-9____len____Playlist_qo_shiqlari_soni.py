class Playlist:
    def __init__(self, songs):
        self.songs = songs 
    def __len__(self):
        return len(self.songs)
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    songs = []
    for _ in range(n):
        song = input().strip()
        if not song:
            raise ValueError
        songs.append(song)    
    print(len(Playlist(songs)))
except ValueError:
    print("BAD")