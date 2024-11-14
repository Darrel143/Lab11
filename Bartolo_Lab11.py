words = []
for i in range(10):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

while True:
    length = input("Enter a length/number: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Invalid input. Please enter a numeric value.")

matching_words = [word for word in words if len(word) >= length]

if matching_words:
    print("Words with the specified length:", ', '.join(matching_words))
else:
    print("No words found with the specified length.")
