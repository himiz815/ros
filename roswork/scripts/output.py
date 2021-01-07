#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

print("数値を入力してEnter")
number =int(input())

def cb(message):
	rospy.loginfo(message.data * number)
if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up', Int32, cb)
	rospy.spin()
