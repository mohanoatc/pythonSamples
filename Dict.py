'''
person3 = { 'Name': 'Ford Prefect',             'Gender': 'Male',             'Occupation': 'Researcher',             'Home Planet': 'Betelgeuse Seven' }
print(person3['Name'])

person3['Age']=33
print(person3)
'''

dict={'e':0,'i':0,'o':0,'u':0,'a':0}
vowels =['a','e','i','o','u']
word= input('enter ur name:')
word=word.lower()
for i in word:
    if i in vowels:
        dict[i] += 1
        # if i in dict[i]:
        #     list.append(i)
for k in sorted(dict):
    print(k,'times shown', dict[k])
print (dict.items())