class VGIK_Policy:
    def __init__(self,) -> None:
        self.thungsten_discount = 70
        self.hmi_discount = 70
        self.led_discount = 70

    def calculate_discount(self, category: EstimateItem.category) -> int:
        if category == "THUNGSTEN_LIGHT":
            return self.thungsten_discount
        elif category == "HMI_LIGHT":
            return self.hmi_discount
        elif category == "LED_LIGHT":
            return self.led_discount

        else: 
            return 0