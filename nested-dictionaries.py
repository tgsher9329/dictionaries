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

# get ramits email

print('---ramits email---')
print(ramit['email'])

# --------- get ramits first interest

print('---ramits first interest---')
print(ramit['interests'][0])

# ------------ get the email address of jasmine

print('---Jasmines email---')
print(ramit['friends'][0]['email'])

# --------- get jans second interest

print("---Jan's second interest---")
print(ramit['friends'][1]['interests'][1])

# -------