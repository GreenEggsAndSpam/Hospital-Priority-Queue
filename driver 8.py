'''
Author: Vrishank Kulkarni
KUID: 3115417
Date: 04/14/24
Lab: lab 08
Last modified: 2/25/24
Purpose: this program will create a cue for a hospital and when given a file it will output the number of patients and
the patients that need to be treated
'''

from hospital import Hospital

def process_commands_from_file(file_name):
    hospital = Hospital()
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if parts[0] == 'ARRIVE':
                first_name, last_name, age, illness, severity = parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])
                hospital.arrive(first_name, last_name, age, illness, severity)
            elif parts[0] == 'NEXT':
                next_patient = hospital.next_patient()
                if next_patient:
                    print("Next patient:")
                    print(f"    Name: {next_patient.last_name}, {next_patient.first_name}.")
                    print(f"    Age: {next_patient.age}")
                    print(f"    Suffers from: {next_patient.illness}")
                    print(f"    Illness severity: {next_patient.severity}")
                    print(f"    Arrival order: {next_patient.arrival_order}")
                else:
                    print("No patients in queue.")
            elif parts[0] == 'TREAT':
                treated_patient = hospital.treat_patient()
                if treated_patient:
                    print("Patient treated:")
                    print(f"    Name: {treated_patient.last_name}, {treated_patient.first_name}.")
                    print(f"    Age: {treated_patient.age}")
                    print(f"    Suffers from: {treated_patient.illness}")
                    print(f"    Illness severity: {treated_patient.severity}")
                    print(f"    Arrival order: {treated_patient.arrival_order}")
                else:
                    print("No patients to treat.")
            elif parts[0] == 'COUNT':
                print("There are", hospital.count_patients(), "patients waiting.")

# Sample usage
file_name = input("Enter the file name: ")
process_commands_from_file(file_name)
