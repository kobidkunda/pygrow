import RPi.GPIO as GPIO
import time
import json


class DHTTools(object):
    """
    Tools for working with DHT temperature/humidity sensor.
    """

    def __init__(self):
        self.type = 'DHT11'

    def binary_to_decimal(self, string_num):
        """
        Convert a binary number to a decimal.
        """
        # Return a string representing the integer value of the string passed to this function in base 2 (binary)
        return str(int(string_num, 2))

    def read_sensor(self):
        """
        Read temperature and humidity from DHT sensor.
        """
        # Create a data array
        data = []

        # Use the Broadcom numbers instead of the WiringPi numbers
        GPIO.setmode(GPIO.BCM)

        # Set it as an output:
        GPIO.setup(4,GPIO.OUT)
        # Write a 1:
        GPIO.output(4,GPIO.HIGH)
        # Wait for 25 ms
        time.sleep(0.025)
        # Write a 0
        GPIO.output(4,GPIO.LOW)
        # Wait for 20 ms
        time.sleep(0.02)

        # Change the pin to read mode, with a pullup resistor
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # 501 times
        for i in range(0,500):
            # Read a bit from the GPIO, as fast as possible (no wait)
            data.append(GPIO.input(4))

        bit_count = 0
        tmp = 0
        count = 0
        humidity_bit = ''
        temperature_bit = ''
        crc = ''

        try:
            # As long as you read a 1
            while data[count] == 1:
                tmp = 1
                # Count how many 1s have been read
                count = count + 1

            # Do this 33 times
            for i in range(0, 32):
                # Reset the bit count each time
                bit_count = 0

                # As long as a 0 is read
                while data[count] == 0:
                    tmp = 1
                    # Move on to the next bit
                    count = count + 1

                # As long as a 1 is read
                while data[count] == 1:
                    # Count how many 1s in a row
                    bit_count = bit_count + 1
                    # Move on to the next bit
                    count = count + 1

                # If there were mote than 3 * 1-bits in a row
                if bit_count > 3:
                    # If we're in the 1st byte
                    if i >= 0 and i < 8:
                        # Append a 1 to the humidity bitstring
                        humidity_bit = humidity_bit + "1"
                    # If we're in the 3rd byte
                    if i >= 16 and i < 24:
                        # Append a 1 to the temperature bitstring
                        temperature_bit = temperature_bit + '1'
                # If there weren't at least 3 * 1-bits
                else:
                    # If we're in the 1st byte
                    if i >= 0 and i < 8:
                        # Append a 0 to the humidity bitstring
                        humidity_bit = humidity_bit + '0'
                    # If we're in the 3rd byte
                    if i >= 16 and i < 24:
                        # Append a 0 to the temperature bitstring
                        temperature_bit = temperature_bit + '0'

        except:
            # Return Range error
            print 'DHTTools - Error Range'
            return 'ERROR_RANGE'
            # Exit program
            exit(0)

        try:
            # Do this 9 times
            for i in range(0, 8):
                # Reset the bit counter
                bit_count = 0

                # As long as a 0 was read
                while data[count] == 0:
                    tmp = 1
                    # Move on to the next bit
                    count = count + 1

                # As long as a 1 was read
                while data[count] == 1:
                    # Count how many 1s
                    bit_count = bit_count + 1
                    # Move on to the next bit
                    count = count + 1

                # If there were at least 3 * 1-bits
                if bit_count > 3:
                    # Append a 1 to the CRC (cyclic redundancy check) bitstring
                    crc = crc + '1'
                # If there were less than 3* 1-bits
                else:
                    # Append a 0 to the CRC bitstring
                    crc = crc + '0'
        except:
            # Return Range error
            print 'DHTTools - Error Range'
            return 'ERROR_RANGE'
            # Exit program
            exit(0)

        # Convert the binary bitstrings to  decimal values
        reading_temperature = binary_to_decimal(temperature_bit)
        reading_humidity = binary_to_decimal(humidity_bit)

        reading_timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Test whether the CRC indicates that the reading was good
        if int(reading_humidity) + int(reading_temperature) - int(binary_to_decimal(crc)) == 0:
            print 'DHTTools - Temperature reading' + reading_temperature
            print 'DHTTools - Humidity reading: ' + reading_humidity
            print 'DHTTools - Timestamp reading: ' + reading_timestamp
            # Create JSON with reading values
            reading = json.dumps({
                'reading_temperature': reading_temperature,
                'reading_humidity': reading_humidity,
                'reading_timestamp': reading_timestamp,
            })
            return reading
        else:
            # Return CRC error
            print 'DHTTools - Error CRC'
            return 'ERROR_CRC'
            # Exit program
            exit(0)