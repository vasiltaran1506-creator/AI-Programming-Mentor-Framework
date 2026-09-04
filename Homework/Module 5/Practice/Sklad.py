from dataclasses import dataclass

@dataclass
class Equipment:
    name: str
    price_per_day: float

    #def __init__(self, name, price_per_day):
    #    self.name = name
    #    self.price_per_day = price_per_day 
#
    #def __str__(self) -> str:
    #    return f"Название: {self.name}        Цена за день: {self.price_per_day}"

class Camera(Equipment):
    def __init__(self, name, price_per_day):
        super().__init__(name, price_per_day)

    def calculate_price(self, days):
        total_price = self.price_per_day * days
        return total_price
        

class Light(Equipment):
    def __init__(self, name, price_per_day, insurance_fee):
        super().__init__(name, price_per_day)
        self.insurance_fee = insurance_fee

    def calculate_price(self, days):
        total_price = (self.price_per_day * days) + self.insurance_fee
        return total_price


class Cable(Equipment):
    def __init__(self, name, price_per_day):
        super().__init__(name, price_per_day)

    def calculate_price(self, days):
        total_price = self.price_per_day * days
        return total_price


class Drone(Equipment):
    def __init__(self, name, price_per_day, calibration_fee):
        super().__init__(name, price_per_day)
        self.calibration_fee = calibration_fee  

    def calculate_price(self, days):
        total_price = (self.price_per_day * days) + self.calibration_fee
        return total_price


def calculate_total_estimate(equipment_list: list, days: int) -> float:
    prices = []
    for item in equipment_list:
        prices.append(item.calculate_price(days))
    return float(sum(prices))

def main():
    cam1 = Camera("Sony FX3", 2500)
    light1 = Light("Aputure 600C Pro II", 5600, 500)
    cable1 = Cable("Schuko 3x16Ax220V 10m", 100)
    drone1 = Drone("DJI Mavic 4", 8000, 500)
    equipment_list = [cam1, light1, cable1, drone1]
    days = 5

    print(cam1)
    print("")
    print(light1)

    print(calculate_total_estimate(equipment_list, days))    


if __name__ == "__main__":
    main()