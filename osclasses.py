class StoreItem:
    def __init__(self, rating, name, author):
        self.rating = rating
        self.name = name
        self.author = author

    def default_description(self): # In case user does not input description.
            print("This app is called " + self.name + " with a rating of " + self.rating + ", created by " + self.author + ".")

class TextDoc:
    def __init__(self, name, text):
        self.name = name
        self.text = text

class Person:

    addr_book_priority = None

    def __init__(self, first_name, middle_initial, last_name, full_name, phone_num, email):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.full_name = first_name + middle_initial + last_name
        self.phone_num = phone_num
        self.email = email

    def contact_introduce(self):
        print("Name: " + self.full_name + "\n"
              "Phone Number: " + self.phone_num + "\n"
              "Email: " + self.email)
        # Usage
        # person1 = Person("John ", "A.", " Smith", "", "911", "johnsmith@email.com")
        # person1.contact_introduce()

#a = StoreItem(str(5.0), "Test", "John Smith")



