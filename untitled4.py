import matplotlib.pyplot as plt

def midPointCircleDraw(x_centre, y_centre, r):
    """Draws a circle using the Midpoint Circle Algorithm."""
    
    x = r
    y = 0

    # Initialize the plot
    plt.figure(figsize=(6, 6))  # Adjust figure size as needed
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Midpoint Circle Algorithm')
    plt.grid(True)

    # Plotting the initial points
    plt.plot(x + x_centre, y + y_centre, 'ro')  # Red circle marker
    plt.plot(x + x_centre, -y + y_centre, 'ro')
    plt.plot(y + x_centre, x + y_centre, 'ro')
    plt.plot(-y + x_centre, x + y_centre, 'ro')

    # Initializing the value of P
    P = 1 - r

    while x > y:
        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if (x < y):
            break

        # Plotting the generated points and their reflections
        plt.plot(x + x_centre, y + y_centre, 'ro')
        plt.plot(-x + x_centre, y + y_centre, 'ro')
        plt.plot(x + x_centre, -y + y_centre, 'ro')
        plt.plot(-x + x_centre, -y + y_centre, 'ro')

        if x != y:
            plt.plot(y + x_centre, x + y_centre, 'ro')
            plt.plot(-y + x_centre, x + y_centre, 'ro')
            plt.plot(y + x_centre, -x + y_centre, 'ro')
            plt.plot(-y + x_centre, -x + y_centre, 'ro')

    # Show the plot
    plt.axis('equal')  # Ensure circle appears round
    plt.show()

# Driver Code
if __name__ == '__main__':
    # To draw a circle of radius 3 centered at (0, 0)
    midPointCircleDraw(0, 0, 3)