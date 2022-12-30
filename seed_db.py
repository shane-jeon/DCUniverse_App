"Drop database/Create database/ Create tables/ Populate database with data, using data from JSON files from data folder."

import os
import json
import crud
import model
import server
from dict_reform import access_creators, access_biography, access_gender, access_comicvineID, access_name, access_powers, access_image

os.system("dropdb characters")
os.system("createdb characters")

model.connect_to_db(server.app)
model.db.create_all()

directory = 'data/characters'

char_dicts = []

for char_file in os.listdir(directory):
  # f is a single file
  f = os.path.join(directory, char_file)
  print('f', f)
  if os.path.isfile(f):
    # reads JSON file for character
    json_string = open(f).read()
    # print('json_string', json_string)

  # returns JSON file as python dictionary
  json_dict = json.loads(json_string)
  # print('json_dict', json_dict)

  # accesses 'results' and returns dictionary containing only relevant information
  char_results = json_dict['results']
  # print('char_results', char_results)
    
  character_dictionary = {}

  creators = access_creators(char_results)
  biography = access_biography(char_results)
  gender = access_gender(char_results)
  id = access_comicvineID(char_results)
  name = access_name(char_results)
  powers = access_powers(char_results)
  image = access_image(char_results)

  character_dictionary['id'] = id
  character_dictionary['image'] = image
  character_dictionary['name'] = name
  character_dictionary['gender'] = gender
  character_dictionary['biography'] = biography
  character_dictionary['powers'] = powers
  character_dictionary['creators'] = creators

  char_dicts.append(character_dictionary)
  print(f'character_dictionary {character_dictionary}')

print('*'*20)
print(char_dicts)
print('*'*20)
# 12/29/2022 --> will need to create new dictionary to hold results from API request to more easily seed database
characters_in_db = []
# for character in char_dict:
for char in char_dicts:
  # print(character)
  print(char['id'], char['name'], char['biography'])
  id, image, name, gender, biography, power, creator = (
    # character['creators'][1]['name'],
    # character_creators,
    char['id'],
    char['image'],
    char['name'],
    char['gender'],
    char['biography'],
    char['powers'],
    char['creators'],
  )

  db_character = crud.create_character(id, image, name, gender, biography, power, creator)
  characters_in_db.append(db_character)

model.db.session.add_all(characters_in_db)
model.db.session.commit()



# def seed_db_comicvine(char_dict):
#   """Seeding available character data from Comicvine API."""

#   id = char_dict['id']
#   char_name = char_dict['name']


# def create_biography(char_data, char):
#   """Create a character's biography summary."""
  
#   # putting a pin on this ** 10/26/2022 **
#   # char_gender_key = char_data[char]['appearance']['gender'] 
#   # genders = {'female': ['she', 'her', 'hers'], 'male': ['he', 'him', 'his'], 'nonbinary': ['they', 'them', 'their']}

#   # for gender in genders:
#   #   if char_gender_key == gender:

#   char_dict = char_data[char]
#   char_name = char_dict['name']
#   biography_access = char_dict['biography']
#   char_stats = char_dict['powerstats']
#   char_bio = f'''{char_name}, also known as {biography_access['full-name']} first appeared in {biography_access['first-appearance']} and is originally based in {char_dict['work']['base']}. {char_name}'s professional and personal affiliations include '{char_dict['connections']['group-affiliation']}' and
#   '{char_dict['connections']['relatives']}', respectively. {char_name}'s stats are as below:
  
#              {char_name}'s POWERSTATS  
#   +----------------------------------------------+
#     Intelligence: {char_stats['intelligence']}, 
#     Strength: {char_stats['strength']},         
#     Speed: {char_stats['speed']},               
#     Durability: {char_stats['durability']},     
#     Power: {char_stats['power']},               
#     Combat: {char_stats['combat']}              
#   +----------------------------------------------+
#   '''
#   return char_bio


# chars_in_db = []

# for char in char_data:
#   # print(char_data[char])
#   print("char: ", char)
#   char_id, name, alignment, biography = (
#     char_data[char]['id'], 
#     char_data[char]['name'],
#     char_data[char]['biography']['alignment'],
#     create_biography(char_data, char), 
#   )


#   db_char = crud.create_char(char_id, name, alignment, biography)
#   chars_in_db.append(db_char)

# 




# TROUBLESHOOTING 10/25/2022
  # iterate through all values in json file 
  # assign variables to dictionary access contents

  # getting error 'can't dapt type 'dict''
    # blocker resolved: it's because biography is a dictionary,
    # look into this later'
  # error with 'name' column not in relation with something
    # just dropdb and createdb
  # look into why calling crud function just returns <function> i forgot
      # have to be in the database to use said functions (remember to store calls in variables)