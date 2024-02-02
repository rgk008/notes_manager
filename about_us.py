def about_us(db):
     
     col = db["creator"]
     print("This project is created by")
     # print("Renukesvr,Gowdhamkumar, Jayasurya")

     us = col.find()
     us= list(us)
     # print(us)
     n=1
     for i in us:
          print(n,i['name']+" "+i["designation"],sep=".")
          n+=1