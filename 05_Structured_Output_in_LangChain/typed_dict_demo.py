from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str


new_person: Person = {
    "name": "Alice",
    "age": 30,
    "email": 'alice@me.com'
}
print(new_person)

# ask the user for their information
name = input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid integer for age.")
email = input("Enter your email: ")

# email = input("Enter your email: ")

user_person: Person = {
    "name": name,
    "age": age,
    "email": email
}
print(user_person)