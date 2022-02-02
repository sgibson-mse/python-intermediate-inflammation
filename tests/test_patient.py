"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Gibson'
    d = Doctor(name=name)

    assert d.name == name


def test_patient_list():
    from inflammation.models import Doctor

    sam = Doctor('Gibson')

    test_patients = ['A', 'B', 'C']
    sam.add_patients(test_patients)

    assert len(sam.patients) == len(test_patients)