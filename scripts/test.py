def image_callback(msg, args);
    twist_publisher, predefined_ids = args

    #将ROS图像转换成Numpy数组并且转换颜色空间（RGB到BGR）
    np_image = ros_numpy.numpify(msg)
    np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

    #定义ArUco marker字典
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters()

    #识别marker
    corners, ids, rejectedImgPoints = aruco.detectMarkers(np_image, aruco_dict,
                                                          parameters=parameters)

    #识别的id，打印出来
    if ids is not None:
        for id in ids:  
            print("Detected Marker ID:", id[0]) #打印所有识别出来的id                                                     

    #指定最近的一个号码
    closest_marker = find_closest_marker(ids, corners, predefined_ids)

    #输出最近的一个marker
    if closest_marker is not None:
        marker_id, marker_corner = closest_marker
        print("Cloest Marker ID:", marker_id)

def find_cloest_marker(ids, corners, predefined_ids):
    closest_marker = None
    max_size = 0
    if ids is not None:
        for i, corner in zip(ids, corners):
            #计算识别出的marker的面积
            if i[0] in predefined_ids: 
                size = cv2.contourArea(corner)
                if size > max_size:
                    max_size = size
                    closest_marker = (i[0], corner)
    return closest_marker


if __name__ == '__main__':
    predefined_ids = [1, 3]
    rospy.init_node('aruco_image_listener', anonymous=True)
    twist_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber(
        "/camera/rgb/image_raw",
        Image,
        image_callback,
        callback_args=(twist_publisher, predefined_ids)
    )

    rospy.spin()
    cv2.destroyAllWindows()
