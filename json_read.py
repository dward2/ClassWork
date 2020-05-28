import json

def input_json(input_filename):
    in_file = open(input_filename, 'r')
    new_variable = json.load(in_file)
    in_file.close()
    return new_variable
    
if __name__ == "__main__":
    fn = input("Filename: ")
    x = input_json(fn)
    print(x)
    print(type(x))
    
    