#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def perform_trajectory():
    rospy.init_node('custom_arm_trajectory_publisher')
    controller_name='/custom_arm_controller/command'
    trajectory_publisher = rospy.Publisher(controller_name, JointTrajectory, queue_size=10)

    argv = sys.argv              
    custom_arm_joints = ['joint_1', 'joint_2', 'joint_3', 'joint_4']
    goal_positions = [float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4]) ]
 
    rospy.loginfo("Goal Position set lets go ! ")
    rospy.sleep(1)

    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = custom_arm_joints
    trajectory_msg.points.append(JointTrajectoryPoint())
    # print(JointTrajectoryPoint())
    trajectory_msg.points[0].positions = goal_positions
    trajectory_msg.points[0].velocities = [0.0 for i in custom_arm_joints]
    trajectory_msg.points[0].accelerations = [0.0 for i in custom_arm_joints]
    trajectory_msg.points[0].time_from_start = rospy.Duration(3)
    rospy.sleep(1)
    trajectory_publisher.publish(trajectory_msg)



if __name__ == '__main__':
    perform_trajectory()