# Haseeb Ali Khan
# Student Number: 764066
# Teacher: Mr. King
# Course: ICS38
# Variable dictionary
# filename: The name of the file containing Wordle data.
# data_lines: A list of lines read from the Wordle data file.
# words: A list of Wordle solution words.
# dates: A list of dates corresponding to the Wordle words.
# original_words: A copy of the original list of Wordle words (unsorted).
# original_dates: A copy of the original list of dates (unsorted).

# Merge sort to sort words and corresponding dates
def merge_sort(word_list, date_list, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(word_list, date_list, left, mid)
        merge_sort(word_list, date_list, mid + 1, right)
        merge(word_list, date_list, left, mid, right)

# Helper function to merge two halves
def merge(word_list, date_list, left, mid, right):
    left_words = word_list[left:mid + 1]
    right_words = word_list[mid + 1:right + 1]
    left_dates = date_list[left:mid + 1]
    right_dates = date_list[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_words) and j < len(right_words):
        if left_words[i] <= right_words[j]:
            word_list[k] = left_words[i]
            date_list[k] = left_dates[i]
            i += 1
        else:
            word_list[k] = right_words[j]
            date_list[k] = right_dates[j]
            j += 1
        k += 1

    while i < len(left_words):
        word_list[k] = left_words[i]
        date_list[k] = left_dates[i]
        i += 1
        k += 1

    while j < len(right_words):
        word_list[k] = right_words[j]
        date_list[k] = right_dates[j]
        j += 1
        k += 1

# Combine year, month, and day into a single integer date
def combine_date(year, month, day):
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    try:
        month_number = months.index(month.lower()) + 1
        if len(day) == 1:
            day = "0" + day
        return int(year + f"{month_number:02d}" + day)
    except ValueError:
        return 0

# Find a word or date using binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Check if a word exists and return its date
def find_word(word, word_list, date_list):
    index = binary_search(word_list, word)
    if index != -1:
        return date_list[index]
    return 0

# Read and process the Wordle data file
filename = "wordle.dat"
with open(filename, "r") as file:
    data_lines = [line.strip() for line in file.readlines()]

words, dates = [], []
for line in data_lines:
    month, day, year, word = line.split()
    if len(day) == 1:
        day = "0" + day
    merged_date = combine_date(year, month, day)
    dates.append(merged_date)
    words.append(word)

original_words = words[:]
original_dates = dates[:]
merge_sort(words, dates, 0, len(words) - 1)

print("Welcome to the Wordle Database!")
while True:
    option = input("Enter 'w' to search for a word or 'd' to search by date: ").lower()
    if option in ['w', 'd']:
        break

if option == 'w':
    while True:
        user_word = input("Enter a 5-letter word: ").upper()
        if len(user_word) == 5:
            break
    result_date = find_word(user_word, words, dates)
    if result_date:
        print(f"The word {user_word} appeared on {result_date}.")
    else:
        print(f"The word {user_word} is not in the database.")

elif option == 'd':
    while True:
        year = input("Enter the year: ")
        month = input("Enter the month (e.g., Jan, Feb): ")
        day = input("Enter the day: ")
        if len(day) == 1:
            day = "0" + day
        date = combine_date(year, month, day)
        if date:
            break

    if date < min(dates):
        print(f"The date {date} is too early. No Wordle puzzles exist before {min(dates)}.")
    elif date > max(dates):
        print(f"The date {date} is too late. No Wordle puzzles exist after {max(dates)}.")
    else:
        word_index = binary_search(original_dates, date)
        if word_index != -1:
            print(f"The word for {date} was {original_words[word_index]}.")
        else:
            print(f"No word found for {date}.")
