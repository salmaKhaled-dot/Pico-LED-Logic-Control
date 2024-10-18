# Raspberry Pi Pico LED & Logic Gate Control Simulation

## Overview

This project simulates a system that uses a Raspberry Pi Pico to control a set of LEDs and logic gates, including AND, OR, and NOT gates, through multiplexers and push buttons. The project is designed for simulation on Wokwi, allowing users to interact with the components virtually.

### Features:

- **LED Control**: 8 LEDs are controlled through the Pico's GPIO pins.
- **Logic Gates**: The circuit includes AND, OR, and NOT gates for logical operations.
- **Multiplexers**: Used to switch between inputs and manage logic gate controls.
- **Pushbuttons**: Three pushbuttons provide user input to interact with the system.
- **Slide Switches**: Four switches are used to toggle inputs to the logic gates.

This project is ideal for demonstrating digital logic and basic electronics using the Raspberry Pi Pico.

## Components

1. **Raspberry Pi Pico**: The microcontroller controlling the circuit.
2. **LEDs**: 8 red LEDs connected to the GPIO pins of the Pico.
3. **Pushbuttons**: 3 green pushbuttons for user input (GP16, GP17, GP18).
4. **Logic Gates**: AND, OR, and NOT gates for logical operations.
5. **Multiplexers**: Two 2-to-1 multiplexers to control the input signals.
6. **Slide Switches**: 4 switches used for logic input (connected to the multiplexers).

## Simulation

You can simulate this project on Wokwi, an online platform for hardware simulation. The Wokwi simulation provides an interactive environment where you can observe how pressing buttons and toggling switches affects the state of the LEDs and logic gates.

### Simulate the Project on Wokwi:

[Simulate on Wokwi](https://wokwi.com/projects/394022579727792129)

## How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/pico-led-logic-simulation.git
   ```

2. **Run the Wokwi Simulation**:
   - Visit the simulation link to interact with the project in a virtual environment.
   - Alternatively, you can upload the project files to [Wokwi](https://wokwi.com) and run the simulation.

## Files

- `diagram.json`: Contains the wiring and component setup for the project.
- `main.py`: Contains the MicroPython code for controlling the LEDs and logic gates with the Pico.
- `wokwi-project.txt`: A link to the Wokwi simulation for quick access.
