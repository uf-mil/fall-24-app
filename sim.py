#👇-----DO NOT EDIT-----👇#
import pygame
import asyncio
import numpy as np
from classes import Topic, Subscriber
#👆-----DO NOT EDIT-----👆#

#👇-----DO NOT EDIT-----👇#
# Initialize pygame window for the simulator
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

DOWN_CAM_TOPIC = Topic("/robot/camera")
DOWN_CAM_PUBLISHER = Publisher(DOWN_CAM_TOPIC)

# Function to draw the path the robot must follow
def draw_path():
    screen.fill(BLUE)  

    pygame.draw.line(screen, ORANGE, (0, 15), (400, 15), 10)
    
    pygame.draw.line(screen, ORANGE, (400, 10), (400, 200), 10)
    
    pygame.draw.line(screen, ORANGE, (400, 200), (600, 400), 10)
    
    pygame.draw.line(screen, ORANGE, (600, 400), (790, 200), 10)
    
    pygame.draw.line(screen, ORANGE, (790, 200), (790, 600), 10)

# Helper function used to update where the robot is in the simulation. This function should be used as the callback for the subscriber to the robot position in the simulation.
async def update_position(position):
    draw_path()
    pygame.display.flip()

    # Sample publisher
    matrix = down_cam_driver(position[0], position[1])
    await DOWN_CAM_PUBLISHER.publish(matrix)
  
    pygame.draw.circle(screen, (255, 0, 0), position, 10)
    pygame.display.flip()

def down_cam_driver(center_x, center_y):
    """
    This function allows us to tap into the simulation and get the colors surrounding the robot. The name of this function is a tribute to how we collect data from our sensors in the lab.
    """
    half_size = 10  # 20x20 matrix, so half size is 10
    matrix = np.zeros((20, 20, 3), dtype=np.uint8)  # Initialize a 20x20 matrix with RGB channels

    for i in range(-half_size, half_size):
        for j in range(-half_size, half_size):
            x = center_x + i
            y = center_y + j
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                matrix[i + half_size, j + half_size] = screen.get_at((x, y))[:3]  # Get the color

    return matrix
#👆-----DO NOT EDIT-----👆#

#🟢----- CODE HERE -----🟢#
# Main function to handle the simulation
async def main():
  # Initialize your topic for robot position.

  # Create a subscriber to robot position and the /robot/camera topic.

  # Start the robot at position (0,15) and have it traverse the course until it reaches the bottom right corner of the screen.
  pass
#🛑----- CODE HERE -----🛑#

#👇-----DO NOT EDIT-----👇#
# Run the Pygame event loop in a separate task
async def pygame_event_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        await asyncio.sleep(0.01)

# Run the Pygame event loop and simulation concurrently
async def run_simulation():
    await asyncio.gather(main(), pygame_event_loop())

try:
    asyncio.run(run_simulation())
except KeyboardInterrupt:
    pass
finally:
    pygame.quit()
#👆-----DO NOT EDIT-----👆#
