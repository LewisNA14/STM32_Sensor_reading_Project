import serial
import csv

ser = serial.Serial('COM7', 38400, timeout=1)

with open('sensor_data.csv', 'w', newline='', buffering=1) as csvfile:
    # Write Header of .csv file
    fieldnames = ['Time', 'Temp', 'Pressure']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').rstrip()
                if data:  # skip empty lines
                    # Split CSV manually
                    time_str, temp_str, pres_str = data.split(',')
                    print(f"Time: {time_str}, Temp: {temp_str}°C, Pressure: {pres_str} hPa")
                    
                    # Write to CSV using DictWriter
                    writer.writerow({'Time': time_str, 'Temp': temp_str, 'Pressure': pres_str})
                    csvfile.flush()

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()
