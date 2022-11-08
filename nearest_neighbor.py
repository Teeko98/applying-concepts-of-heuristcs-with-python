import datetime
from post_office_class import PostOffice


# O(n)^2
def get_nearest_neighbor():
    PostOffice.reset_post_office()
    # Simulates each trucks delivery. Truck[0] leaves at 8:00 am, Truck[1] leaves when Truck[0] completes it's route,
    # and Truck[2] leaves at 10:20 am to ensure package #9 is delivered at the appropriate time
    for x in range(0, len(PostOffice.truck_fleet)):
        if x == 0:
            temp_time = datetime.time(8, 0)
        elif x == 1 and (PostOffice.truck_fleet[0].finished_time != datetime.time(23, 59)):
            temp_time = PostOffice.truck_fleet[0].finished_time
        elif x == 2 and PostOffice.current_time >= datetime.time(10, 20):
            temp_time = datetime.time(10, 20)
        else:
            break
        if PostOffice.current_time > temp_time:
            PostOffice.truck_fleet[x].left_hub = True
        current_address = 'HUB'
        next_address = ''
        packages_delivered = 0
        # Simulates the current trucks route running from 8:00 am until the given time
        while PostOffice.current_time > temp_time:
            min_dist = 500
            package_location = None
            package_deadline = datetime.time(23, 59)
            # Tests each package in the truck's inventory to find which one has the nearest delivery address
            for i in range(0, len(PostOffice.truck_fleet[x].inventory)):
                test_address = f'{PostOffice.truck_fleet[x].inventory[i][1].address} '\
                               f'({PostOffice.truck_fleet[x].inventory[i][1].zip_code})'
                if PostOffice.truck_fleet[x].inventory[i][1].is_delivered:
                    continue
                temp_dist = float(PostOffice.address_distance_map.distance_between(
                    current_address, test_address))
                # Checks if the package is delayed and if it can be delivered yet
                if "Delayed on flight" in PostOffice.truck_fleet[x].inventory[i][1].notes:
                    if temp_time < datetime.time(9, 5):
                        continue
                # Prioritizes any packages with deadlines and finds their next closest delivery location
                if PostOffice.truck_fleet[x].inventory[i][1].deadline < package_deadline:
                    if temp_dist < min_dist:
                        min_dist = temp_dist
                        next_address = test_address
                        package_location = i
                        continue
                # Finds the next closest delivery location
                if temp_dist < min_dist:
                    min_dist = temp_dist
                    next_address = test_address
                    package_location = i
            if packages_delivered == len(PostOffice.truck_fleet[x].inventory):
                PostOffice.truck_fleet[x].finished_time = temp_time
                break
            # Calculate elapsed time (truck drives at 18mph)
            elapsed_time = (min_dist / 18) * 60
            time_delta = datetime.timedelta(minutes=elapsed_time)
            temp_time = increase_time(temp_time, time_delta)
            if temp_time > PostOffice.current_time:
                break
            PostOffice.truck_fleet[x].delivered(package_location, temp_time)
            PostOffice.total_elapsed_mileage += min_dist
            PostOffice.truck_fleet[x].inventory[package_location][1].is_delivered = True
            packages_delivered += 1
            current_address = next_address
            next_address = ''


def increase_time(time, time_delta):
    start = datetime.datetime(2022, 2, 22, hour=time.hour, minute=time.minute, second=time.second)
    end = start + time_delta
    return end.time()