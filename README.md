# Pi-Top Robotics Workshop

Python scripts for the [pi-top](https://www.pi-top.com/) robotics platform, written for an
applied robotics workshop I designed and led at my former high school. The workshop
introduced students to programming and coordinate-based navigation through hands-on
problems on a real robot.

## Scripts

### `line-follower.py`: marker-counting navigation
The rover drives along a track and uses its camera to count orange markers. Each marker
crossed counts as one unit of distance, which turns the track into a simple 1-D coordinate
system.

1. **Find the start.** The rover makes short forward probes that grow in length until the
   camera sees orange, so it begins on a known marker.
2. **Plan the moves.** You enter a number of cycles. Each cycle has a direction (`f`/`b`)
   and a number of units.
3. **Execute.** Each frame is converted to HSV and thresholded for orange. A unit is counted
   on each orange → not-orange → orange transition. The rover stops once it reaches the
   target count.

Hardware setup: drive motors on ports `M3` (left) and `M0` (right), with the camera at
640×480.

### Miniscreen demos
Short animations for the pi-top's 128×64 miniscreen, which were useful warm-up exercises:

| Script | What it shows |
|---|---|
| `test.py` | A smiley face for 10 s. A quick check that the display works. |
| `rainbow.py` | Scrolling rainbow stripes for 10 s. |
| `tree.py` | A recursive fractal tree swaying in the "wind" for 15 s. |

## Requirements

- pi-top robot with miniscreen (and camera plus drive motors for `line-follower.py`)
- Python 3
- [pi-top Python SDK](https://github.com/pi-top/pi-top-Python-SDK) (`pitop`)
- OpenCV (`opencv-python`), NumPy, Pillow

## Running on the robot

```bash
scp <script>.py pi@<pi-top-ip>:~/
ssh pi@<pi-top-ip>
python3 <script>.py
```

## License

[MIT](LICENSE)
