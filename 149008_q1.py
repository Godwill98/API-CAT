# Patient management system

# Function to add a new patient
def add_patient(patients):
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    illness = input("Enter patient's illness: ")
    patient = {'name': name, 'age': age, 'illness': illness}
    patients.append(patient)
    print(f"Patient {name} added successfully.")

# Function to display all patients
def display_patients(patients):
    if not patients:
        print("No patients in the system.")
    else:
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

# Function to search for a patient by name
def search_patient(patients):
    name = input("Enter the name of the patient to search for: ")
    found = False
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            found = True
            break
    if not found:
        print(f"No patient found with the name {name}.")

# Function to remove a patient by name
def remove_patient(patients):
    name = input("Enter the name of the patient to remove: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.")
            return
    print(f"No patient found with the name {name}.")

# Main function to run the program
def main():
    patients = []
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            remove_patient(patients)
        elif choice == '5':
            print("Exiting the program. Goodbye,Adios!!!!")
            break
        else:
            print("Too bad Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
