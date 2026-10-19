from homework_7.homework_7_3.doctors.doctor import Doctor


class Dentist(Doctor):
    def treat(self) -> None:
        print("Стоматолог лечит зубы")
