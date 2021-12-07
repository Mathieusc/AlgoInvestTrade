# Knapsack Problem -> Find the best solution (value) with these values:
# items = the number of items      (N)
# capacity = the knapsack capacity (C)
# value = the value of each item   (v)
# weight = the weight of each item (w)


# Knapsack problem with a real life example :
# Projects, Time required (days), Profit(€)
# Here the knapsack capacity is 30 days max

capacity = 30
projects = [
    ("Project 1", 4, 500),
    ("Project 2", 3, 250),
    ("Project 3", 10, 1500),
    ("Project 4", 12, 1600),
    ("Project 5", 9, 1200),
    ("Project 6", 6, 800),
    ]

time_required = [project[1] for project in projects]
profit = [profit[2] for profit in projects]

for project in projects:
    print(f"{project[0]} : {project[1]} days required, {project[2]}€.")


# Dynamic Programming Algorithm
# max(item, capacity) : the maximum value that can be obtained with capacity
#                       less than or equal to capacity using each item

# Step 1: m(0, capacity) = 0 for each capacity

# Step 2: for each item and each capacity,
#         if weight <= capacity,
#             m(1, c) = max{m(i - 1, c), v + m(i - 1, c - w)}
#         else
#             m(i c,) = m(i - 1, c)


def knapsack(value, weight, capacity):
    """
    :param list value in euros
    :param list weight in days
    :param int knapsack capacity - 30 days max
    """
    items_number = len(value)
    results = {}

    # Step 1 : m(0, c) function
    for c in range(capacity + 1):
        results[(0, c)] = 0

    # Step 2 : nested loop
    for i in range(1, items_number + 1):
        for c in range(capacity + 1):
            if weight[i - 1] <= c:
                results[(i, c)] = max(results[(i - 1, c)], profit[i - 1] + results[(i - 1, c - weight[i - 1])])
            else:
                results[(i, c)] = results[(i - 1, c)]

    print(results)


knapsack(profit, time_required, capacity)