# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name"""
    #The code above is an example of a Docstring - it documentates my function.
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs." 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What's your name? "), input("What's your last name? ")))
