import datetime

import post_office_class


class Truck:
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.is_full = False
        self.inventory = []
        self.finished_time = datetime.time(23, 59)
        self.left_hub = False

    # Loads given package into truck if truck is not full.
    def load(self, package):
        if not self.is_full:  # Check if truck is already full
            if not package[1].is_in_truck:  # Check if package is not already in a truck
                self.inventory.append(package)
                package[1].is_in_truck = True
                package[1].truck_number = self.truck_number
                if len(self.inventory) >= 16:
                    self.is_full = True
            else:
                print(f'Error loading package #{package[1].package_id}! Package is on a different truck')
                return
        else:
            print(f"Error loading package #{package[1].package_id}! Truck is full.")
            return

    def delivered(self, package_location, time):
        post_office_class.PostOffice.packages_delivered += 1
        self.inventory[package_location][1].is_delivered = True
        self.inventory[package_location][1].time_delivered = time
