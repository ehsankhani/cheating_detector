def sort_by_person_age(people_list):
    sorted_list = sorted(people_list, key=lambda p: p['age'])
    return sorted_list

def show_people(people_list):
    print("People list sorted by their age values:")
    for person in people_list:
        print(f"Name: {person['name']}, Age: {person['age']}")

def main():
    persons = [
        {'name': 'Alice', 'age': 34},
        {'name': 'Bob', 'age': 23},
        {'name': 'Charlie', 'age': 29},
        {'name': 'Diana', 'age': 40},
        {'name': 'Eve', 'age': 22}
    ]
    sorted_persons = sort_by_person_age(persons)
    show_people(sorted_persons)

if __name__ == "__main__":
    main()
