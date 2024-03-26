import matplotlib.pyplot as plt





def main():

    fig, ax = plt.subplots()
    counter = -20
    x_points = []
    y_points = []

    #reimann_style = input('Type "L" for left, "R" for right, "M" for middle, and "T" for trapazoid: ')

    while counter < 21:
        
        current_output = counter^2

        x_points.append(counter)
        y_points.append(current_output)
        
        counter = counter + 1
    print(x_points)
    print(y_points)
        
    ax.plot(x_points, y_points)
    plt.show()
        

if __name__ == '__main__':
    main()
   