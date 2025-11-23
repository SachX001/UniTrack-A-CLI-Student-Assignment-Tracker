# used GFG, StackOverflow for writing the following code
# Here, i'm trying to save the data in a txt file named vit_projects to access all the data at once
def save_data(all_tasks):
    # here 'w' mode overwrites the file every time so that we can save the latest list
    with open("vit_projects.txt", "w") as f:
        for item in all_tasks:
            # making a string line: "description|Date"
            # uing "|" makes it easier to read
            line = item['desc'] + "|" + item['date'] + "\n"
            f.write(line)

def load_data():
# Defining a function load_data to read the data back
# The following code was written by taking help from GFG and Stack Overflow threads

    projects = []
# Using a try and except block just in case vit_projects doesnt exists yet

    try:
        # Here, 'r' mode is for reading the data
        with open("vit_projects.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                # removes the hidden newline characters
                clean_line = line.strip()
                
                # if the line is empty, we can skip it for a safe check
                if not clean_line:
                    continue

                # Split the text back into two parts using the same "|"
                parts = clean_line.split("|")

                # We can now rebuild the dictionary using the split parts
                # We can assume part[0] is des and part[1] is date as the data is split 
                task_obj = {'desc': parts[0], 'date': parts[1]}

                # Appending new data in the dictionary as the loop proceeds
                projects.append(task_obj)

    except FileNotFoundError:
      # If the file isn't there, we can return an empty list 
      return []

    return projects
