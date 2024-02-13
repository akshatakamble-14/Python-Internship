lis = []
num = int(input("How many elements you want to enter:  ")

for i in range(1, num+1):
  element = int(input("enter exact number:  "))
  lis.append(element)

print("Original list is : ", lis)
print("Smallest number is :  ", min(lis))
