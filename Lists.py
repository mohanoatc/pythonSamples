list=[]
vowels =['a','e','i','o','u']
word= input('enter ur name:')
for i in word:
    if i in vowels:
        if i not in list:
            list.append(i)
print(list)




