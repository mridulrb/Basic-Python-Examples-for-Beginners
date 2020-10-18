n=input("Enter numbers which form proper pyramid(3,6,10,15,21,28,36...): ")
k,i,a=1,1,-1
while i<=n:
        for j in range(0,k):
                if i<=n:
                    print i,
                else:
                    break
                i+=1
        a+=1
        k+=1
        print
i=i-k-a
l=k-2
while l>=0:
        for r in range(1,l+1):
                print i+r,
        l-=1
        print
        i=i-l
