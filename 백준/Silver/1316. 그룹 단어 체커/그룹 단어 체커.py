T = int(input())
word = []
group = T

for _ in range(T):
    word.append(str(input()))

for i in range(T):
    for j in range(0,len(word[i])-1):
        if word[i][j] == word[i][j+1]:
            pass
        elif word[i][j] in word[i][j+1:]:
            group -= 1 
            break

print(group)
