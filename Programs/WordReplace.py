word1="bells"
word2="stars"
line="jingle bells jingle bells jingle all the way"
l=line.split(" ")
for i in range(len(l)):
    if (l[i]==word1):
        l[i]=word2
line=""
for j in range(len(l)):
    line+=l[j]+" "
print line
