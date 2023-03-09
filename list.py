#--------List operation learning

#(1)--------create list 
list_inp = [1,2,3,4]

#(2)--------get string input from user and convert it to list

user_input = input()
inp_str = user_input.strip()
list_create = []
for i in inp_str:
    list_create.append(int(i))


#(3)--------get random input with extra char from user and convert it to list, for eg: 1,2,3,4

newinp = input()
newlist = []
for i in newinp.replace(",", " ").split():
    newlist.append(int(i))
print(newlist)




