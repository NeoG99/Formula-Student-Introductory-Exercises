#!/usr/bin/env python2

# This node will recieve the int from topic "gumbel", divide by q, with q = 0.15,
# and publish the result to topic "results" with rate 20 Hz

# The code seems to work as intended, but there are slight rounding errors, as well as "results" not publishing the first value of k (0)

import rospy
from std_msgs.msg import Int16

def publish(number):
    pub = rospy.Publisher("results", Int16, queue_size = 10)
    rate = rospy.Rate(1)
    q = 0.15
    k = number.data
    y = k/q

    pub.publish(y)
    rate.sleep()    


def listener():
    rospy.init_node("NodeB", anonymous=True)
    rospy.Subscriber("gumbel", Int16, publish)
    rospy.loginfo("Subscriber Node has started, now publishing!")

    rospy.spin()
  

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass