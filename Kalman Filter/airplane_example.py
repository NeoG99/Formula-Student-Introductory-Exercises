import numpy as np
from matplotlib import pyplot as plt

kalman_prediction_x = list()
kalman_prediction_v = list()

# Observations

x = np.array([4000, 4260, 4550, 4860, 5110])
v = np.array([280, 282, 285, 286, 290])

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

for i in range(2):

    # The predicted state

    A = np.matrix([[1, delta_t], [0,1]])
    x_k_previous = np.matrix([[x[i]], [v[i]]])
    B = np.matrix([[0.5*delta_t ** 2], [delta_t]])
    u_k = a_x
    w_k = 0

    x_k = A * x_k_previous + B * u_k + w_k

    # The initial process covariance matrix

    P_k_previous = np.matrix([[delta_P_x ** 2, delta_P_x * delta_P_v], [delta_P_x * delta_P_v, delta_P_v ** 2]]) # Cross terms usually set to zero for some reason
    # P_k_previous = np.matrix([[delta_P_x ** 2, 0], [0, delta_P_v ** 2]])
    # The predicted process covariance matrix

    Q_k = 0

    P_k = A * P_k_previous * np.transpose(A) + Q_k

    # The Kalman gain

    R = np.matrix([[delta_x ** 2, 0], [0, delta_v ** 2]])

    K = P_k * np.identity(2) / (np.identity(2) * P_k * np.identity(2) + R)

    # The new observation

    Z_k = 0 # Error in electronic measuring equipment, for example

    y_k_previous = np.matrix([[x[1]], [v[1]]])

    y_k = np.identity(2) * y_k_previous + Z_k

    # Calculate the current state

    x_k = x_k + K * (y_k - np.identity(2) * x_k) # Doesn't give quite the correct answer, but this most likely has to do with how he does it in the video

    kalman_prediction_x.append(x_k[0])
    kalman_prediction_v.append(x_k[1])
    
    # Updating the process covariance matrix

    P_k_previous = (np.identity(2) - K * np.identity(2)) * P_k_previous

    x_k_previous = x_k


plt.scatter(x, v)
plt.scatter(kalman_prediction_x, kalman_prediction_v) # Well something is very wrong here. Not sure what.
plt.show()

print(kalman_prediction_x)
print(kalman_prediction_v)


