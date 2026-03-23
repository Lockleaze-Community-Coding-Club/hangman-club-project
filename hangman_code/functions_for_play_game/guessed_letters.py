
def used_letters_function(letter_list, new_text):
    letter_list [:]= [item.lower() for item in letter_list]
            
    new_text = new_text.lower()
    # Step 1: convert to lowercase
    letter_list.append(new_text)   # Add text to the end of the list
    return letter_list
    print(letter_list)










