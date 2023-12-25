def solution(statues):
    statues.sort() #sorts statues list in ascending order
    additional_statues=0 #counter for additional statues needed
    
    for i in range(len(statues)-1):
        gap = statues[i+1] - statues[i] - 1
        if gap > 0:
            additional_statues += gap
        
    return additional_statues
    
statues = [6, 2, 3, 8]
result = solution(statues)
print(f"The minimum number of additional statues needed is: {result}!")