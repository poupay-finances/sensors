import asyncio

from sensors.ht11 import HT11


async def main():
    sensor = HT11()
    await sensor.generate()


if __name__ == "__main__":
    print("Gerando dados")
    asyncio.run(main())
