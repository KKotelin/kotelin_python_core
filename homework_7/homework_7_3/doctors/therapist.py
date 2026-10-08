from homework_7.homework_7_3.doctors.dentist import Dentist
from homework_7.homework_7_3.doctors.doctor import Doctor
from homework_7.homework_7_3.doctors.surgeon import Surgeon
from homework_7.homework_7_3.patient import Patient


class Therapist(Doctor):
    def treat(self) -> None:
        print("Терапевт назначает медикаментозное лечение")

    def assign_doctor(self, patient: Patient) -> None:
        print(
            f"\nПациент: {patient.name}\n"
            f"Возраст: {patient.age}"
        )
        match patient.treatment_plan:
            case 1:
                print("Пациенту назначено направление к хирургу")
                patient.doctor = Surgeon()
            case 2:
                print("Пациенту назначено направление к стоматологу")
                patient.doctor = Dentist()
            case _:
                print("Пациенту назначено направление к терапевту")
                patient.doctor = self
