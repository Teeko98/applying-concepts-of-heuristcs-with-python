# Alberto Sosa #000842667


from post_office_class import PostOffice
import user_interface as ui
from nearest_neighbor import get_nearest_neighbor


def main_menu():
    # Displays the main menu screen
    ui.print_menu_screen()
    # Receives user input
    temp_input = input('Choose An Option to Proceed: ')
    ui.wipe_screen()
    # Checks if input is a valid integer between 0 and 4
    if not temp_input.isdigit() or (int(temp_input) > 3 or int(temp_input) < 0):
        print('\nInvalid Input!\n')
        ui.navigation_prompt()
        return True
    # Option 0: Quit
    if int(temp_input) == 0:
        ui.quit_message()
        return False
    # Option 1: Update Time
    elif int(temp_input) == 1:
        update_time()
        return True
    # Option 2: Package status
    elif int(temp_input) == 2:
        get_nearest_neighbor()
        check_all_package_status()
        return True
    # Option 3: Individual Package Lookup
    elif int(temp_input) == 3:
        get_nearest_neighbor()
        check_specific_status()
        return True


# Receives user input to update the current_time class variable of the PostOffice class
def update_time():
    new_time = str(ui.update_time())
    if new_time.isdigit() and int(new_time) == 0:
        ui.wipe_screen()
        return
    while True:
        try:
            if (not (':' in new_time.lower())) or (not ('am' in new_time.lower() or 'pm' in new_time.lower())) or \
                    (not (new_time.split(':')[0].isdigit() or new_time.split(':')[1].split(' ')[0].isdigit())) or \
                    (int(new_time.split(':')[0]) < 1 or int(new_time.split(':')[0]) > 12) or \
                    (int(new_time.split(':')[1].split(' ')[0]) < 0 or int(new_time.split(':')[1].split(' ')[0]) > 59):
                new_time = input("Please enter a valid time in the following format: 00:00 AM/PM: ")
                continue
        except (IndexError, ValueError):
            new_time = input("Please enter a valid time in the following format: 00:00 AM/PM: ")
            continue
        break
    PostOffice.update_time(new_time)
    print(f'The current time is now: {PostOffice.current_time}\n')
    ui.navigation_prompt()
    ui.wipe_screen()


# Prompts the user to enter a time and returns the status of all packages at the given time
def check_all_package_status():
    ui.check_all_packages_status()
    PostOffice.package_hashtable.print_all_package_data()
    PostOffice.print_delivery_status()
    ui.navigation_prompt()
    return


# Searches a given package ID and returns that package's info if it exists
def check_specific_status():
    package_id = ui.check_specific_status()
    while True:
        if int(package_id) == 0:
            ui.wipe_screen()
            return
        if not package_id.isdigit():
            package_id = input("Please enter a valid package ID or 0 to exit: ")
            continue
        break
    # Checks if package exists
    if PostOffice.package_hashtable.search(int(package_id)) is not None:
        PostOffice.package_hashtable.print_specific_package(int(package_id))
    else:
        print('\nPackage Does Not Exists!\n')
    ui.navigation_prompt()
    return


# Starts the program and keeps it running until the user quits
while True:
    if not main_menu():
        break
