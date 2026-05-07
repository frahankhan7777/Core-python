list = [1, 2, 2, 1]
copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("palindrome")

else:
    print("not a palindrome")