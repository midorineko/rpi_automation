import pygame
import pygame.camera

pygame.camera.init()
cam = pygame.camera.Camera(0,(640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"last_capture.jpg")