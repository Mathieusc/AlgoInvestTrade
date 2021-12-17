from csv import reader
from time import time
from timeit import timeit
from memory_profiler import profile

start_time = time()

actions = [
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


def dataset(file):
    with open(file) as f:
        read = reader(f)

        share_list = []

        for row in read:
            # print(row)
            share_list.append((row[1], row[2]))

    return share_list[1:]


share_list = dataset("dataset1_Python+P7.csv")
convert_list = [(int(float((x[0]))), float(x[1])) for x in share_list]
# print(convert_list)

# {Action: Profit} in euros dict :
# action_profit = {action[0]: (action[0] * action[1]) / 100 for action in actions}

# (Action, Profit) in euros List of tuples :
action_profit = [(action[0], (action[0] * action[1]) / 100) for action in actions]

# @profile
def dynamic_prog(budjet, actions):
    # Create an emtpy list for each action from 0 to 500 euros
    matrice = [[0 for x in range(budjet + 1)] for x in range(len(actions) + 1)]
    # print(actions)

    # Loop through each actions :
    for i in range(1, len(actions) + 1):
        print(actions[i - 1])
        if actions[i - 1][0] < 0:
            continue
        # Loop from 0 to 500 euros one by one :
        for budj in range(1, budjet + 1):
            if actions[i - 1][0] <= budj:
                # print(actions[i - 1][0])
                # print(budj - actions[i - 1][0])
                matrice[i - 1][budj - actions[i - 1][0]]

                matrice[i][budj] = max(
                    (actions[i - 1][1]) + matrice[i - 1][budj - actions[i - 1][0]],
                    matrice[i - 1][budj],
                )
            else:
                matrice[i][budj] = matrice[i - 1][budj]

    # Retrouver les éléments en fonction de la somme
    budj = budjet
    actions_combinations = len(actions)
    elements_selection = []

    while budj >= 0 and actions_combinations >= 0:
        best_profit = actions[actions_combinations - 1]
        if (
            matrice[actions_combinations][budj]
            == matrice[actions_combinations - 1][budj - best_profit[0]] + best_profit[1]
        ):
            elements_selection.append(best_profit)
            budj -= best_profit[0]

        actions_combinations -= 1

    return matrice[-1][-1], elements_selection


def display_optimized(method):
    """
    Display the best combinations of actions in euros (total + each action)
    and the best profit in euros.
    """
    total_cost = 0
    action_combinations = []

    for actions in method[1]:
        total_cost += actions[0]
        action_combinations.append(actions[0])
    best_profit = f"Best combination of actions in euros : {action_combinations}\n\
Profit : {method[0]:.2f} euros\n\
Total cost : {total_cost} euros\n"
    print(best_profit)


def execution_time(start, end):
    """
    Display the executime of the bruteforce method.
    """
    execution_time = end - start
    display_execution_time = f"The optimized method took {execution_time:.3f} seconds."
    print(display_execution_time)


optimized_method = dynamic_prog(500, convert_list)

optimized_time = timeit(lambda: dynamic_prog(500, action_profit), number=1)
display_optimized(optimized_method)
print(f"The optimized method took {optimized_time:.3f} seconds.")
# end_time = time()
# execution_time(start_time, end_time)
