def solution(answers):
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0]*3
    answer = []
    
    for i in range(len(answers)):
        ans = answers[i]
        if ans == man1[i%len(man1)]:
                score[0] += 1
        if ans == man2[i%len(man2)]:
                score[1] += 1
        if ans == man3[i%len(man3)]:
                score[2] += 1
    
    for i in range(3):
        if max(score) == score[i]:
            answer.append(i+1)
    
    answer.sort()
    return answer