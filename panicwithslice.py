phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# newlist=plist[1:8]
'''newlist1=plist[4:8]
newlist1=newlist1.remove(" ")
newlist2=newlist1.insert(1,newlist1.pop())'''
# newlist.remove("'")
# # ['o', 'n', 't', ' ', 'p', 'a']
# newlist1 = newlist.insert(3,newlist.pop(5))
# print(newlist)
# print(newlist1)
# print(newlist,newlist1)


newphrase = ''.join(plist[1:3])
newphrase = newphrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(newphrase)