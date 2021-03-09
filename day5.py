#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for number in range(0, int(nr_letters)):
#     print(random.choice(letters), end='')
#
# for number in range(0, int(nr_symbols)):
#     print(random.choice(symbols), end='')
#
# for number in range(0, int(nr_numbers)):
#     print(random.choice(numbers), end='')

#Hard Level - Order of characters randomised:


list_letters = []
list_number = []
list_symbols = []

for number in range(0, int(nr_letters)):
    list_letters.append(random.choice(letters))

for number in range(0, int(nr_symbols)):
    list_symbols.append(random.choice(numbers))

for number in range(0, int(nr_numbers)):
    list_number.append(random.choice(symbols))

all_list = list_number + list_symbols + list_letters

total_lenght = nr_numbers + nr_letters + nr_symbols

new_list = random.sample(all_list, len(all_list))

for number in range(0, total_lenght):
    print(new_list[number], end='')


#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P