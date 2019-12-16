#!/usr/bin/env python
import rospy
import turtlesim
import os
import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill

PI = 3.1415926535897

from geometry_msgs.msg import Twist

def move_fwd(dist):

    speed = 2
    t0 = rospy.Time.now().to_sec()

    vel_msg.linear.x = speed
    current_distance = 0

    while(current_distance < dist):
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance= speed*(t1-t0)
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

def rotate(angle):

    angular_speed = abs(angle)/angle*30*2*PI/360
    angle_deg = angle*2*PI/360

    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    vel_msg.angular.z = angular_speed

    while(abs(current_angle) < abs(angle_deg)):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def kill_turtle():
    rospy.wait_for_service('kill')
    try:
        delete_turtle = rospy.ServiceProxy('kill', Kill)
        delete_turtle('turtle1')
    except rospy.ServiceException, e:
            print "Service call failed to kill turtle: %s" % e

def spawn_turtle(x, y):
    rospy.wait_for_service('spawn')
    try:
        create_turtle = rospy.ServiceProxy('spawn', Spawn)
        create_turtle(x, y, 0, 'turtle1')
    except rospy.ServiceException, e:
            print "Service call failed to kill turtle: %s" % e

def draw_2():
    move_fwd(1.3)
    rotate(-90)
    move_fwd(1)
    rotate(-90)
    move_fwd(1)
    rotate(90)
    move_fwd(1)
    rotate(90)
    move_fwd(1)

def draw_4():
    rotate(-93)
    move_fwd(1)
    rotate(90)
    move_fwd(1)
    rotate(90)
    move_fwd(1)
    rotate(180)
    move_fwd(2)

def draw_8():
    rotate(-93)
    move_fwd(2)
    rotate(90)
    move_fwd(1)
    rotate(90)
    move_fwd(2)
    rotate(90)
    move_fwd(1)
    rotate(90)
    move_fwd(1)
    rotate(90)
    move_fwd(1)

if __name__ == '__main__':
    try:
        rospy.init_node('drawer', anonymous=True)
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()

        kill_turtle()
        spawn_turtle(0.5, 7)
        draw_2()
        kill_turtle()
        spawn_turtle(2, 7)
        draw_4()
        kill_turtle()
        spawn_turtle(3.5, 7)
        draw_2()
        kill_turtle()
        spawn_turtle(5, 7)
        draw_2()
        kill_turtle()
        spawn_turtle(6.5, 7)
        draw_8()
        kill_turtle()
        spawn_turtle(8, 7)
        draw_4()

    except rospy.ROSInterruptException: passs
