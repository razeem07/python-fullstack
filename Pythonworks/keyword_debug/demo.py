


def sample_function(*args):

    # (10,20,30)
    for num in args:

        yield num**3

    print(sum(args))

generator_objects=sample_function(10,20,30)

for val in generator_objects:
    print(val)



def smart_function(num1,num2):

    assert num1>0,"num1 should be > 0"

    assert num2>0,"num2 should be > 0"

    yield num1-num2

    yield num1/num2



generator_objects=smart_function(10,0)

for result in generator_objects:

    print(result)

    