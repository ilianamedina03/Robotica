#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill

def move_two_shapes_loop():
    rospy.init_node('move_two_shapes_loop')

    # Matar tortuga2 si ya existía
    try:
        rospy.wait_for_service('/kill', timeout=2.0)
        kill_turtle = rospy.ServiceProxy('/kill', Kill)
        kill_turtle('turtle2')
    except:
        pass  # No existía, seguimos

    # Crear tortuga2 en otra posición (lejos de turtle1)
    rospy.wait_for_service('/spawn')
    try:
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        spawn_turtle(8.0, 8.0, 0.0, 'turtle2')
    except rospy.ServiceException as e:
        rospy.logwarn("No se pudo crear turtle2: %s" % e)

    # Publicadores
    pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    # Duraciones y velocidades precisas para dibujar las figuras
    square_linear_speed = 1.0
    square_turn_speed = 1.57  # ~90 grados en 1s
    square_side_duration = 1.5
    square_turn_duration = 1.0

    triangle_linear_speed = 1.0
    triangle_turn_speed = 2.09  # ~120 grados en 1s
    triangle_side_duration = 1.5
    triangle_turn_duration = 1.0

    start_time = rospy.get_time()

    while not rospy.is_shutdown():
        now = rospy.get_time()
        elapsed_sq = (now - start_time) % ((square_side_duration + square_turn_duration) * 4)
        elapsed_tr = (now - start_time) % ((triangle_side_duration + triangle_turn_duration) * 3)

        # ----------- Turtle 1: Cuadrado -------------
        twist1 = Twist()
        if elapsed_sq % (square_side_duration + square_turn_duration) < square_side_duration:
            twist1.linear.x = square_linear_speed
            twist1.angular.z = 0.0
        else:
            twist1.linear.x = 0.0
            twist1.angular.z = square_turn_speed

        # ----------- Turtle 2: Triángulo -------------
        twist2 = Twist()
        if elapsed_tr % (triangle_side_duration + triangle_turn_duration) < triangle_side_duration:
            twist2.linear.x = triangle_linear_speed
            twist2.angular.z = 0.0
        else:
            twist2.linear.x = 0.0
            twist2.angular.z = triangle_turn_speed

        pub1.publish(twist1)
        pub2.publish(twist2)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_two_shapes_loop()
    except rospy.ROSInterruptException:
        pass
