# Resources
- **[Udemy Course: ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF](https://www.udemy.com/course/robotics-with-ros-build-robotic-arm-in-gazebo-and-moveit/)**

- **[Course Repository](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-)**

- **[Panda URDF](https://github.com/HarshBhatt09/Franka-Emika-Panda-7-DOF-Robot-ROS-Noetic)**

# Installations
```bash
sudo apt-get install ros-noetic-joint-trajectory-controller
sudo apt-get install ros-noetic-effort-controllers
sudo apt-get install ros-noetic-position-controllers
```

# Packages
## custom_arm

### Rostopics
```bash
/clock
/custom_arm_controller/command
/custom_arm_controller/follow_joint_trajectory/cancel
/custom_arm_controller/follow_joint_trajectory/feedback
/custom_arm_controller/follow_joint_trajectory/goal
/custom_arm_controller/follow_joint_trajectory/result
/custom_arm_controller/follow_joint_trajectory/status
/custom_arm_controller/state
/gazebo/link_states
/gazebo/model_states
/gazebo/parameter_descriptions
/gazebo/parameter_updates
/gazebo/performance_metrics
/gazebo/set_link_state
/gazebo/set_model_state
/joint_states
/rosout
/rosout_agg
/tf
/tf_static
```

### custom_arm_controller/command  
- Type: trajectory_msgs/JointTrajectory
```bash
header: 
  seq: 1
  stamp: 
    secs: 0
    nsecs:         0
  frame_id: ''
joint_names: 
  - joint_1
  - joint_2
  - joint_3
  - joint_4
points: 
  - 
    positions: [0.4, 0.2, 0.4, 0.4]
    velocities: [0.0, 0.0, 0.0, 0.0]
    accelerations: [0.0, 0.0, 0.0, 0.0]
    effort: []
    time_from_start: 
      secs: 3
      nsecs:         0
---
```

## panda_franka

### Rostopics
```bash
/clock
/gazebo/link_states
/gazebo/model_states
/gazebo/parameter_descriptions
/gazebo/parameter_updates
/gazebo/performance_metrics
/gazebo/set_link_state
/gazebo/set_model_state
/gazebo_ros_control/pid_gains/panda_joint1/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint1/parameter_updates
/gazebo_ros_control/pid_gains/panda_joint2/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint2/parameter_updates
/gazebo_ros_control/pid_gains/panda_joint3/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint3/parameter_updates
/gazebo_ros_control/pid_gains/panda_joint4/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint4/parameter_updates
/gazebo_ros_control/pid_gains/panda_joint5/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint5/parameter_updates
/gazebo_ros_control/pid_gains/panda_joint6/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint6/parameter_updates
/gazebo_ros_control/pid_gains/panda_joint7/parameter_descriptions
/gazebo_ros_control/pid_gains/panda_joint7/parameter_updates
/joint_states
/panda_controller/command
/panda_controller/follow_joint_trajectory/cancel
/panda_controller/follow_joint_trajectory/feedback
/panda_controller/follow_joint_trajectory/goal
/panda_controller/follow_joint_trajectory/result
/panda_controller/follow_joint_trajectory/status
/panda_controller/state
/rosout
/rosout_agg
/tf
/tf_static
```

### /panda_controller/command
```bash
header: 
  seq: 1
  stamp: 
    secs: 0
    nsecs:         0
  frame_id: ''
joint_names: 
  - panda_joint1
  - panda_joint2
  - panda_joint3
  - panda_joint4
  - panda_joint5
  - panda_joint6
  - panda_joint7
points: 
  - 
    positions: [1.57, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocities: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    accelerations: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    effort: []
    time_from_start: 
      secs: 3
      nsecs:         0
---

```
