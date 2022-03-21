# Importing Libraries
import serial
import time
import keyboard
from random import randint
from time import sleep
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(1)
    data = arduino.readline()
    return data

def main():
    num = input("Enter parameters ")  # Taking input from user
    value = write_read(num)
    print(value)  # printing the value
    for x in range(29):
        try:
            if keyboard.is_pressed(' '):
                print("You pressed space")
                break
        except:
            pass
        sleep(randint(3, 5))
        try:
            if keyboard.is_pressed(' '):
                print("You pressed space")
                break
        except:
            pass
        arduino.write(bytes("1", 'utf-8'))
        try:
            if keyboard.is_pressed(' '):
                print("You pressed space")
                break
        except:
            pass
    arduino.close()

if __name__ == "__main__":
    main()

