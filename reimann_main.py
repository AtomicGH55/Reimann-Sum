import matplotlib.pyplot as plt

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

def mid_sum(y_points, seg_len):
    del y_points[len(y_points)-1]
    mid_area = 0
    for i in range(len(y_points)-1):
        current_area = ((y_points[i]+y_points[i+1])/2)*seg_len
        print(current_area)
        mid_area = mid_area + current_area



    return mid_area

def main():

    fig, ax = plt.subplots()

    min_x = -10
    max_x = 10
    seg_ammount = 4
    seg_len = (max_x-min_x)/seg_ammount
    
    x_points = []
    y_points = []

    counter = min_x

    while counter <= max_x:

        polynomial = counter**3 +3*counter**2 - 10

        x_points.append(counter)
        y_points.append(polynomial)

        counter = counter + seg_len
        
        ax.plot(x_points, y_points)
        ax.plot(x_points, y_points, "ro")
    print(y_points)


    area = mid_sum(y_points, seg_len)


    print("Area =", area)
    plt.show()

if __name__ == '__main__':
    main()

