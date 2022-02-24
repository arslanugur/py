# This is an improvement to the SoloLearn OOP module... 
# under "simple game"". 
# Their code had a few bugs and for learners was a bit complicated. 
# Feel free to go through this code and ask questions in the comments. 
# You can improve upon this code. Cheers! Python rocks

class GameObject:
    class_name=""
    desc=""
    objects={}
    my_objects={}
    
    def __init__(self,name):
        self.name=name
        GameObject.objects  [self.name]=self
        GameObject.objects[self.class_name]=self
    def get_desc (self):
       return "A "+self.name+", "+self.desc+" of "+self.class_name+" origin!"
       
    def get_class_desc(self):
        return self.class_name +"\n"+ self.desc
        
        
class Goblin(GameObject):
    def __init__(self,name):
        self.class_name ="Goblin"
        self.desc ="This is a strong foul creature"
        self._health = 3
        super().__init__(name)  #python 2.x use super(Goblin,self).__init__(name) and add __metaclass__ = type at the very top of your script
        
    @property 
    def goblin_health(self):
        return  self._health 
        
    @goblin_health.setter
    def goblin_health(self,value):
        self._health=value
        
def examine(noun):
    if noun in GameObject.objects:
        print (GameObject.objects[noun].get_desc())
    elif noun in GameObject.my_objects:
        print (GameObject.my_objects[noun].get_class_desc())
    else:
        print ( "{} has not been detected".format(noun))
        
def hit(noun):
    if noun in GameObject.objects:
        health = GameObject.objects[noun].goblin_health-1
        GameObject.objects [noun].goblin_health=health
        if health ==2:
            print ("The {} is now wounded".format(noun))
        elif health ==1:
            print ("The {} now has no arm".format(noun))
        else:
            print ("The {} is now dead. Stop hitting it!".format(noun))
    elif noun in GameObject.my_objects:
        print (" {} master is untouchable".format(noun))
    else:
        print("Nothing called {} to hit has been detected!".format(noun))
        
        
goblin = Goblin("Green Goblin")

verb_dict = {"examine":examine,"hit":hit}

def get_input():
    command = input(":").split()
    verb_word = command [0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print ("Action to {} does not exist".format(verb_word))
    
    if len(command)>=2:
        noun_word = command [1]
        verb(noun_word)
    else:
        print ("You put nothing after your action")
        
while True:
    get_input()
# 


    
    
    
