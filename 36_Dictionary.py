dict1 = {'Name':'First','Age':20,}
print(dict1['Name'],dict1['Age'])

#add
dict1['Lastname'] = 'Onez'
print("Hello",dict1['Name'],dict1['Lastname'])

#delete
#dict1.clear()

#change
dict1['Name'] = 'Mind'
print(dict1)

word = {'Ant':'ทด','Bird':'นก','Cat':'แมว','Dog':'หมา','Ebola':'โรคอีโบล่า'}
print(word['Dog'])

print(word.keys())
for i in word.keys():
    print(i)

