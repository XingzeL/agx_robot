#!/usr/bin/env python3
# coding=UTF-8

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

def distance_callback(data, cmd_vel_publisher):
    if data.data > 0.3:
        move_cmd = Twist()
        move_cmd.linear.x = 0.1
        move_cmd.linear.y = 0.0
        move_cmd.linear.z = 0.0
        move_cmd.angular.x = 0.0
        move_cmd.angular.y = 0.0
        move_cmd.angular.z = 0.0

        cmd_vel_publisher.publish(move_cmd)
    else :
        stop_cmd = Twist()
        cmd_vel_publisher.publish(stop_cmd)

def main():
    rospy.init_node('limo_controller', anonymous=True)

    cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/front_obstacle_distance', Float32, lambda msg:distance_callback(msg, cmd_vel_publisher))
    rospy.spin()

if __name__ == '__main__':
        main()

