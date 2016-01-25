from __future__ import print_function
from pysis import SIS
from time import sleep

if __name__ == '__main__':

    sisapi = SIS()


    while True:
        facility = sisapi.facilities.get(id=65)

        sleep(10)

        print('facility name: ' + facility.name)
