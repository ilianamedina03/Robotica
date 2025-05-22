#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

# Variables globales para guardar la posición actual de cada tortuga
pose_turtle1 = None
pose_turtle2 = None

def callback_turtle1(pose):
    global pose_turtle1, pose_turtle2
    pose_turtle1 = pose
    if pose_turtle2 is not None:
        print_pose()

def callback_turtle2(pose):
    global pose_turtle1, pose_turtle2
    pose_turtle2 = pose
    if pose_turtle1 is not None:
        print_pose()

def print_pose():
    # Imprime las posiciones de ambas tortugas en una línea
    rospy.loginfo("[TURTLE1] x=%.2f, y=%.2f, θ=%.2f | [TURTLE2] x=%.2f, y=%.2f, θ=%.2f",
                  pose_turtle1.x, pose_turtle1.y, pose_turtle1.theta,
                  pose_turtle2.x, pose_turtle2.y, pose_turtle2.theta)

def leer_pose_dos_tortugas():
    rospy.init_node('leer_pose_dos_tortugas', anonymous=True)

    rospy.Subscriber('/turtle1/pose', Pose, callback_turtle1)
    rospy.Subscriber('/turtle2/pose', Pose, callback_turtle2)

    rospy.spin()

if __name__ == '__main__':
    leer_pose_dos_tortugas()
