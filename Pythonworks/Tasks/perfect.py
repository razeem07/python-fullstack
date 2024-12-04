


num=int(request.POST["num"])


factors_sum=sum([i for i in range(1,num) if num%i==0])

print("perfect" if num==factors_sum else "not perfect")

