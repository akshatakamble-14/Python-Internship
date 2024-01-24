username= "myusername"
password= "mypassword"

input_username=input("Enter your username:  ")
input_password=input("Enter your password:  ")

if input_username==username and input_password==password:
  print("Login successfully Welcome back,"+input_username+ "!")
else:
  print("Login failed.Invalid username or password.")
