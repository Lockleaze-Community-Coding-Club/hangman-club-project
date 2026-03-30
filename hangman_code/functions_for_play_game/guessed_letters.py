
def used_letters_function(letter, used_letters):
    used_letters [:]= [item.lower() for item in used_letters]
            
    letter = letter.lower()
    # Step 1: convert to lowercase
    used_letters.append(letter)   # Add text to the end of the list
    print(used_letters)
    return used_letters










