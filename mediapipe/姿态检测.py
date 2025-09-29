import mediapipe as mp
import cv2

# 引入姿态检测
mp_pose = mp.solutions.pose
# 引入姿态对象
pose = mp_pose.Pose()
# 引入绘制
mp_draw = mp.solutions.drawing_utils

img = cv2.imread('kongfu.jpg')
h, w, c = img.shape
img = cv2.resize(img, (int(w / 4), int(h / 4)))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

res = pose.process(img)
pose_landmarks = res.pose_landmarks

# 绘制2D关键点
# mp_draw.draw_landmarks(img, pose_landmarks, mp_pose.POSE_CONNECTIONS)

# 绘制3D关键点
mp_draw.plot_landmarks(pose_landmarks, mp_pose.POSE_CONNECTIONS)

# cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()