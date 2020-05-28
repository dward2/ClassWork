import json

def create_person():
    bob = {"First Name": "Robert",
           "Last Name": "Smith",
           "Age": 35,
           "Visits": ["1/1/2020", "1/10/2020", 
                      "3/15/2020"]}
    return bob

def output_json(my_dict):
    filename = "patient.json"
    out_file = open(filename, 'w')
    json.dump(my_dict, out_file)
    out_file.close()

if __name__ == "__main__":
    x = create_person()
    output_json(x)

