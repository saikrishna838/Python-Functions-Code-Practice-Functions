def valid_string(string):
    valid_length = len(string) >= 6
    is_first_character_digit = string[0].isdigit()
    
    if valid_length or is_first_character_digit:
        statement = "Valid String"
    else:
        statement = "Invalid String"
    return statement
     



string = input()

result = valid_string(string)

print(result)