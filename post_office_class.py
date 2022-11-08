import address_distance_map
from package_hashtable import PackageHashTable
import truck_class
import datetime


class PostOffice:
    address_distance_map = address_distance_map.AddressDistanceMap()
    package_hashtable = PackageHashTable()
    truck_fleet = []
    current_time = datetime.time(8, 0)
    total_elapsed_mileage = 0.0
    packages_delivered = 0
    trucks_loaded = False

    @classmethod
    def reset_post_office(cls):
        cls.packages_delivered = 0
        cls.total_elapsed_mileage = 0.0
        if not cls.trucks_loaded:
            cls.create_truck()
            cls.load_trucks()
            cls.trucks_loaded = True
        for i in range(0, len(cls.truck_fleet)):
            cls.truck_fleet[i].finished_time = datetime.time(23, 59)
            cls.truck_fleet[i].left_hub = False
            for j in range(0, len(cls.truck_fleet[i].inventory)):
                cls.truck_fleet[i].inventory[j][1].is_delivered = False
                cls.truck_fleet[i].inventory[j][1].time_delivered = datetime.time(23, 59)
                cls.truck_fleet[i].inventory[j][1].is_in_truck = True

    @classmethod
    def create_truck(cls, num_of_trucks=3):
        for i in range(num_of_trucks):
            truck = truck_class.Truck(i)
            cls.truck_fleet.append(truck)

    @classmethod
    def load_trucks(cls):
        # Ensures packages 13, 14, 15, 16, 19, and 20 are on the same truck, as per requirements;
        # 1, 6, 7, 20, 29, 30, 31, 34, 37, 40 have deadlines before 10:30
        for i in [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 6, 7]:
            cls.truck_fleet[0].load(cls.package_hashtable.search(i))
        # Ensure packages 3, 18, 36, and 38 are delivered by truck 2, as per the requirements
        for i in [3, 18, 36, 38]:
            cls.truck_fleet[1].load(cls.package_hashtable.search(i))
        # These package cannot depart before 10:20 am so truck 3 will depart at a later time
        for i in [9, 25, 28, 32]:
            cls.truck_fleet[2].load(cls.package_hashtable.search(i))
        # Divide packages that have a delivery deadline between the first two trucks
        for i in range(1, cls.package_hashtable.total_packages + 1):
            if not cls.package_hashtable.search(i)[1].is_in_truck:
                if cls.package_hashtable.search(i)[1].deadline <= datetime.time(10, 30):
                    if len(cls.truck_fleet[0].inventory) > len(cls.truck_fleet[1].inventory) and not cls.truck_fleet[1].is_full:
                        cls.truck_fleet[1].load(cls.package_hashtable.search(i))
                        cls.package_hashtable.search(i)
                    else:
                        cls.truck_fleet[0].load(cls.package_hashtable.search(i))
        # Divides remaining packages onto all trucks
        for i in range(1, cls.package_hashtable.total_packages + 1):
            if not cls.package_hashtable.search(i)[1].is_in_truck:
                if len(cls.truck_fleet[0].inventory) > len(cls.truck_fleet[1].inventory) > len(
                        cls.truck_fleet[2].inventory) and not cls.truck_fleet[2].is_full:
                    cls.truck_fleet[2].load(cls.package_hashtable.search(i))
                elif len(cls.truck_fleet[0].inventory) > len(cls.truck_fleet[1].inventory) and not cls.truck_fleet[1].is_full:
                    cls.truck_fleet[1].load(cls.package_hashtable.search(i))
                else:
                    cls.truck_fleet[0].load(cls.package_hashtable.search(i))

    @classmethod
    def update_time(cls, new_time):
        if 'pm' in new_time.lower() and int(new_time.split(':')[0]) != 12:
            cls.current_time = datetime.time((int(new_time.split(':')[0]) + 12),
                                                    (int(new_time.split(':')[1].split(' ')[0])))
        elif 'am' in new_time.lower() and int(new_time.split(':')[0]) == 12:
            cls.current_time = datetime.time(0, (int(new_time.split(':')[1].split(' ')[0])))
        else:
            cls.current_time = datetime.time(int(new_time.split(':')[0]),
                                                    (int(new_time.split(':')[1].split(' ')[0])))

    @classmethod
    def print_delivery_status(cls):
        print("Current Time: ", cls.current_time)
        print("Total mileage = ", cls.total_elapsed_mileage)
        at_hub = 0
        en_route = 0
        for i in range(0, len(cls.truck_fleet)):
            if not cls.truck_fleet[i].left_hub:
                at_hub += len(cls.truck_fleet[i].inventory)
            else:
                for j in range(len(cls.truck_fleet[i].inventory)):
                    if not cls.truck_fleet[i].inventory[j][1].is_delivered:
                        en_route += 1
        print("Packages at hub: ", at_hub)
        print("Packages en route: ", en_route)
        print("Packages delivered: ",  cls.packages_delivered)
