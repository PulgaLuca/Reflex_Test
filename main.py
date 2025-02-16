'''
pip install pygame
pip install pyinstaller
python -m PyInstaller --onefile main.py
'''

import pygame
import random
import time

pygame.init()

# Dimensioni della finestra
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Light Challenge: Bus Driver Reflex Test")

colors = {
    'rosso': (255, 0, 0),
    'giallo': (255, 255, 0),
    'verde': (0, 255, 0)
}

pygame.mixer.init()
sound1 = pygame.mixer.Sound("bell.wav")
sound2 = pygame.mixer.Sound("vibration.wav")

def mostra_pallina(colore):
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, colors[colore], (width//2, height//2), 50)
    pygame.display.flip()

def riproduci_suono(suono):
    screen.fill((0, 0, 0))
    pygame.display.flip()
    suono.play()
    time.sleep(2)  # Durata del suono

def schermo_nero():
    screen.fill((0, 0, 0))
    pygame.display.flip()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scelta = random.choice(['pallina', 'suono'])
        if scelta == 'pallina':
            colore = random.choice(list(colors.keys()))
            mostra_pallina(colore)
            time.sleep(2)  # La pallina è visibile per 2 secondi
            schermo_nero()
            time.sleep(1)  # Ritardo di 1 secondo con schermo nero
        else:
            suono = random.choice([sound1, sound2])
            riproduci_suono(suono)
            time.sleep(1)  # Ritardo di 1 secondo dopo il suono

    pygame.quit()

if __name__ == "__main__":
    main()