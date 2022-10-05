from time import sleep
import smbus
import time
import RPi.GPIO as GPIO
import sys, os

pin = 23
setgpio = (29,31,32,33,35,36,37,38)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(setgpio,GPIO.OUT)

p1 =GPIO.PWM(29,50)
p2 =GPIO.PWM(31,50)
p3 =GPIO.PWM(32,50)
p4 =GPIO.PWM(33,50)
p5 =GPIO.PWM(35,50)
p6 =GPIO.PWM(36,50)
p7 =GPIO.PWM(37,50)
p8 =GPIO.PWM(38,50)
p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
p5.start(0)
p6.start(0)
p7.start(0)
p8.start(0)

i2c = smbus.SMBus(1)
address1 = 0x70
address2 = 0x71
address3 = 0x72
address4 = 0x73
address5 = 0x74
address6 = 0x75
address7 = 0x76
address8 = 0x77
SLEEPTIME = 0.08
DELAY = 0.08
bis1 = bis2 = bis3 = bis4 = bis5 = bis6 = bis7 = bis8 = 180
i = j = k = l = m = n = o = p = 0
    
if __name__ == '__main__':
    try:
        while True:
            button = GPIO.input(pin)
            if button == False:
                break
            
            i2c.write_i2c_block_data(0x70,0x00,[0x51])
            i2c.write_i2c_block_data(0x71,0x00,[0x51])
            i2c.write_i2c_block_data(0x72,0x00,[0x51])
            i2c.write_i2c_block_data(0x73,0x00,[0x51])
            i2c.write_i2c_block_data(0x74,0x00,[0x51])
            i2c.write_i2c_block_data(0x75,0x00,[0x51])
            i2c.write_i2c_block_data(0x76,0x00,[0x51])
            i2c.write_i2c_block_data(0x77,0x00,[0x51])
            time.sleep(DELAY)  
            
            block1 = i2c.read_i2c_block_data(address1,0x00,4)
            block2 = i2c.read_i2c_block_data(address2,0x00,4)
            block3 = i2c.read_i2c_block_data(address3,0x00,4)
            block4 = i2c.read_i2c_block_data(address4,0x00,4)
            block5 = i2c.read_i2c_block_data(address5,0x00,4)
            block6 = i2c.read_i2c_block_data(address6,0x00,4)
            block7 = i2c.read_i2c_block_data(address7,0x00,4)
            block8 = i2c.read_i2c_block_data(address8,0x00,4)
            time.sleep(SLEEPTIME)
            dis1 = (block1[2]<<8 | block1[3])
            dis2 = (block2[2]<<8 | block2[3])
            dis3 = (block3[2]<<8 | block3[3])
            dis4 = (block4[2]<<8 | block4[3])
            dis5 = (block5[2]<<8 | block5[3])
            dis6 = (block6[2]<<8 | block6[3])
            dis7 = (block7[2]<<8 | block7[3])
            dis8 = (block8[2]<<8 | block8[3])
            time.sleep(SLEEPTIME)
            
            if abs(bis1 - dis1) > 100 and i != 1:
                dis1 = bis1
                i = 1
                if dis1 == 0:
                    dis1 = 9999999
                Dcycle1 = -0.91 * dis1 + 154.7
                if Dcycle1 < 0:
                    Dcycle1 = 0
                if Dcycle1 > 100:
                    Dcycle1 = 100
                GPIO.output(29,GPIO.HIGH)
                p1.ChangeDutyCycle(Dcycle1)
            elif abs(bis1 - dis1) < 100 or i == 1:
                if dis1 == 0:
                    dis1 = 9999999
                Dcycle1 = -0.91 * dis1 + 154.7
                if Dcycle1 < 1:
                    Dcycle1 = 0
                if Dcycle1 > 100:
                    Dcycle1 = 100
                GPIO.output(29,GPIO.HIGH)
                p1.ChangeDutyCycle(Dcycle1)
                i = 0
                bis1 = dis1
                
            if abs(bis2 - dis2) > 100 and j != 1:
                dis2 = bis2
                j = 1
                if dis2 == 0:
                    dis2 = 9999999
                Dcycle2 = -0.91 * dis2 + 154.7
                if Dcycle2 < 1:
                    Dcycle2 = 0
                if Dcycle2 > 100:
                    Dcycle2 = 100
                GPIO.output(31,GPIO.HIGH)
                p2.ChangeDutyCycle(Dcycle2)

            elif abs(bis2 - dis2) < 100 or j == 1:
                if dis2 == 0:
                    dis2 = 9999999
                Dcycle2 = -0.91 * dis2 + 154.7
                if Dcycle2 < 1:
                    Dcycle2 = 0
                if Dcycle2 > 100:
                    Dcycle2 = 100
                GPIO.output(31,GPIO.HIGH)
                p2.ChangeDutyCycle(Dcycle2)
                j = 0
                bis2 = dis2
                
            if abs(bis3 - dis3) > 100 and k != 1:
                dis3 = bis3
                k = 1
                if dis3 == 0:
                    dis3 = 9999999
                Dcycle3 = -0.91 * dis3 + 154.7
                if Dcycle3 < 1:
                    Dcycle3 = 0
                if Dcycle3 > 100:
                    Dcycle3 = 100
                GPIO.output(32,GPIO.HIGH)
                p3.ChangeDutyCycle(Dcycle3)
            elif abs(bis3 - dis3) < 100 or k == 1:
                if dis3 == 0:
                    dis3 = 9999999
                Dcycle3 = -0.91 * dis3 + 154.7
                if Dcycle3 < 1:
                    Dcycle3 = 0
                if Dcycle3 > 100:
                    Dcycle3 = 100
                GPIO.output(32,GPIO.HIGH)
                p3.ChangeDutyCycle(Dcycle3)
                k = 0
                bis3 = dis3
                
            if abs(bis4 - dis4) > 100 and l != 1:
                dis4 = bis4
                l = 1
                if dis4 == 0:
                    dis4 = 9999999
                Dcycle4 = -0.91 * dis4 + 154.7
                if Dcycle4 < 1:
                    Dcycle4 = 0
                if Dcycle4 > 100:
                    Dcycle4 = 100
                GPIO.output(33,GPIO.HIGH)
                p4.ChangeDutyCycle(Dcycle4)
                        
            elif abs(bis4 - dis4) < 100 or l == 1:
                if dis4 == 0:
                    dis4 = 9999999
                Dcycle4 = -0.91 * dis4 + 154.7
                if Dcycle4 < 1:
                    Dcycle4 = 0
                if Dcycle4 > 100:
                    Dcycle4 = 100
                GPIO.output(33,GPIO.HIGH)
                p4.ChangeDutyCycle(Dcycle4)
                l = 0
                bis4 = dis4
                
            if abs(bis5 - dis5) > 100 and m != 1:
                dis5 = bis5
                m = 1
                if dis5 == 0:
                    dis5 = 9999999
                Dcycle5 = -0.91 * dis5 + 154.7
                if Dcycle5 < 1:
                    Dcycle5 = 0
                if Dcycle5 > 100:
                    Dcycle5 = 100
                GPIO.output(35,GPIO.HIGH)
                p5.ChangeDutyCycle(Dcycle5)
                        
            elif abs(bis5 - dis5) < 100 or m == 1:
                if dis5 == 0:
                    dis5 = 9999999
                Dcycle5 = -0.91 * dis5 + 154.7
                if Dcycle5 < 1:
                    Dcycle5 = 0
                if Dcycle5 > 100:
                    Dcycle5 = 100
                GPIO.output(35,GPIO.HIGH)
                p5.ChangeDutyCycle(Dcycle5)
                m = 0
                bis5 = dis5
                
            if abs(bis6 - dis6) > 100 and n != 1:
                dis6 = bis6
                n = 1
                if dis6 == 0:
                    dis6 = 9999999
                Dcycle6 = -0.91 * dis6 + 154.7
                if Dcycle6 < 1:
                    Dcycle6 = 0
                if Dcycle6 > 100:
                    Dcycle6 = 100
                GPIO.output(36,GPIO.HIGH)
                p6.ChangeDutyCycle(Dcycle6)
                        
            elif abs(bis6 - dis6) < 100 or n == 1:
                if dis6 == 0:
                    dis6 = 9999999
                Dcycle6 = -0.91 * dis6 + 154.7
                if Dcycle6 < 1:
                    Dcycle6 = 0
                if Dcycle6 > 100:
                    Dcycle6 = 100
                GPIO.output(36,GPIO.HIGH)
                p6.ChangeDutyCycle(Dcycle6)
                n = 0
                bis6 = dis6
                
            if abs(bis7 - dis7) > 100 and o != 1:
                dis7 = bis7
                o = 1
                if dis7 == 0:
                    dis7 = 9999999
                Dcycle7 = -0.91 * dis7 + 154.7
                if Dcycle7 < 1:
                    Dcycle7 = 0
                if Dcycle7 > 100:
                    Dcycle7 = 100
                GPIO.output(37,GPIO.HIGH)
                p7.ChangeDutyCycle(Dcycle7)
                        
            elif abs(bis7 - dis7) < 100 or o == 1:
                if dis7 == 0:
                    dis7 = 9999999
                Dcycle7 = -0.91 * dis7 + 154.7
                if Dcycle7 < 1:
                    Dcycle7 = 0
                if Dcycle7 > 100:
                    Dcycle7 = 100
                GPIO.output(37,GPIO.HIGH)
                p7.ChangeDutyCycle(Dcycle7)
                o = 0
                bis7 = dis7
                
            if abs(bis8 - dis8) > 100 and p != 1:
                dis8 = bis8
                p = 1
                if dis8 == 0:
                    dis8 = 9999999
                Dcycle8 = -0.91 * dis8 + 154.7
                if Dcycle8 < 1:
                    Dcycle8 = 0
                if Dcycle8 > 100:
                    Dcycle8 = 100
                GPIO.output(38,GPIO.HIGH)
                p8.ChangeDutyCycle(Dcycle8)
                        
            elif abs(bis8 - dis8) < 100 or p == 1:
                if dis8 == 0:
                    dis8 = 9999999
                Dcycle8 = -0.91 * dis8 + 154.7
                if Dcycle8 < 1:
                    Dcycle8 = 0
                if Dcycle8 > 100:
                    Dcycle8 = 100
                GPIO.output(38,GPIO.HIGH)
                p8.ChangeDutyCycle(Dcycle8)
                p = 0
                bis8 = dis8
            
    finally:
        GPIO.cleanup()
        print("finish!!")