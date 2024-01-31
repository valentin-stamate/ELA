import re

from src.utils import write_file


def extract_values_from_line(line):
    # Define the regular expression
    regex_pattern = r'^(.*)\(P([^)]+)\)$'

    # Use re.search to find the match in the line
    match = re.search(regex_pattern, line)

    # If a match is found, return a tuple with the text value before "Pxx" and "Pxx"
    if match:
        # print('match')
        return match.group(1).strip(), match.group(2)
    else:
        return None, None


def main():
    # Specify the path to your file
    file_path = 'input/labels.txt'  # Replace 'your_file.txt' with the actual file path
    tags = {}
    try:
        # Open the file and read each line
        with open(file_path, 'r', encoding='utf-8') as file:
            # print('read')
            for line in file:

                # print(line)  # Call the function to extract values from each line
                text_value, pxx_value = extract_values_from_line(line.strip())

                # Print the extracted values (or handle them as needed)
                if text_value is not None and pxx_value is not None:
                    tags["P" + pxx_value] = text_value
            print(tags)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
