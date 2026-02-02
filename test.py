from pitop.miniscreen import Miniscreen
from PIL import Image, ImageDraw
import time

# Initialize the miniscreen
miniscreen = Miniscreen()

# Create a blank image for drawing
image = Image.new("RGB", (128, 64), (0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw the face circle
draw.ellipse((30, 10, 98, 54), outline=(255, 255, 0))

# Draw the eyes
draw.ellipse((45, 20, 55, 30), fill=(255, 255, 255))  # Left eye
draw.ellipse((73, 20, 83, 30), fill=(255, 255, 255))  # Right eye

# Draw pupils
draw.ellipse((48, 23, 52, 27), fill=(0, 0, 0))  # Left pupil
draw.ellipse((76, 23, 80, 27), fill=(0, 0, 0))  # Right pupil

# Draw a smile (arc)
draw.arc((40, 20, 88, 45), 0, 180, fill=(255, 255, 255), width=2)

# Display the image on the miniscreen
miniscreen.display_image(image)

# Keep the image displayed for 10 seconds
time.sleep(10)