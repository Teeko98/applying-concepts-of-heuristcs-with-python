import csv


# address_array index positions map to distance_table
# ie: distance between address_array[0] and address_array[5] is located at both dist_array[0][5] or dist_array[5][0]
class AddressDistanceMap:
    def __init__(self):
        self.address_array = []
        self.distance_table = []
        # Fill address_array with address data from the given file
        with open("distance_table_file.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                if isinstance(line[0], str):
                    self.address_array.append(str.strip(line[1].replace("\n", " ")
                                                        .replace("South", "S")
                                                        .replace("East", "E")
                                                        .replace("North", "N")
                                                        .replace("West", "W")))
        # Fill dist_array with distance map from the given file
        with open("distance_table_file.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            x = 0
            for line in csv_reader:
                self.distance_table.append([])
                for i in range(0, x + 1):
                    if isinstance(line[i + 2], str):
                        self.distance_table[x].append(line[i + 2])
                x += 1
        # Fill in the mirrored distance data
        for i in range(len(self.distance_table)):
            for n in range(i):
                self.distance_table[n].append(self.distance_table[i][n])

    def address_search(self, address):
        for i in range(0, len(self.address_array)):
            if address == self.address_array[i]:
                return i
        for i in range(0, len(self.address_array)):
            if address in self.address_array[i]:
                if input(f"\nDid you mean: {self.address_array[i]}? (Enter Y/N): ").upper() == "Y":
                    return i
        return False

    def distance_between(self, x, y):
        if x.isdigit() and y.isdigit():
            return self.distance_table[x][y]
        else:
            x_array_pos = self.address_search(x)
            y_array_pos = self.address_search(y)
            return self.distance_table[x_array_pos][y_array_pos]
