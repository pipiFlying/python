"""
手部关键点检测：
1. 使用opencv捕获摄像头
2. 使用mediapipe进行手部关键点识别
"""
import cv2
import mediapipe as mp

# 导入手部检测模块
mp_hands = mp.solutions.hands
# 创建功能对象
hand = mp_hands.Hands()
# 创建绘制关键点
mp_draw = mp.solutions.drawing_utils
# 设置绘制样式
landmark_style = mp_draw.DrawingSpec(color=(0, 255, 255), thickness=10, circle_radius=1)
connection_style = mp_draw.DrawingSpec(color=(0, 0, 255), thickness=4)

cap = cv2.VideoCapture('hands.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 视频中画面是镜像后的，所以需要翻转
    # flipCode == 0 垂直翻转
    # flipCode > 0 水平翻转
    # flipCode < 0 水平垂直翻转
    frame = cv2.flip(frame, 1)

    # BGR -> RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 手部关键点检查
    # 以下函数返回的是 NameTuple, 里面包含三个属性：
    # multi_hand_landmarks: 检测到所有的手部关键点
    # multi_hand_word_landmarks: 检测到所有的手部关键点(3D)
    # multi_handedness: 检测到的手部信息(包含了手的类型)
    res = hand.process(frame_rgb)
    # 获取手部关键点
    mul_hand_landmarks = res.multi_hand_landmarks
    if mul_hand_landmarks is not None:
        # hand_landmarks里面的landmarks存储的是手部的21个关键点坐标
        # 关键点坐标的xyz值是一个比例值
        for hand_landmarks in mul_hand_landmarks:
            print(hand_landmarks)
            # mp_hands.HAND_CONNECTIONS 绘制关键点连接线
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, landmark_style, connection_style)

    cv2.imshow('frame', frame)

    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()