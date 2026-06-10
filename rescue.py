word_list= ["Racecar", "Vellore", "Madam"]
valid_palindromes=[]
for current_word in word_list:
    clean= current_word.lower()
    reverse_word= clean[::-1]
    is_match= (clean==reverse_word)
    if is_match:
        valid_palindromes.append(current_word)
print(f"Valid palindromes found: {valid_palindromes}")