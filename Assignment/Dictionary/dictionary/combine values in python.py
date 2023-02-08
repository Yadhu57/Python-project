listofdict = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
#print("The given dictionary is : ",listofdict)
newdict = {}
list1 = []
for d in listofdict: #d gives each dictionary
    #print(d)
    p = list(d.values()) #creates list of values
    list1.append(p[0])
    list1.append(p[1])#list1 contains all individual values in a single list
print(list1)

for i in range(0,len(list1),2): #taking each 2nd item in list1
    #print(i)
    if list1[i] in newdict:
        rep = list1[i]
        print(rep)
        index = list1.index(rep)
        print(index)#finding index of repeated variable
        list1[index+1] = list1[index+1]+list1[i+1] #adding corresponding value
        print(list1[index+1])
        print(list1[i+1])
        newdict[list1[i]] = list1[index +1] #updating value of repeated element
        print(newdict[list1[i]])
    else:
        newdict.setdefault(list1[i],list1[i+1]) #adding values to dicitonary as key:value pairs

#print("The combined dictionary is : ",newdict)










