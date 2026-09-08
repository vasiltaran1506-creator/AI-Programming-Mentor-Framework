from abc import ABC, abstractmethod


class PricePolicy(ABC):
    @abstractmethod
    def calculate_discount(self, category: str):
        pass


class VGIK_Policy(PricePolicy):
    def __init__(self) -> None:
        self.vgik_thung_discount = 70
        self.vgik_hmi_discount = 60
        self.vgik_led_discount = 50

    def calculate_discount(self, category):
        if category == "THUNGSTEN_LIGHT":
            return self.vgik_thung_discount
        elif category == "HMI_LIGHT":
            return self.vgik_hmi_discount
        elif category == "LED_LIGHT":
            return self.vgik_led_discount
        else:
            return 0

class Standart_Policy(PricePolicy):
    def __init__(self) -> None:
        self.standart_policy_discount = 0

    def calculate_discount(self, category):
        return self.standart_policy_discount