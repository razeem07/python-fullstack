
# read two limits 
# sample input (1)
    # start=2
    # end=10
# samplle output(1)
    # even
    # 2,4,6,8

# sample input (2)
    # start=10
    # end=2
# samplle output(1)
    # even
    # 8,6,4,2



begin=int(input("enter start"))

end=int(input("enter end"))


reverse=True if begin>end else False

i=begin

while(i<=end if reverse==False else i>=end):

    if i%2==0:

        print(i)

    if reverse==False:

        i=i+1
    else:
        i=i-1









