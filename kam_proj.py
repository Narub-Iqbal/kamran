import pandas as pd
name=input("May I know Your Good Name?\n")
print("Welcom ",name,''' 
if you want to book a room for you, you are at right place''')
city=input("Which City you want to live?\n")
print("We have followning hotels in ",city)
for hotel in ['pc','Ramada','Continental','Luxery']:
    print(hotel)
choose_hotel=input("which hotel you want to book in "+city+": ")
room_type=input("Which type of room do you want?\n")
rooms=input("How many rooms do You want to book?\n")
night=input("How many nights do you want to stay?\n")
persons=int(input("How many persons you are staying?\n"))
names=[]
phone=[]
address=[]
id_card=[]
age=[]
gender=[]
security=[]
for i in range(persons):
    nm=input("Enter you Name: ")
    pn=input("Enter your Phone number: ")
    ad=input("Enter your Address: ")
    ic=input("Enter your ID Card number: ")
    ag=input("Enter your Age: ")
    gnr=input("Enter your Gender: ")
    sc=input("Enter your security code: ")
    names.append(nm)
    phone.append(pn)
    address.append(ad)
    id_card.append(ic)
    age.append(ag)
    gender.append(gnr)
    security.append(sc)
choice=pd.DataFrame({'City':[city], 'Hotel':[choose_hotel],'Room Type':[room_type],'Room Numbers':[rooms],'Nights':[night],'Person staying':[persons]})
personal_info=pd.DataFrame({'Names':names,'Phone Numbers':phone,'Address':address,'ID card No':id_card,'Age':age,'Gender':gender,'Security Code':security})
print(choice)
print(personal_info)
#stores informations in excel sheets
choice.to_csv("user_choice.csv",index=False)
personal_info.to_csv("user_information.csv",index=False)
print("Details are received, Wait for the confirmation messages")