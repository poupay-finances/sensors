import time
from datetime import datetime
from sensors.sensor import Sensor
import numpy as np


class HT11(Sensor):
    def generate(self):
        print("Simulando dados de temperatura")
        base = self.get_random_number()
        while True:
            data_temperature = np.random.uniform(low=base - 2, high=base + 2)
            data = np.random.choice([np.round(data_temperature, 1), None], p=[0.9, 0.1])
            date_now = datetime.now()
            print(f"{date_now.strftime('%m/%d/%Y %H:%M:%S')} - {data} Cº")
            time.sleep(1)

    def get_random_number(self):
        return np.random.uniform(low=30.5, high=45.5)
