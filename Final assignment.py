# Author : Haseeb Ali Khan
# Student Number: 754066
# Revison date : January 22nd 2025
# Variable Dictionary:
# filename: Name of the input file containing data
# fh: File handle for reading the input file
# names: List to store full names (first and last names combined)
# cc_nums: List to store credit card numbers
# cc_types: List to store credit card types (e.g., VISA, Mastercard)
# expiry_dates: List to store credit card expiry dates as integers (YYYYMM format)
# lines: List of all lines read from the input file
# given_name, surname: First and last names of a person (from input data)
# cc_type: Credit card type for a person (from input data)
# cc_number: Credit card number for a person (from input data)
# exp_mo, exp_yr: Expiry month and year of a credit card (from input data)
# expiry_date: Combined expiry year and month as a single integer
# output_file_name: Name of the file to write the output to
# output_file: File handle for writing the output file
# expired_text: String indicating whether the card is expired or needs renewal
# arr, arr2, arr3, arr4: Arrays used in merge sort for expiry dates, names, card numbers, and types
# l, r, m: Left, right, and middle indices for subarrays in merge sort
# L, R: Temporary arrays for left and right subarrays in merge sort (for expiry dates)
# L2, R2, L3, R3, L4, R4: Temporary arrays for names, card numbers, and types in merge sort
# i, j, k: Indices used in the merge function to track positions in arrays

def mergeSort(arr, arr2, arr3, arr4, l, r):
    # Recursive function to sort arrays using merge sort
    if l < r:
        # Find the middle point of the current subarray
        m = l + (r - l) // 2

        # Recursively sort the first half
        mergeSort(arr, arr2, arr3, arr4, l, m)
        # Recursively sort the second half
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        # Merge the sorted halves
        merge(arr, arr2, arr3, arr4, l, m, r)

def merge(arr, arr2, arr3, arr4, l, m, r):
    # Merge function to combine two sorted subarrays into one

    # Determine the sizes of the two subarrays
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays for each input array
    L = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2

    # Copy data into the temporary arrays
    for i in range(n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]

    # Merge the temporary arrays back into the original arrays
    i = 0  # Index for the left subarray
    j = 0  # Index for the right subarray
    k = l  # Index for the merged array

    # Compare and copy the elements from both subarrays into the main array
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Open the file containing the data
filename = "data.dat"
fh = open(filename, 'r')

# Initialize empty lists to store names, credit card numbers, types, and expiry dates
names = []
cc_nums = []
cc_types = []
expiry_dates = []

# Read all lines from the file
lines = fh.readlines()

# Remove the first line (header) from the list of lines
lines.pop(0)

# Process each line in the file
for line in lines:
    # Split the line into individual components
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    
    # Combine the first and last names
    name = given_name + ' ' + surname
    # Add the name to the list of names
    names.append(name)
    # Add the credit card type to the list
    cc_types.append(cc_type)
    # Add the credit card number to the list
    cc_nums.append(cc_number)
    # Add a leading zero to single-digit months
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    # Combine year and month into a single expiry date
    expiry_date = exp_yr + exp_mo
    # Add the expiry date to the list (as an integer)
    expiry_dates.append(int(expiry_date))

# Close the file after reading all the data
fh.close()

# Sort the lists using merge sort based on expiry dates
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)

# Open the output file to write the results
output_file_name = "output.txt"
output_file = open(output_file_name, "w")

# Go through each expiry date and determine its status
for i in range(len(expiry_dates)):
    # Stop if the expiry date is greater than January 2025 (not expired)
    if expiry_dates[i] > 202501:
        break
    # Set the status to "RENEW IMMEDIATELY" by default
    expired_text = "RENEW IMMEDIATELY"
    # If the expiry date is before January 2025, set the status to "EXPIRED"
    if expiry_dates[i] < 202501:
        expired_text = "EXPIRED"
    # Print the data in a formatted manner
    print("%-35s %-15s %-20s %-10s %-15s" % (names[i] + ':', cc_types[i], '#' + cc_nums[i], expiry_dates[i], expired_text))
    # Write the same data to the output file
    output_file.write("%-35s %-15s %-20s %-10s %-15s\n" % (names[i] + ':', cc_types[i], '#' + cc_nums[i], expiry_dates[i], expired_text))

# Close the output file after writing
output_file.close()

# Print a message indicating where the output was saved
print("\nOutput sent to %s" % output_file_name)
