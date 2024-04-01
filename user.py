class User:
    def __init__(self, id, name, age): # This is the constructor of the class
        self.id = id
        self.name = name
        self.age = age

############################################
# Define list of users outside the class
# This is simulating a database
# To create a object, you need to call the class and pass the arguments to the constructor, in this case the constructor requires 3 arguments
# id, name and age. That's the __init__ method in the class User that will initialize the object with the values passed to the constructor
############################################
users = [
    User(1, "John", 30),
    User(2, "Jane", 25),
    User(3, "Robert", 35),
    User(4, "Tom", 40),
    User(5, "Jim", 45)
]

User.users = users # Assign the list of users to the class attribute