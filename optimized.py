"""
optimized.py finds the most optimal result for either 20, or 1000 actions (using datasets files) that cost less
than 500 euros in total and find the best profit in euros.
The execution time for this method is also calculated.
"""

from csv import reader
from time import time

start_time = time()

actions = [
    ("action-1", 20, 5),
    ("action-2", 50, 15),
    ("action-3", 30, 10),
    ("action-4", 70, 20),
    ("action-5", 60, 17),
    ("action-6", 80, 25),
    ("action-7", 22, 7),
    ("action-8", 26, 11),
    ("action-9", 48, 13),
    ("action-10", 34, 27),
    ("action-11", 42, 17),
    ("action-12", 110, 9),
    ("action-13", 38, 23),
    ("action-14", 14, 1),
    ("action-15", 18, 3),
    ("action-16", 8, 8),
    ("action-17", 4, 12),
    ("action-18", 10, 14),
    ("action-19", 24, 21),
    ("action-20", 114, 18),
]


def dataset(file):
    """
    Extract the data from the csv files.
    The columns 'name', 'price' and 'profit' from the files are returned as a list
    of tuples (name, price, profit).
    Shares with a negative cost or equal to zero are ignored.
    """
    with open(file) as f:
        read = reader(f)
        share_list = []

        for row in read:
            try:
                if float(row[1]) > 0:
                    share_list.append((row[0], row[1], row[2]))
            except ValueError:
                continue

    return share_list


# Use the dataset 1 or dataset 2 files :
share_list = dataset("datasets/dataset1_Python+P7.csv")

# Dataset variable for the algorithm :
datasets_actions_profit = [
    (x[0], float(x[1]), (float(x[1]) * float(x[2])) / 100) for x in share_list
]

# 20 actions variables (converted percent to euros) :
actions_profit = [
    (action[0], float(action[1]), (action[1] * action[2]) / 100) for action in actions
]


def dynamic_prog(actions, budjet=500):
    # Create an emtpy list for each action from 0 to 500 euros
    matrice = [[0 for x in range(budjet + 1)] for x in range(len(actions) + 1)]

    # Loop through each actions :
    for i in range(1, len(actions) + 1):
        # Loop from 0 to 500 euros one by one :
        for budj in range(1, budjet + 1):
            if actions[i - 1][1] < budj:
                matrice[i][budj] = max(
                    (actions[i - 1][2]) + matrice[i - 1][int(budj - actions[i - 1][1])],
                    matrice[i - 1][budj],
                )
            else:
                matrice[i][budj] = matrice[i - 1][budj]

    # Find shares names with the best result :
    budj = budjet
    actions_combinations = len(actions)
    elements_selection = []

    while budj >= 0 and actions_combinations >= 0:
        best_profit = actions[actions_combinations - 1]
        if (
            matrice[actions_combinations][int(budj)]
            == matrice[actions_combinations - 1][int(budj - best_profit[1])]
            + best_profit[2]
        ):
            elements_selection.append(best_profit)
            budj -= best_profit[1]

        actions_combinations -= 1

    max_invest = budjet - budj

    return matrice[-1][-1], elements_selection, max_invest


def display_method(algo):
    """
    Display the best combinations of actions in euros (total + each action)
    and the best profit in euros.
    """
    print("\nBest actions to choose :\n")
    for shares in algo[1]:
        print(
            f"{shares[0]}\tCost : {shares[1]:.2f} euros\tProfit : {shares[2]:.2f} euros"
        )
    print(f"\nTotal cost : {algo[2]:.2f} euros\nTotal profit : {algo[0]:.2f} euros\n")


def execution_time(start, end):
    """
    Display the executime of the bruteforce method.
    """
    execution_time = end - start
    display_execution_time = f"The optimized method took {execution_time:.3f} seconds."
    print(display_execution_time)


optimized_method = dynamic_prog(datasets_actions_profit)
display_method(optimized_method)


end_time = time()
execution_time(start_time, end_time)
