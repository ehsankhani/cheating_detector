def sort_by_age(people):
    sorted_people = sorted(people, key=lambda person: person['age'])
    return sorted_people

def print_people(people):
    print("People sorted by age:")
    for person in people:
        print(f"Name: {person['name']}, Age: {person['age']}")

def main():
    people = [
        {'name': 'Alice', 'age': 34},
        {'name': 'Bob', 'age': 23},
        {'name': 'Charlie', 'age': 29},
        {'name': 'Diana', 'age': 40},
        {'name': 'Eve', 'age': 22}
    ]
    sorted_people = sort_by_age(people)
    print_people(sorted_people)

if __name__ == "__main__":
    main()
