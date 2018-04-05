##Bubble Sort##

def bbSort(list):
    switch = 0
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                switch = list[j+1]
                list[j+1] = list[j]
                list[j] = switch
            else:
                continue

    return list
                
