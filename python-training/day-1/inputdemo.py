




#---- conditional statement with input 
# if age is < 18 ,print -> not allowed to vote ,if age >=18 and <70 allwed to vote ,else print -> senior citi

user_age=int(input('Enter user age'))

if user_age <= 0:
    print ('please enter valid age')
elif user_age <18:
    print('Not allowed to vote')
elif user_age >=18 and user_age< 70:
    print('voting allowed')
else:
    print('senior citizen')