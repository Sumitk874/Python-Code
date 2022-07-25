import pickle
import sys

try:
    f=open('email.dat','rb')
    d=pickle.load(f)   
    f.close()
       
except:    
    d={}

while True:

    print('\n1. Find a email address')
    print('2. Add name and email address')
    print('3. Change an email address')
    print('4. Delete an email address')
    print('5. Exit\n')

    choice=input('\nEnter a choice: ')

    if choice:
        choice=int(choice)
    else:
        print('\nEnter a number')
        continue    

    if choice == 1:

        while True:

            name=input('\nEnter the name ')

            if name:
                if name in d:
                    print('\n%s is the email id of %s \n' % (d[name],name))
                    break
                else:
                    print('\n Email not found \n')
                    break
            else:
                print('\nName cannot be empty\n')
                continue
            
    elif choice==2:

        while True:            
        
            name=input('\nEnter the name ')

            if name:
                break;
            else:
                print('\nName cannot be empty \n')
                continue

        while True:            
        
            email=input('\nEnter the email address ')

            if email:
                d[name]=email
                break
            else:
                print('\nEmail cannot be empty\n')
                continue
            
    elif choice==3:

        while True:            
        
            name=input('\nEnter the name to change the email address ')

            if name:
                if name in d:
                    email=input('\nEnter the new email address ')
                    d[name]=email
                    print('\nEmail address changed \n')
                    break;
                else:
                    print('\nName not found \n')
                    break
            else:
                print('\nName cannot be empty \n')
                continue
            
    elif choice == 4:

        while True:            
        
            name=input('\nEnter the name to remove ')

            if name:
                if name in d:
                    del d[name]
                    print('\nName and Email address removed \n ')
                    break;
                else:
                    print('\nName not found \n')
                    break
            else:
                print('\nName cannot be empty\n')
                continue

    elif choice == 5:
        
        f=open('email.dat','wb')
        pickle.dump(d,f)
        f.close()
        sys.exit()
    else:
        print('\nEnter a valid choice ')   