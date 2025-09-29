"""
安装mediapipe:
    pip install mediapipe -i https://pypi.tuna.tsinghua.edu.cn/simple/

使用mediapipe步骤
1. 导入mediapipe
2. 加载对应功能模块
3. 创建对应功能对象
4. 调用处理函数 process

** 使用mediapipe需要掌握调试
"""
import mediapipe as mp

# 比如需要完成手部关键点检测，需要加载对应模块
mp_hands = mp.solutions.hands

# 创建对应功能对象
hand = mp_hands.Hands()

# 调用处理函数 process
hand.process()