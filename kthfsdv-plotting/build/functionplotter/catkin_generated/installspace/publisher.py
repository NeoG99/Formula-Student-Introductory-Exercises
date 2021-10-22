#!/usr/bin/env python2

# This is a publisher node that publishes the output of a function one point at the time

import rospy
import numpy as np
from functionplotter.msg import valuepair # Custom message of two floats

def functionpublisher():
    pub = rospy.Publisher("functionvalue", valuepair, queue_size = 10)
    rospy.init_node("publisher", anonymous = True)
    rate = rospy.Rate(10) # Sets the rate to 10 Hz
    rospy.loginfo("Publisher node has started, now sending function values!")

    resolution = 0.01
    length = 200 # I know this is supposed to be 100, but I will leave it at 200 to demonstrate functionalities of the subsriber node
    t = 0.0
    i = 0
    lambd  = 5*np.sin(2*np.pi*t)
    h = 3*np.pi*np.exp(-lambd)

    while not rospy.is_shutdown():
        msg = valuepair()
        msg.t = t
        msg.h = h
        
        pub.publish(msg)
        
        lambd  = 5*np.sin(2*np.pi*t)
        h = 10 * 3*np.pi*np.exp(-lambd)
        
        t = t + resolution
        i = i+1
       
        if i == length + 1: # Breaks the loop when last function value is sent
            break
        
        rate.sleep()
    
    rospy.on_shutdown(shutdown)

def shutdown():
    print("Node shutting down!")


if __name__ == "__main__":
    try:
        functionpublisher()
    except rospy.ROSInterruptException:
        pass

