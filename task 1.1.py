from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']


    def running(self):
        print('stop,', self.__color[0])
        sleep(7)
        print('be ready,', self.__color[1])
        sleep(3)
        print('move,', self.__color[2])
        sleep(7)
        return

tr_light = TrafficLight()
tr_light.running()




