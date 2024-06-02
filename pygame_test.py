import cv2
import numpy as np
import math

def draw_waves_from_line(canvas, start_point, end_point, line_color, wave_color, wave_speed, wave_frequency, wave_amplitude):
    # Draw the line
    cv2.line(canvas, start_point, end_point, line_color, 2)

    # Calculate the line parameters
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    line_length = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)

    # Draw the waves
    for i in range(100):
        t = i / 100
        x = int(start_point[0] + t * dx)
        y = int(start_point[1] + t * dy + wave_amplitude * math.sin(i * wave_frequency + cv2.getTickCount() * wave_speed / cv2.getTickFrequency()))
        offset_x = int(wave_amplitude * math.sin(angle + math.pi/2) * math.sin(i * wave_frequency + cv2.getTickCount() * wave_speed / cv2.getTickFrequency()))
        offset_y = int(wave_amplitude * math.cos(angle + math.pi/2) * math.sin(i * wave_frequency + cv2.getTickCount() * wave_speed / cv2.getTickFrequency()))
        cv2.circle(canvas, (x + offset_x, y + offset_y), 5, wave_color, -1)

# Set the window size
width, height = 800, 600

# Set the line properties
line_color = (255, 255, 255)  # White
start_point = (600, 100)
end_point = (700, 500)

# Set the wave properties
wave_color = (255, 255, 0)  # Cyan
wave_speed = 1
wave_frequency = 0.02
wave_amplitude = 50

# Create a blank canvas
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Game loop
while True:
    # Clear the canvas
    canvas.fill(0)

    # Draw the waves from the line
    draw_waves_from_line(canvas, start_point, end_point, line_color, wave_color, wave_speed, wave_frequency, wave_amplitude)

    # Display the canvas
    cv2.imshow("Waves from Line", canvas)

    # Check for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all windows
cv2.destroyAllWindows()