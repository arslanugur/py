# Files Examples
# Example: to Merge Mails into one

# When we want to send the same invitations to many people, 
# the body of the mail does not change. Only the name (and maybe address) needs to be changed.

# Mail merge is a process of doing this. 
# Instead of writing each mail separately, we have a template for body of the mail and a list of names that we merge together to form all the mails.

# Source Code to Merge Mails
  # Python program to mail merger
  # Names are in the file names.txt
  # Body of the mail is in body.txt

# open names.txt for reading
with open("names.txt", 'r', encoding='utf-8') as names_file:

    # open body.txt for reading
    with open("body.txt", 'r', encoding='utf-8') as body_file:

        # read entire content of the body
        body = body_file.read()

        # iterate over names
        for name in names_file:
            mail = "Hello " + name.strip() + "\n" + body

            # write the mails to individual files
            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)
#                
# For this program, we have written all the names in separate lines in the file "names.txt". The body is in the "body.txt" file.

# We open both the files in reading mode and iterate over each name using a for loop. 
# A new file with the name "[name].txt" is created, where name is the name of that person.

# We use strip() method to clean up leading and trailing whitespaces (reading a line from the file also reads the newline '\n' character). 
# Finally, we write the content of the mail into this file using the write() method.


# Learn more about files in Python.
# Python programming topics:
#     String Methods
#     Python File I/O



