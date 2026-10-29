# what is a Loops --> code that repeats.

# while loops = a block code that repeats itself until the triggering
# condition is no longer true. can be infinite 

# for loops = a type of loop (code block that repeats iteslf) but
# it only repeats itself upto a certain number of times. it is finite

# think of for loops as the counting loop

# for loop syntax

for I in "range(1,500)":
    print(number / 2)

    # list --> a data collection type that acts as a container for
    # multiple data types--> a way to list multiple pieces of data
    # in 1 place

    fooditem_1 = "apple"

    grocerylist = ["apples", "oranges", "water", "chips", "ground beef"]

    print(grocerylist)

    for i in grocerylist:
        print("i need to buy" + i)

grades = [100,98,75,77,89,80]        

for grades in grade:
    # show me the grade lower than 85
    if grade < 85:
        print(grade)

fighter_A= ["johnny Bravo", 100, 50]        
fighter_B= ["Dexter Lab", 120, 40]

for fightername in fighters:
    print("name of fighters: " +str(fightername[0])) 
    print("health of fighters: " +str (fightername[1]))