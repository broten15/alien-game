import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and make a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen, ai_settings)

    # Main loop for game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
