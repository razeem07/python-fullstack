number=int(input("enter number")) #51

prev=0

current=1

is_fibo=False


for i in range(1,number+1):#0 1 1 2 3 5 8 13 21 34 55 89 144 ,,,,,,,

    next=prev+current

    prev=current

    current=next

    if next==number:

        is_fibo=True

        break

print(is_fibo)







def wrapper(self,request,*args,**kwargs):

    if request.user.is_superuser:

        return render()
    
