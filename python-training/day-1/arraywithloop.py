
userdata=['admin','manager','qa']

for udata in userdata:
    print(udata)


#-----------

userdata=['admin','manager','qa']

for i,data in enumerate(userdata):
    print(i, data)

#---------------
projectType=['HRMS','IT','Finance']

dummy=[]

for project in projectType:
    if project =='Banking':
        continue
    else:
        print(f"Developing Project {project}")
dummy.append('Banking')
print(f"Delevoped {dummy}")