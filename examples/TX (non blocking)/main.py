from jetson_sx126x import SX1262, Pin
import time


def cb(events):
    if events & SX1262.TX_DONE:
        print("TX done.")


try:
    sx = SX1262(cs=24, irq=13, rst=18, gpio=22, device="/dev/spidev3.0")

    # LoRa
    sx.begin()

    # FSK
    ##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
    ##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
    ##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
    ##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
    ##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
    ##            tcxoVoltage=1.6, useRegulatorLDO=False,
    ##            blocking=True)

    sx.setBlockingCallback(False, cb)

    while True:
        sx.send(b"Hello World!")
        time.sleep(10)
finally:
    Pin.cleanup()
