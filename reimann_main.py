import matplotlib.pyplot as plt





def main():

    fig, ax = plt.subplots()
    counter = -20
    x_points = []
    y_points = []

    current_function = counter^2
    reimann_style = input('Type "L" for left, "R" for right, "M" for middle, and "T" for trapazoid: ')

    while counter < 20:
        
        current_output = current_function

        x_points.append(counter)
        y_points.append(current_output)
        
        counter = counter + 1
        
    ax.plot(x_points, y_points)
    plt.show()
        

if __name__ == '__main__':
    main()
   