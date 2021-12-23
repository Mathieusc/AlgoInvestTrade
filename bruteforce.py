"""
bruteforce.py tries all combinations possible of actions that cost less
than 500 euros and find the best profit in euros.
The execution time for this method is also calculated.
"""


from itertools import combinations
from time import time


start_time = time()

# Data : (Cost in euros, Profit in percent)
shares = [
    (20, 5),
    (30, 10),
    (50, 15),
    (70, 20),
    (60, 17),
    (80, 25),
    (22, 7),
    (26, 11),
    (48, 13),
    (34, 27),
    (42, 17),
    (110, 9),
    (38, 23),
    (14, 1),
    (18, 3),
    (8, 8),
    (4, 12),
    (10, 14),
    (24, 21),
    (114, 18),
]

# Create a list of action cost.
shares_cost_list = [action[0] for action in shares]
# Associate each action cost to their profit (calculated in euros) in a dictionary.
shares_profit = {action[0]: (action[0] * action[1]) / 100 for action in shares}


def bruteforce(action, profit):
    """
    Try all combinations of actions below 500 euros
    using the combinations method from the itertools module.
    Return:
        tuple() - The single best combination of profit in euros and their actions.
    """
    results = []
    for i in range(1, len(action) + 1):
        action_combinations = combinations(action, i)
        actions_profit_list = []
        for action_combination in action_combinations:
            if sum(action_combination) <= 500:
                actions_profit_list.append(
                    (
                        action_combination,
                        sum([profit[action] for action in action_combination]),
                    )
                )
        results += actions_profit_list

    return max(results, key=lambda x: x[1])


def execution_time(start, end):
    """
    Display the executime of the bruteforce method.
    """
    execution_time = end - start
    display_execution_time = f"The bruteforce method took {execution_time:.2f} seconds."
    print(display_execution_time)


def display_best_profit(bruteforce_result):
    """
    Display the best combinations of actions in euros (total + each action)
    and the best profit in euros.
    """
    best_profit = f"Best combination of shares in euros : {bruteforce_result[0]}\n\
Profit : {bruteforce_result[1]:.2f} euros\n\
Total cost : {sum(bruteforce_result[0])} euros\n"
    print(best_profit)


find_best_profit = bruteforce(shares_cost_list, shares_profit)
display_best_profit(find_best_profit)
end_time = time()
execution_time(start_time, end_time)
