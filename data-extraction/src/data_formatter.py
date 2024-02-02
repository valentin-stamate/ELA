import os

from src.logger import LOGGER
from src.conf import TAGS


def list_files_in_folder(folder_path):
    try:
        # Use os.listdir to get a list of all files in the specified folder
        files = os.listdir(folder_path)

        return files

    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'your_folder_path' with the actual folder path

def main():
    folder_path = 'output\\wikidata\\'
    cwd = os.path.join(os.getcwd(), folder_path)

    files = list_files_in_folder(folder_path)
    for file in files:
        filepath = os.path.join(cwd, file)
        try:
            with open(filepath, 'r') as f:
                LOGGER.info(f"reading file {filepath}")
                content = f.read()
                for tag in TAGS.keys():
                    # LOGGER.info(f"replacing {tag} with {TAGS[tag]}")
                    content = content.replace(tag + '"', TAGS[tag] + '"')
                updated_file = os.path.join(cwd, 'updated')
                updated_file = os.path.join(updated_file, file)
                with open(updated_file, 'w+') as uf:
                    LOGGER.info(f"writing file {updated_file}")
                    uf.write(content)
        except:
            pass

        # break


if __name__ == '__main__':
    main()
