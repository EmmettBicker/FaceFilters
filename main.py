from enum import Enum
import cv2
import mediapipe as mp
import numpy as np
import constants
import wave_functionality
from features import Features

global number_of_outer_rings
global outer_ring_exponential_distance
global feature_to_layer_modifier

number_of_outer_rings = 5
outer_ring_exponential_distance = 0.70

wave_functionality.set_wave_speed(20)
wave_functionality.set_wave_frequency(3)
wave_functionality.set_wave_amplitude(5)


feature_to_layer_modifier = {
    Features.Unordered : 0,
    Features.FaceOval : 0,
    Features.LeftEye : -2,
    Features.RightEye : -2,
    Features.Lips: -2,
    Features.Nose: -2
}


global sign
sign = 1

# Load the video
def main():
    cap = cv2.VideoCapture('Blue Sequence 02.mp4')

    # Initialize the Mediapipe face mesh model
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Initialize the drawing utility
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(255, 255, 255))

    # Initialize variables for smoothing
    smoothing_window_size = 5
    smoothed_landmarks = None


    width, height = 800, 600

    # Set the line properties
    line_color = (255, 255, 255)  # White
    start_point = (600, 100)
    end_point = (700, 500)




    t = 0
    while cap.isOpened():
        
        # Read a frame from the video
        success, frame = cap.read()
        if not success:
            break

        height, width, _ = frame.shape
        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        results = face_mesh.process(frame_rgb)

        # Check if any faces are detected
        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]

            # Convert landmark coordinates to a NumPy array
            landmarks = np.array([(lm.x, lm.y, lm.z) for lm in face_landmarks.landmark])
            landmarks_x_y = landmarks[:,0:2]
            # Smooth the landmarks using a moving average filter
            if smoothed_landmarks is None:
                smoothed_landmarks = landmarks
            else:
                smoothed_landmarks = (smoothed_landmarks * (smoothing_window_size - 1) + landmarks) / smoothing_window_size

            # Update the face_landmarks with the smoothed landmarks
            for i, lm in enumerate(face_landmarks.landmark):
                lm.x, lm.y, lm.z = smoothed_landmarks[i]


            from mediapipe.python.solutions.face_mesh_connections import (
                FACEMESH_FACE_OVAL, FACEMESH_LEFT_EYE, FACEMESH_RIGHT_EYE,
                FACEMESH_LIPS, FACEMESH_NOSE
            )

            if True:

                oval_points = [landmarks_x_y[idx,:] for idx in FACEMESH_FACE_OVAL]
                # oval_points = oval_points[:(int(len(oval_points)/2))]
                left_eye_points = [landmarks_x_y[idx,:] for idx in FACEMESH_LEFT_EYE]
                right_eye_points = [landmarks_x_y[idx,:] for idx in FACEMESH_RIGHT_EYE]
                lips_points = [landmarks_x_y[idx,:] for idx in FACEMESH_LIPS]
                nose_points = [landmarks_x_y[idx,:] for idx in FACEMESH_NOSE]
                
                draw_waves(oval_points, frame, line_color, width, height, Features.FaceOval)
                draw_waves(left_eye_points, frame, line_color, width, height, name = Features.LeftEye)
                draw_waves(right_eye_points, frame, line_color, width, height, name = Features.RightEye)
                draw_waves(lips_points, frame, line_color, width, height, name = Features.Lips)
                draw_waves(nose_points, frame, line_color, width, height, name = Features.Unordered)

        # Display the filtered frame
        cv2.imshow('Face Filters', frame)

        # Break the loop if 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        global sign
        
        if key == ord('-'): 
            sign = -1
        elif key == ord('+'):
            sign = 1

        if key == ord('f'): 
            wave_functionality.change_wave_frequency(0.1* sign)
            print(f"frequency: {wave_functionality.get_wave_frequency()}")
        if key == ord('a'): 
            wave_functionality.change_wave_amplitude(1 * sign)
            print(f"amplitude: {wave_functionality.get_wave_amplitude()}")
        if key == ord('s'):
            wave_functionality.change_wave_speed(0.1 * sign)
            print(f"speed: {wave_functionality.get_wave_speed()}")
        if key == ord('d'):
            global outer_ring_exponential_distance
            outer_ring_exponential_distance += 0.01 * sign
            print(f"outer rings: {outer_ring_exponential_distance}")


        

        t += 1
    # Release the video capture and close the display window
    cap.release()
    cv2.destroyAllWindows()

def unnormalize(point, width, height):
    return (int(point[0] * width), int(point[1] * height))


def draw_waves(oval_points,frame,line_color, width, height, name):
    average_points = [0,0]
    for i in range(len(oval_points) - 1):
        average_points[0] += oval_points[i][0][0]
        average_points[1] += oval_points[i][0][1]

    average_points[0] /= len(oval_points) - 1
    average_points[1] /= len(oval_points) - 1

    average_points = unnormalize(average_points, width, height)

    for i in range(len(oval_points) - 1):
        if name in constants.feature_to_ordering:

            correct_i= constants.feature_to_ordering[name][i]
            correct_i_p1= constants.feature_to_ordering[name][i+1]
            
        else:
            correct_i = i
            correct_i_p1 = i+1

        global feature_to_layer_modifier
        layer_modifier = feature_to_layer_modifier[name]
        oval_x_y = oval_points[correct_i][0]
        next_oval_x_y = oval_points[correct_i_p1][0]
        
        start_point = (int(oval_x_y[0] * width), int(oval_x_y[1] * height))
        end_point = (int(next_oval_x_y[0] * width), int(next_oval_x_y[1] * height))

        
        # # cv2.line(frame, start_point, end_point, (255, 255, 255))
        # cv2.putText(
        #     frame,
        #     f"{i}",
        #     start_point,
        #     0,
        #     0.5,
        #     (255,255,255)
        # )

        test_dont_draw_waves = False
        # Draw waves between the current line
        if not test_dont_draw_waves:
            wave_functionality.draw_waves_from_line(frame, start_point, end_point, line_color, average_points, 0+layer_modifier)

        if True:
            global number_of_outer_rings
            global outer_ring_exponential_distance
            for i in range(number_of_outer_rings):
                # Translate the points to the origin
                start_point_2 = np.array(start_point) - np.array(average_points)
                end_point_2 = np.array(end_point) - np.array(average_points)
                # cv2.circle(frame, average_points, 4, (255,255,0),-1)
                # Scale the points by the scale factor
                scaled_point_start = start_point_2 * outer_ring_exponential_distance ** i
                scaled_point_end = end_point_2 * outer_ring_exponential_distance ** i

                # Translate the points back to the original position
                scaled_point_start += np.array(average_points)
                scaled_point_end += np.array(average_points)

                scaled_point_start = [p for p in scaled_point_start]
                scaled_point_end = [p for p in scaled_point_end]
                layer = i

                if not test_dont_draw_waves:
                    wave_functionality.draw_waves_from_line(frame, scaled_point_start, scaled_point_end, line_color, average_points, layer+layer_modifier)
        
    # # Connect the last point to the first point to complete the oval
    # first_oval_x_y = oval_points[0][0]
    # last_oval_x_y = oval_points[-1][0]
    # start_point = (int(last_oval_x_y[0] * width), int(last_oval_x_y[1] * height))
    # end_point = (int(first_oval_x_y[0] * width), int(first_oval_x_y[1] * height))
    
    # cv2.line(frame, start_point, end_point, (255, 255, 255))


main()