class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lots = {
            1: big,
            2: medium,
            3: small,
        }
    
    def addCar(self, carType: int) -> bool:
        if self.lots[carType] > 0:
            self.lots[carType] -= 1
            return True
        return False
