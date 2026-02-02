from pitop.miniscreen import Miniscreen
from PIL import Image, ImageDraw
import time
import math

# Initialize the miniscreen
miniscreen = Miniscreen()

# Screen dimensions
width, height = 128, 64

# Function to generate rainbow colors
def rainbow_color(position):
    position = position % 255
    if position < 85:
        return (255 - position * 3, 0, position * 3)
    elif position < 170:
        position -= 85
        return (0, position * 3, 255 - position * 3)
    else:
        position -= 170
        return (position * 3, 255 - position * 3, 0)

# Animation loop
start_time = time.time()
shift = 0

try:
    while time.time() - start_time < 10:  # Run for 10 seconds
        # Create a new image for each frame
        image = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Draw rainbow stripes that shift left
        stripe_width = 10
        for x in range(-stripe_width, width + stripe_width, stripe_width):
            adjusted_x = (x + shift) % (width + stripe_width * 2) - stripe_width
            color_position = ((x + shift) * 255 // (width + stripe_width * 2)) % 255
            color = rainbow_color(color_position)
            draw.rectangle([adjusted_x, 0, adjusted_x + stripe_width, height], fill=color)
        
        # Display the image
        miniscreen.display_image(image)
        
        # Update shift amount for next frame
        shift += 2
        
        # Small delay to control animation speed
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Animation stopped")

# Clear the screen when done
image = Image.new("RGB", (width, height), (0, 0, 0))
miniscreen.display_image(image)
print("Animation complete")