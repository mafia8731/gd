# 郭寒熙   练习文件
# 时间 2024/5/7 21:06

import cv2

# 导入numpy
import numpy as np
# 导入姿势识别器
from poseutil import PoseDetector
cap = cv2.VideoCapture('1.mp4')
da = PoseDetector()



def get_pos(keypoints):
    str_pose = ""
    # 计算左臂与水平方向的夹角
    keypoints = np.array(keypoints)
    v1 = keypoints[12] - keypoints[11]
    v2 = keypoints[13] - keypoints[11]
    angle_left_arm = get_angle(v1, v2)
    #计算右臂与水平方向的夹角
    v1 = keypoints[11] - keypoints[12]
    v2 = keypoints[14] - keypoints[12]
    angle_right_arm = get_angle(v1, v2)
    #计算左肘的夹角
    v1 = keypoints[11] - keypoints[13]
    v2 = keypoints[15] - keypoints[13]
    angle_left_elow = get_angle(v1, v2)
    # 计算右肘的夹角
    v1 = keypoints[12] - keypoints[14]
    v2 = keypoints[16] - keypoints[14]
    angle_right_elow = get_angle(v1, v2)

    if angle_left_arm<0 and angle_right_arm<0:
        str_pose = "LEFT_UP"
    elif angle_left_arm>0 and angle_right_arm>0:
        str_pose = "RIGHT_UP"
    elif angle_left_arm<0 and angle_right_arm>0:
        str_pose = "ALL_HANDS_UP"
        if abs(angle_left_elow)<120 and abs(angle_right_elow)<120:
            str_pose = "TRIANGLE"
    elif angle_left_arm>0 and angle_right_arm<0:
        str_pose = "NORMAL"
        if abs(angle_left_elow)<120 and abs(angle_right_elow)<120:
            str_pose = "AKIMBO"
    return str_pose
