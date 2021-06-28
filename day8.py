import collections

alf_list = collections.deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

shift_list = collections.deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


def encrypt():
    output = []
    user_word = input("PLease enter a word to encrypt")
    shift_number = int(input("please enter to shift number: "))
    user_list = list(user_word)
    shift_list.rotate(shift_number)
    for letter in user_list:
        n = alf_list.index(letter)
        output.append(shift_list[n])
    print(output)


def decrypt():
    output = []
    user_word = input("PLease enter a word to decrypt")
    shift_number = int(input("please enter to shift number: "))
    user_list = list(user_word)
    shift_list.rotate(-abs(shift_number))
    for letter in user_list:
        n = alf_list.index(letter)
        output.append(shift_list[n])
    print(output)

