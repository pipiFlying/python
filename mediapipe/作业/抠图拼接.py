import mediapipe as mp
import cv2
import numpy as np

# 加载获取pose功能
mp_pose = mp.solutions.pose
# 创建功能对象
pose = mp_pose.Pose(enable_segmentation=True)

img = cv2.imread('../kongfu.jpg')
bg = cv2.imread('location.png')
h, w, _ = img.shape
img = cv2.resize(img, (int(w / 4), int(h / 4)))
s_h, s_w, _ = img.shape
img_rgb = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

res = pose.process(img)
mask = res.segmentation_mask
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask_ac = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=8)

print(img.shape)
print(mask_ac.shape)
# mask_ac是float32不能作为掩码图需要转换为uint8
mask_ac_uint8 = cv2.convertScaleAbs(mask_ac * 255)
img_black = cv2.bitwise_and(img, img, mask=mask_ac_uint8)
img_ac_not = cv2.bitwise_not(mask_ac_uint8)
x = 450
y = 100
bg_split = bg[y:s_h + y, x:s_w + x]
print(bg_split.shape)

bg_split_black = cv2.bitwise_and(bg_split, bg_split, mask=img_ac_not)
or_img = cv2.bitwise_or(img_black, bg_split_black)

bg[y:s_h + y, x:s_w + x] = or_img
cv2.imshow('win', bg)
cv2.waitKey(0)
cv2.destroyAllWindows()