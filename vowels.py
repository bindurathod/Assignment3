vowels =['a','e','i','o','u']
word = input("Enter any word : ")
data = set(word)
result = data.intersection(vowels)
print("Vowels present in given statement :",result)
