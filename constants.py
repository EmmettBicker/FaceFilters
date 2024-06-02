import cv2
import time
from features import Features


ordering_of_oval_face = [8, 19, 18, 33, 21, 3, 11, 29, 1, 27, 13, 9, 12, 4, 22, 17, 7, 31, 28, 23, 24, 34, 14, 16, 6, 25, 0, 30, 2, 15, 20, 5, 10, 26, 32, 8]
ordering_of_left_eye = [14, 8, 3, 10, 6, 11, 9, 5, 12, 2, 1, 4, 0, 13, 7,14]
ordering_of_right_eye = [3, 6, 11, 5, 0, 8, 14, 4, 7, 9, 12, 2, 10, 13, 3, 3]
ordering_of_lips = [22, 33, 32, 4, 14, 18, 6, 0, 26, 10, 37, 31, 9 , 24, 15, 2, 36, 35, 14, 29, 30 ,21, 17, 28, 20, 1, 34, 8, 25, 7, 23, 10, 11, 5, 38, 3, 27, 19, 2, 22]
ordering_of_nose = [10, 8, 5, 12, 1, 6, 4, 2, 20, 21, 13, 9, 23, 15, 19, 0, 16, 3, 17, 14, 18, 22, 8, 11, 10]

feature_to_ordering = {
    Features.FaceOval : ordering_of_oval_face,
    Features.LeftEye : ordering_of_left_eye,
    Features.RightEye : ordering_of_right_eye,
    Features.Lips : ordering_of_lips,
    Features.Nose : ordering_of_nose
}


DOUBLE_HELIX_FREQUENCY = 3.4


