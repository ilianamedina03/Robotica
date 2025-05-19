#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def mover_tortugas():
    rospy.init_node('mover_tortugas', anonymous=True)
    pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    start_time = rospy.get_time()

    while not rospy.is_shutdown():
        elapsed = rospy.get_time() - start_time

        cmd1 = Twist()
        cmd2 = Twist()

        if elapsed % 4 < 2:
            # Ambas tortugas avanzan
            cmd1.linear.x = 0.5
            cmd1.angular.z = 0.0
            cmd2.linear.x = 0.3
            cmd2.angular.z = 0.0
        else:
            # Ambas tortugas giran (en sentidos opuestos para distinguir)
            cmd1.linear.x = 0.0
            cmd1.angular.z = 1.0
            cmd2.linear.x = 0.0
            cmd2.angular.z = -1.0

        pub1.publish(cmd1)
        pub2.publish(cmd2)

        rate.sleep()

if __name__ == '__main__':
    try:
        mover_tortugas()
    except rospy.ROSInterruptException:
        pass
# This script moves two turtles in a simulation environment.
# It alternates between moving them forward and rotating them in opposite directions.
# The turtles are controlled using the /turtle1/cmd_vel and /turtle2/cmd_vel topics.
# Make sure to have the turtlesim package installed and running.
# You can start the turtlesim environment with:
# rosrun turtlesim turtlesim_node
# Then, run this script in another terminal with:
# rosrun turtle_control move_two_turtles.py 