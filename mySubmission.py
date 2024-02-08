""""Emmaleigh Hawkins VRP solution
References used: """

from sys import argv
import math

# To drive from (x1, y1) to (x2, y2) takes sqrt((x2-x1)^2 + (y2-y1)^2) minutes

# Each driver starts and ends his shift at a depot located at (0,0)

# Drivers start and end at (0,0)

# Must be < 12 hrs total drive time; euclidean distance < 12*60

# Need list of drivers, each with ordered list of loads to complete (all loads must be assigned to a driver)

def euclidean_distance(p1, p2): 
    # if tuple:
    x1, y1 = p1
    x2, y2 = p2
    euc_distance = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    return euc_distance

number_of_drivers = 0
total_number_of_driven_minute = 0
max_time = 12*60
data = []
coordinates = []
distance = []
time_per_driver = []
test_file = "Training\TrainingProblems\problem1.txt"
with open(test_file, "r") as file:
    # Ignore first line


    # Read routes into array
    # first line: load_id, pick_up, drop_off
    file_lines = [file.readline().strip("\n")]

    # get data (probs need to use dictionary), need to convert from string to int
    full_data = file.readlines()
    
    for line in full_data:
        data.append(line.strip().split("\n"))
    for element in data:
        for x in element:
            coordinates.append(x.split())
    print(coordinates)
    print(data)


    # get number of loads:
    num_loads = len(data)
    loads_assigned = []
    loads_remaining = [int(load[0]) for load in data]

    # calculate euclidean distance for each pair, put in distances list

    distance_matrix = [[0] * len(coordinates) for _ in range(len(coordinates))]

    # Calculate distance between each pair of locations
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])



# minimize both number of drivers and minutes driven
 
# Total cost of solution: 
total_cost = 500*number_of_drivers + total_number_of_driven_minute
