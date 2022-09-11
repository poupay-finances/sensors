import asyncio
from datetime import datetime
from sensors.sensor import Sensor
import numpy as np
import uuid


class HT11(Sensor):
    async def generate(self):
        print("Simulando dados de temperatura")
        base = self.get_random_number()
        while True:
            data_temperature = np.random.uniform(low=base - 2, high=base + 2)
            self.data = np.random.choice([np.round(data_temperature, 1), None], p=[0.9, 0.1])
            date_now = datetime.now()
            self.data = {
                "temperature": self.data,
                "date_register": date_now.strftime('%m/%d/%Y %H:%M:%S'),
                "message_id": str(uuid.uuid4())
            }
            print(f"{self.data['date_register']} - {self.data['temperature']} Cº")
            await self.send_data()
            await asyncio.sleep(1)

    def get_random_number(self):
        return np.random.uniform(low=30.5, high=45.5)
