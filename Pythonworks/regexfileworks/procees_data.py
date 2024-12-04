

from re import findall

f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\regexfileworks\\data.txt")


content=f.read()


pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

all_dates=findall(pattern,content)

for date in all_dates:

    print(date)



# fundamentals(variable,operators,datatype)
# decisionmaking(if,if..else,if..elif..else)
# looping(for,while)
# functions(),lambda function
# string class methods
# collections 
    #list methods
    #tuple methods
    #set methods
    #dictionary methods

#nested collections
#fileOperations
# processing json
# regularexpression


# pending 
    # *args,**kwargs

    # decorators
    # break
    # Frontend (html,css,bs) 2.5 weeks

    # object oriented programming

    #error handling
    # python main exam
    
# yield
   
# Django (python)