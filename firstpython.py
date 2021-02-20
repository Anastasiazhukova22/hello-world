#i wrote a code by myself 

num = int(input("Enter the number between 10 and 20"))
while num<10 or num>20:
if num<10:
print("too low")
num = int(input('try again'))
elif num>20:
print("Too high")
num = int(input('try again'))
else:
print('Thank you')
