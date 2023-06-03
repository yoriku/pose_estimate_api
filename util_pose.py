import numpy as np
import matplotlib.pyplot as plt
import cv2
import mediapipe as mp



def get_image(path="img/test.jpg", return_rgb=True):
    img = cv2.imread(path)
    if return_rgb:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def binaly2img(body):
    arr = np.frombuffer(body, dtype=np.uint8)
    img = cv2.imdecode(arr, flags=cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def pose_estimate(image, plot=False):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(static_image_mode=True) as pose:
        # image = get_image(path="img/both_down.jpg")
        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(image)
        d={}
        d.update(RIGHT_SHOULDER_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width)
        d.update(RIGHT_SHOULDER_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height)

        d.update(RIGHT_ELBOW_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * image_width)
        d.update(RIGHT_ELBOW_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * image_height)

        d.update(RIGHT_INDEX_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x * image_width)
        d.update(RIGHT_INDEX_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y * image_height)

        d.update(LEFT_SHOULDER_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * image_width)
        d.update(LEFT_SHOULDER_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * image_height)

        d.update(LEFT_ELBOW_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * image_width)
        d.update(LEFT_ELBOW_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * image_height)

        d.update(LEFT_INDEX_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x * image_width)
        d.update(LEFT_INDEX_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y * image_height)
        
        if plot:
            print(d)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            plt.imshow(image)
            plt.tight_layout()
            plt.show()
        return d

if __name__ == "__main__":
    image = get_image()
    pose_estimate(image)