# Applying Concepts of Heuristcs with Python

This program showcases a practical application of heuristic concepts, self adjusting data structures, and sorting algorithms by solving a callous twist on the infamous [traveling salesman problem.](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
 
## The Scenario
A fictous delivery service needs to determine an efficient route and delivery distribution for their daily local deliveries. The company has three trucks, two drivers, and 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

The goal is to present a solution where all 40 packages are delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles.

Additionally, the program must display the status of each truck and its packages, including what has been delivered and at what time the delivery occurred at any requested interval.

## Supplied Data
### You are supplied with two spreedsheets containing valuable data.
* **Spreadsheet 1** (package_file.csv) contains a list of packages with their respective delivery addresses and weight.
  - A handful of these packages have delivery time constraints, unexpected delays, incorrect information, delivery truck restrictions, and/or are required to be delivered with other packages.
* **Spreadsheet 2** (distance_table_file.csv) contains an incomplete table of the delivery addresses and the distance between them.

## Constaints
* You have 3 delivery trucks at your disposal, but only two drivers.
* Each truck is limited in its carrying capacity.
* Trucks move at an average speed of 18mph.
* All packages must be delivered by 5pm.

## Solution Notes
* My solution utilitzes the nearest neighbor algorithm and has a time and space complexity of O(n^2).
* The given data set is delivered at 12:16pm with a sum of 99.9 miles traveled.
* The program processes external data rather than relying on fixed variables making it scalable with various data sets. 
* The utilization of hash tables to store and process data greatly reduces runtime.
  
## Features/Showcases
* A text-based UI that provides the user the option of computing the optimal route algorithm, searching the data set, and checking the delivery status of all packages and trucks at any given time.
* A sorting algorithm to determine which packages are to be delivered by which truck.
* A *greedy* algorithm to determine the optimal delivery route for each truck.
* Data manipulation of external files with Python.
* Implementation of a self-adjusting hash table.



