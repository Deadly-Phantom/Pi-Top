from pitop.miniscreen import Miniscreen
from PIL import Image, ImageDraw
import math
import time
import random

# Initialize the miniscreen
miniscreen = Miniscreen()

# Screen dimensions
width, height = 128, 64

def draw_branch(draw, x, y, angle, depth, length):
    """Draw a recursive fractal tree branch"""
    if depth <= 0:
        return
        
    # Calculate end point
    x2 = x + math.cos(math.radians(angle)) * length
    y2 = y + math.sin(math.radians(angle)) * length
    
    # Draw the branch
    draw.line((x, y, x2, y2), fill=255, width=max(1, depth//2))
    
    # Draw smaller branches
    new_length = length * 0.7
    draw_branch(draw, x2, y2, angle - 25, depth - 1, new_length)
    draw_branch(draw, x2, y2, angle + 25, depth - 1, new_length)

def draw_wind_tree(frame):
    """Draw a tree with wind animation effect"""
    # Create a new image for each frame
    image = Image.new("1", (width, height), 0)  # 1-bit black and white
    draw = ImageDraw.Draw(image)
    
    # Wind effect - sway the tree by adjusting the initial angle
    wind_angle = 10 * math.sin(frame * 0.1)
    
    # Draw the tree
    base_x = width // 2
    base_y = height - 5
    draw_branch(draw, base_x, base_y, -90 + wind_angle, 7, 20)
    
    return image

# Animation loop
start_time = time.time()
frame = 0

try:
    while time.time() - start_time < 15:  # Run for 15 seconds
        image = draw_wind_tree(frame)
        miniscreen.display_image(image)
        frame += 1
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("Animation stopped")

# Draw final frame - a fully grown tree
final_image = Image.new("1", (width, height), 0)
draw = ImageDraw.Draw(final_image)
draw_branch(draw, width // 2, height - 5, -90, 9, 20)
miniscreen.display_image(final_image)

print("Animation complete")