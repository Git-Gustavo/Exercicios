import pygame
def tocar_musicamp3(love):
    pygame.mixer.init()
    pygame.mixer.music.load(love)
    pygame.mixer.music.play()
   
if __name__ == "__main__":
    love = "love.mp3"

tocar_musicamp3(love)

while pygame.mixer.music.get_busy():
    pass