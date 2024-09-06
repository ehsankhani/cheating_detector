def custom_compare(person1, person2):
    if person1['age'] < person2['age']:
        return -1
    elif person1['age'] > person2['age']:
        return 1
    else:
        return 0

def sort_people_with_custom_compare(people):
    sorted_people = sorted(people, key=lambda person: person['age'], cmp=custom_compare)
    return sorted_people

def print_sorted_people(people):
    print("Sorted list of people by age using custom comparison:")
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
    sorted_people = sort_people_with_custom_compare(people)
    print_sorted_people(sorted_people)

if __name__ == "__main__":
    main()
