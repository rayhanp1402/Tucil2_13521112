import matplotlib.pyplot as plt
import algo

points = []

n = int(input('Dimension : '))
total_points = int(input('Total Points : '))

for i in range(total_points): # Generate random points
    points.append(algo.randomCoordinate(n))

# Check and replace duplicate points
duplicate = True
while (duplicate == True):
    duplicate = False
    for i in range(total_points):
        for j in range(total_points):
            if(i != j and points[i] == points[j]):
                duplicate = True
                points[j] = algo.randomCoordinate(n)
                
# Sorting
algo.selectionSort(points)

# Outputs the points
print('\nPoints : ')
for i in range(total_points):
    print(str(i + 1) + '. ' + str(points[i]))

# Find the closest pair of points
closest_pair = algo.divideAndConquer(points)
print('\nClosest Pairs : ')
print('Point 1 = ' + str(closest_pair[0]))
print('Point 2 = ' + str(closest_pair[1]))
print('Distance = ' + str(round(closest_pair[2], 2)))

# Visualizer
plot_color = 'blue'

if (n == 1):
    max = points[0][0]
    min = points[0][0]  # Search for minimum/leftmost and max/rightmost point
    for i in range(total_points): # Just for drawing the horizontal line
        if(points[i][0] > max):
            max = points[i][0]
        if(points[i][0] < min):
            min = points[i][0]

    plt.hlines(0, min, max, color='black')  # Draw a horizontal line
    for i in range(total_points):
        plot_color = 'blue'
        if(points[i] == closest_pair[0] or points[i] == closest_pair[1]):
            plot_color = 'orange'

        plt.scatter(points[i][0], 0, color=plot_color)

    plt.yticks([]) # Disable y-axis

elif (n == 2):
    for i in range(total_points):
        plot_color = 'blue'
        if(points[i] == closest_pair[0] or points[i] == closest_pair[1]):
            plot_color = 'orange'

        plt.scatter(points[i][0], points[i][1], color=plot_color)

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')

elif (n == 3):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(total_points):
        plot_color = 'blue'
        if(points[i] == closest_pair[0] or points[i] == closest_pair[1]):
            plot_color = 'orange'

        ax.scatter(points[i][0], points[i][1], points[i][2], color=plot_color)

    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')

plt.show()