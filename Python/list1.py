print ('Hello World')
My_list=[10,40,50,20,30,10,40,10]
Your_list=['saw','small','foxes','he','six']
print("The First List created",My_list)
print("The Second List created is",Your_list)
My_list.append(60)
print("After Appending First List created",My_list)
My_list.insert(1,70)
print("After inserting at 2nd position First List created",My_list)

My_list.sort()
print("After sorting first list created",My_list)
My_list.sort(reverse=True)
print("After desending sorting first list",My_list)
Your_list.append(3.5)
print("After Appending second list created",Your_list)
Your_list.pop(5)
print("After poping second list created",Your_list)

Your_list.append(3.5)
print("After Appending second list created",Your_list)
Your_list.remove(3.5)
print("After Removing Second list",Your_list)

Merge_list=My_list+Your_list
print("After Merging list is ",Merge_list)
total=sum(My_list)
print("The total is",total)

My_list.sort()
print("The smallest no",min(My_list))
print("The smallest no",max(My_list))
print("The second max no",My_list[len(My_list)-2])


from collections import Counter
occurences=Counter(My_list)
print("The counter of data elements",occurences)

print("the scling opertion",Your_list[1:4])
print("the scling opertion",Your_list[-3:1])
l=len(Your_list)
mid=l//2
print("the mid element",mid)
print("The after mid element",Your_list[mid+1:])
print("The before mid element",Your_list[mid-1::-1])


