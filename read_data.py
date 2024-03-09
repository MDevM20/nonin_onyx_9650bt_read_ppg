
import serial
import csv
import datetime
import argparse


parser=argparse.ArgumentParser(description="Read Nonin DATA from Serial Port")
parser.add_argument("port",help="Serial Port Name", default="COM6", type=str)
args=parser.parse_args()
port=args.port

# Message format for selecting the desired data - max resolution waveform
msg_sel_format = bytes([0x02,0x70,0x02,0x02,0x07, 0x03])
# Serial port configuration

baudrate = 9600

def check_crc(data, start_byte):
    return data[start_byte+4] == (data[start_byte]+data[start_byte+1]+data[start_byte+2]+data[start_byte+3])%256

def find_next_frame(data, start_byte):
    for i in range(start_byte, len(data) - 5):
        if check_crc(data, i):
            return i
    return -1


def decode_frame(data):
    record = {}
    record['waveform'] = (int)(data[1])*256 + (int)(data[2])
    return record
    

def decode_nonin_7(data):
    waveform = []
    start_byte = find_next_frame(data, 0)

    for i in range(start_byte, len(data) - 5, 5):
        if check_crc(data, i):
            waveform.append(decode_frame(data[i:i+5])['waveform'])
    return waveform


ser = serial.Serial(port, baudrate)
ser.write(msg_sel_format)
ser.flush()

fieldnames = ["time", "waveform"]
file_name = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S.csv")

with open(file_name, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames,lineterminator='\n')
    csv_writer.writeheader()

print('Connection established. Writing data to:', file_name)
print ('\nPress Ctrl+C to stop')
timestamp = 0.0
while True:
    try:
        with open(file_name, 'a') as csv_file:
            data = ser.readline()
            if data:
                wave_data = decode_nonin_7(data)
                for value in wave_data:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames,lineterminator='\n')
                    info = {
                        "time": timestamp,
                        "waveform": value
                    }
                    csv_writer.writerow(info)
                    timestamp = timestamp + 1.0/75
            

    except KeyboardInterrupt:
      ser.close()
      print('Exiting...')
      break