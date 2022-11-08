# Package Class
import datetime

import post_office_class


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass, notes):
        self.package_id = package_id
        self.address = address.replace('South', 'S').replace('East', 'E').replace('North', 'N').replace('West', 'W')
        self.city = city
        self.state = state
        self.zip_code = zip_code
        if deadline == 'EOD':
            self.deadline = datetime.time(23, 59, 59)
        else:
            if 'pm' in deadline.lower() and int(deadline.split(':')[0]) != 12:
                self.deadline = datetime.time((int(deadline.split(':')[0]) + 12), (int(deadline.split(':')[1].split(' ')[0])))
            elif 'am' in deadline.lower() and int(deadline.split(':')[0]) == 12:
                self.deadline = datetime.time(0, (int(deadline.split(':')[1].split(' ')[0])))
            else:
                self.deadline = datetime.time(int(deadline.split(':')[0]), (int(deadline.split(':')[1].split(' ')[0])))
        self.mass = mass
        self.notes = notes
        self.is_in_truck = False
        self.truck_number = 0
        self.is_delivered = False
        self.time_delivered = datetime.time(0, 0)

    def __lt__(self, other):
        return self.package_id < other.package_id

    @staticmethod
    def print_package_header():
        header = f"{'ID':^4}|{'Address':^70}|{'Deadline':^10}|{'Wt':^4}|{'Status':^30}"
        print(header)
        for _ in range(len(header)):
            print('*', end='')
        print()

    def print_package_data(self):
        full_address = self.address + ", " + self.city + ", " + self.state + " " + self.zip_code
        if self.is_delivered:
            package_status = f"Delivered at {self.time_delivered}!"
        elif post_office_class.PostOffice.truck_fleet[self.truck_number].left_hub:
            package_status = f"Out for delivery on truck #{self.truck_number}"
        else:
            package_status = "Package at hub"
        print(f"{self.package_id:^4}|{' ' + full_address:<70}| {self.deadline} |{self.mass:^4}|{' ' + package_status:<30}")

    def get_address_data(self):
        return f'{self.address} ({self.zip_code})'
