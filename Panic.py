phrase = "Don't panic!"
plist = list(phrase)
print("first block",phrase)
print("list block",plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
'''
plist.remove('D')
plist.remove("'")

plist.remove('i')
plist.remove('c')
plist.remove('!')
# plist.remove('n')
plist.pop(6)
'''
#Phrase new ont pa
plist.insert(3, plist.pop(2))
plist.insert(4, plist.pop(5))
#plist.insert,(pop(3))

'''
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2, plist.pop(3))
'''
new_phrase = ''.join(plist)
print("second block",plist)
print("Phrase new",new_phrase)


