veh=[['x5','bmw',2020,'petrol',20,1],['panamera','porsche',2022,'gas',25,2]]
import datetime
while True:
 print('''
1.vehicle details
2.view vehicle details
3.upadte vehicle details
4.delete vehicle details
5.search vehicle
6.add details
7.exit
          ''')
 
 choice=int(input("enter your choice :"))
 if choice==1:
         name=str(input("enter name :"))
         brand=str(input("enter brand :"))
         model=int(input("enter the model :"))
         fueltype=str(input("enter fueltype :"))
         mileage=int(input("enter the mileage :"))
         insurance=int(input("enter the insurance :"))
         veh.append([name,brand,model,fueltype,mileage,insurance])
 elif choice==2:
      for i in veh:
           print(i)
 
 elif choice==3:
         name=str(input("enter name :"))
         print('''
1.enter brand
2.enter model
3.enter fueltype
4.enter mileage
5.enter insurance
''')
         f=0
         for i in veh:
              if name in i:
                   choice=int(input("enter your choice :"))
                   if choice==1:
                        brand=str(input("enter brand :"))
                        i[1]=brand
                   elif choice==2:
                        model=int(input("enter model :"))
                        i[2]=model
                   elif choice==3:
                        fueltype=str(input("enter fueltype  :"))
                        i[3]=fueltype
                   elif choice==4:
                        mileage=str(input("enter mileage :"))
                        i[4]=mileage
                   elif choice==5:
                        insurance=int(input("enter insurance :"))
                        i[5]=insurance
                   f=1           
         if f==0:
              print('invalid name') 
 elif choice==4:
      name=str(input("enter name :"))
      f=0
      for i in veh:
           if name in i:
                veh.remove(i)
                f=1
      if f==0:
           print('invalid name')
 elif choice==5:
      name=str(input("enter name :"))
      f=0
      for i in veh:
           if name in i:
                print(i)
                f=1
      if f==0:
           print('invalid name')
 elif choice==6:
     id=str(input('enter name :'))
     for i in veh:
         if id in i:
             
             date=datetime.datetime.now().strftime('%x')
             i.append([date])

 elif choice==7:
     break
 else:
     print('invalid choice')
