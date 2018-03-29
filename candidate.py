
#the votes come in an array in wich the elements are the candidates that they are destined to

# example: votes= ["A","B",.......]
#the 1st vote would be to candidate A



def candidate(votes):
    supposedCandidate = [" ", 0]
    for i in range(len(votes)):
        if supposedCandidate[1] == 0:
            supposedCandidate[0] = votes[i]
            supposedCandidate[1] += 1
        else:
            if votes[i] == supposedCandidate[0]:
                supposedCandidate[1] += 1
            else:
                supposedCandidate[1] -= 1
        if supposedCandidate[1] > len(votes[i:]):
            return "The candidate that won with a majority of votes was candidate " + supposedCandidate[0]
            break
        
    return "No one won with a mojority of votes"
            
