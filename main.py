print (4.0 + 4.0)
print (10.0 - 2.0)
print (16.0 / 2.0)
print (4.0 * 2.0)
favourite_number = int(input("please input your favourite number: "))
print (f"Your number is : {favourite_number}")

names = ["John", "Alice", "Steve"]
message_john = (f"Greetings \n\t{names[0].upper()}, \n\t\thow are you doing?")
message_alice = (f"Greeting \n\t{names[1].title()}, \n\t\thow are you doing?")
message_steve = (f"Greetings \n\t{names[-1].upper()}, \n\t\tand how are you doing?") 
print (message_john)
print (message_alice)
print (message_steve)
