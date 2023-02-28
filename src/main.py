import matplotlib.pyplot as plt
import time
import platform
import algo

print('=========================================================') 
print('   _____ _                     _     _____      _       ')
print('  / ____| |                   | |   |  __ \    (_)      ')
print(' | |    | | ___  ___  ___  ___| |_  | |__) |_ _ _ _ __  ')
print(' | |    | |/ _ \/ __|/ _ \/ __| __| |  ___/ _\` | | \'__| ')
print(' | |____| | (_) \__ \  __/\__ \ |_  | |  | (_| | | |    ')
print('  \_____|_|\___/|___/\___||___/\__| |_|   \__,_|_|_|    ')
print('        / _| |  __ \    (_)     | |                     ')
print('   ___ | |_  | |__) |__  _ _ __ | |_ ___                ')
print('  / _ \|  _| |  ___/ _ \| | \'_ \| __/ __|               ')
print(' | (_) | |   | |  | (_) | | | | | |_\__ \               ')
print('  \___/|_|   |_|   \___/|_|_| |_|\__|___/               ')
print('\n=========================================================\n')                           

points = []

flag = False
while(flag == False):
    try:
        n = int(input('Dimension n (n > 0) : '))
        if (n <= 0):
            print('Invalid input, n must be greater than 0')
        else:
            break
    except ValueError:
        print('Invalid input type, must be integer')

while(flag == False):
    try:
        total_points = int(input('Total Points k (k > 1) : '))
        if (total_points <= 1):
            print('Invalid input, k must be greater than 1')
        else:
            break
    except ValueError:
        print('Invalid input type, must be integer')

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
                
# Sort based on x-axis value
algo.selectionSort(points)

# Outputs the points
print('\nPoints : ')
for i in range(total_points):
    print(str(i + 1) + '. ' + str(points[i]))

# Find the closest pair of points
print('\nClosest pair of points : ')
# Using Brute Force Algorithm
start_time = time.time()
closest_pair_bf = algo.bruteForce(points)
end_time = time.time() - start_time
print('Brute Force : ')
print('Point 1 = ' + str(closest_pair_bf[0]))
print('Point 2 = ' + str(closest_pair_bf[1]))
print('Distance = ' + str(round(closest_pair_bf[2], 2)))
print('Euclidean Operation Count = ' + str(closest_pair_bf[3]))
print("Execution Time = %s seconds" % (end_time))
print('Run in ' + platform.processor() + ', ' + platform.platform())

# Using Divide and Conquer Algorithm
start_time = time.time()
closest_pair_dnc = algo.divideAndConquer(points, 0)
end_time = time.time() - start_time
print('\nDivide and Conquer : ')
print('Point 1 = ' + str(closest_pair_dnc[0]))
print('Point 2 = ' + str(closest_pair_dnc[1]))
print('Distance = ' + str(round(closest_pair_dnc[2], 2)))
print('Euclidean Operation Count = ' + str(closest_pair_dnc[3]))
print("Execution Time = %s seconds" % (end_time))
print('Run in ' + platform.processor() + ', ' + platform.platform())

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
        if(points[i] == closest_pair_dnc[0] or points[i] == closest_pair_dnc[1]):
            plot_color = 'orange'

        plt.scatter(points[i][0], 0, color=plot_color)

    plt.yticks([]) # Disable y-axis

elif (n == 2):
    for i in range(total_points):
        plot_color = 'blue'
        if(points[i] == closest_pair_dnc[0] or points[i] == closest_pair_dnc[1]):
            plot_color = 'orange'

        plt.scatter(points[i][0], points[i][1], color=plot_color)

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')

elif (n == 3):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(total_points):
        plot_color = 'blue'
        if(points[i] == closest_pair_dnc[0] or points[i] == closest_pair_dnc[1]):
            plot_color = 'orange'

        ax.scatter(points[i][0], points[i][1], points[i][2], color=plot_color)

    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')

plt.show()