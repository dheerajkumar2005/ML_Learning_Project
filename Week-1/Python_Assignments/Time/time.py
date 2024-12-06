'''
Implement a class Time to represent and manipulate quantities of time stored in 
hours (non-negative integer-valued) and minutes (non-negative real-valued).
The number of minutes should always be less than 60.
  
The variables, inside the class, storing hours and minutes should be declared private.

Implement a constructor taking no argument, meant to initialize the times to 0 hours and 0 minutes.
When this is called, it should print out “Default Constructor called”.

Implement a constructor taking two arguments meant to initialize the hours and minutes values.
When this is called, it should print out “Constructor with two arguments called for (hours,minutes)”
where hours and minutes should actually show the values and not letters.

Implement the destructor, which should output a message, i.e, when this is called,
it should print out “Destructor called for (hours,minutes)” where hours and minutes should actually show the real values (not the letters).

Implement overloaded operators + and - to perform, respectively, addition and subtraction.
If a larger quantity of time is being subtracted from a smaller quantity of time, then the result should be 0 hours and 0 minutes.
The overloaded operators should work when:
both the operands are of the type of the time object;
the second operand is an integer (indicating minutes).

Implement overloaded operators * and / to perform multiplication and division with a positive scalar.

Implement an overloaded operator = to perform assignment when the right hand side is an object of type Time and also when the right hand side is an integer (indicating minutes).

Implement overloaded operators ==, <, > to perform comparisons and return a value of type bool. In this case, the second operand can either be an object of type Time or an integer (indicating minutes).

Implement a counter variable (count) within the class that keeps a track of the number of objects that are existing i.e. with memory allocated at any point in the program.

Instructions for usage:

Do not modify the main function, comment out some parts for debugging or testing purposes if needed.

Only modify the class Time in the TODO sections. Remove the pass statement before adding your code.

Run `python3 autograder.py` to check the output of your code.


'''


class Time:
    
    count = 0 # static variable to keep track of the number of objects

    def __init__(self, hours=0, minutes=0):
        #Implement constructor here
        #TODO
        pass

    def __del__(self):
        #Implement destructor here
        #TODO
        pass

    def __add__(self, other):
        #Implement addition overload here
        #TODO
        pass

    def __sub__(self, other):
        #Implement subtraction overload here
        #TODO
        pass

    def __mul__(self, scalar):
        #Implement multiplication overload here
        #TODO
        pass
    def __truediv__(self, scalar):
        #Implement division overload here
        #TODO
        pass

    def __eq__(self, other):
        #Implement equal overload here
        #TODO
        pass

    def __lt__(self, other):
        #Implement less than overload here
        #TODO
        pass

    def __gt__(self, other):
        #Implement greater than overload here
        #TODO
        pass

    def __assign__(self, other):
        #Implement assignment overload here
        #TODO
        pass

def main():
    print(f"current count: {Time.count}")
    

    t1 = Time(7, 4.5)
    t2 = Time(3, 30)
    scalar = 5

    print(f"t1 = {t1}")
    print(f"t2 = {t2}")
    print(f"current count: {Time.count}")

    sum_time = t1 + t2
    print(f"t1 + t2 = {sum_time}")

    difference = t1 - t2
    print(f"t1 - t2 = {difference}")

    product = t1 * scalar
    print(f"t1 * scalar = {product}")
    print(f"current count: {Time.count}")

    divided = t2 / scalar
    print(f"t2 / scalar = {divided}")

    t3 = Time()
    t3.__assign__(100.5)
    
    print(f"t3 = {t3}")

    t3 = t3 + 100
    print(f"t3 += 100: {t3}")
    print(f"current count: {Time.count}")

    t3 = t3 - 70
    print(f"t3 -= 70: {t3}")

    if t3 < 100:
        print("t3 is less than 100")
    else:
        print("t3 is not less than 100")

    if t3 > 100:
        print("t3 is greater than 100")
    else:
        print("t3 is not greater than 100")

    if t1 < t2:
        print("t1 is less than t2")
    else:
        print("t1 is not less than t2")

    if t3 > t2:
        print("t3 is greater than t2")
    else:
        print("t3 is not greater than t2")

    if t1 == t3:
        print("t1 is equal to t3")
    else:
        print("t1 is not equal to t3")

    print(f"current count: {Time.count}")

if __name__ == "__main__":
    main()