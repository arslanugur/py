INPUT               METHOD                  OUTPUT
--------------------------------------------------------------
"Hello World"       .endswith("by")         False
"Hello World"       .startswith('Hello')    True
"hello world"       .capitalize()           "Hello World"
"13/11/2021"        .split("/")             ["13","11","2021"]
" Hello "           .strip()                "Hello"
"Hello A"           .replace("A","B")       "Hello B"
"hello world"       .count("o")             2
"Hello World"       .find("o")              4                 # Index Number
"123456"            .isnumeric()            True
"HELLO"             .lower()                "hello"
"hello"             .upper()                "HELLO"
"I am the Batman"   .title()                "I Am The Batman"



message = "Hello there. I am the Batman."

message = message.split()
message = message.split('.')   # splits from dots, not the space
message = ' '.join(message)    # * instead of the space

index = message.find('the')
print(index)                  # output: 6  --> 6th index
                              # output: -1 --> no word in the sentence

isFound = message.startswith('H') # True
isFound = message.endswith('H')   # False
print(isFound)

message = message.replace('Batman', 'Superman')
message = message.replace(' ', '*')
message = message.replace('ç', 'c')
                 .replace('ş','s')
                 .replace('ö','o')
    
message = message.center(100)      # puts the message in the middle of 100 characters (Container)
message = message.center(50, '*')  # puts * instead of the space
print(message)


print(message[2]) # by using split method 
                  # each index number shows word in the array


