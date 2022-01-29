####### 
def deco(fun):
    def wrap(name,surname):
        print('|'*(len(surname)+len(name)))
        fun(name, surname )
        print('|'*(len(surname)+len(name)))
    return wrap

def print_text(name, surname):
    print(name+''+surname)

print_text  = deco(print_text)
print_text("Ugur " ,"Arslan")


####### DECORATED VERSION #############

def deco2(fun):
    def wrap(name,surname):
        print('|'*(len(surname)+len(name)))
        fun(name, surname )
        print('|'*(len(surname)+len(name)))
    return wrap

@deco2
def print_text2(name, surname):
    print(name+''+surname)
    
print_text2("Pillars = " ,"number of letters")


