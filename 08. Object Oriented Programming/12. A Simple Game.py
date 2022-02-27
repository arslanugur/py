# SECTION 1
# Object-orientation is very useful when managing different objects and their relations. 
# That is especially useful when you are developing games with different characters and features.

# Let's look at an example project that shows how classes are used in game development.
# The game to be developed is an old fashioned text-based adventure game.
# Below is the function handling input and simple parsing.
def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

while True:
  get_input()
#

# The code above takes input from the user, and tries to match the first word with a command in verb_dict. 
# If a match is found, the corresponding function is called.

# (1): def get_input(): command = input(": ").split() verb_word = command[0] 
# if verb_word in verb_dict: verb = verb_dict[verb_word] else: print("Unknown verb {}".format(verb_word)) return 
# if len(command) >= 2: noun_word = command[1] print(verb(noun_word)) else: print(verb("nothing")) 
# def say(noun): return 'You said "{}"'.format(noun) verb_dict = { "say": say, } while True: get_input() 
# OUTPUT: >>> : say Hello! You said "Hello!" : say Goodbye! You said "Goodbye!" :test Unknown verb test
# (2): Thanks to the reply of Jonathon McEwan to the question comment of Egildio Nham, 
# I luckily managed to figure out that the verb_dict is a dictionary that's DEFINED towards the BOTTOM of the code!!! 
# Admittedly, with this whole OOP module, reading code from bottom to top instead can awkwardly help a lot sometimes. 
# Last code block of the example code is the following. 
# while True: get_input() The while True bit indicates that there will NEVER ever be an END to the repeated execution of the code get_input(). 
# An infinite loop I think this gets called. That's why trying the code out, you would be REPEATEDLY prompted for user input really. 
# Hence why in the OUTPUT that's shown, though there's ">>>" at the beginning of the OUTPUT, it's not there at the end, 
# since there's no actual end to the infinite loop, it goes on FOREVER.
# (3): Now, let's go through what you see in the OUTPUT they've got there. 
# Program starts up, and aside from the bunch of 2 function definitions, the dictionary assignment of verb_dict, 
# you've got the following code which is what causes something to ultimately be OUTPUT. while True: get_input() 
# So, the code (the function I mean) get_input() gets executed. 
# Now, consider how this get_input() function is DEFINED. def get_input(): command = input(": ").split() 
# User gets prompted to enter input right after ": " on the OUTPUT screen. User enters say Hello!, and so input(": ") is taken as the string "say Hello!". 
# So, I presume the following interpretations
# (4): command = input(": ").split() command = "say Hello!".split() 
# Now, plz see the PIC on the following link to quickly remind yourself of the split method, and what it means to have nothing inside the parenthesis () of split(). 
# https://pythonproject.files.wordpress.com/2014/05/split_method.jpg 
# Hence, command variable is assigned to be equal to a LIST of 2 strings. That's it. command = ["say", "Hello!"] 
# Then, you've got the following. verb_word = command[0] 
# So, verb_word variable is assigned to be equal to the index 0 element of the list called command, which is the string "say". Therefore,
# (5): verb_word = "say" Look at the BOTTOM of the example code now. 
# See how verb_dict = {"say": say}, so verb_dict really refers to a dictionary, with just a single element really, namely the Key:Value element given by "say": say. 
# OK, next consider the following code line, which gets interpreted presumably as follows. 
# if verb_word in verb_dict: verb = verb_dict[verb_word] if "say" in {"say": say}: verb = verb_dict[verb_word] Of course, "say" refers to the Key "say", since in a dictionary, 
# though the there may be one or more Values being the EXACT SAME Values, all Keys MUST be DISTINCT, 
# and because of this, we identify any specific element of a dictionary by its Key.
# (6): The key "say" certainly exists in the dictionary {"say": say}, so really the first line of the 2 line code block becomes "if True:", 
# and so the 2nd line of code gets executed for sure. 
# verb = verb_dict[verb_word] We know verb_dict={"say": say} and that verb_word = "say", hence verb = say Also, recall that command=["say", "Hello!"]. 
# Clearly, this has got 2 elements and so has a length of 2. Thus, len(command) = 2. if len(command) >= 2: noun_word = command[1] print(verb(noun_word))          
# (7): Since, len(command) ≥ 2 holds True, the 2 lines indented code block is surely executed. 
# I suppose the following interpretations get made. Remember command[1] refers to the index 1 element of the LIST assigned to command, 
# and that verb = say noun_word = command[1] print(verb(noun_word)) noun_word = "Hello!" print(say("Hello!")) 
# This is just saying that apply the function say on the string "Hello!", 
# and then whatever gets RETURNED by the function, that you print right away. 
# So, now you look at the way the say function is DEFINED, which you find if you look at what come after the definition of the get_input() function.
# (8): def say(noun): return 'You said "{}"'.format(noun) 
# I think the following interpretations get made. say("Hello!") RETURN 'You said "{}"'.format("Hello!") say("Hello!") RETURN 'You said "Hello!"' 
# So, print(say("Hello!")) would print You said "Hello!" to OUTPUT
# https://pythonproject.files.wordpress.com/2014/05/split_method.jpg   # reminder regarding the SPLIT method

# There are a few things that I didn't quite much get... 
# First thing is: print(verb(noun_word)) verb is a variable... not a function ! But even if it was... 
# how does this work ? I am really confused ! Second thing is: def say(noun): return 'You said "{}"'.format(noun) 

# The code takes the user input: say hello And using split makes it an array consisting of 'say' and 'hello' both assigned to the variable 'command' 
# command = ["say","hello"] verb_dict is referring to a dictionary declared near the bottom. 
# The key value pair here is Key: say Value: say(noun) Which is assigned to the variable verb noun_word=command[1] 
# So when print(verb(noun_word)) is called its actually calling say("hello")


# What does the split method called on the input do?  -- Divides the input into separate words
# https://www.pythonforbeginners.com/dictionary/python-split
# https://pythonproject.files.wordpress.com/2014/05/split_method.jpg
# "Split" separate the words from space between them and put them into a list.  

# Split a string into a list where each word is a list item: 
txt = "welcome to the jungle" 
x = txt.split() 
print(x) # ['welcome', 'to', 'the', 'jungle']


# SECTION 2
# A Simple Game
# The next step is to use classes to represent game objects.
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self
    # This puts an instance (self, so the whole object, or more exactly, a reference to where that object lies in the memory) 
    # of the class Goblin in the GameObject.objects{} map, 
    # with the key ”Goblin” (the name of the class to which that instance belongs to, its inherited attribute class_name). 
    # Problem is, I think, you cannot instantiate more than one Goblin as the map won't admit more than one ”Goblin” key. 
    # The code is horrible,, and not only this, and though it's just trying to show some things, it should note which are not the way of doing things. 
    # they could even point that those if could be a mapping through a map, 
    # one line of code and as many different messages as you want just adding them to the map, 
    # which is as clear to read even could be given to non-programmers to mantain, translate, ... being read from a plain text file.

  def get_desc(self):
   return self.class_name + "\n" + self.desc


class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)  
#

# We created a Goblin class, which inherits from the GameObjects class.
# We also created a new function examine, which returns the objects description.
# Now we can add a new "examine" verb to our dictionary and try it out! 
verb_dict = {
  "say": say,
  "examine": examine,
}

# Combine this code with the one in our previous example, and run the program.
>>>
: say Hello!
You said "Hello!"

: examine goblin
goblin
A foul creature

: examine elf
There is no elf here.
:

# Explanation of GameObject.objects[self.class_name]=self : 
# When goblin object(of class Goblin) is created, __init__ method gets called(as Goblin is inherited from GameObject class) Self is nothing but name of the object. so, goblin.name=Gobbly LHS =GameObject.objects[self.class_name] // self is nothing but object name = GameObject.objects[goblin.class_name] // replaced self word with goblin = GameObject.objects[goblin] // goblin.class_name means we are referencing Goblin class through its object goblin. goblin.class_name=goblin RHS = self = goblin // as said, self is object name Hence, GameObject.objects[goblin]=goblin. This made the dictionary objects = {"goblin" : goblin}

# objects = {} # creates a dictonary in the class "GameObject" To have access to the dictionary, the code is: "GameObject.objects" ... 
# In fact, if you digit this code, you will have an empty brackets >>> GameObject.objects {} There are no elements in it. 
# With the next code you create a key “elf” with a value elf (notice that elf is the label of an object) 
# GameObject.objects["elf"] = elf to do so in the class in a generic way (for every istance you will create later), 
# there is that line: GameObject.objects[self.class_name] = self 
# So let's see the key first: 
# self.class_name self is the name of the istance you create (goblin in the code) class_name is the string "goblin" created when the istance is created 
# The instance is > goblin = Goblin("Gobbly") goblin is the istance made using the blueprint of Goblin Goblin (the class) creates 2 attributes of goblin (the instance) one of this is the class_name = "goblin"


Krishna Limani
7
https://www.sololearn.com/learning/1073/2474/5147/1
  
