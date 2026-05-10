def used_letters_function(used_letters, letter):
   
    used_letters [:]= [item.lower() for item in used_letters]
            
    letter = letter.lower()
    # Step 1: convert to lowercase
    used_letters.append(letter)   # Add text to the end of the list
    return used_letters






