
db = list()

class Person:
    
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    
    def full_name(self):
        return "{} {}".format(self.firstname, self.lastname)
        
    def age_in_x_years(self, number_of_years):
        return self.age + number_of_years
        
    def output_all(self):
        print(self.firstname)
        print(self.lastname)
        print(self.age)
        
    
def make_person(first_name, last_name, age):
    new_person = Person(first_name, last_name, age)
    # new_person.firstname = first_name
    # new_person.lastname = last_name
    # new_person.age = age
    return new_person
    
def create_people():
    with open("data.txt", 'r') as in_file:
        inline = in_file.readline().strip("\n")
        while inline != "END":
            data = inline.split(',')
            new_person=Person(data[0], data[1], data[2])
            db.append(new_person)
            inline = in_file.readline().strip("\n")

    
if __name__ == "__main__":
    create_people()
    for x in db:
        x.output_all()
   
  
    

    
    