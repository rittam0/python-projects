word_a= "listen"
word_b="silent"
lower_a=word_a.lower()
lower_b=word_b.lower()
sorted_a=sorted(lower_a)
sorted_b=sorted(lower_b)
is_anagram= (sorted_a==sorted_b)
print(f"are they anagrams?: {is_anagram}")