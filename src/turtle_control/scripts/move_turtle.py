#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
# Este script mueve una tortuga en el entorno de ROS utilizando el tópico /turtle1/cmd_vel
# Asegúrate de que el paquete 'turtlesim' esté instalado y en ejecución
# Puedes iniciar el entorno de turtlesim con el siguiente comando:
# rosrun turtlesim turtlesim_node
# Luego, ejecuta este script en otra terminal con:
# rosrun turtle_control move_turtle.py
# Asegúrate de que el paquete 'turtle_control' esté creado y configurado correctamente
# en tu espacio de trabajo de ROS.
# Este script mueve la tortuga hacia adelante y gira en un bucle   
def mover_tortuga():
    rospy.init_node('mover_tortuga', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)  # 2 Hz

    cmd = Twist()
    cmd.linear.x = 0.5    # velocidad hacia adelante
    cmd.angular.z = 0.5   # velocidad de giro

    while not rospy.is_shutdown():
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover_tortuga()
    except rospy.ROSInterruptException:
        pass