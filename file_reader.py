import os


class FileReader:
    def __init__(self, directory):
        self.directory = directory

    def read_files(self):
        files = {}
        print(f"Reading files from directory: {self.directory}")  # Log the directory path
        for filename in os.listdir(self.directory):
            if filename.endswith('.py') or filename.endswith('.cpp'):
                file_path = os.path.join(self.directory, filename)
                print(f"Reading file: {file_path}")  # Log each file being read
                with open(file_path, 'r', encoding='utf-8') as file:
                    files[filename] = file.read()
        print(f"Total files read: {len(files)}")  # Log the number of files found
        return files
