# when we are building complex programs, we need a
# way to pass in data that is not always
# from the user.

# Parameters- this is placeholder data for 
# a function. variables inside the curly brackets

# Agruments- and parameters are ways to 
# pass in data to a function to a function from possibly 
# another function.

# function parameters- this is placeholder data for
# function. variable inside the curly brackets

# memory trick - parameter and placeholder both
# start with the letter P 



memory trick - parameters and placeholder both 
# start with the letter P
def check_water_depth(depth):
    print(depth)
    print(depth > 10) # true if depth is greater than 10 feet
    # return depth

# function agruments- this is the real data that we pass into
# the function call.
# memory trick- if you make a real world agrument with a person
# you need to come with real facts (data)
check_water_depth(3)

# return - this keyword allows us to pass data from inside 1 function
# into another function

def username(name):
    print("this data is coming fromanother function...")
    return name 

def confirmlogin():
    name = username("Carl")
    print name

