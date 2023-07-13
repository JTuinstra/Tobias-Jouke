class WriteInFile:
    def __init__(self):
        self.file = "test.txt"
        self.title = input("Title: ")
        self.text = input("Text: ")
        self.file_content = self.get_file_content()

    def get_file_content(self):
        file = open(self.file, 'r')
        content = file.read()
        file.close()
        return content

    def write_in_file(self):
        file = open(self.file, 'a')
        file.write(self.title)
        file.write(self.text)
        file.close()


filewrite = WriteInFile()
filewrite.get_file_content()


