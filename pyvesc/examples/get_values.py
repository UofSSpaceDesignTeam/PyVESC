import pyvesc
from pyvesc import GetValues, SetRPM, SetCurrent, SetRotorPositionMode, GetRotorPosition
import serial
import time

# Set your serial port here (either /dev/ttyX or COMX)
serialport = '/dev/ttyACM0'

def get_values_example():
    rpm = 5000
    with serial.Serial(serialport, baudrate=115200, timeout=0.05) as ser:
        try:
            # Optional: Turn on rotor position reading if an encoder is installed
            ser.write(pyvesc.encode(SetRotorPositionMode(SetRotorPositionMode.DISP_POS_MODE_ENCODER )))
            print("config")
            while True:
                # Set the ERPM of the VESC motor
                #    Note: if you want to set the real RPM you can set a scalar
                #          manually in setters.py
                #          12 poles and 19:1 gearbox would have a scalar of 1/228
                ser.write(pyvesc.encode(SetRPM(rpm)))

                # Request the current measurement from the vesc
                ser.write(pyvesc.encode_request(GetRotorPosition))

                # Check if there is enough data back for a measurement
                if ser.in_waiting > 0:
                    buffer = ser.readline()
                    try:
                        (response, consumed) = pyvesc.decode(buffer)

                        # Print out the values
                        if response.__class__ == GetRotorPosition:
                            print(response.rotor_pos)
                            if response.rotor_pos >= 70 and rpm < 0:
                                rpm = 5000
                            elif response.rotor_pos <= 40 and rpm > 0:
                                rpm = -5000

                        # print(response.rpm)

                    except:
                        # ToDo: Figure out how to isolate rotor position and other sensor data
                        #       in the incoming datastream
                        #try:
                        #    print(response.rotor_pos)
                        #except:
                        #    pass
                        pass

                time.sleep(0.001)

        except KeyboardInterrupt:
            # Turn Off the VESC
            ser.write(pyvesc.encode(SetCurrent(0)))

if __name__ == "__main__":
    get_values_example()
