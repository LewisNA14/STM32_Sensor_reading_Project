# BMP280 Sensor Reader / Visualiser

## Overview
The goal of this project was to read temperature and pressure data from a BMP280 sensor using an STM32 Nucleo-F334R8 and then visualise the readings on a PC.
A Python script receives the UART output, removes unnecessary formatting, extracts timestamps/temperature/pressure values, and either:

- plots them live on a graph, or
- logs/appends them into a .csv file for later analysis.

This project combines embedded programming, data parsing, and basic data visualisation.

### Hardware Used
- STM32 NUCLEO-F334R8 Development Board
- BMP280 Pressure and Temperature sensor (I2C)
- 4x Jumper Wires
- Breadboard
- USB-Mini B Cable

#### Wiring Diagram
| BMP280 Pin | Nucleo Pin     |
| ---------- | -------------- |
| **VCC**    | 3.3V           |
| **GND**    | GND            |
| **SCL**    | PB8 (I2C1_SCL) |
| **SDA**    | PB9 (I2C1_SDA) |


### Software Requirements
- STM32CubeIDE version 1.19
- HAL / LL drivers
- PuTTy

## Aims
Beyond building the BMP280 reader/visualiser, the project was designed to develop some practical engineering skills:
1. Improving C and Python ability through embedded code + scripting.
2. Learning to interface with an I2C sensor via external libraries
3. Configuring STM32 peripherals such as clocks, GPIOs, and I2C.
4. Gaining familiarity with the STM Cube IDE / MX
5. Practising real-hardware debugging (breakpoints, logic errors, communication issues).
6. Developing confidence wiring components together on a breadboard.

## Contacts
**Email:** lewisnich01@outlook.com

**LinkedIn:** www.linkedin.com/in/lewis-nicholson-a-435670242
