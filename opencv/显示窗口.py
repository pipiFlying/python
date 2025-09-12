import cv2

img = cv2.imread('testa.jpg')

"""
显示图像
参数一：显示图像的窗口名称，如果该窗口实现没有创建，那么这里会自动创建
如果事先创建了该窗口，就使用创建好的窗口
参数二：需要显示的图像
"""
# winname是窗口名，不能是中文名
cv2.imshow('meinv', img)

"""
delay：0表示永远，也就是一直等待，直到按下键
delay > 0 表示等待毫秒数
waitKey(): -> 返回值是按下键的key

其中常用的 esc = 27  q = 113

返回的键盘值可以用 ord(字母)来作对比
"""
code = cv2.waitKey(0)
print(code)
print(ord('q'))
