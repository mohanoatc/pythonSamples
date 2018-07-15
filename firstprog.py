#print("hello world".find('r'))


#name = "Mohan"
#number = 10
#print("{0} Is a good boy ".format(name))

student_names= ['Prasad','Mohan','Vamsi','xxxx']
print (student_names[-3:])
print(len(student_names))
student_names.append('bunny')
print(student_names)
del student_names[-1]
print(student_names)
student_names.append(['Prasad','rammm'])
print(student_names)
for name in  student_names :
    print("inloop" , name)
    print("Is List ", isinstance(name, (list,tuple)))
    isLstBln = isinstance(name, (list,tuple))
    if isLstBln == True:
        for innerList in name:
            print("Returning Inner List : "+innerList)