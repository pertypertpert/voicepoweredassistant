import pygame
import imgkit
from io import BytesIO
pygame.init()
class displayhtml():
    def htmldisplay(self, x):
        config = imgkit.config(wkhtmltoimage=r'wkhtmltopdf\\bin\\wkhtmltoimage.exe')
        html = f"{x}"
        img = imgkit.from_string(html, False, config=config)
        return img