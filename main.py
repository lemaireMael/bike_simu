import pygame
from Manager import Manager
import pylab
import time
import matplotlib
matplotlib.use("agg")

import matplotlib.backends.backend_agg as agg

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_s,
    KEYDOWN,
    KEYUP,
    QUIT,
)

speed_list = []
time_list = []

pygame.init()

fig = pylab.figure(dpi=100)
ax = fig.gca()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

manager = Manager()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    stats = manager.handle_actions(pressed_keys)

    times = stats.times
    data = stats.data
    ax.plot(times, data)
    try :
        ax.set_xlim(times[-20], times[-1])
    except IndexError:
        pass

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    surf = pygame.image.fromstring(raw_data, canvas.get_width_height(), "RGB")
    screen.blit(surf, (0, 0))
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()