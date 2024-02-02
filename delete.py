def delete(db):
     
    col = db["notes"]
    print("These are the notes available")
    data=col.find({},{'heading'})
    # print(list(data))
    n=1
    for d in data:
        print( n,d['heading'],sep=".")
        n+=1
    remove=int(input("which filename do you want to delete:"))
    col.delete_one({"_id":remove})
    print("Deleted successfully")
    input()