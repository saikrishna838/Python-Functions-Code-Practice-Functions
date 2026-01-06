def count_of_uppercase(word):
    count = 0
    
    for each_letter in word:
        is_upper_letter = each_letter.isupper()
        
        if is_upper_letter:
            count += 1
        
    return count



word = input()

result = count_of_uppercase(word)

print(result)