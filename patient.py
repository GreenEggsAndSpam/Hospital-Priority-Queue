'''
Author: Vrishank Kulkarni
KUID: 3115417
Date: 04/14/24
Lab: lab 08
Last modified: 2/25/24
Purpose: this program will create a cue for a hospital and when given a file it will output the number of patients and
the patients that need to be treated
'''

class Patient:
    def __init__(self, first_name, last_name, age, illness, severity, arrival_order):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity
        self.arrival_order = arrival_order

    def __lt__(self, other):
        if self.severity == other.severity:
            if self.age == other.age:
                return self.arrival_order < other.arrival_order
            return self.age > other.age
        return self.severity > other.severity