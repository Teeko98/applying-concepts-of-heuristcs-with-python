# Prints the main menu screen
def print_menu_screen():
    print('************************************************************\n'
          '*                                                          *\n'
          '*                  WGUPS Distribution Hub                  *\n'
          '*                                                          *\n'
          '************************************************************\n'
          '*                                                          *\n'
          '*       1)  Update Time                                    *\n'
          '*                                                          *\n'
          '*       2)  Check Status of All Packages                   *\n'
          '*                                                          *\n'
          '*       3)  Check Specific Package Status                  *\n'
          '*                                                          *\n'
          '*                                                          *\n'
          '*                                                          *\n'
          '*       0)  QUIT                                           *\n'
          '*                                                          *\n'
          '************************************************************')
    return


def update_time():
    print('************************************************************\n'
          '*                                                          *\n'
          '*                        Update Time                       *\n'
          '*                                                          *\n'
          '************************************************************\n')
    return input('Enter a time between 8:00 AM and 11:59 PM (Enter 0 to Return to Main Menu: ')


def check_all_packages_status():
    print('************************************************************\n'
          '*                                                          *\n'
          '*                    All Packages Status                   *\n'
          '*                                                          *\n'
          '************************************************************\n')


def check_specific_status():
    print('************************************************************\n'
          '*                                                          *\n'
          '*                     Package Search                       *\n'
          '*                                                          *\n'
          '************************************************************\n')
    return input("Enter the Package ID to Check its Status (Enter 0 to Return to Menu): ")


# Waits for user input before continuing
def navigation_prompt():
    print('************************************************************\n'
          '*                                                          *\n'
          '*               Press Enter Key To Continue                *\n'
          '*                                                          *\n'
          '************************************************************')
    input()
    wipe_screen()
    return


# Clears the screen
def wipe_screen():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    return


# prints quit message
def quit_message():
    print('************************************************************\n'
          '*                                                          *\n'
          '*                    THANK YOU, GOODBYE!                   *\n'
          '*                                                          *\n'
          '************************************************************')
    return
