#strong password

def strongPassword(password):
    #check capital
    #if there is not at least one capital then return 1 edit
    #if there is one or more capitals then return zero edits
    count = 0
    for letter in password:
        if letter.isupper():
            count += 1
            print(count)
     if count >= 1:
         edit += 1

strongPassword("String")
