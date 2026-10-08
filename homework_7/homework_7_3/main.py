from homework_7.homework_7_3.doctors.therapist import Therapist
from homework_7.homework_7_3.patient import Patient

if __name__ == '__main__':
    therapist = Therapist()

    patient_1 = Patient("Kirill", 27, 1)
    patient_2 = Patient("Vladislav", 35, 2)
    patient_3 = Patient("Anton", 74, 3)

    therapist.assign_doctor(patient_1)
    therapist.assign_doctor(patient_2)
    therapist.assign_doctor(patient_3)

    patient_1.doctor.treat()
    patient_2.doctor.treat()
    patient_3.doctor.treat()
