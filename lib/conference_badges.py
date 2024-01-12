# You're hosting a conference and need to print badges for the speakers. Each badge should read: "Hello, my name is _____." Write a badge_maker() function that, when provided a person's name, will create and return the message
def badge_maker(name):
    return f"Hello, my name is {name}."

# Write a batch_badge_creator() function that takes a list of names as an argument and returns a list of badge messages.
# 1. Using list comprehension
def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

# 2. Using for loop
# def batch_badge_creator(names):
#    result = []
#    for name in names:
#        result.append(f"Hello, my name is {name}.")
#    return result

# Return a new list of strings representing room assignments in the form of: "Hello, _____! You'll be assigned to room _____!"
# Hint: Think about how you will assign a room number to each person. List items are indexed, meaning that you can access each element by its index number.
# Hint: Be sure to return a new list that contains the messages and leave the original list as is.
def assign_rooms(names):
    assignments = []
    for room in range(1, 9):
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    
    return assignments

# Now you have to tell the printer what to print. Create a function called printer() that will output first the results of the batch_badge_creator() function, and then the output of the assign_rooms() function, to the screen.
# Hint: remember you can call one function from inside another function. If the return value of assign_rooms() is a list of room assignments, how can you print out each assignment? You'll need to iterate over your list of room assignments in order to print out each individual assignment.
def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)
