# The following code was written with the help of GFG, Stack Overflow and existing GITHUB repos

# This is a Module for handling the task for creation and formatting of dictionary
def create_dictionary(desc_text, date_text):
    # This function builds the dictionary so we dont have to type curly braces everywhere
    # Using the same keys 'desc' and 'date' to match our storage system
    new_task = {
        'desc': desc_text,
        'date': date_text
    }
    return new_task

def get_readable_dictionary(task_obj):
    # This funcion takes the dictionary and makes it look nice for the user 
    # formatting it like" "[Description] - Due by: [Date]"
    
    display_string = f"{task_obj['desc']} - Due by: {task_obj['date']}"
    return display_string
