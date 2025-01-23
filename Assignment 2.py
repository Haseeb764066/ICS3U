# Author: Haseeb Ali Khan (Student Number:764066)
# Date: January 22nd 2025
# Teacher: Mr. King
# user_input: Stores the user's input as text (string).
# num_photos: The number of photos input by the user, stored as an integer.
# factors: A list of numbers that divide evenly into num_photos.
# largest_factor: The largest factor of num_photos.
# corresponding_factor: The factor paired with the largest factor to multiply to num_photos.
# perimeter: The total perimeter based on the photo arrangement dimensions.

import math

# Function to find factors of a number
def photo_factors(N):
    factors = []
    limit = math.floor(math.sqrt(N))
    for x in range(1, limit + 1):
        if N % x == 0:
            factors.append(x)
    return factors

# Function to calculate and display the minimum perimeter
def calculate_perimeter(N):
    factors = photo_factors(N)
    largest_factor = 1
    for factor in factors:
        if factor > largest_factor:
            largest_factor = factor
    corresponding_factor = N // largest_factor
    perimeter = 2 * (largest_factor + corresponding_factor)
    print("Minimum perimeter is %d with dimensions: %d x %d" % (perimeter, largest_factor, corresponding_factor))

# Function to check if the input is valid
def check_input(N):
    if N <= 0:
        print("%d is not a valid number of photos" % N)
        print("Please input a positive number")
    else:
        calculate_perimeter(N)

# Main program loop
print("Welcome to the school yearbook")
