names= "BOBY"
next=f"my name is",{names}

print(f"my name is",{names})

names="BABBY"
print(f"my name is",{names})

#Defining a template and then working on it using Format functiom
n="bob"
template= "Hello, {},""What your name? Isn't it {}"
ans=template.format(n,names)
print(ans)
