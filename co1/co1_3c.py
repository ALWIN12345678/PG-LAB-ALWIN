word=input("Enter word")
print("the original string",word)
for i in word:
    if i in ['a','A','e','E','i','I','o','O','u','U']:
        print([i],end=" ")