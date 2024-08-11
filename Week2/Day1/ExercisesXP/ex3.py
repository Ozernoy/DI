'''
 Exercise 3 : Who’s the song producer?
Instructions
Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


Then, call the sing_me_a_song method. The output should be:

There’s a lady who's sure
all that glitters is gold
and she’s buying a stairway to heaven
'''

class Song:

    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for el in self.lyrics:
            print(el)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
