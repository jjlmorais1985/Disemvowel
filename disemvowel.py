def disemvowel(string_):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
              string_ = string_.replace(vowel, '')
    return string_
