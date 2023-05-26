l=['BOB','JACK','GARY']#list .append(), .remove()
t=('BOB','JACK','GARY')#tuple
s={'BOB','JACK','GARY'}#set function .add()
r={'ROLF'}
print(t[0])#list and set can be accsessd like this but set dosen't allow this form
l.append("Smith")#element will be added at the end of the list
l.remove("BOB")#element will be removed
print(l)
#tuple cannot append any element


#operations of set
print(s.difference(r))
print(s.intersection(r))
print(s.union(r))