f1=open("satya.txt",'w')
f1.write("welcome to bhimavaram institute of engineering and technology")
f1.close()
f1=open("satya.txt","r")
print(f1.read())
f1.close()
f1=open("sweety.txt",'w')
line=['python\n','programming\n','language']
f1.writelines(line)
f1.close()
f1=open("sweety.txt",'r')
print(f1.read())
f1.close()
f1=open("sweety.txt","a")
f1.write("\nsatyavathi")
f1.close()
f1=open("sweety.txt",'a')
f1.write("\n welcome to python files")
f1.close()
f1=open("sweety.txt","r")
print(f1.read())
f1.close()
