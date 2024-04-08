import matplotlib.pyplot as plt

def main():

    fig, ax = plt.subplots()

    seg_len = 1
    counter = -10
    x_points = []
    y_points = []

    

    while counter <= 10:

        polynomial = counter**2 + 3*counter + 4

        x_points.append(counter)
        y_points.append(polynomial)

        counter = counter + 1

        ax.plot(x_points, y_points, "ro")


    #left_area = left_sum(y_points, seg_len)
    print(len(y_points))
    plt.show()

if __name__ == '__main__':
    main()

def left_sum(y_points, seg_len):
    for i in y_points:
        left_area = y_points*seg_len

    left_area = left_area - (y_points[len(y_points)-1])