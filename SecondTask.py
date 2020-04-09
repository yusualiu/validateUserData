
# collect user details
def collectUser():
  firstname = input('What is your Firstname: ')
  lastname = input('What is your Lastname: ')
  email = input('What is your Email: ')
  
  containerDict = {'firstname':firstname,'lastname':lastname,'email':email}  
  
  # generate user password
  userFirstLetters =firstname[:2]
  userLastLetters = lastname[-2:]
  #create password
  password = ''.join([userFirstLetters,userLastLetters,randomised()])  
  print('Your password is ',password)
  status = input('Are you satisfied with your password? Type yes or no ')
  status = status.strip()
  if status.lower() == 'yes':
    print(f'Your Firstname is {firstname} \nYour Lastname is {lastname} \nYour Email is {email}')    
  else:    
    userPassword = input('Please put your password(must be greater than 7 characters) ')
    papasswordLength = len(userPassword)
    while papasswordLength < 7:
      userPassword = input('Please put your password(must be greater than 7 characters) ')
      papasswordLength = len(userPassword)
    print(f'Your Firstname is {firstname} \nYour Lastname is {lastname} \nYour Email is {email} \n')
  return containerDict
    

# random string generator
def randomised(stringLength=5):
  import random
  import string
  letters = string.ascii_lowercase
  # random.choice(letters)# get random single character
  listCharacter = [random.choice(letters) for element in range(stringLength)] #create list of characters
  randomStrings = ''.join(listCharacter) # convert list to string
  return randomStrings




#store more than one user details
container = []
counter = 1
while counter:
  item = collectUser()
  container.append(item)
  counter = 0
  
print('User has been added\n--------------')

for item in container:
  print(item)

# print(externalContainer)
# print('The users container is shown below\n--------------')
# for key,item in externalContainer.items():
#   print(f"Your {key} is {item}")
 







    