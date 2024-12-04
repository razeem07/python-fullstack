

start=int(input("enter start number"))#10


end=int(input("enter end limit"))#50


if start<end:

    for num in range(start,end+1,1):

        print(num)

else:

    for num in range(start,end-1,-1):

        print(num)

