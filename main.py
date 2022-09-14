import asyncio

from sensors.dht11 import DHT11


async def main():
    sensor = DHT11()
    await sensor.generate()


if __name__ == "__main__":
    print("Gerando dados")
    asyncio.run(main())
