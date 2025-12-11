import serial
import matplotlib.pyplot as plt

# Serial port setup
ser = serial.Serial('COM7', 38400, timeout=1)

# Lists to store incoming data
times = []
temps = []
pressures = []

WINDOW_SIZE = 50  # number of latest points to display

# Initialize plot
plt.ion()
fig, ax = plt.subplots()
temp_line, = ax.plot([], [], color='red', label='Temp')
press_line, = ax.plot([], [], color='blue', label='Pressure')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Values')
ax.set_title('Temp / Pressure Sensor Graph')
ax.legend()

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            if data:
                # Parse CSV line
                time_str, temp_str, press_str = data.split(',')

                # Convert time HH:MM:SS to seconds
                h, m, s = map(int, time_str.split(':'))
                time_sec = h * 3600 + m * 60 + s

                # Convert values to float
                temp_float = float(temp_str)
                press_float = float(press_str)

                # Append to lists
                times.append(time_sec)
                temps.append(temp_float)
                pressures.append(press_float)

                # Keep only last WINDOW_SIZE readings
                times_window = times[-WINDOW_SIZE:]
                temps_window = temps[-WINDOW_SIZE:]
                pressures_window = pressures[-WINDOW_SIZE:]

                # Update plot data
                temp_line.set_data(times_window, temps_window)
                press_line.set_data(times_window, pressures_window)

                # Clear previous text annotations
                for txt in ax.texts:
                    txt.remove()
                # Display current values on plot if there’s at least one point
                if times_window:
                    ax.text(times_window[-1], temps_window[-1], f'{temps_window[-1]:.2f}°C', color='red', fontsize=10)
                    ax.text(times_window[-1], pressures_window[-1], f'{pressures_window[-1]:.2f} hPa', color='blue', fontsize=10)

                # Update legend with current values
                temp_line.set_label(f'Temp: {temps_window[-1]:.2f}°C')
                press_line.set_label(f'Pressure: {pressures_window[-1]:.2f} hPa')
                ax.legend()

                # Rescale axes
                ax.relim()
                ax.autoscale_view()

                # Refresh plot
                plt.pause(0.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
    plt.ioff()
    plt.show()
