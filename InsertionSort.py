##Insertion Sort##


def inSort(l):
    switch = []
    skip = 1
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            while l[i] < l[i-skip]:
                skip += 1
                if i - skip < 0 :
                    switch = [l[i]]
                    l[:] = switch + l[:i] + l[i+1:]
                    skip = 1
                    break
                else: continue
            switch = [l[i]]
            l[:] = l[:i-skip + 1] + switch + l[i-skip + 1:i] + l[i+1:]
            skip = 1
        else:
            continue
    return l 
            
            
                
