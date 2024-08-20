import pygame.image


class Photo():
    def __init__(self, screen, path, ini_x, ini_y):
        self.screen = screen
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.centerx = ini_x
        self.rect.centery = ini_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
