# 郭寒熙   练习文件
# 时间 2024/5/7 23:11
# 郭寒熙   练习文件
# 时间 2024/5/7 21:06
# 导入opencv工具包
import cv2



#JAFUJDWJDAHJWIAHFWAFHAIWFHAIWHFIDA
# 导入numpy
import numpy as np
# 导入姿势识别器
from poseutil import PoseDetector
import math
# 打开视频文件
cap = cv2.VideoCapture(0)
# 姿势识别器
detector = PoseDetector()

dir = 0
count = 0

def fu_wo_chen():
    # 获取俯卧撑的角度
    global dir
    global count
    bili1 = detector.find_bili(img, 16, 12, 28)
    bar = np.interp(bili1, (45, 150), (w // 2 - 100, w // 2 + 100))
    # 角度小于50度认为撑下
    if bili1 < 0.050:
        if dir == 0:
            count = count + 0.5
            dir = 1
    # 角度大于125度认为撑起
    if bili1 > 0.1:
        if dir == 1:
            count = count + 0.5
            dir = 0
    cv2.putText(img, str(int(count)), (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 20,
                cv2.LINE_AA)


def angle_line(p1,p2,draw = True):

    x1, y1 = detector.lmslist[p1][1], detector.lmslist[p1][2]
    x2, y2 = detector.lmslist[p2][1], detector.lmslist[p2][2]
    x3, y3 = x2+50,y2

    angle_l = int(math.degrees(math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2)))
    if angle_l < 0:
        angle_l = angle_l + 360
    if angle_l > 180:
        angle_l = 360 - angle_l

    if draw:
        cv2.circle(img, (x1, y1), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 5, (0, 255, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255, 3))
        cv2.line(img, (x2, y2), (x3, y3), (255, 255, 255, 3))
        cv2.putText(img, str(angle_l), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
    return angle_l



def shen_dun():
    global dir
    global count
    angle1 = detector.find_angle(img, 23, 25, 27)
    #bar = np.interp(angle1, (45, 150), (w // 2 - 100, w // 2 + 100))
    #cv2.rectangle(img, (w // 2 - 100, h - 150), (int(bar), h - 100), (20, 0, 0), cv2.FILLED)
    # 角度小于50度认为撑下
    if angle1 < 110:
        if dir == 0:
            count = count + 0.5
            dir = 1
    # 角度大于125度认为撑起
    if angle1 > 160:
        if dir == 1:
            count = count + 0.5
            dir = 0
    cv2.putText(img, str(int(count)), (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 20,
                cv2.LINE_AA)



def yang_wo():
    global dir
    global count
    angle1 = detector.find_angle(img, 11, 23, 27)
    #bar = np.interp(angle1, (45, 150), (w // 2 - 100, w // 2 + 100))
    #cv2.rectangle(img, (w // 2 - 100, h - 150), (int(bar), h - 100), (20, 0, 0), cv2.FILLED)
    # 角度小于50度认为撑下
    if angle1 < 140:
        if dir == 0:
            count = count + 0.5
            dir = 1
    # 角度大于125度认为撑起
    if angle1 > 150:
        if dir == 1:
            count = count + 0.5
            dir = 0
    cv2.putText(img, str(int(count)), (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 20,
                cv2.LINE_AA)



def po_se():
    str_pose = ""
    # 计算左臂与水平方向的夹角
    detector.lmslist = np.array(detector.lmslist)
    angle_left_arm = detector.find_angle(img,12,11,13,True)
    # 计算右臂与水平方向的夹角
    angle_right_arm = detector.find_angle(img,11,12,14,True)
    # 计算左肘的夹角
    angle_left_elow = detector.find_angle(img,11,13,15,True)
    # 计算右肘的夹角
    angle_right_elow = detector.find_angle(img,12,14,16,True)
    #计算左膝盖角度
    angle_left_leg = detector.find_angle(img,23,25,27)
    #计算右膝盖角度
    angle_right_leg = detector.find_angle(img, 24, 26, 28)
    #计算与地面角度
    angle_ground = angle_line(23,27,draw=True)
    #angle_ground_sd = angle_line(23, 27, draw=True)


    if (60 < angle_ground < 120) and (angle_left_elow < 100 or angle_right_elow < 100):
        str_pose = "shendun"
    elif (angle_ground < 60 or angle_ground > 120) and 130 > angle_left_leg > 50 :
        str_pose = "yangwoqizuo"
    elif (angle_ground < 60 or angle_ground > 120) and (angle_left_leg > 150 or angle_right_leg > 150):
        str_pose = "fuwochen"
    else:
        str_pose = "     "
    return str_pose



# 视频宽度高度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 录制视频设置
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('videos/pushupoutput.mp4', fourcc, 30.0, (width, height))

while True:
    # 读取摄像头，img为每帧图片e
    success, img = cap.read()
    if success:
        h, w, c = img.shape
        # 识别姿势
        img = detector.find_pose(img, draw=False)
        # 获取姿势数据
        positions = detector.find_positions(img)

        if positions:
            yang_wo()
           #姿势识别
            cv2.putText(img, po_se(), (w // 5, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 4,
                        cv2.LINE_AA)



        # 打开一个Image窗口显示视频图片
        cv2.imshow('Image', img)

        # 录制视频
        out.write(img)
    else:
        # 视频结束退出
        break

    # 如果按下q键，程序退出
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 关闭视频保存器
out.release()
# 关闭摄像头
cap.release()
# 关闭程序窗口
cv2.destroyAllWindows()
