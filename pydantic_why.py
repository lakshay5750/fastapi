def load_data(name:str,age:int):
    print(name)
    print(age)
    print("added to the database")



##new way to do that
def insert_data(name,age):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("data added successfully")
    else :
        print("not with type")    
    
insert_data("lakshay",30)