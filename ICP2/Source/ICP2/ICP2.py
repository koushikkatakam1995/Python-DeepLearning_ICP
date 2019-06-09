# Lbs to Kgs conversion
Lbs = []
Kgs = []
n = int(input("Enter the number of students:"))
for i in range(n):
    num = int(input('Enter the value to be inserted:'))
    Lbs.append(num)
    kilograms = num * 0.454
    Kgs.append(round(kilograms))
print(Lbs)
print(Kgs)

# string alternative function


def string_alternative(input):
    return input[::2]


word = input("Enter the word:")
res = string_alternative(word)
print(res)




# Word frequency in file
fileName = input("Enter the name of file:")
word_frequency = {}
file = open(fileName, 'r')
text_string = file.read().lower()
des = text_string.strip("!()-[]{};:'\,<>./?@#$%^&*_~ ")
desired = des.split(" ")

for word in desired:
    count = word_frequency.get(word, 0)
    word_frequency[word] = count + 1

frequency_list = word_frequency.keys()


for words in frequency_list:
    print(words, word_frequency[words])