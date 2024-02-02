def view(db):
    col = db["notes"]
    print("These are the notes available")
    data=col.find({},{'heading'})
    # print(list(data))
    n=1
    for d in data:
        print( n,d['heading'],sep=".")
        n+=1

    print()
    
    value=int(input("which notes do you want to access:"))

    note = col.find_one({"_id":value})

    print("Heading")
    print(note['heading'])
    print('--------------------**********--------------------')
    print("Paragraph")
    print(note['paragraph'])
    print("--------------------**********--------------------")
    print()
    print("Creator")
    print(note['creator'])
    input()