#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Quaternion
import sys

Pi = 3.141592653589793

def send_goal(x, y, z, w):
    rospy.init_node('send_node_goal', anonymous=True)
   
    #create a publiser pub PoseStamped msgs
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped,queue_size=10)

    #PoseStamped message input
    goal = PoseStamped()
    #goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"
    #destination
    goal.pose.position.x = float(x) 
    goal.pose.position.y = float(y)
    goal.pose.position.z = 0
    
    #roll = 0
    #pitch = 0
   # yaw = float(theta) * (Pi / 180)
   # quaternion = quaternion_from_euler(roll, pitch, yaw)

    goal.pose.orientation.x = 0
    goal.pose.orientation.y = 0

    goal.pose.orientation.z = z 
    goal.pose.orientation.w = w
    #print("set pose")
    pub.publish(goal)
    #print("set goal")
    #rospy.sleep(1)
    #rospy.spin()

def main():
    if len(sys.argv) != 5:
        print("args: x y z w\n");
    send_goal(0,0,0,0) #第一个message会被吞

    x = sys.argv[1];
    y = sys.argv[2];
    z = sys.argv[3];
    w = sys.argv[4];

    # x = input("Input x: ")
    # y = input("Input y: ")
    # theta = input("Input theta: ")

    send_goal(x, y, z, w)
        #rospy.sleep(1)
    #print("set destination")
    #rospy.shutdown()

if __name__ == '__main__':
    main()
