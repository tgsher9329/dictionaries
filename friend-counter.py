ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}


# --------


# write a function countFriends() that accepts a dictionary 
# as an argument and returns a new dictionary that includes a new key friends_count:


def countFriends(dic):
    friends_count = {
        len(ramit['friends'])
    }
    return friends_count

result = (countFriends(ramit))
print(result)