# Phonebook Directory System

This repository contains a Python implementation of a simple Phonebook Directory system using object-oriented principles. The system supports managing contact details with functionality to add, remove, search, and display contact information. The Phonebook system uses two dictionaries to store data: one based on names and the other on phone numbers.

## Features

- **Add Contact**: You can add contacts by name and phone number.
- **Remove Contact**: You can remove contacts either by phone number or by name.
- **Search Contact**: Allows searching for a contact either by name or phone number.
- **Display All Contacts**: Prints all the contacts in the phonebook, sorted by name.

## Classes

### `Person`
Represents an individual contact in the phonebook.

- **Attributes**:
  - `name`: Name of the person.
  - `phone`: A set of phone numbers associated with the person.

- **Methods**:
  - `addNumber(number)`: Adds a phone number to the contact.
  - `delNumber(number)`: Removes a phone number from the contact.
  - `__str__()`: Returns a string representation of the contact.

### `Phonebook`
Represents the entire phonebook, which stores contacts.

- **Attributes**:
  - `namelist`: A dictionary mapping names to `Person` objects.
  - `phonelist`: A dictionary mapping phone numbers to `Person` objects.

- **Methods**:
  - `addName(personName, personPhoneNumber)`: Adds a new contact or updates an existing one.
  - `remove(delete)`: Removes a contact by name or phone number.
  - `search(search)`: Searches for a contact by name or phone number.
  - `printlist()`: Prints all contacts, sorted by name.

## Example Usage

```python
def main():
    phone_book = Phonebook()

    # Adding contacts
    phone_book.addName('Aaaaaa', 100000000)
    phone_book.addName('Aaaaaa', 300000000)
    phone_book.addName('Bbbbbb', 200000000)
    phone_book.addName('Cccccc', 400000000)

    # Displaying all contacts
    phone_book.printlist()

    # Searching contacts
    phone_book.search('Aaaaaa')  # Search by name
    phone_book.search(300000000)  # Search by phone number

    # Removing contacts
    phone_book.remove(200000000)  # Remove by phone number
    phone_book.remove('Cccccc')  # Remove by name

    # Displaying all contacts after removal
    phone_book.printlist()

main()
```
Sample Output
```yaml
Printing list:
Name: Aaaaaa, Phone numbers: 100000000, 300000000
Name: Bbbbbb, Phone numbers: 200000000
Name: Cccccc, Phone numbers: 400000000

Search result:
Name: Aaaaaa, Phone numbers: 100000000, 300000000

Search result:
Name: Aaaaaa, Phone numbers: 100000000, 300000000

Printing list:
Name: Aaaaaa, Phone numbers: 100000000, 300000000
Name: Bbbbbb, Phone numbers: 200000000
Name: Cccccc, Phone numbers: 400000000

Printing list:
Name: Aaaaaa, Phone numbers: 100000000, 300000000
Name: Bbbbbb, Phone numbers: 200000000
```
