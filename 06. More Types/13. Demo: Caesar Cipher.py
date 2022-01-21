def rot(character, key):
    size_of_alphabet = ord('Z') - ord('A') + 1
    key %= size_of_alphabet
    if key < 0: 
        key = size_of_alphabet + key
    new_char = ord(character)
    new_char += key
    

    #check if our character is a letter
    if  'a' <= character <= 'z':
        new_char = (new_char - ord('a')) % size_of_alphabet + ord('a')
    elif 'A' <= character <= 'Z':
        new_char = (new_char - ord('A')) % size_of_alphabet + ord('A')
    else:
        #there was no change so we can return what was passed
        return character
    
    return chr(new_char) #convert ASCII number to char


def rot_whole_string(text,key):
    return "".join(rot(character,key) for character in text)

text = """
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!
"""

print(rot_whole_string(text, 13))


"""
Output:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complicated.
Flat is better than nested.
Sprase si better than dense.
Readability counts.
Special cases aren't special enoguh to break the rules.
Although practicality betas purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation ot guess.
There should be one-- and preferablyonly one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than neever.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""




# SECOND WAY
# This code is meant to decipher the example text used in the Text Analyzer lesson of module 5: "More Types" of the Python 3 Tutorial

# Below is the text that needs to be deciphered. 
# Little background info about the encryption method (you can skip this explanation): 
# It is encrypted with a Caesar cipher where each letter is moved 13 places to the left. 
# So "o" usually has value 15, but in the encrypted text, o's value has been changed to: 15 - 13 = 2, which is the value of letter "b". 
# So in the encrypted text, we need to change each "o" for a "b". 4
# In cases of negative values, we just add them to 26, so for example: 
# the letter "a" has value 1; and in the encrypted text, the value of "a" is: 1 - 13 = -12; 
# now we add that to 26, so we get: 26 + (-12) = 14, which corresponds to the letter "n"; so we replace each "a" with an "n".

text = """
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!
"""

# Below is the decipher function. I called it "tdec" which is an abbreviated version of "text decipherer"

def tdec(text):

    # Defining a dictionary with the numerical values of each letter
    numVals = {1:'a', 2:'b', 3:'c',4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    
    # Defining a dictionary with the letters of the alphabet ordered
    alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    
    newtext = text.lower() # Changing the text to all lower case letters to make life easier
    
    msg = "" # Defining an empty string that will eventually be the deciphered message
    
    # The below code will iterate through each character of the text, concatinate it with the msg string and return msg. Conversion will be done for all the characters that are letters of the alphabet. 
    for char in newtext:
        if char in alphabet:
            newValue = numConv(alphabet.get(char))
            char = numVals.get(newValue)
        msg += char
    return msg
    
    
#the numerical value conversion function
def numConv(num):
    return num-13 if num>13 else 26+num-13

print(tdec(text))






