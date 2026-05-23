#File-Based Data Storage
#How would you store user data permanently using files and retrieve it later?

while True:
    print("1)STORE DATA")
    print("2)RETRIEVE DATA")
    print("3)EXIT:")
    ch=input("CHOOSE:")
    if ch=="1":
        name=input("ENETR THE NAME:")
        age=int(input("ENTER THE AGE:"))
        salary=int(input("ENTER THE SALARY:"))
        file=open("hi.txt","a")
        file.write(name+","+str(age)+","+str(salary)+"\n")
        file.close()
    elif ch=="2":
        file=open("hi.txt","r")
        for line in file:
             data=line.strip().split(",")
             name=data[0]
             age=data[1]
             salary=data[2]
             print("NAME:",name)
             print("AGE:",age)
             print("SALARY:",salary)
             print("----")
        file.close()
    elif ch=="3":
        print("THANK YOU!")
        break
