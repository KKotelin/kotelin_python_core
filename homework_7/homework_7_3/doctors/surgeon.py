from homework_7.homework_7_3.doctors.doctor import Doctor


class Surgeon(Doctor):
    def treat(self) -> None:
        print("Хирург проводит операцию")
