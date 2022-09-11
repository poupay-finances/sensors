from sensors.ht11 import HT11


def main():
    sensor = HT11()
    temparature = sensor.generate()


if __name__ == "__main__":
    main()
