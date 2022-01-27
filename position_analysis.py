from math import *
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

def q4_10_c():
    print("*"*8 + " Question 4.10 Part C " + "*"*8)
    L_a=3
    L_b=8
    L_c=2
    print("Theta_2\t\tTheta_3\t\td")
    for theta_2 in range(0,360,5):
        theta_2_rad = theta_2*pi/180
        theta_3_rad=asin( (L_a*sin(theta_2_rad)-L_c)/L_b )
        d=L_a*cos(theta_2_rad) - L_b*cos(theta_3_rad)
        theta_3=theta_3_rad*180/pi
        print("%3.3f\t\t%3.3f\t\t%3.3f" % (theta_2, theta_3, d) )
    pass


if __name__ == "__main__":
    q4_10_c()