import asyncio
from datetime import datetime
from sensors.sensor import Sensor
import numpy as np
import uuid


class DHT11(Sensor):

    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.energy = 100.0
        self.humidity = 0
        self.date_register = datetime.now()

    async def generate(self):
        print("Simulando dados de temperatura")
        base_temperature = self.get_random_number(20.5, 38.5)
        base_humidity = self.get_random_number(30, 98)
        while self.energy > 0:
            error_register = np.random.choice([False, True], p=[0.97, 0.03])
            if error_register:
                self.set_data_error()
            else:
                self.set_humidity(base_humidity)
                self.set_temperature(base_temperature)
                self.update_date_register()
                self.set_data_success()
            print(f"{self.data.get('date_register')} - {self.data.get('temperature')} Cº - Umidade: "
                  f"{self.data.get('humidity')}%")
            await self.send_data()
            self.energy = 0.005
            await asyncio.sleep(60)
        self.energy = 0
        print("Sensor descarregado!")

    def set_temperature(self, base_temperature):
        temperature = np.random.uniform(low=base_temperature - 2, high=base_temperature + 2)
        self.temperature = np.round(temperature, 1)

    def set_humidity(self, base_humidity):
        humidity = np.random.uniform(low=base_humidity - 2, high=base_humidity + 2)
        self.humidity = np.round(humidity, 0)

    def update_date_register(self):
        self.date_register = datetime.now()

    def set_data_success(self):
        self.data = {
            "energy": round(self.energy, 3),
            "humidity": self.humidity,
            "temperature": self.temperature,
            "date_register": self.date_register.strftime('%m/%d/%Y %H:%M:%S'),
            "message_id": str(uuid.uuid4())
        }

    def set_data_error(self):
        self.data = {
            "energy": round(self.energy, 3),
            "humidity": None,
            "temperature": None,
            "date_register": self.date_register.strftime('%m/%d/%Y %H:%M:%S'),
            "message_id": str(uuid.uuid4())
        }
        return self.data

    def get_random_number(self, min, max):
        return np.random.uniform(low=min, high=max)
