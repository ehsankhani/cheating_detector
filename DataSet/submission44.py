def arrange_by_age(people_group):
    result = sorted(people_group, key=lambda individual: individual['age'])
    return result

def output_people(people_group):
    print("Outputting the sorted list of individuals by age:")
    for individual in people_group:
        print(f"Person: {individual['name']}, Age: {individual['age']}")

def main():
    group_of_people = [
        {'name': 'Alice', 'age': 34},
        {'name': 'Bob', 'age': 23},
        {'name': 'Charlie', 'age': 29},
        {'name': 'Diana', 'age': 40},
        {'name': 'Eve', 'age': 22}
    ]
    sorted_group = arrange_by_age(group_of_people)
    output_people(sorted_group)

if __name__ == "__main__":
    main()
