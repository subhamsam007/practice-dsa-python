# hash map question
# 383. Ransom Note
ran = "aaa"
mag = "aab"

need={}
have={}

for i in ran:
    if i in need:
        need[i]+=1
    else:
        need[i]=1
print(need)

for i in mag:
    if i in have:
        have[i]+=1
    else:
        have[i]=1
print(have)

for i in need:
    if i not in have or need[i]>have[i]:
        print(False)
    else:print(True)