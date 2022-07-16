def fprint(name, object, max_length=60):
    """ A fancier print function
    
    Args:
        name (str): Title of the printout
        object (str): The variable / object you like to print
        max_length (int): Defines the width of the print box
    """
    object = str(object)
    name = str(name)
    hr = "#" + "="*(max_length - 2) + "#"
    def text_field(name):
        length = len(name)
        return str("#" + " "*int((max_length - length)/2 - 1) + name +
              " "*int((max_length - length)/2 + 1*(len(name)%2 - 1)) + "#")
    if len(name) > max_length - 5:
        name_split = []
        while len(name) > max_length - 5:
            name_split.append(name[:max_length-5])
            name = name[max_length-5:]
        name_split.append(name[:max_length-5])
    else:
        name_split = [name]
    
    if len(object) > max_length - 5:
        object_split = []
        while len(object) > max_length - 5:
            object_split.append(object[:max_length-5])
            object = object[max_length-5:]
        object_split.append(object[:max_length-5])
    else:
        object_split = [object]
    
    print("")
    print(hr)
    print(text_field(name))
    print(hr)
    for obj in object_split:
        print(text_field(obj))
    print(hr)
    print("")
    
if __name__ == "__main__":
    fprint("test", "Hello World!", 40)
    fprint("A python list", [1, 2, 3, 4, 5])
    fprint("A python dict", {"a": "b", "c": "d"})