from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save('hello.mp3')
import pygame, time
pygame.init()
pygame.mixer.music.load('hello.mp3')
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.fadeout(5)