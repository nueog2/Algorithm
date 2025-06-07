word = input().strip().upper()

count = [0]*26

for w in word:
    count[ord(w) - ord('A')] += 1

max_count = max(count)

if count.count(max_count) > 1:
    print('?')
else: 
    print(chr(count.index(max_count) + ord('A')))