# 郭寒熙   练习文件
# 时间 2024/5/12 17:37
if positions:
    # 获取俯卧撑的角度
    bili1 = detector.find_bili(img, 16, 12, 28)
    # 进度条长度
    bar = np.interp(bili1, (45, 150), (w // 2 - 100, w // 2 + 100))
    cv2.rectangle(img, (w // 2 - 100, h - 150), (int(bar), h - 100), (255, 0, 0), cv2.FILLED)
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

