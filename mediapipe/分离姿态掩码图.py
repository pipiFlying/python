import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
# static_image_mode 获取掩码需要开启掩码捕获
pose = mp_pose.Pose(enable_segmentation=True)

img = cv2.imread('kongfu.jpg')
h, w, _ = img.shape
img = cv2.resize(img, (int(w / 4), int(h / 4)))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
res = pose.process(img_rgb)

mask = res.segmentation_mask

cv2.imshow('win', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

