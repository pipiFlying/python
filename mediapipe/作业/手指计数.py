import mediapipe as mp
import cv2

# 创建手部检测功能
mp_hands = mp.solutions.hands
# 创建功能对象
hand = mp_hands.Hands()
# 创建绘制单元
mp_draw = mp.solutions.drawing_utils

# 根据mediapipe手部图谱得知，手指尖编号
finger_tops = [4, 8, 12, 16, 20]
# 存储每根手指是否展开
# 展开的标准，就是指尖的关节点，y坐标 > 次关节点的y坐标
# 具体原因是关节点的图左上角是原点
# 对应finger_tops关节点展示是True
finger_tops_flag = [False, False, False, False, False]

count_a = finger_tops_flag.count(True)
print(count_a)

cap = cv2.VideoCapture('../hands.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 视频镜像，需要还原，进行手部翻转
    frame = cv2.flip(frame, 1)
    # 帧转RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hand.process(frame_rgb)
    # 通过debuger获取返回值参数
    multi_hand_landmarks = res.multi_hand_landmarks
    for hand_landmarks in multi_hand_landmarks:
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        for idx, finger in enumerate(finger_tops):
            top_y = hand_landmarks.landmark[finger].y
            next_y = hand_landmarks.landmark[finger - 1].y
            if top_y < next_y:
                finger_tops_flag[idx] = True
            else:
                finger_tops_flag[idx] = False

    count = finger_tops_flag.count(True)

    cv2.putText(frame, f'{count}', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
