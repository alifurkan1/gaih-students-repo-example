#First Part of The HW1
my_list=list(range(10))
half_list=int(len(my_list)/2)
new_list=my_list.copy()
for i in range(half_list):
    new_list[i]=my_list[i+half_list]
    new_list[i+half_list]=my_list[i]
print(new_list)    

#Second Part of The HW1
my_number=int(input("Please input a number:"))
print({i for i in my_number if i%2==0})