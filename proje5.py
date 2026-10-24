#validate user input exercise
# 1 username is no more than 12 characters
#2 username must not contain spaces
# 3 username must not contain digits


username = input("enter  a username: ")

if len(username) > 12:
    print(" your username cant  be more than 12 characters")
elif not username.find(" ") == -1:
    print("your username cant contain spaces")
elif not username.isalpha():
    print("your username cant contain numbers")
else:
    print(f"welcome {username}")  