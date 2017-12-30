#!/usr/bin/env python

import rospy
from mashinka.msg import MashinkaCommand


class Car(object):

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.command)

    def listener(self):
        rospy.init_node('car_main', anonymous=True)
        rospy.Subscriber('mashinka_command', MashinkaCommand, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()


if __name__ == '__main__':
    Car().listener()
