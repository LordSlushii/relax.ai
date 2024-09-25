import csv
fob=open("relax.csv","a")
obj=csv.writer(fob)
##obj.writerow(["Date","Points"])
date=input("Enter The Date:")
points=int(input("Enter The Points:"))
lis=[date,points]
obj.writerow(lis)
fob.close()
