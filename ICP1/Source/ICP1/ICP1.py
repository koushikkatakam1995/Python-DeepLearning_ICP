# Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.
s = input('Enter the string:')
num = int(input('Enter number of characters to delete:'))

res = s[0:-num]
print(res[::-1])


# Take two numbers from user and perform arithmetic operations on them.
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

print('Addition:',a + b)
print('Subtraction:',a-b)
print('Multiplicaation:',a * b)
print('Division:',a / b)
print('Modulus:',a % b)
print('Exponent:',a ** b)
print('Floor division:',a // b)


#  Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex
str = input('Enter the string:')

res = str.find('Python')

print(str.replace("python","Pythons"))