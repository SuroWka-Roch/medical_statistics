#!/usr/bin/env python3.5
import datetime


class DrugSusceptibility:

    def __init__(self, id, bakteria_type, sus):
        self.DrugId = id
        self.bacteriaId = bakteria_type
        self.Susceptibility = sus
    


class Bacteria:

    def __init__(self, id, test, type):
        self.bacteriaId = id
        self.testId = test
        self.idType = type

        self.DrugSusceptibility = []

    def add_susceptibility(self, drugSusceptibility):
        self.DrugSusceptibility.append(drugSusceptibility)


class Test:

    def __init__(self, test, patient, datedata, material):
        self.testId = test
        self.PatientId = patient
        self.materialId = material
        self.Bacteria = []

        datadata = datedata.split("-")
        self.date = datetime.date(
            int(str(19) + datadata[-1]), int(datadata[-2]), int(datadata[-3]))

    def is_date_between(self, date_min, date_max):
        return date_min <= self.date <= date_max

    def add_bacteria(self, bacteria):
        self.Bacteria.append(bacteria)


class Patient:

    def __init__(self, patient, sex, department):
        self.PatientId = patient
        self.sex = sex
        self.department = []
        self.department.append(department)
        self.test = []

    def add_test(self, test):
        self.test.append(test)
    
    def extend_department(self, patient):
        self.department.extend( patient.department )
        


if __name__ == "__main__":
    pass
