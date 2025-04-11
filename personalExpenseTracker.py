import csv
import os
while True:
    print('Choose from the options below')
    print('1.Add')
    print('2.Display')
    print('3.Modify')
    print('4.Search')
    print('5.Delete')
    print('6.Exit')
    choice=eval(input('Enter your choice:'))

    if choice==1: 
        f=open('personalExpenseTracker.csv','a',newline='')
        fw=csv.writer(f,delimiter=',')
        while True:
            category=input('Enter category:')
            amount=eval(input('Enter amount:'))
            date=input('Enter date:')
            fw.writerow((category,amount,date))
            ans=input('Want to enter more? y/n:')
            if ans.lower()=='n':
                break
        f.close()

    if choice==2:
        f=open('personalExpenseTracker.csv')
        w=csv.reader(f,delimiter=',')
        for i in w:
            print(i)
        f.close()


    if choice==3:
        f1=open('personalExpenseTracker.csv')
        category=input('Enter category to be updated:')
        print('Choose from the options below:')
        print('1.Edit Date')
        print('2.Edit Amount')
        choice1=eval(input('Enter your choice:'))
        if choice1==1:
            date=input('Enter new date:')
            fr=csv.reader(f1,delimiter=',')
            f2=open('personalExpenseTracker1.csv','w',newline='')
            fw=csv.writer(f2,delimiter=',')
            for i in fr:
                if i[0]==category:
                    i[2]=date
                fw.writerow(i)
            f1.close()
            f2.close()
            os.remove('personalExpenseTracker.csv')
            os.rename('personalExpenseTracker1.csv','personalExpenseTracker.csv')
            print('Updated Info!!')
        if choice1==2:
            amount=eval(input('Enter new amount:'))
            fr=csv.reader(f1,delimiter=',')
            f2=open('personalExpenseTracker1.csv','w',newline='')
            fw=csv.writer(f2,delimiter=',')
            for i in fr:
                if i[0]==category:
                    i[1]=amount
                fw.writerow(i)
            f1.close()
            f2.close()
            os.remove('personalExpenseTracker.csv')
            os.rename('personalExpenseTracker1.csv','personalExpenseTracker.csv')
            

    if choice==4:
        f=open('personalExpenseTracker.csv')
        w=csv.reader(f,delimiter=',')
        s=input('Enter category you want to search…')
        for i in w:
            if (i[0])==s:
                print(i)
        f.close()

    if choice==5:
        f1=open('personalExpenseTracker.csv')
        category=input('Enter category to be deleted:')
        fr=csv.reader(f1,delimiter=',')
        f2=open('personalExpenseTracker1.csv','w',newline='')
        fw=csv.writer(f2,delimiter=',')
        for i in fr:
            if (i[0])!=category:
                fw.writerow(i)
        f1.close()
        f2.close()
        os.remove('personalExpenseTracker.csv')
        os.rename('personalExpenseTracker1.csv','personalExpenseTracker.csv')
        print('Deleted!!')
    if choice==6:
        print('Exiting Program!!')
        print('Exited Succesfully!!')
        break
    

    
