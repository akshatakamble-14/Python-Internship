def remove_duplicates(my_list)
   unique_list = list(set(my_list))
   return unique_list

original_list = [1,2,2,3,4,4,5]
list_without_duplicates = remove_duplicates(original_list)

print(f"Original list : {original_list}")
print(f"List without duplicates : {list_without_duplicates}")
