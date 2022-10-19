#game "idle slayer" has mechanic called minions
#each minion has a cost, cost per run, a time per run, and a cumulative reward per run with a cap.
#ex: minion #1 costs 1200 and 10 per run and gives +1 per run with a cap of 100.
#so run 1 gives 10, run 2 gives 20, and both run 10 and run 15 give 100.
#given a cost, run cost, reward, and cap how many runs will it take to make the original cost back?
import sys
from math import sqrt
try:
    cost = int(input("Cost: "))
    max_level = int(input("Max level: "))
    reward = int(input("Reward per level: "))
    run_cost = int(input("Cost per run: "))
except ValueError:
    sys.exit("Incorrect input")
checklist = [cost, max_level, reward, run_cost]
for check in checklist:
    try: 
        sqrt(check)
    except ValueError:
        sys.exit("No negative inputs")
current_value = cost * -1
current_level = 1
count = 0

while current_value < cost and count < 1000000:
    if current_level < max_level:
        current_value = (current_value - run_cost + (reward * current_level))
        current_level += 1
        count += 1
        print(current_value)
    elif current_level == max_level:
        current_value = (current_value - run_cost + (reward * current_level))
        count += 1
        print(current_value)
    else:
        sys.exit("Unknown Error")

print(f"Count: {count}")

        