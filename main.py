# The following code was written citing from GFG, Stack Overflow and existing Github repos
# Here, in main.py, im trying to import everything together and integrate the whole project together
# To run the project one just has to run the main.py now
import Dictionaries
import storing_data

def main_menu():
    print("--- UniTrack: Project Manager  ---")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Save and Exit")

def main():
    # load existing data first
    projects = storing_data.load_data()
    print(f"Loaded {len(projects)} existing projects")

    while True:
        main_menu()
        user_choice = input("Choose an Option(1-3): ")

        if user_choice == "1":
            desc = input("Enter project descriptio: ")
            due = input("Enter due date(DD/MM): ")

            new_entry = Dictionaries.create_dictionary(desc, due)

            projects.append(new_entry)
            print("Project added Successfully!")

        elif user_choice == "2":
            print("Current Assignments")
            
            for proj in projects:
                readable = Dictionaries.get_readable_dictionary(proj)
                print(readable)

        elif user_choice == "3":
            storing_data.save_data(projects)
            print("Data Saved!, Exiting now ... ")
            break

        else:
            print("Invalid selection, Please try again")

if __name__ == "__main__":
    main()
