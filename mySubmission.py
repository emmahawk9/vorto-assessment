""""Emmaleigh Hawkins VRP solution
References used: """

from sys import argv

# To drive from (x1, y1) to (x2, y2) takes sqrt((x2-x1)^2 + (y2-y1)^2) minutes

# Each driver starts and ends his shift at a depot located at (0,0)

# Drivers start and end at (0,0)

# Must be < 12 hrs total drive time; euclidean distance < 12*60

# Need list of drivers, each with ordered list of loads to complete (all loads must be assigned to a driver)



number_of_drivers = 0
total_number_of_driven_minute = 0

test_file = "Training\TrainingProblems\problem1.txt"
with open(test_file, "r") as file:
    # Ignore first line


    # Read routes into array
    array_lines = [line for line in file.readlines().strip("\n")]

# get load id, pick-up, drop-off from 1st line in file
load_id, pick_up, drop_off = array_lines[0].split(" ")


# minimize both number of drivers and minutes driven
 
# Total cost of solution: 
total_cost = 500*number_of_drivers + total_number_of_driven_minute
