import socket
import serial
import sys
import time

TCP_IP = 'localhost' #GANTI IP JURI (COACH)
TCP_PORT = 28097

print "Bismillah... Run Saitama, RUN!!!"
print "Loading, wait for 5 seconds."

try:
    BUFFER_SIZE = 1024
    MESSAGE = "Saitama"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
except:
    print "Error, Check COACH IP."
    sys.exit(-1)
    
print "Coach Mode = Success"


try:
    global ser
    ser = serial.Serial('COM3', 9600) #Ganti COM BLUETOOTH
except:
    print "Gagal Koneksi Ke Saitama. Ulangi Lagi."
    global ser
    ser = serial.Serial('COM3', 9600) #Ganti COM BLUETOOTH
    ser.open()
    time.sleep(1)
    ser.close()
    ser.disconnect()
    sys.exit(-1)



print "Berhasil Konek Ke Saitama Robot."

print "Menunggu Data Juri"

#s.close() #close UDP

while 1:
    data = s.recv(BUFFER_SIZE)
    print "Data:", data
    if data == 'S':
        ser.write("R")
    if data == 'k':
        ser.write("L")

