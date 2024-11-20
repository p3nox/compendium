import re

def delete_page_lines(file_path):
    try:
        # Open the file and read all lines
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Filter out lines that match the pattern
        pattern = re.compile(r'^.*\bpage\s\d+\b.*$', re.IGNORECASE)
        filtered_lines = [line for line in lines if not pattern.match(line)]
        
        # Write the filtered lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)
        
        print(f"Lines containing 'page <number>' have been removed from {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'standards - Copy.md'  # Replace with your Markdown file's path
delete_page_lines(file_path)
