#!/usr/bin/env python

import rospy
from mashinka.msg import MotorCommand
from geometry_msgs.msg import PoseStamped


class VirtualMotors(object):
    def __init__(self):
        self.publisher = rospy.Publisher('PoseStamped', PoseStamped, queue_size=10)
        self.pose_stamped = PoseStamped()

    def callback(self, data):
        rospy.loginfo("{}. Left: {}, right: {}".format(rospy.get_caller_id(), data.left, data.right))
        self.pose_stamped.header.stamp = rospy.Time.now()
        self.pose_stamped.pose.position.y += data.left
        # tf.transformations.quaternion_from_euler(roll, pitch, yaw)
        self.publisher.publish(self.pose_stamped)


    def listener(self):
        rospy.init_node('virtual_motors', anonymous=True)
        rospy.Subscriber('motor_command', MotorCommand, self.callback)
        rospy.spin()


if __name__ == '__main__':
    VirtualMotors().listener()
