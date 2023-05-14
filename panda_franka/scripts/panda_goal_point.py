#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys
from spatialmath.base import *
from spatialmath import SE3
import spatialmath.base.symbolic as sym
import roboticstoolbox as rtb
import numpy as np

def perform_trajectory():
    rospy.init_node('panda_trajectory_publisher')
    contoller_name='/panda_controller/command'
    trajectory_publihser = rospy.Publisher(contoller_name,JointTrajectory, queue_size=10)
    argv = sys.argv[1:]                         
    panda_joints = ['panda_joint1','panda_joint2','panda_joint3','panda_joint4','panda_joint5',
                    'panda_joint6','panda_joint7']
    
    panda = rtb.models.URDF.Panda()
    point = SE3(float(argv[0]) , float(argv[1]) , float(argv[2]) ) # end effector point
    joint_angles = panda.ikine_LM(point)[0]
    print("angles\n:", joint_angles)
 
    rospy.loginfo("Goal Position set lets go ! ")
    rospy.sleep(1)


    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = panda_joints
    trajectory_msg.points.append(JointTrajectoryPoint())
    trajectory_msg.points[0].positions = joint_angles
    trajectory_msg.points[0].velocities = [0.0 for i in panda_joints]
    trajectory_msg.points[0].accelerations = [0.0 for i in panda_joints]
    trajectory_msg.points[0].time_from_start = rospy.Duration(3)
    rospy.sleep(1)
    trajectory_publihser.publish(trajectory_msg)


if __name__ == '__main__':
    perform_trajectory()