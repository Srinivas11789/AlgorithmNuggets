# Logic 1: naive logic with global for current light tracking --> 100 pass 71 % faster
class TrafficLight(object):
    
    def __init__(self):
        # Current Traffic Light that is GREEN
        self.current_green_light = 1

        # The Gist
        """
        self.current_green_light = "A"
        # Direction mapped to the Road A and B
        self.light = ["A", "A", "B", "B"]
        self.result_car = "Car %d Has Passed Road A In Direction %d"
        self.result_light = "Traffic Light On Road %s Is Green"
        """

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        """
        :type roadId: int --> // ID of the car
        :type carId: int --> // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        :type direction: int --> // Direction of the car
        :type turnGreen: method --> // Use turnGreen() to turn light to green on current road
        :type crossCar: method --> // Use crossCar() to make car cross the intersection
        :rtype: void
        """

        if roadId == self.current_green_light:
            crossCar()
        else:
            self.current_green_light = roadId
            turnGreen()
            crossCar()

        # The Gist
        """
        if self.light[direction] == self.current_green_light:
            return self.result_car % (carId, direction)
        else:
            self.current_green_light = self.light[direction]
            return self.result_light % (self.light[direction]) + "," + self.result_car % (carId, direction)
        """

            
        
        

        
