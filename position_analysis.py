from math import *
from multiprocessing.sharedctypes import Value
from pickletools import read_float8
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

def q4_10_c():
    print("*"*39 + " Question 4.10 Part C " + "*"*39 + "\n")

    #Given Values
    a_meters=3
    b_meters=8
    c_meters=2

    theta_2_degrees_array = []
    theta_3_degrees_array = []
    d_meters_array = []

    print("Theta_2\t\tTheta_3\t\td")
    for theta_2_degrees in range(-30,330,5):
        theta_2_radians = theta_2_degrees*pi / 180
        theta_3_radians = asin( (a_meters*sin(theta_2_radians) - c_meters) / b_meters )
        d_meters = a_meters*cos(theta_2_radians) - b_meters*cos(theta_3_radians)
        theta_3_degrees = degrees(theta_3_radians)

        theta_2_degrees_array.append(theta_2_degrees)
        theta_3_degrees_array.append(theta_3_degrees)
        d_meters_array.append(d_meters)

        print("%3.3f\t\t%3.3f\t\t%3.3f" % (theta_2_degrees, theta_3_degrees, d_meters) )

    # Theta 3
    x = theta_2_degrees_array
    y = theta_3_degrees_array
    plt.plot(x, y, 'o', color='black')
    plt.title("Theta 3")
    plt.ylabel("Theta_3 (degrees)")
    plt.show()

    # D
    y = d_meters_array
    plt.plot(x, y, 'o', color='black')
    plt.title("D")
    plt.ylabel("D (meters)")
    plt.show()

    print("\n" + "*"*100)

def winshield_wiper(a, b, c, d):
    print("*"*41 + " Windshield Wiper " + "*"*41 + "\n")

    #Given Values
    a_meters=a #1.5
    b_meters=b #13
    c_meters=c #2.2
    d_meters=d #13

    k_1 = d_meters/a_meters
    k_2 = d_meters/c_meters
    k_3 = ( a_meters**2 - b_meters**2 + c_meters**2 + d_meters**2 ) / ( 2 * a_meters * c_meters )
    k_4 = d_meters/b_meters
    k_5 = ( c_meters**2 - d_meters**2 - a_meters**2 - b_meters**2 ) / ( 2 * a_meters * b_meters )

    theta_2_degrees_array = []
    theta_3_p_degrees_array = []
    theta_3_n_degrees_array = []
    theta_4_p_degrees_array = []
    theta_4_n_degrees_array = []
    l_degrees_array = []

    theta_4_max = 0
    theta_4_min = 360
    l_min = 90

    # Part A - Mathematical Analysis

    print("\n" + "*"*8 + " Part A " + "*"*8 + "\n")

    print("Theta_2\tTheta_3 Open\tTheta_3 Cross\tTheta_4 Open\tTheta_4 Cross\tlambda")
    for theta_2_degrees in range(0,360,5):

        theta_2_radians = radians(theta_2_degrees)

        A = cos(theta_2_radians) - k_1 - k_2 * cos(theta_2_radians) + k_3
        B = -2 * sin(theta_2_radians)
        C = k_1 - (k_2 + 1) * cos(theta_2_radians) + k_3

        D = cos(theta_2_radians) - k_1 + k_4 * cos(theta_2_radians) + k_5
        E = B
        F = k_1 + (k_4 - 1) * cos(theta_2_radians) + k_5
        try:
            theta_4_p_radians = 2*atan( (-B + sqrt( B**2 - 4*A*C )) / ( 2*A ) )
            theta_4_p_degrees = degrees(theta_4_p_radians)

            theta_4_n_radians = 2*atan( (-B - sqrt( B**2 - 4*A*C )) / ( 2*A ) )
            theta_4_n_degrees = degrees(theta_4_n_radians)

            theta_3_p_radians = 2*atan( (-E + sqrt( E**2 - 4*D*F )) / ( 2*D ) )
            theta_3_p_degrees = degrees(theta_3_p_radians)

            theta_3_n_radians = 2*atan( (-E - sqrt( E**2 - 4*D*F )) / ( 2*D ) )
            theta_3_n_degrees = degrees(theta_3_n_radians)

            if abs(theta_3_p_radians-theta_4_p_radians) < pi/2:
                l_radians = abs(theta_3_p_radians-theta_4_p_radians)
            else:
                l_radians = pi - abs(theta_3_p_radians-theta_4_p_radians)

            l_degrees = degrees(l_radians)

            if l_degrees < l_min:
                l_min = l_degrees
            if theta_4_n_degrees > theta_4_max:
                theta_4_max = theta_4_n_degrees
            elif theta_4_n_degrees < theta_4_min:
                theta_4_min = theta_4_n_degrees
            
            theta_2_degrees_array.append(theta_2_degrees)
            theta_3_p_degrees_array.append(theta_3_p_degrees)
            theta_3_n_degrees_array.append(theta_3_n_degrees)
            theta_4_p_degrees_array.append(theta_4_p_degrees)
            theta_4_n_degrees_array.append(theta_4_n_degrees)
            l_degrees_array.append(l_degrees)
  
            print( "%3.0f\t   %3.3f\t    %3.3f\t    %3.3f\t  %3.3f\t   %3.3f" % 
                (theta_2_degrees,theta_3_n_degrees,theta_3_p_degrees,theta_4_n_degrees,theta_4_p_degrees,l_degrees) )
        except ValueError:
            print("%3.0f\t" % (theta_2_degrees) + "-"*73)

    # Part B - Graphical Analysis
    print("\n" + "*"*8 + " Part B " + "*"*8 + "\n - See Graphs")

    #Theta 4
    x = theta_2_degrees_array
    y = theta_4_p_degrees_array
    plt.plot(x, y, 'o', color='black')
    y = theta_4_n_degrees_array
    plt.plot(x, y, 'o', color='blue')
    plt.title("Theta 4")
    plt.xlabel("Theta_2")
    plt.ylabel("Theta_4 (degrees)    (Cross:Black Open:Blue)")
    plt.show()

    #Theta 3
    y = theta_3_p_degrees_array
    plt.plot(x, y, 'o', color='black')
    y = theta_3_n_degrees_array
    plt.plot(x, y, 'o', color='blue')
    plt.title("Theta 3")
    plt.ylabel("Theta_3 (degrees)    (Cross:Black Open:Blue)")
    plt.show()

    #Lambda
    y = l_degrees_array
    plt.plot(x, y, 'o', color='black')
    plt.title("Lambda")
    plt.ylabel("Lambda (degrees)")
    plt.show()

    # Part C - Transmission Angle
    print("\n" + "*"*8 + " Part C " + "*"*8 + "\n - Minimum Transmission angle: %0.3f" % l_min)
    if l_min >= 40:
        print(" -- Remained above 40...no binding.")
    else:
        print(" -- Dropped under 40...may cause binding.")

    # Part D - Theta 4 Min and Max
    print("\n" + "*"*8 + " Part D " + "*"*8 + "\n - Theta 4 Max: %0.3f\t\tTheta 4 Min: %0.3f\n - Total Sweep: %0.3f" % (theta_4_max, theta_4_min, theta_4_max-theta_4_min) )

    print("\n" + "*"*100)
#windshield_wiper()

if __name__ == "__main__":
    q4_10_c()
    winshield_wiper(a=1.5,b=13,c=2.2,d=13)
    winshield_wiper(a=4.5,b=14,c=3.1,d=13)