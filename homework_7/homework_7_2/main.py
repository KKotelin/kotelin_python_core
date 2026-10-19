from homework_7.homework_7_2.atm import Atm
from homework_7.homework_7_2.atm_console import AtmConsole

if __name__ == '__main__':
    atm = Atm(1, 1, 1)
    atm_console = AtmConsole(atm)
    atm_console.run_atm()
