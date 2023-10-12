import smbus					#import SMBus module of I2C
from time import sleep          #import

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

class Accelerometer:
    bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards

    def MPU_Init(self):
        #write to sample rate register
        self.bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
        
        #Write to power management register
        self.bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        
        #Write to Configuration register
        self.bus.write_byte_data(Device_Address, CONFIG, 0)
        
        #Write to Gyro configuration register
        self.bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
        
        #Write to interrupt enable register
        self.bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(self, addr):
        #Accelero and Gyro value are 16-bit
            high = self.bus.read_byte_data(Device_Address, addr)
            low = self.bus.read_byte_data(Device_Address, addr+1)
        
            #concatenate higher and lower value
            value = ((high << 8) | low)
            
            #to get signed value from mpu6050
            if(value > 32768):
                    value = value - 65536
            return value

    def compute_acceleration(self):
        acc_x = self.read_raw_data(ACCEL_XOUT_H)
        acc_y = self.read_raw_data(ACCEL_YOUT_H)
        acc_z = self.read_raw_data(ACCEL_ZOUT_H)

        #Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0

        return (Ax, Ay, Az)

    def compute_angular_velocity(self):
        gyro_x = self.read_raw_data(GYRO_XOUT_H)
        gyro_y = self.read_raw_data(GYRO_YOUT_H)
        gyro_z = self.read_raw_data(GYRO_ZOUT_H)

        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0

        return (Gx, Gy, Gz)



Device_Address = 0x68   # MPU6050 device address
# acc = Accelerometer()
# acc.MPU_Init()
# sleep(1)

# print (" Reading Data of Gyroscope and Accelerometer")

# while True:	
#     acceleration = acc.compute_acceleration()
#     angular_velocity = acc.compute_angular_velocity()	

#     print("Gx=%.2f" %angular_velocity[0], u'\u00b0'+ "/s", "\tGy=%.2f" %angular_velocity[1], u'\u00b0'+ "/s", "\tGz=%.2f" %angular_velocity[2], u'\u00b0'+ "/s", "\tAx=%.2f g" %acceleration[0], "\tAy=%.2f g" %acceleration[1], "\tAz=%.2f g" %acceleration[2]) 	
#     sleep(1)
