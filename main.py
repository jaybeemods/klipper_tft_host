# Klipper TFT Host
# This project allows a TFT35 or similar to interface with Klipper by passing commands to Moonraker

import serial
import websockets
import logging
import configparser

# Parse Config
config = configparser.ConfigParser()
config.read('config')


# Setup Logging
if config.get('logging', 'level') == 'DEBUG':
    level = logging.DEBUG
elif config.get('logging', 'level') == 'INFO':
    level = logging.INFO
elif config.get('logging', 'level') == 'WARNING':
    level = logging.WARNING
elif config.get('logging', 'level') == 'ERROR':
    level = logging.ERROR
else:
    level = logging.CRITICAL

logging.basicConfig(filename=config.get('logging', 'path'), level=level, filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')


# Create a open connection and return the pointer
def open_serial_port(com, baud):
    try:
        serial_object = serial.Serial(com, baud)  # open serial port
        logging.debug('Serial port opened at ' + serial_object.name)
        return serial_object
    except:
        logging.critical('UNABLE TO OPEN SERIAL PORT, check your config!!')
        exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.info('Starting')
    serial = open_serial_port(config.get('serial', 'port'), config.get('serial', 'baud'))

    loop = True
    while loop:
        line = serial.readline()
        print(line)
        if line == b'M105\n':
            serial.write(b'ok T:201 /202 B:117 /120 \n')
