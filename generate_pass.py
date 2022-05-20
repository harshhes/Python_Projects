import random
pass_len = int(input("Enter length of password: "))
s ="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,pass_len))
print(p)