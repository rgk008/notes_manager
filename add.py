def add(db):

    col = db["notes"]

    h = input("Enter a heading: ")
    p = input("Enter a paragraph: ")
    crn = input("Enter the creator name: ")

    x = col.find()
    x = list(x)
    a = {
        "_id":len(x)+1,
        "heading":h,
        "paragraph":p,
        "creator":crn
    }
    col.insert_one(a)
