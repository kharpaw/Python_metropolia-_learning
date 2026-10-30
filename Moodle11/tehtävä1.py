class Publication:
    def __init__(self, name):
        self.name = name
        

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f"Publication name is : {self.name}")
        print(f"The author name is: {self.author}") 
        print(f"Total page counts are: {self.page_count}")
    
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
        
        
    def print_information(self):
        print(f"Publication name is: {self.name}")
        print(f"The editor is {self.chief_editor}")
        
        

book = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyyppä")

book.print_information()
magazine.print_information()


        
    
