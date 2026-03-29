import csv
import random

names = [
    "James", "Mary", "Robert", "Patricia", "Michael", "Jennifer", "William", "Linda",
    "David", "Barbara", "Richard", "Elizabeth", "Joseph", "Susan", "Thomas", "Jessica",
    "Charles", "Sarah", "Christopher", "Karen", "Daniel", "Nancy", "Matthew", "Lisa",
    "Anthony", "Betty", "Mark", "Margaret", "Donald", "Sandra", "Steven", "Ashley",
    "Paul", "Dorothy", "Andrew", "Kimberly", "Joshua", "Emily", "Kenneth", "Donna",
    "Kevin", "Carol", "Brian", "Michelle", "George", "Amanda", "Edward", "Melissa",
    "Ronald", "Deborah", "Timothy", "Stephanie", "Jason", "Rebecca", "Jeffrey", "Sharon"
]

surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Young"
]

cities = [
    "New York", "Los Angeles", "Chicago", "Houston"
]

genders = ["Male", "Female"]
passed = ["Yes", "No"]

records = []
for i in range(200):
    name = f"{random.choice(names)} {random.choice(surnames)}"
    gender = random.choice(genders)
    city = random.choice(cities)
    result = random.choice(passed)
    records.append([name, gender, city, result])

with open('sample_data.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(records)