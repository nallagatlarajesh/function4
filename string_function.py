#string as parameter
def fullname(fname,lname):
    fullname=fname+" "+lname
    return f"hello {fullname}"
first=input("enter 1st name :")
last=input("enter 2nd name:")
#function calling
fullname(first,last)
