# Pi-Top Projects

A collection of Python scripts for the Pi-Top robot, including line-following navigation and miniscreen animations.

## Scripts

### line-follower.py
Autonomous line-following program using the Pi-Top camera and drive controller. The rover detects an orange line via HSV color filtering and follows it across user-defined cycles, supporting both forward and backward directions.

### rainbow.py
Displays an animated rainbow stripe pattern on the Pi-Top miniscreen for 10 seconds.

### tree.py
Renders an animated fractal tree with a wind-swaying effect on the miniscreen for 15 seconds.

### test.py
Draws a smiley face on the miniscreen for 10 seconds. Useful for verifying the display is working.

## Requirements

- Pi-Top device with miniscreen
- Python 3
- [pi-top SDK](https://github.com/pi-top/pi-top-Python-SDK) (`pitop`)
- OpenCV (`opencv-python`)
- NumPy
- Pillow

## Deployment

1. Transfer a script to the Pi-Top:
   ```bash
   scp <filename> pi@<pi-top-ip>:~/
   ```
2. SSH into the Pi-Top:
   ```bash
   ssh pi@<pi-top-ip>
   ```
3. Run the script:
   ```bash
   python3 <filename>
   ```
