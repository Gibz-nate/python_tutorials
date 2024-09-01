def count_vowels(text):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    total = 0
    u_vowels = set()
    for char in text:
        for vowel in vowels:
            if char == vowel:
                total += 1
                u_vowels.add(char)
    return total, u_vowels            

