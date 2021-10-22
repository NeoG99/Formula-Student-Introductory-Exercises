This is my crude attempt at a program that plots a function, live, with data coming from a ROS publisher node. The publisher node sends a custom message containing two Float32 values, an input variable and a function output, at a rate of 10 Hz, and with the input-variable increasing by 0.01 per iteration. The subscriber takes this custom message and uses it to update a matplotlib scatter-plot, contained within an object named "functionplotter". The plot initializes with set axle-limits, but will switch to auto-scale mode if the values it recieves are greater than expected. This does not currently work with negative values.

To run the "program" simply start the subscriber and publisher, preferably in that order, located under src/functionplotter/scripts.
 

  
