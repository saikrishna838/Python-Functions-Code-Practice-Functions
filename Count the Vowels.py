def count_the_vowels(word):
    count = 0
    for letter in word:
        is_a = letter == 'a'
        is_e = letter == 'e'
        is_i = letter == 'i'
        is_o = letter == 'o'
        is_u = letter == 'u'
        is_vowel = ((((is_a or is_e) or is_i) or is_o) or is_u)
        if is_vowel:
            count += 1
    return count

word = input()
result = count_the_vowels(word)
print(result)
