stored_inputs = []

def store_input(text):
    text = text.lower()          # Step 1: convert to lowercase
    stored_inputs.append(text)   # Add text to the end of the list

def show_matrix():
    for index, item in enumerate(stored_inputs, start=1):   # Number each item
        print(f"{index}: {item}")                           # Print each row

def clear_storage():
    stored_inputs.clear()        # Clear the stored inputs list








