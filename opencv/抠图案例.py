import cv2
import numpy as np

def hsv_red_mask(img):
    """
    :param img: 原始图像
    :return: 掩码图
    """
    # 定义低值区红色hsv范围
    low01 = np.uint8([0, 43, 46])
    up01 = np.uint8([10, 255, 255])
    # 定义高值区红色hsv范围
    low02 = np.uint8([156, 43, 46])
    up02 = np.uint8([180, 255, 255])

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 获取低值区在原图中的掩码
    mask01 = cv2.inRange(img_hsv, low01, up01)
    # 获取高值区在原图中的掩码
    mask02 = cv2.inRange(img_hsv, low02, up02)
    # 将mask01和mask02做按位或运算
    mask = cv2.bitwise_or(mask01, mask02)
    return mask

if __name__ == '__main__':

    cv2.namedWindow('win', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('win', 400, 700)
    img = cv2.imread('rose.jpg')
    # 获取mask
    mask = hsv_red_mask(img)
    # 抠图：按位与运算获取红色区域
    rose = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('win', rose)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
