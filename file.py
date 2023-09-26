f1=open("satya.txt",'w')
f1.write("welcome to bhimavaram institute of engineering and technology")
f1.close()
f1=open("satya.txt","r")
print(f1.read())
f1.close()
f1=open("sweety.txt",'w')
lines=['python\n','programming\n','language']
f1.writelines(lines)
f1.close()


