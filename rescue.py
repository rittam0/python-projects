word="Racecar"
clean= word.lower()
print(clean)

reverse_word= clean[::-1]
print(reverse_word)
is_match= (clean==reverse_word)
print("is it a pallindrome", is_match)