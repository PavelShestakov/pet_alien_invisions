import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (self.settings.bg_color)
        self.ship = Ship(self)


    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #отслеживагие событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #отображение последнего прорисованого экрана
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
if __name__=="__main__":
    #создание элемента класса игры и запусск игры
    ai = AlienInvasion()
    ai.run_game()

#249