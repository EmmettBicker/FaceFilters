import cv2
import math
import constants
import time
import time_functionality

import random

global wave_speed
global wave_frequency
global wave_amplitude
wave_speed = 5
wave_frequency = 0.6
wave_amplitude = 50

def set_wave_speed(number):
    global wave_speed
    wave_speed = number

def set_wave_frequency(number):
    global wave_frequency
    wave_frequency = number

def set_wave_amplitude(number):
    global wave_amplitude
    wave_amplitude = number

def change_wave_speed(number):
    global wave_speed
    wave_speed += number

def change_wave_frequency(number):
    global wave_frequency
    wave_frequency += number

def change_wave_amplitude(number):
    global wave_amplitude
    wave_amplitude += number


def get_wave_speed():
    global wave_speed
    return wave_speed

def get_wave_frequency():
    global wave_frequency
    return wave_frequency

def get_wave_amplitude():
    global wave_amplitude
    return wave_amplitude




def draw_waves_from_line(canvas, start_point, end_point, line_color, center_point, layer):
    
    # Set the wave properties
    wave_potential_colors = (
        (147, 187, 241),  # deep blue
        (16, 85, 201),
        (55, 121, 234),
        (203, 231, 237),
        (17, 50, 154),
        (231, 69, 77)
    
    )


    global wave_speed
    global wave_frequency
    global wave_amplitude
    # Draw the line
    # cv2.line(canvas, start_point, end_point, line_color, 2)

    # Calculate the line parameters
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    line_length = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)

    # Calculate the direction vector from the center point to the start point
    center_dx = start_point[0] - center_point[0]
    center_dy = start_point[1] - center_point[1]
    center_distance = math.sqrt(center_dx**2 + center_dy**2)
    center_angle = math.atan2(center_dy, center_dx)

    # Draw the waves
    total = 10
    for i in range(total):
        t = i / total
        x = int(start_point[0] + t * dx + random.random()*3)
        y = int(start_point[1] + t * dy)
        
        # Calculate the offset based on the distance and angle from the center point
        offset_factor = math.sin(i * wave_frequency + cv2.getTickCount() * wave_speed / cv2.getTickFrequency())
        calc_trick = math.cos(i * wave_frequency + cv2.getTickCount() * wave_speed / cv2.getTickFrequency())
        offset_distance = wave_amplitude * offset_factor
        offset_x = int(offset_distance * math.cos(center_angle))
        offset_y = int(offset_distance * math.sin(center_angle))
        
        center_point_2 = (int(center_point[0] * canvas.shape[0]), int(center_point[1] * canvas.shape[1]))


        time_factor = time.time() - time_functionality.get_held_time()
        thickness = 5 - int(time_factor*6)

        if offset_factor < 0.01 and calc_trick > 0.9:
            time_functionality.update_held_time()
        elif offset_factor < 0.01 and calc_trick > 0.7:
            thickness = 1
        elif offset_factor < 0.01 and calc_trick > 0.75:
            thickness = 2
        elif offset_factor < 0.01 and calc_trick > 0.8:
            thickness = 3
        elif offset_factor < 0.01 and calc_trick > 0.85:
            thickness = 4

        thickness += round(random.random()*3-1.5)
        thickness += layer
        thickness = max(thickness, 0)
        
        
        if thickness != 0:
            cv2.circle(canvas, (x + offset_x, y + offset_y), thickness, random.choice(wave_potential_colors), -1)


if __name__ == "__main__":
    import main 
    main.main()