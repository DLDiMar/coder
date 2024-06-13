# The input array of [(int, string)] format is sorted in ascending order by number 
def sort_array_by_number(input_array):
    input_array.sort(key=lambda x: int(x[0]))
    sorted_array = [(str(i + 1), word) for i, (_, word) in enumerate(input_array)]
    return sorted_array

# Decodes a number pyramid-style encryption file to output as sequence of strings
# Assumes input file has randomized numbering, yet has every sequential integer available within it's range
def decode(file_path):
    try:
        with open(file_path, 'r') as file:
            message = file.read().split('\n')

        if not message:
            raise ValueError("Error: Empty message file.")
        
        input_array = []

        # Read and place encoded message from the file into an array
        # Verify in-place a valid format of (int, string)
        for line in message:
            if line.strip() != '':
                try:
                    parts = line.split()
                    if len(parts) != 2:
                        raise ValueError("Invalid line format in file. Must contain two parts.")
                    
                    number, word = parts
                    if not number.isdigit():
                        raise ValueError("Invalid line format in file. First part of line must be a non-negative integer.")
                    if not isinstance(word, str):
                        raise ValueError("Invalid line format in file. Second part of line must be a string.")
                    
                    input_array.append((number, word))
                    
                except ValueError as e:
                    print(f"Error: {e}")
        
        sorted_array = sort_array_by_number(input_array)
        
        # Initialize variables to store decoded message and range of lines in file
        decoded_message = []
        initialKey, _ = sorted_array[0]
        finalKey, _ = sorted_array[len(sorted_array)-1]

        # Calculate if value is last value in number pyramid (y = (x * (x+1)) // 2)
        for key, word in sorted_array:
            if any(int(key) == (n * (n + 1)) // 2 for n in range(int(initialKey), int(finalKey))):
                decoded_message.append((key, word))
            else:
                continue

        # Append to a decoding string output
        decoded_string = ' '.join([f"{word}" for _, word in decoded_message])

        return decoded_string
    
    except Exception as e:
        # Handle exceptions here, e.g., print an error message or log the exception
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = '<inputPath>/input.txt'  # Replace with the actual file path
decoded_result = decode(file_path)
print(decoded_result)