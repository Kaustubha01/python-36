input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()

print('list: ', user_list)

print('list_sorted:',sorted(input_string))

user_list.sort()
print('list_sort:',user_list)
