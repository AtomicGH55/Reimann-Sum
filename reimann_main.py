import matplotlib.pyplot as plt
import numpy as np

def polynomial(counter):

    polynomial = counter**3 +3*counter**2 - 10

    return polynomial

def left_sum(y_points, seg_len):
    del y_points[len(y_points)-1]
    left_area = 0
    for i in range(len(y_points)):
        current_area = y_points[i]*seg_len
        print(current_area)
        left_area = left_area + current_area

    return left_area

def right_sum(y_points, seg_len):
    del y_points[0]
    right_area = 0
    for i in range(len(y_points)):
        current_area = y_points[i]*seg_len
        print(current_area)
        right_area = right_area + current_area

    return right_area

def mid_sum(x_points, seg_len):
    mid_area = 0
    for i in range(len(x_points)-1):
        current_area = (polynomial((x_points[i]+x_points[i+1])/2))*seg_len
        print(current_area)
        mid_area = mid_area + current_area

    return mid_area

def trap_sum(y_points, seg_len):
    trap_area = 0
    for i in range(len(y_points)):
        current_area = y_points[i]*(seg_len/2)
        print(current_area)
        trap_area = trap_area + current_area
    del y_points[len(y_points)-1]
    del y_points[0]
    for j in range(len(y_points)):
        current_area = y_points[j]*(seg_len/2)
        print(current_area)
        trap_area = trap_area + current_area

    return trap_area

def main():

    fig, ax = plt.subplots()
    x_points = []
    y_points = []
    seg_len = (1/10)
    
    min_x = -10
    max_x = 10
    counter = min_x

    while counter <= max_x:

            poly_point = polynomial(counter)

            x_points.append(counter)
            y_points.append(poly_point)

            counter = counter + seg_len
            
            ax.plot(x_points, y_points)
    x_axis = [min_x, max_x]
    seg_ammount = 4
    seg_len = (max_x-min_x)/seg_ammount
    
    
    x_points = []
    y_points = []
    left_side_x = []
    left_side_y = []
    right_side_x = []
    right_side_y = []
    top_x = []
    top_y = []

    counter = min_x

    sum_choice = input("Type r for Right, l for Left, m for Mid, t for Trap: ")

    if sum_choice == "r":

        while counter <= max_x:

            poly_point = polynomial(counter)

            x_points.append(counter)
            y_points.append(poly_point)

            counter = counter + seg_len
            
            ax.plot(x_points, y_points, "ro")
        print(y_points)
        area = right_sum(y_points, seg_len)
        #del x_points[0]
        #del y_points[0]
        for a in range(seg_ammount):
            print(a)
            left_side_x.append(x_points[a])
            left_side_x.append(x_points[a])
            left_side_y.append(0)
            left_side_y.append(y_points[a])
            right_side_x.append(x_points[a+1])
            right_side_x.append(x_points[a+1])
            right_side_y.append(0)
            right_side_y.append(y_points[a])
            top_x.append(x_points[a])
            top_x.append(x_points[a+1])
            top_y.append(y_points[a])
            top_y.append(y_points[a])
            print(left_side_x)
            print(left_side_y)
            print(right_side_x)
            print(right_side_y)
            print(top_x)
            print(top_y)

            ax.plot(left_side_x, left_side_y, "g")
            ax.plot(right_side_x, right_side_y, "g")
            ax.plot(top_x, top_y, "g")

            left_side_x = []
            left_side_y = []
            right_side_x = []
            right_side_y = []
            top_x = []
            top_y = []

    elif sum_choice == "l":
        while counter <= max_x:

            poly_point = polynomial(counter)

            x_points.append(counter)
            y_points.append(poly_point)

            counter = counter + seg_len
            
            ax.plot(x_points, y_points, "ro")
        print(y_points)
        area = left_sum(y_points, seg_len)

        for a in range(seg_ammount):
            print(a)
            left_side_x.append(x_points[a])
            left_side_x.append(x_points[a])
            left_side_y.append(0)
            left_side_y.append(y_points[a])
            right_side_x.append(x_points[a+1])
            right_side_x.append(x_points[a+1])
            right_side_y.append(0)
            right_side_y.append(y_points[a])
            top_x.append(x_points[a])
            top_x.append(x_points[a+1])
            top_y.append(y_points[a])
            top_y.append(y_points[a])
            print(left_side_x)
            print(left_side_y)
            print(right_side_x)
            print(right_side_y)
            print(top_x)
            print(top_y)

            ax.plot(left_side_x, left_side_y, "g")
            ax.plot(right_side_x, right_side_y, "g")
            ax.plot(top_x, top_y, "g")

            left_side_x = []
            left_side_y = []
            right_side_x = []
            right_side_y = []
            top_x = []
            top_y = []

    elif sum_choice == "m":
        while counter <= max_x:

            poly_point = polynomial(counter)

            x_points.append(counter)
            y_points.append(poly_point)

            counter = counter + seg_len
            
            ax.plot(x_points, y_points, "ro")
        print(y_points)
        area = mid_sum(x_points, seg_len)

        del x_points[0]
        del y_points[0]

        for a in range(seg_ammount-1):
            print(a)
            left_side_x.append(x_points[a]-(seg_len/2))
            left_side_x.append(x_points[a]-(seg_len/2))
            left_side_y.append(0)
            left_side_y.append(y_points[a])
            right_side_x.append(x_points[a+1]-(seg_len/2))
            right_side_x.append(x_points[a+1]-(seg_len/2))
            right_side_y.append(0)
            right_side_y.append(y_points[a])
            top_x.append(x_points[a]-(seg_len/2))
            top_x.append(x_points[a+1]-(seg_len/2))
            top_y.append(y_points[a])
            top_y.append(y_points[a])
            print(left_side_x)
            print(left_side_y)
            print(right_side_x)
            print(right_side_y)
            print(top_x)
            print(top_y)

            ax.plot(left_side_x, left_side_y, "g")
            ax.plot(right_side_x, right_side_y, "g")
            ax.plot(top_x, top_y, "g")

            left_side_x = []
            left_side_y = []
            right_side_x = []
            right_side_y = []
            top_x = []
            top_y = []

    elif sum_choice == "t":
        while counter <= max_x:

            poly_point = polynomial(counter)

            x_points.append(counter)
            y_points.append(poly_point)

            counter = counter + seg_len
            
            ax.plot(x_points, y_points, "ro")
        print(y_points)
        for a in range(seg_ammount):
            print(a)
            left_side_x.append(x_points[a])
            left_side_x.append(x_points[a])
            left_side_y.append(0)
            left_side_y.append(y_points[a])
            right_side_x.append(x_points[a+1])
            right_side_x.append(x_points[a+1])
            right_side_y.append(0)
            right_side_y.append(y_points[a+1])
            top_x.append(x_points[a])
            top_x.append(x_points[a+1])
            top_y.append(y_points[a])
            top_y.append(y_points[a+1])
            print(left_side_x)
            print(left_side_y)
            print(right_side_x)
            print(right_side_y)
            print(top_x)
            print(top_y)

            ax.plot(left_side_x, left_side_y, "g")
            ax.plot(right_side_x, right_side_y, "g")
            ax.plot(top_x, top_y, "g")

            left_side_x = []
            left_side_y = []
            right_side_x = []
            right_side_y = []
            top_x = []
            top_y = []

        area = trap_sum(y_points, seg_len)
        
    ax.plot(x_axis, [0,0])
    print("Area =", area)
    plt.show()

if __name__ == '__main__':
    main()

