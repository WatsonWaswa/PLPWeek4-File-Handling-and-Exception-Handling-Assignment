def create_file(filename, content):
    """Creates a new file and writes initial content."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f" File '{filename}' created successfully.")
    except Exception as e:
        print(f" Error creating file: {e}")

def modify_file_content(filename):
    """Reads the file, modifies its content, and writes to a new file."""
    try:
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify content (convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Create a new file and write the modified content
        new_filename = "PLP-modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f" Modified content saved in '{new_filename}'")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: Permission denied. Unable to access the file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Step 1: Create a file with the name "PLP-filename.txt"
filename = "PLP-filename.txt"
initial_content = "Hello, this is a PLP sample file."
create_file(filename, initial_content)

# Step 2: Modify the file content
modify_file_content(filename)