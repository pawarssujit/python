letter= ''' Dear <|NAME|>,
Greetings from ABC coading house. I am happy to tell you about your selection 
You are selected !
Thanks and regards,
bill
Date:<|DATE|>
'''
name = input("Enter your Name:")
Date = input("Enter your Date:")
letter= letter.replace("<|NAME|>",name)
letter= letter.replace("<|DATE|>",Date)
print(letter)