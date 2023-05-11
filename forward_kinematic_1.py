import numpy as np

# Given link lengths and joint angles
L1 = 85  # Length of link 1
L2 = 165 # Length of link 2
L3 = 155  # Length of link 3

theta1 = 613  # Joint angle 1 in radians
theta2 = 253  # Joint angle 2 in radians
theta3 = 349  # Joint angle 3 in radians

# Transformation matrix from frame 0 to frame 1
T0_1 = np.array([
    [np.cos(theta1), -np.sin(theta1), 0, 0],
    [np.sin(theta1), np.cos(theta1), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Transformation matrix from frame 1 to frame 2
T1_2 = np.array([
    [np.cos(theta2), -np.sin(theta2), 0, L1],
    [0, 0, -1, 0],
    [np.sin(theta2), np.cos(theta2), 0, 0],
    [0, 0, 0, 1]
])

# Transformation matrix from frame 2 to frame 3
T2_3 = np.array([
    [np.cos(theta3), -np.sin(theta3), 0, L2],
    [0, 0, 1, 0],
    [-np.sin(theta3), -np.cos(theta3), 0, 0],
    [0, 0, 0, 1]
])

# Transformation matrix from frame 3 to frame 4
T3_4 = np.eye(4)

# Overall transformation matrix from frame 0 to frame 4
T0_4 = np.dot(np.dot(np.dot(T0_1, T1_2), T2_3), T3_4)

# Extract the X, Y, and Z coordinates from the translation components
X = T0_4[0, 3]
Y = T0_4[1, 3]
Z = T0_4[2, 3]

print(f"X: {X}, Y: {Y}, Z: {Z}")

