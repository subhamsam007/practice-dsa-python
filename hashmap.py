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
# ------------------------------------------------------------------------------------------------------
# 1189. Maximum Number of Balloons
need1 = {'b': 1,'a': 1,'l': 2,'o': 2,'n': 1}
have1={}
text = "loonbalxballpoon"

for i in text:
    if i in have1 :
        have1[i]+=1
    else:
        have1[i]=1
print(have1)
ans=[]
for i in need1:
    if i in have :
        times= have1[i]//need1[i]
        ans.append(times)
print(min(ans))

print(ans)

#------------------------------------------------------------------------------------------------------
#409. Longest Palindrome
s = "ccccdd"
nee={}
for i in s:
    if i in nee:
        nee[i]+=1
    else:
        nee[i]=1
print(nee)

left=''
right=''
mid=''
for i in nee:
    if nee[i] %2==0:
        left+= i*(nee[i]//2)
        right+= i*(nee[i]//2)
    else:
        mid = i
print(left,right)
ans = left + mid + right[::-1]
print(ans)