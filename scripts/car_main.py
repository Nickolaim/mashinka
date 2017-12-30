#!/usr/bin/env python

import rospy
from mashinka.msg import MashinkaCommand, MotorCommand

NODE_NAME = 'car_main'


class Car(object):
    def __init__(self):
        self.publisher = rospy.Publisher('motor_command', MotorCommand, queue_size=10)


    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + '. I heard %s', data.command)
        motor_command = MotorCommand()
        motor_command.left = 1.0
        motor_command.right = -1.0
        self.publisher.publish(motor_command)

    def listener(self):
        rospy.init_node(NODE_NAME, anonymous=True)
        rospy.Subscriber('mashinka_command', MashinkaCommand, self.callback)

        rospy.spin()


if __name__ == '__main__':
    Car().listener()
