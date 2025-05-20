#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move_both_turtles():
    rospy.init_node('move_heart_and_tree', anonymous=True)

    pub_heart = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub_tree = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(20)
    start_time = rospy.get_time()

    twist_heart = Twist()
    twist_tree = Twist()

    while not rospy.is_shutdown():
        t = rospy.get_time() - start_time
        if t > 10:
            break

        # Movimiento tipo corazón (aproximado)
        twist_heart.linear.x = 1.5 * abs(math.sin(t))
        twist_heart.angular.z = 2 * math.cos(t)

        # Movimiento tipo árbol: tronco + ramas (más continuo)
        twist_tree.linear.x = 0.5 + 0.3 * math.sin(2 * t)
        twist_tree.angular.z = 1.5 * math.sin(t)

        pub_heart.publish(twist_heart)
        pub_tree.publish(twist_tree)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_both_turtles()
    except rospy.ROSInterruptException:
        pass
