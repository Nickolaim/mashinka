#!/usr/bin/env python

import rospy
from mashinka.msg import MashinkaCommand

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.command)

def listener():

    rospy.init_node('mashinka', anonymous=True)
    rospy.Subscriber('mashinka_command', MachinkaCommand, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
