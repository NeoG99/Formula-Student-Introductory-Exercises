#!/usr/bin/env python

#

import rospy
from matplotlib import pyplot as plt
from functionplotter.msg import valuepair # Custom message type of two floats

class visualize():
    def __init__(self, xlabel = None, ylabel = None, title = None, xlimit = [], ylimit = []):
        self.x = xlabel
        self.y = ylabel
        self.t = title
        self.xl = xlimit
        self.yl = ylimit

        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.title(self.t)
        plt.xlim(self.xl)
        plt.ylim(self.yl)        

        # Characteristics of the scatter-plot. Can all theoretically be updated as the program runs

    def update(self, data):
        rospy.loginfo("t: %f h(t): %f", data.t, data.h) # Prints out recieved date to terminal
        
        if  (self.xl[1] < data.t) or (self.yl[1] < data.h):
            plt.autoscale(enable=True, axis='both', tight=None) # Rescales window to fit unexpectedly large function values. Does not work for negative values.
        
        plt.scatter(data.t, data.h, color = "blue") # Plots a blue dot according to recieved data
        plt.pause(0.001)
    
    def show(self):
        plt.show() # Necessary to make the graph display properly


def listener():

    functionvalues = visualize("t", "h", "KTHFS-testfunktion", [0,1], [0, 2000]) # Initializing the functionvalues object 

    rospy.init_node("subscriber", anonymous=True)
    rospy.Subscriber("functionvalue", valuepair, functionvalues.update)
    rospy.loginfo("Plotter node has started!")
    
    functionvalues.show()

    rospy.spin()
    
  
if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass