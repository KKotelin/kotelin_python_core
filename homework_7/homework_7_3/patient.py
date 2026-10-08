from homework_7.homework_7_3.doctors.doctor import Doctor


class Patient:
    def __init__(self, name: str, age: int, treatment_plan: int) -> None:
        self.name = name
        self.age = age
        self.treatment_plan = treatment_plan
        self.doctor: Doctor | None = None
