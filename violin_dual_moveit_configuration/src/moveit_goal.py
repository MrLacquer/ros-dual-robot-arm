#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def move_to_goal():

    # Set-up
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

    # declarations
    robot = moveit_commander.RobotCommander()
    groupL = moveit_commander.MoveGroupCommander("left_arm" )
    groupR = moveit_commander.MoveGroupCommander("right_arm")

    # set target for left arm
    targetL = geometry_msgs.msg.Pose()
    targetL.orientation.w = 1.0
    targetL.position.x = 0.2
    targetL.position.y = 0.2
    targetL.position.z = 0.2
    groupL.set_joint_value_target(targetL)

    planL = groupL.plan()

    groupL.execute(planL)

    groupL.clear_pose_targets()

    # set target for right arm
    targetR = geometry_msgs.msg.Pose()
    targetR.orientation.w = 1.0
    targetR.position.x =  0.2
    targetR.position.y = -0.2
    targetR.position.z =  0.2
    groupR.set_joint_value_target(targetR)

    planR = groupR.plan()

    groupR.clear_pose_targets()

    groupR.execute(planR)


print "============ Waiting for RVIZ..."
rospy.sleep(10)
print "============ Starting tutorial "
move_to_goal()