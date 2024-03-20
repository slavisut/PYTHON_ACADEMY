"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Slavík
email: slavik.work@seznam.cz
discord: slavisut
"""
# Import texts for examination
import task_template
TEXTS = task_template.TEXTS

login_credentials = {
    'bob' : '123',
    'ann' : 'pass123',   
    'mike' : 'password123', 
    'liz' : 'pass123'   
}

# Variables used in this code - for clarity
nb_texts = len(TEXTS)       # number of texts to be analysed
word_list = []              # list of words in text
cap_word_count = 0          # number of words with 1st capital letter
all_cap_word_count = 0      # number of words with all capital letters
all_low_word_count = 0      # number of words with all lower  letters
cap_counter = 0             # helper counter of capital letters
low_counter = 0             # helper lower of capital letters
num_sequence = ''           # helper empty sequence for numbers 
total_sum = 0               # numerical sequence sum variable
num_sequences = []          # numerical sequence list
word_lengths_dict = dict()  # inital dictionary for lengths of words + frequence
gaps = 0                    # nb of gaps in fina l formating, see lower

# Login sequence - test if username is in dictionary, then if password is correct
user = input('Username: ')
if user in login_credentials.keys():
  password = input('Password: ')
  if password == login_credentials[user]:
    print('----------------------------------------\n'+'Welcome to the app, '+user)
    print('We have 3 texts to be analyzed.')

# Enter number of text to be evaluated, check if number is digit, then if its inside specified range
    text_code = input('----------------------------------------\n'+'Enter a number btw. 1 and 3 to select: ')
    if text_code.isdigit() == False:
      print('You have entered a letter, text code must be a number ranging 1-3, terminating the program...')
    else:
      text_code = int(text_code)
      if text_code not in range(1,nb_texts+1):                                                                             
        print('Invalid selection, text code must be a number ranging 1-3, terminating the program...')

# Clean up of text, to get rid of paragraphs, dots, comas and such
      else:
        text = TEXTS[text_code-1].replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('?', ' ').replace('!', ' ')

# Create list of words, test to prevent creation of null strings in list
        for word in text.split(' '):
          if len(word) > 0:
            word_list.append(word)
            word_count = len(word_list)

# Identifying words with 1st capital letter, adding to the counter 
        for cap_word in word_list:
          if cap_word[0].isupper() == True:
            cap_word_count += 1

# Identifying the sequences in word list: All_capital, all_lower, numerical. testing word lengths and adding to a dictioanry
        for real_word in word_list:
          cap_counter = 0
          low_counter = 0
          num_sequence = ''
          word_legth = len(real_word)
          if word_legth not in word_lengths_dict.keys():
            word_lengths_dict.update({word_legth:0})
          word_lengths_dict.update({word_legth:word_lengths_dict[word_legth]+1})
          for letter in real_word:
            if letter.isupper() == True:
              cap_counter += 1
            elif letter.islower() == True:
              low_counter += 1
            elif letter.isdigit():
              num_sequence += letter
            if cap_counter == len(real_word):
              all_cap_word_count += 1
            elif low_counter == len(real_word):
              all_low_word_count += 1
          if num_sequence != '':
            num_sequences.append(num_sequence)
            total_sum = total_sum + int(num_sequence)

# Sorting by word lengths into new dictionary, where key is word length and values is count of such words
        sorted_keys = sorted(word_lengths_dict.keys())
        sorted_word_lengths_dict = dict()
        max_value = max(word_lengths_dict.values())

# Printing results so far
        print('----------------------------------------')
        print('There are',word_count,'words in the selected text.')
        print('There are',cap_word_count,'titlecase words.')
        print('There are',all_cap_word_count,'uppercase words.')
        print('There are',all_low_word_count,'lowercase words.')
        print('There are',len(num_sequences),'numeric strings.')
        print('The sum of all the numbers ',total_sum)
        print('----------------------------------------')

# formating gaps - if there are more than 11 occurences, * character graph is too long, so also |NR must be further
# Printing charrt with headers
        if max_value > 11:
          gaps = max_value-11
        print('LEN|  OCCURENCES  '+str(gaps*' ')+'|NR.')
        print('----------------------------------------')
        for key in sorted_keys:
          sorted_word_lengths_dict.update({key:word_lengths_dict[key]})
          print('{:3d}'.format(key)+'| '+'*'*word_lengths_dict[key]+(2+max_value-word_lengths_dict[key])*' '+'|'+str(word_lengths_dict[key]))
        
  else:
    print('Wrong password, terminating the program...')
else:
  print('User is not registered, terminating the program...')
  
