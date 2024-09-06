from operator import itemgetter

def sort_people(people):
    sorted_people = sorted(people, key=itemgetter('age'))
    return sorted_people

def display_people(people):
    print("Sorted list of people by their ages:")
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
    sorted_people = sort_people(people)
    display_people(sorted_people)

if __name__ == "__main__":
    main()
