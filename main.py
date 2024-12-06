from src.phonebook import Phonebook

phonebook = Phonebook()
phonebook.add("Dreno","1")
phonebook.add("Creno","2")
phonebook.add("Breno","3")
r = phonebook.get_name_by_number("4")
print(r)
print(phonebook.get_numbers())


