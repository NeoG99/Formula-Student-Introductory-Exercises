#!/usr/bin/env python2

# Apparently it is VERY important that this little asswipe bit of code
# is at the very top of the document...

# Write a publisher node that sends a number k > 0 increasing by
# n each generation at the rate 20 Hz and where n = 4. Send it to a
# topic named "gumbel". If possible try to reduce network throughput. 
# How the fuck I am supposed to do that is as of yet unclear.
# In the last step also create a plot using rqt_plot

import rospy
from std_msgs.msg import Int16

def int_increaser():
    pub = rospy.Publisher("gumbel", Int16, queue_size = 10) # Not sure what I should use for queue_size here
    rospy.init_node("publisher", anonymous = True)
    rate = rospy.Rate(20) # Sets the rate in Hz
    rospy.loginfo("Publisher Node has started, now publishing!")

    k = 0
    n = 4

    while not rospy.is_shutdown():
        pub.publish(k)
        k = k + n
        rate.sleep()

if __name__ == "__main__":
    try:
        int_increaser()
    except rospy.ROSInterruptException:
        pass
