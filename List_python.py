x = ["abc","xyz","adg","kkd"]

for value in x:
    if value[0] =="a":
        print(value)
    else:
        print("NF")


print(x[2])
print(x[1])    
print(x[3])   #prints the second element of the list

		
l2 = [item for item in x if item[0]=="a"]
print(l2)
l2.append("abc")              #add item in list
print(l2)
x.append(l2)                 #append two lists(it will add list as an element and not as values(use extend for adding lists)   
print(x)     
x.extend(l2)                  # add two lists
print(x)

x=[ ["d", "b"], ["c","e", "sdf"]]
print(min(x))
print(max(x))


## where is problems that we solved on saturday n sunday?







#[item for item in range(10) if  item > 5]     \\Creates a list of 5 elements starting with 6 till 10.





