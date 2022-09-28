class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def bitum(self):
        bitum_depth = 5
        bitum_mass = 15
        return self._length * self._width * bitum_depth * bitum_mass



road = Road(10, 4)
print(road.bitum())





