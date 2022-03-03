'''
This is the simple text based game from the Python OOP section of the course. 
It was inadequitely explained for the most part so I decided to go through the entire code and add comments to tell me what was happening. 
It has helped my understanding of OOP immensely. Hopefully it'll help you too
'''

# Superclass
class GameObject:   # blank class attributes to be filled in by the subclass
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):   # The __init__ magic method is called when an instance (object) of the class is created, using the class name as a function
        # You can see the first argument to the method is self. It is a special variable which points to the current object
        # Within a method definition, self refers to the instance (object) calling the method
        self.name = name # This defines the attribute name. It can be accessed by putting a dot, and the attribute name after an instance
        GameObject.objects[self.class_name] = self # GameObject.objects is the Class dictionary (you access the attributes of the class with '.') and [self.class_name] is a key of the dictionary
        # e.g. If self = goblin, then self.class_name = goblin.class_name = "goblin"
        # Also, GameObject.objects = {} is a (empty) dictionary
        # For GameObject.objects["goblin"] = goblin, a new element gets added to the GameObject.objects={} dictionary which has its Key: Value as equal to "goblin": goblin

    def get_desc(self): # Describes what is displayed when the 'examine' command is called
        return self.class_name + "\n" + self.desc # Calls the object instance (self) and then retrieves the attribute (.attribute) from the class (or subclass)
        # e.g. In the instance "goblin = Goblin()", it would be goblin.class_name + "\n" + goblin.desc ==> "goblin" + "\n" + "A foul creature"


class Goblin(GameObject):   # The class Goblin INHERITS from the class GameObject. Hence, the class methods, attributes and variable of class GameObject get "copied and pasted" onto the class Goblin
    def __init__(self, name):
        self.class_name = "goblin" # The attribute class_name of the class Goblin gets re-assigned to the string "goblin" from the (empty) string "".
        self.health = 3
        self._desc = "A foul creature" # Also, the attribute desc gets re-assigned to the string "A foul creature" from the (empty) string ""
        super().__init__(name) # super ()__init__(name) is called because the child constructor overrides the super.
        # However, the child constructor doesnt create the name (which the super does). So the super ()__init__(name) is called to create the name

    @property # A property is a function with no argument and can be called without parentheses.
    # Hence, it syntactically behaves as an attribute when called, except it cannot be assigned. Also, it is more than an attribute because it can perform calculation.
    # It essentially makes the contents within read only
    def desc(self): # This property modifies what is returned if the desc function is called (e.g. by using the examine command) 
    # A different string is returned depending on which conditions are met
    # e.g. if you used the hit command, a string indicating injury is returned, rather than the default subclass desc attribute
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm hs been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter  # A setter is a method that sets the value of a property. It hides a private field from public access as indicated by ._attribute 
    def desc(self, value):
        self._desc = value


goblin = Goblin("Gobbly") # An instance named goblin (the goblin object is = self parameter of the class) of the Goblin class gets created, with its name-attribute equal to the string "Gobbly". So, goblin.name = "Gobbly".
#  The class Goblin (that has GameObject as superclass) and creates the class_name = 'goblin' then goes to the super class GameObject and passes the "Gobbly" argument to self.name
# Instead of self, when you initialise a class, you will have goblin so -> goblin.name "Gobbly" -> goblin.class_name "goblin"
# So, name is personal to this instance, and class_name is inherited from the Goblin class

def get_input():
    command = input(": ").split() # input is entered as a string which is split to be equal to a LIST of strings and assigned to the command variable
    verb_word = command[0]
    # verb_word variable is assigned to be equal to the index 0 element of the list called command
    # e.g if you type 'say hello' it becomes ['say', 'hello'] and 'say' is in the index command[0] and is assigned to variable verb_word
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
        # checks if verb_word (e.g 'say') is a value in the verb_dict (e.g {"say": say}) and then assigns it to a variable
        # this retrieves say from the key:value pairs in the dictionary (defined as a function later in the code) instead of 'say' which is a string
    else:
        print("Unknown verb {}". format(verb_word)) # Prints this if the verb_word is not in the verb_dict
        return

    if len(command) >= 2:
        noun_word = command[1]
        # noun_word variable is assigned to be equal to the index 1 element of the list called command
        # e.g if you type 'say hello' it becomes ['say', 'hello'] and 'hello' is in the index command[1] and is assigned to variable noun_word
        print(verb(noun_word))
        # This calls a function defined in the code, such as say(), and calls it with argument noun_word
        # e.g. if you typed 'say hello' it would here read as say(hello) and excute the function
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)
    # Executes the function using noun_word as an argument as seen above
    # e.g. say(hello) would print 'You said "hello"'

def examine(noun):  # We created the function examine, which returns the objects description.
    if noun in GameObject.objects:  # Checks to see if noun is in GameObject.objects, which is the Class dictionary
        return GameObject.objects[noun].get_desc()  # Executes the get_desc GameObject class function (in this case it returns a string)
    else:
        return "There is no {} here.".format(noun)  # If the noun isn't found in the class dictionary it returns this

def hit(noun):  # The function hit reduces the health attribute of the class specified by the noun argument
    if noun in GameObject.objects:   # Checks to see if noun is in GameObject.objects, which is the SuperClass dictionary
        thing = GameObject.objects[noun]   # Assigns the noun to the variable named thing
        if type(thing) == Goblin:   # Checks if the class assigned to thing is the same the Goblin subclass
            thing.health = thing.health -1  # Modifies the health attribute of the Goblin class
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name) # Returns the string an adds the value assigned to self.class_name in the subclass attributes
        else:
            msg = "There is no {} here.".format(noun)   # If the noun isn't found in the class dictionary it returns this
        return msg

verb_dict = {   # The dictionary stores the key:value pairs that store which commands are recognised by the user input and call defined functions
    "say": say,
    "examine": examine,
    "hit": hit,
}

# The while loop indicates that there will NEVER ever be an END to the repeated execution of the code get_input()
while True:
    get_input()

# The code above takes input from the user, and tries to match the first word with a command in verb_dict.
# If a match is found, the corresponding function is called



