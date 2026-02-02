import time
import numpy as np
import cv2
from pitop import Pitop, DriveController, Camera

# Set up robot and drive controller
robot = Pitop()
drive = DriveController(left_motor_port="M3", right_motor_port="M0")
robot.add_component(drive)
robot.add_component(Camera(resolution=(640, 480), format='PIL', rotate_angle=0, flip_top_bottom=True))

# Color detection for orange
lower_orange = np.array([0, 120, 150])
upper_orange = np.array([30, 255, 255])

# Speed and thresholds
movement_speed = 0.4
min_contour_area = 100

# Flag to track if starting position has been corrected
starting_position_corrected = False

def get_user_inputs():
    motions = int(input("How many cycles should the rover perform? "))
    motion_points = []
    directions = []
    
    for i in range(motions):
        while True:
            direction = input(f"Enter direction for cycle {i + 1} (f for forward, b for backward): ").lower()
            if direction in ['f', 'b']:
                break
            print("Invalid direction. Please enter 'f' for forward or 'b' for backward.")
        
        points = int(input(f"How many units should the rover move for cycle {i + 1}? "))
        motion_points.append(points)
        directions.append(direction)
    
    return motion_points, directions

def detect_orange_line(camera_frame):
    hsv_frame = cv2.cvtColor(np.array(camera_frame), cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            print("Orange Detected!")
            return True
    return False

def correct_starting_position():
    global starting_position_corrected
    if starting_position_corrected:
        return
    
    print("Checking starting position...")
    step_duration = 0.05
    max_multiplier = 10
    movement_speed = 0.2

    for multiplier in range(1, max_multiplier + 1):
        # Forward search
        print(f"Searching forward {multiplier} step(s)...")
        for _ in range(multiplier):
            drive.forward(movement_speed)
            time.sleep(step_duration)
            drive.stop()

            camera_frame = robot.camera.get_frame()
            if detect_orange_line(camera_frame):
                print("Starting point confirmed (forward search).")
                starting_position_corrected = True
                return

        # Return to start position
        for _ in range(multiplier):
            drive.backward(movement_speed)
            time.sleep(step_duration)
            drive.stop()

    print("Could not confirm the starting point.")

def follow_line(units_to_move, direction):
    current_position = 0
    previous_frame_orange = True
    transition_to_non_orange = False
    
    print(f"Starting line following... Direction: {'Forward' if direction == 'f' else 'Backward'}")
    while current_position < units_to_move:
        camera_frame = robot.camera.get_frame()
        current_frame_orange = detect_orange_line(camera_frame)

        # Handle transitions between orange and non-orange
        if previous_frame_orange and not current_frame_orange:
            transition_to_non_orange = True
        elif transition_to_non_orange and current_frame_orange:
            current_position += 1
            transition_to_non_orange = False
            print(f"Orange point crossed: {current_position}/{units_to_move}")
        
        if current_position < units_to_move:
            if direction == 'f':
                drive.forward(0.3)
            else:
                drive.backward(0.3)
        
        previous_frame_orange = current_frame_orange
        time.sleep(0.05)  # Small delay to prevent CPU overload

    drive.stop()
    print(f"Completed {units_to_move} units in {'forward' if direction == 'f' else 'backward'} direction")
    return True

def main():
    try:
        correct_starting_position()
        motion_points, directions = get_user_inputs()
        
        for i, (units, direction) in enumerate(zip(motion_points, directions), 1):
            print(f"\nStarting cycle {i} with {units} units going {'forward' if direction == 'f' else 'backward'}")
            if follow_line(units, direction):
                print(f"Cycle {i} completed successfully")
                time.sleep(1)  # Pause between cycles
            else:
                print(f"Error in cycle {i}")
                break
        
        print("All cycles completed")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        drive.stop()  # Ensure the rover stops in case of error
    finally:
        drive.stop()  # Final safety stop

if __name__ == "__main__":
    main()