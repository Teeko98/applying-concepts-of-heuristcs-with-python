import csv
import package_class


# Hash table class for the package data
# The structure of this hash table is as follows:
# PackageHashTable.table is an array of buckets ie: [[bucket], [bucket], [bucket], ...]
# Each bucket is an array containing key value pairs
# These key value pairs are stored in an array of the format [key, package]
# ie: PackageHashTable.table[1] might contain [[1, package], [11, package], [21, package], ...]
# ie: PackageHashTable.table[1][2] would then return [21, package]
# ie: PackageHashTable.table[1][2][0] would return the key
# ie: PackageHashTable.table[1][2][1] would return the package
class PackageHashTable:
    # Constructor with optional initial capacity parameter to determine the amount of buckets
    # Initializes all buckets with an empty list
    def __init__(self, initial_capacity=10):
        # Creates initial_capacity amount of buckets
        self.total_packages = 0
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
        # Reads in and creates package objects using data from package_file.csv
        # Each package has an ID number which is used as its unique key
        with open("package_file.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                # Checks if data exists on each line (avoids reading in an empty line)
                if isinstance(line[0], str):
                    self.insert(int(line[0]), package_class.Package(int(line[0]), line[1], line[2], line[3],
                                                                    line[4], line[5], int(line[6]), line[7]))

    # Inserts package object and its unique key into the hash table
    def insert(self, package_id, package):
        # Selects the bucket where the package_id belongs.
        bucket = package_id % len(self.table)
        # Checks if the package_id key already exists in the selected bucket
        # Updates existing package if it already exists
        for key in self.table[bucket]:
            if key[0] == package_id:
                key[1] = package
                return True
        # If the package_id key does not exist in the selected bucket,
        # the package_id key is inserted at the end of bucket
        self.table[bucket].append([package_id, package])
        self.total_packages += 1
        return True

    # Searches for a package with the matching package_id key in the hash table.
    # Returns the package object if it is found; otherwise, None is returned.
    def search(self, package_id):
        # Selects the bucket where package_id would be
        bucket = package_id % len(self.table)
        # Searches for the package_id key in the selected bucket
        for i in range(len(self.table[bucket])):
            if package_id == self.table[bucket][i][0]:
                # The package_id key was found and the key value pair is returned
                return self.table[bucket][i]
        # The package_id key was not found
        return None

    # Removes the item from the hashtable with the matching package_id if it exists
    def remove(self, package_id):
        # Selects the bucket where package_id would be
        bucket = package_id % len(self.table)
        # Removes the item from the selected bucket list if it is present.
        for i in range(len(self.table[bucket])):
            if package_id == self.table[bucket][i][0]:
                del self.table[bucket][i]
                self.total_packages -= 1
                return True
        # Returns false if package doesn't exist.
        return False

    # Prints all package data in the hashtable
    def print_all_package_data(self):
        array_of_table = []
        for i in range(len(self.table)):
            for n in range(len(self.table[i])):
                array_of_table.append(self.table[i][n][1])
        sorted_array_of_table = sorted(array_of_table, key=lambda x: x.package_id)
        package_class.Package.print_package_header()
        for i in range(len(array_of_table)):
            sorted_array_of_table[i].print_package_data()
        print()

    # Prints the package data of the corresponding package_id if it exists
    def print_specific_package(self, package_id):
        package_class.Package.print_package_header()
        self.search(package_id)[1].print_package_data()
        print()
