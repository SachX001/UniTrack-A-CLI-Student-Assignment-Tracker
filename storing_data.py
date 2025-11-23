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
