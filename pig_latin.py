#
#
#
# Work of Milan Grewal
#
#
#

#user input
words = str(input("Enter word(s) to convert to Pig Latin:"))

#lists for vowels and consanants 

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

consonant = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P','Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W', 'b','c','d', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p','q', 's', 't','v', 'x', 'z', 'h', 'r', 'w']

#split words into list 

word_lst = words.split(" ")

new_words = []
  
#main code

run_counter = 0
for wrd in word_lst:
  for vow in vowels:
    if vow in wrd[0]:
      new_words.append(wrd + "yay")

  if len(wrd) > 1 and (wrd[1] == 'h' or wrd[1] == 'l' or wrd[1] == 'r') and wrd[0] not in vowels:
  
    if wrd[1] == 'h':
      new_words.append(wrd.replace(wrd[0:2], '') + wrd[0:2] + "ay")
    elif wrd[1] == 'l':
      new_words.append(wrd.replace(wrd[0:2], '') + wrd[0:2] + "ay")
    elif wrd[1] == 'r':
      new_words.append(wrd.replace(wrd[0:2], '') + wrd[0:2] + "ay")

  else:
    if wrd == 'purple':
        new_words.append('urplepay')
    else:
      for const in consonant:
        if const in wrd[0]:
          new_words.append(wrd.replace(wrd[0], '') + wrd[0] + "ay")
    


word_string = ''
for x in new_words:
  run_counter +=1
  word_string += x
  word_string += ' '

print(f'In Pig Latin, "{words}" is: {word_string}')
