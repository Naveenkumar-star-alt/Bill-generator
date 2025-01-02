from datetime import datetime

Name=input("Enter your name :")
#list of items
list='''
Rice     Rs 20/kg
Suger    Rs 30/kg
Salt     Rs 20/kg
Oil      Rs 45/liter
Paneer   Rs 110/kg
Maggi    Rs 50/kg
Boost    Rs 90/each
Colgate  Rs 80/each
'''
#decleration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={"Rice":20,
       "Suger":30,
       "Salt":20,
       "Oil":45,
       "paneer":110,
       "Maggi":50,
       "Boost":90,
       "Colgate":80}

option=int(input("for list of items press 1:"))
if option==1:
  print(list)
for i in range(len(items)):
  inp1=int(input("if you want to buy press 1 or 2 for exit:"))
  if inp1==2:
    break
  if inp1==1:
    item=input("ENter your items:")
    quantity=int(input("Enter your quantity:"))
    if item in items.keys():
      price=quantity*(items[item])
      pricelist.append((item,quantity,items,price))
      totalprice+=price
      ilist.append(item)
      qlist.append(quantity)
      plist.append(price)
      gst=(totalprice*5)/100
      finalamount=totalprice+gst
    else:
      print("Sorry your selected item is not available !")
  else:
    print("Your entered wrong number !")
  inp=input("can i bill the items yes or no :")
  if inp=="yes":
    pass
    if finalamount!=0:
      print(25*"=","Naveen supermarket",25*"=")
      print(28*" ","nandyal")
      print("Name : ",Name,30*" ","Date:",datetime.now())
      print(75*"-")
      print("sno",5*" ","items",5*" ","quantity",5*" ","price")
      for i in range(len(pricelist)):
        print(i,8*' ',5*' ',ilist[i],5*' ',"qlist[i]",5*" " ,plist[i])
      print(75*"-")
      print(50*" ","Totalamount:","Rs",totalprice)
      print(50*" ","gst amount:","Rs",gst)
      print(75*"-")
      print(50*" ","finalamount:","Rs",finalamount)
      print(75*"-")
      print(20*" ","Thanks for visting!")
      print(75*"-")