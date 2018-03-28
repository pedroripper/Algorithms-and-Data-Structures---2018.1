"""
Celebrity Problem
 considerations:
 - celebrity = 1
 - ordinary person = all numbers greater than 1
 - to know someone --> ">="
"""


def celebrity(people):
    change = 0
    for i in range(len(people)-1):
        if people[i] >= people[i+1]:
            continue
        else:
            change = people[i+1]
            people[i+1] = people[i]
            people[i] = change
    if people[len(people)-1] >= people[len(people)-2]:
        return "There is no celebrity"
    else:
        return "There is a celebrity."




        
