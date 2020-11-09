#same list but can't change
tupleExample = ('First','Mark','Aek')
print(tupleExample)
tupleExample2 = ('Gus','Pam')
print(tupleExample2)
tupleExample3 = tupleExample + tupleExample2 *2
print(tupleExample3)
print(tupleExample3[:2])
print('Pan' in tupleExample3)
for i in tupleExample3:
    print("Hello",i)

