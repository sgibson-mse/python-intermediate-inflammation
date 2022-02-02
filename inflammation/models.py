"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    @property
    def last_patient(self):
        return self.patients[-1]

    @property
    def total_patients(self):
        return len(self.patients)

    def add_patients(self, new_patients):
        """ Add patients to a doctor"""

        for patient_name in new_patients:
            self.patients.append(patient_name)

        return

    def __str__(self):
        return self.name


class Patient(Person):
    def __init__(self, name, observations=[]):
        """A Patient in an inflammation study"""
        super().__init__(name)
        self.name = name
        self.observations = observations

    def __str__(self):
        return self.name

    @property
    def last_observation(self):
        return self.observations[-1]

    def add_observation(self, value, day=None):
        """ Add an observation to a particular patient"""
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1
            except IndexError:
                day = 0

        new_observation = {
            'day': day,
            'value': value,
        }

        new_observation = Observation(day, value)

        self.observations.append(new_observation)

        return new_observation


alice = Patient('Alice')

obs = alice.add_observation(3)

bob = Patient('Bob')

obs = bob.add_observation(4)
print(obs)

sam = Doctor('Sam')


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """
    Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D array of which the mean is calculated over the first axis of the array.
    returns: Array of mean values for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """
    Calculate the daily max of a 2D inflammation data array.
    params: data: 2D array of data.
    returns: An array of maximum values along the first axis of the array.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """
    Calculate the daily min of a 2d inflammation data array.
    params: data: 2D array of data
    returns: An array of minimum values for each day.
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    max = np.max(data, axis=1)
    return data / max[:, np.newaxis]

def attach_names(patient_names, patient_data):
    """
    Assign patient names and patient data withn a dictionary structure.
    params: patient_names: list of strings with patient names
            patient_data: numpy array of data
    returns: patients: dictionary of patient names and data
    """

    assert len(patient_names) == len(patient_data) #Raise assertion error if length of data =/= length of names

    patients = []

    for patient, data in zip(patient_names, patient_data):
        print(patient, data)
        patients.append({'name': patient,
                          'data': data
        })

    return patients



# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
