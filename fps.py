import pygame
import time
from collections import deque

pygame.font.init()

class BasicFPS:
    def __init__(self, clock):
        self.clock = clock
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255, 255))
 
    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(),2)), True, (255, 255, 255))
        display.blit(self.text, (0, 0))

class MinMaxFPS:
    def __init__(self, clock):
        self.clock = clock
        self.font = pygame.font.SysFont("Verdana", 20)
        self.fps_values = deque(maxlen=300)  # Assuming 60 FPS, 5 seconds of values.

    def render(self, display):
        current_fps = self.clock.get_fps()
        self.fps_values.append(current_fps)

        if len(self.fps_values) == 300:
            min_fps = min(x for x in self.fps_values if x > 5)
            max_fps = max(self.fps_values)

            fps_text = f"FPS: {round(current_fps, 0)} (Min: {round(min_fps, 0)}, Max: {round(max_fps, 0)})"
            self.text = self.font.render(fps_text, True, (255, 255, 255))
            display.blit(self.text, (0, 0))

class FullFPS:
    def __init__(self, clock):
        self.clock = clock
        self.font = pygame.font.SysFont("Verdana", 16)
        self.fps_values = deque(maxlen=300)  # Assuming 60 FPS, 5 seconds of values.

    def render(self, display):
        current_fps = self.clock.get_fps()
        self.fps_values.append(current_fps)

        if len(self.fps_values) == 300:
            min_fps = min(x for x in self.fps_values if x > 5)
            max_fps = max(self.fps_values)
            avg_fps = sum(self.fps_values) / len(self.fps_values)

            fps_text = f"FPS: {round(current_fps, 0)} (Min: {round(min_fps, 0)}, Max: {round(max_fps, 0)}, Avg: {round(avg_fps, 0)})"
            self.text = self.font.render(fps_text, True, (255, 255, 255))
            display.blit(self.text, (0, 0))