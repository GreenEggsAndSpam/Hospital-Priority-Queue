'''
Author: Vrishank Kulkarni
KUID: 3115417
Date: 04/14/24
Lab: lab 08
Last modified: 2/25/24
Purpose: this program will create a cue for a hospital and when given a file it will output the number of patients and
the patients that need to be treated
'''

from heap import MaxHeap
from patient import Patient

class Hospital:
    def __init__(self):
        self.queue = MaxHeap()
        self.arrival_order = 0

    def arrive(self, first_name, last_name, age, illness, severity):
        self.arrival_order += 1
        patient = Patient(first_name, last_name, age, illness, severity, self.arrival_order)
        self.queue.push(patient)

    def next_patient(self):
        return self.queue.pop()

    def treat_patient(self):
        return self.queue.pop()

    def count_patients(self):
        return len(self.queue.heap)
