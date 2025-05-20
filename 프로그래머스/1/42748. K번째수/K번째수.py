

def solution(array, commands):
    T = len(commands)
    r = []
    for b in range(T):
        answer = []
        i = commands[b][0]
        j = commands[b][1]
        k = commands[b][2]
        
        for a in range(i-1,j):
            answer.append(array[a])
        answer.sort()
        r.append(answer[k-1])
        
    return r