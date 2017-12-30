#!/usr/bin/env python

import rospy
from mashinka.msg import MotorCommand


def callback(data):
    rospy.loginfo("{}. Left: {}, right: {}", rospy.get_caller_id(), data.left, data.right)


def listener():
    rospy.init_node('virtual_motors', anonymous=True)
    rospy.Subscriber('motor_command', MotorCommand, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
