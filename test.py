
with open("followers.txt", "a+") as file_object: # Open the file in append & read mode ('a+')
    file_object.seek(0) # Move read cursor to the start of file.
    data = file_object.read(100) # If file is not empty then append '\n'
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write("hello hi") # Append text at the end of file