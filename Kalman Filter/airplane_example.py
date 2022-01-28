import numpy as np
from matplotlib import pyplot as plt

kalman_prediction_x = list()
kalman_prediction_v = list()

# Observations

x = np.array([4000, 4260, 4550, 4860, 5110, 5500, 5800, 6120, 6240])
v = np.array([280, 282, 285, 286, 288, 287, 289, 290, 291])

# Initial conditions

a_x = 2 # meters/second^2
v_x = 280 # meters/second
delta_t = 1 
delta_x = 25 

# Process error in process covariance matrix

delta_P_x = 20 # meters
delta_P_v = 5 # meters/second

# Observation errors

delta_x = delta_x
delta_v = 6 # meters/second

for i in range(len(x)):

    # The predicted state

    A = np.matrix([[1, delta_t], [0,1]])
    x_k_previous = np.matrix([[x[i]], [v[i]]])
    B = np.matrix([[0.5*delta_t ** 2], [delta_t]])
    u_k = a_x
    w_k = 0 # Noise in estimation. Set to 0 for now

    x_k = A * x_k_previous + B * u_k + w_k

    # We predict the future state based on the input variables and the current measurement, as well as based on the "control"

    # The initial process covariance matrix

    # P_k_previous = np.matrix([[delta_P_x ** 2, delta_P_x * delta_P_v], [delta_P_x * delta_P_v, delta_P_v ** 2]]) # Cross terms usually set to zero for some reason
    P_k_previous = np.matrix([[delta_P_x ** 2, 0], [0, delta_P_v ** 2]])
    # The predicted process covariance matrix

    Q_k = 0 # Noise in covariance-matrix-prediction. Set to 0 for now.

    P_k = A * P_k_previous * np.transpose(A) + Q_k

    # The process covariance matrix represents the error in our estimation. I am still not quite sure exactly how though.

    # The Kalman gain

    R = np.matrix([[delta_x ** 2, 0], [0, delta_v ** 2]]) # Observation errors

    K = P_k * np.identity(2) / (np.identity(2) * P_k * np.identity(2) + R)
    K[0,1] = 0
    K[1, 0] = 0

    # Calculates the kalman gain, which is a measurement of the uncertainty in our estimation vs uncertainty in our measurement
    # For some reason the cross terms have to be set to 0 for anything to work. The guy in the video did not explain overly well...

    # The new observation

    Z_k = 0 # Error in electronic measuring equipment, for example

    y_k_previous = np.matrix([[x[i]], [v[i]]])

    y_k = np.identity(2) * y_k_previous + Z_k

    # Calculate the current state

    x_k = x_k + K * (y_k - np.identity(2) * x_k)

    kalman_prediction_x.append(x_k[0,0])
    kalman_prediction_v.append(x_k[1,0])

    # If E(estimation) is large then the kalman gain is small, resulting in us updating our estimated position very slightly
    # If E(measurement) is large, the kalman gain is large, and we update our prediction with a large value

    
    # Updating the process covariance matrix

    P_k_previous = (np.identity(2) - K * np.identity(2)) * P_k_previous


plt.scatter(x, v)
plt.plot(kalman_prediction_x, kalman_prediction_v, "-r")
plt.show()



