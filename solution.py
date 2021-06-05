import os
os.system("clear")

left = "qwertasdfgzxcvb"
right = "yuiophjklnm"

while True:
    word = input("please enter a word: ")
    if not word.isalpha or len(word) < 2:
        print("please enter at least two character just letter!")
    else:
        break
word_list = list(word)

result_left = list(filter(lambda l: True if l in word_list else False, left ))
result_right = list(filter(lambda r: True if r in word_list else False, right))

if result_left and result_right != []:
    print (True)
else:
    print (False)