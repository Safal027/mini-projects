# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Encoding:
# if the word contains at least 3 characters:
#   remove the first letter and append it at the end and append three random characters at the starting and the end
# else:
#   simply reverse the string and add one random character at the starting and one at the end

# Decoding:
# if the word contains less than 3 characters:
#   reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


import random
import string
import sys

printable_chars = string.digits + string.ascii_letters + string.punctuation
secret_lang_string = ""
eng_string = ""

print()
print("Welcome!")
print()


def encode(eng_string, secret_lang_string, printable_chars):
    eng_string = input("Enter your string to encode: ").strip()
    eng_words = eng_string.split()

    for i in range(len(eng_words)):

        if len(eng_words[i]) >= 3:
            eng_list_of_chars = list(eng_words[i])

            last_position_of_eng_list = len(eng_list_of_chars)-1

            eng_list_of_chars.insert(
                last_position_of_eng_list, eng_list_of_chars.pop(0))

            repositioned_list_of_chars = eng_list_of_chars
            repositioned_chars = "".join(repositioned_list_of_chars)

            rand_set_of_chars_1 = "".join(
                random.choices(printable_chars, k=3))
            rand_set_of_chars_2 = "".join(
                random.choices(printable_chars, k=3))

            secret_lang_word = rand_set_of_chars_1 + \
                repositioned_chars+rand_set_of_chars_2

            secret_lang_string = (secret_lang_string +
                                  " "+secret_lang_word)

        else:
            rand_char_1 = random.choice(printable_chars)
            rand_char_2 = random.choice(printable_chars)

            two_letter_eng_word = eng_words[i]

            reversed_word = "".join(reversed(two_letter_eng_word))
            encoded_word = rand_char_1+reversed_word+rand_char_2

            secret_lang_string = (secret_lang_string +
                                  " "+encoded_word)

    print()
    print(f"Encoded text: \n{secret_lang_string.strip()}")
    eng_string = ""
    secret_lang_string = ""


def decode(eng_string, secret_lang_string):
    while True:
        can_decode = True
        eng_string = ""

        secret_lang_string = input("Enter your string to decode: ").strip()
        secret_lang_words = secret_lang_string.split()

        for i in range(len(secret_lang_words)):

            if len(secret_lang_words[i]) >= 9:
                secret_lang_word_chars_list = list(secret_lang_words[i])

                del secret_lang_word_chars_list[:3]
                del secret_lang_word_chars_list[-3:]

                len_of_secret_lang_word_chars_list = len(
                    secret_lang_word_chars_list)-1

                secret_lang_word_chars_list.insert(
                    0, secret_lang_word_chars_list.pop(len_of_secret_lang_word_chars_list))
                eng_word_char_list = secret_lang_word_chars_list

                eng_word = "".join(eng_word_char_list)

                eng_string = eng_string+" "+eng_word

            elif len(secret_lang_words[i]) <= 4 and len(secret_lang_words[i]) >= 3:
                secret_lang_word_chars_list = list(secret_lang_words[i])

                del secret_lang_word_chars_list[:1]
                del secret_lang_word_chars_list[-1:]

                eng_word_rev = "".join(secret_lang_word_chars_list)

                eng_word = "".join(reversed(eng_word_rev))

                eng_string = eng_string+" "+eng_word

            else:
                can_decode = False

                print()
                print(
                    "The given text cannot be decoded. Please enter the valid language.")
                print()

                break

        if can_decode == True:
            print()
            print(f"Decoded text: \n{eng_string.strip()}")
            break

    eng_string = ""
    secret_lang_string = ""


while True:
    while True:
        choice = input(
            "Do you want to encode or decode? (e/d): ").strip().lower()
        print()

        if choice == "e":
            encode(eng_string, secret_lang_string, printable_chars)
            break

        elif choice == "d":
            decode(eng_string, secret_lang_string)
            break

        else:
            print("Please enter a valid input.")
            print()

    while True:
        print()
        want_to_continue = input(
            "Do you want to continue? (y/n): ").strip().lower()
        print()

        if want_to_continue == "y":
            break

        elif want_to_continue == "n":
            print()
            print("Thanks for using this program!")
            print()
            sys.exit()

        else:
            print("Please enter a valid input.")
