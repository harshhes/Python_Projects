email = input("Enter your email: ")
index = email.index('@')
username = email[:index]
domain = email[index+1:]
print("Username of the email is : ",username)
print("Domain of the email is : ",domain)