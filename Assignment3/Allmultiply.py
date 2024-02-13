def multiply_list_items(my_list):
   result=1
   for item in my_list:
     result *= item
     return result

my_list = [1,2,3,4,5]
result = multiply_list_items(my_list)
print(f"The product of all the items in list is : {result}")
