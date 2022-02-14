'''
list append(), extend() examples
list.append(element)  adds a single element to a list at the extend
list.extend(lsit_x) list1 gets added with list_x element at the end - Extension
'''
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c']
# append and extend on the list
list1.append("new")
print(list1) # [1,2,3,4,5,'new']
list1.extend(list2)
print(list1) #1,2,3,4,5,'new', 'a', 'b', 'c']
