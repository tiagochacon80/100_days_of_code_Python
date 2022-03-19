#simple function
def greet():
    print("Hello Tiago")
    print("How do you do jack? ")
    print("Isn't the weather today")
greet()

print()
#Function that allows for input
#name is parameter
#Jack is argument
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}")
greet_with_name("Jack")

print()
#functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Jack", "Québec")

print()
#Calling greet_with() with positional Arguments
greet_with("Jack", "Nowhere")
greet_with("Nowhere", "Jack")

print()
#Calling greet_with() with keyword arguments
greet_with(location="London", name="Tiago")