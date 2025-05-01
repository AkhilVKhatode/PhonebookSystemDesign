from collections import defaultdict
class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.phone = set()

    def addNumber(self, number) -> None:
        self.phone.add(number)

    def delNumber(self, number) -> None:
        self.phone.remove(number)
    
    def __str__(self):
        return f'Name: {self.name}, Phone numbers: {", ".join(map(str, self.phone))}'

class Phonebook:
    def __init__(self) -> None:
        self.namelist = defaultdict(Person)
        self.phonelist = defaultdict(Person)
    
    def addName(self, personName, personPhoneNumber):
        if personName in self.namelist:
            person_obj = self.namelist[personName]
        else:
            person_obj = Person(personName)
        person_obj.addNumber(personPhoneNumber)
        self.namelist[personName] = person_obj
        self.phonelist[personPhoneNumber] = person_obj
    
    def remove(self, delete):
        if isinstance(delete, int):
            if delete in self.phonelist:
                nameToDelete = self.phonelist[delete].name
                del self.phonelist[delete]
                self.namelist[nameToDelete].delNumber(delete)
                if not self.namelist[nameToDelete].phone:
                    del self.namelist[nameToDelete]
        else:
            if delete in self.namelist:
                noToDelete = self.namelist[delete].phone
                del self.namelist[delete]
                for i in noToDelete:
                    del self.phonelist[i]
        
    def search(self, search):
        if isinstance(search, int):
            if search in self.phonelist:
                nameToSearch = self.phonelist[search].name
        else:
            nameToSearch = search
        print('Search result:')
        print(self.namelist[nameToSearch])
        print()
    
    def printlist(self):
        namesArr = list(self.namelist.keys())
        namesArr.sort()
        print('Printing list:')
        for name in namesArr:
            print(self.namelist[name])
        print()

def main():
    phone_book = Phonebook()
    phone_book.addName('Aaaaaa', 100000000)
    phone_book.addName('Aaaaaa', 300000000)
    phone_book.addName('Bbbbbb', 200000000)
    phone_book.addName('Cccccc', 400000000)
    phone_book.printlist()

    phone_book.search('Aaaaaa')
    phone_book.search(300000000)

    phone_book.remove(200000000)
    phone_book.remove('Cccccc')
    
    phone_book.printlist()

main()
