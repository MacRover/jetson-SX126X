import logging
from jetson_sx126x import SX1262, Pin

logging.basicConfig(level="DEBUG")

try:
    spi_device = SX1262(24, 13, 18, 22, "/dev/spidev3.0", 2000000)
    spi_device.begin()
    # spi_device.begin(
    #     freq=923,
    #     bw=500.0,
    #     sf=12,
    #     cr=8,
    #     syncWord=0x12,
    #     power=-5,
    #     currentLimit=60.0,
    #     preambleLength=8,
    #     implicit=False,
    #     implicitLen=0xFF,
    #     crcOn=True,
    #     txIq=False,
    #     rxIq=False,
    #     tcxoVoltage=1.7,
    #     useRegulatorLDO=False,
    #     blocking=True,
    # )

    while True:
        msg, err = spi_device.recv()
        if len(msg) > 0:
            error = SX1262.STATUS[err]
            print (msg)
            print(error)

finally:
    Pin.cleanup()