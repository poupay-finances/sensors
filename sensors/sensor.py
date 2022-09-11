import abc
import json

from azure.iot.device import Message

from constants import CONNECTION_STRING
from azure.iot.device.aio import IoTHubDeviceClient

class Sensor(abc.ABC):
    def __init__(self):
        self.data = 0
        self.device = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    @abc.abstractmethod
    async def generate(self):
        pass

    async def send_data(self):
        try:
            # Create IoTHubRegistryManager
            message = Message(json.dumps(self.data))
            await self.device.send_message(message)
            print("Enviando mensagem para Nuvem")
        except Exception as ex:
            print("Unexpected error " + ex)
            return
