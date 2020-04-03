
# collect user details
def collectUser():
  firstname = input('What is your Firstname: ')
  lastname = input('What is your Lastname: ')
  email = input('What is your Email: ')
  
  container = {'firstname':firstname,'lastname':lastname,'email':email}  
  
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
  return container
    

# random string generator
def randomised(stringLength=5):
  import random
  import string
  letters = string.ascii_lowercase
  # random.choice(letters)# get random single character
  listCharacter = [random.choice(letters) for element in range(stringLength)] #create list of characters
  randomStrings = ''.join(listCharacter) # convert list to string
  return randomStrings

  
    
# users container
externalContainer = {}
containerLength = 0
while containerLength < 1:
  container = collectUser()  #each user details
  externalContainer.update(container)
  containerLength += 1


# print(externalContainer)
print('The users container is shown below\n--------------')
for key,item in externalContainer.items():
  print(f"Your {key} is {item}")
 



# print(collectUser())



    