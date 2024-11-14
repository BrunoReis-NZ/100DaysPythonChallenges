# Project: Random Matchmaker
#
# Goal: Create a simple "Matchmaker" program that pairs participants and assigns a random activity for each pair.
#
# Instructions:
#
# 1. List of Participants:
#   - Define a list of exactly 8 participants.
#
# 2. List of Activities:
#   - Define a tuple with 8 possible activities (e.g., "Bowling," "Tennis," "Cooking Class," "Escape Room").
#
# 3. Random Pairing:
#   - Use random.choice() and random.sample() to pair participants and assign them an activity.
#
# 4. Display Matches:
#   - Show each pair and the activity they’ll be doing together.

import random

# List of Participants
males= ["John", "Michael", "Robert", "David"]
females = ["Linda", "Susan", "Karen", "Sarah"]

# List of Activities
activities = ("Bowling", "Tennis", "Cooking Class", "Escape Room", "Painting Class", "Hiking", "Karaoke", "Movie Night")

# Pair random participants (the same participant can't be paired twice)
pair_1 = random.sample(males, 1) \
         + random.sample(females, 1)
pair_2 = random.sample([male for male in males if male not in pair_1], 1) \
         + random.sample([female for female in females if female not in pair_1], 1)
pair_3 = random.sample([male for male in males if male not in pair_1 + pair_2], 1) \
         + random.sample([female for female in females if female not in pair_1 + pair_2], 1)
pair_4 = random.sample([male for male in males if male not in pair_1 + pair_2 + pair_3], 1) \
         + random.sample([female for female in females if female not in pair_1 + pair_2 + pair_3], 1)

# Assign random activities to each pair of participants (each activity can only be assigned once)

activity_1 = random.choice(activities)
activity_2 = random.choice([activity for activity in activities if activity not in [activity_1]])
activity_3 = random.choice([activity for activity in activities if activity not in [activity_1, activity_2]])
activity_4 = random.choice([activity for activity in activities if activity not in [activity_1, activity_2, activity_3]])

# Display Matches
print("\n--- Matchmaker Results ---")
print(f"{pair_1[0]} and {pair_1[1]} will be doing {activity_1} together.")
print(f"{pair_2[0]} and {pair_2[1]} will be doing {activity_2} together.")
print(f"{pair_3[0]} and {pair_3[1]} will be doing {activity_3} together.")
print(f"{pair_4[0]} and {pair_4[1]} will be doing {activity_4} together.")



