# Fault Analysis of Power System
# Simple educational simulation

import math


class FaultAnalysis:

    def __init__(self, voltage_kv, impedance_percent):
        self.voltage_kv = voltage_kv
        self.impedance_percent = impedance_percent

    def base_impedance(self):
        # Zbase = V^2 / S
        # For this simple model, assume 10 MVA base
        base_mva = 10

        z_base = (self.voltage_kv ** 2) / base_mva
        return z_base

    def fault_impedance(self):
        z_base = self.base_impedance()

        # Convert percentage impedance to actual impedance
        z_fault = (self.impedance_percent / 100) * z_base

        return z_fault

    def three_phase_fault(self):
        # I = V / (sqrt(3) * Z)
        voltage = self.voltage_kv * 1000
        impedance = self.fault_impedance()

        current = voltage / (math.sqrt(3) * impedance)

        return current

    def single_line_ground_fault(self):
        # Simplified educational calculation
        # Assume equal sequence impedances
        current = self.three_phase_fault() * 0.577

        return current

    def line_to_line_fault(self):
        # Simplified educational calculation
        current = self.three_phase_fault() * 0.866

        return current

    def display_results(self):
        z_base = self.base_impedance()
        z_fault = self.fault_impedance()

        three_phase = self.three_phase_fault()
        single_line = self.single_line_ground_fault()
        line_line = self.line_to_line_fault()

        print("\n======================================")
        print("     POWER SYSTEM FAULT ANALYSIS")
        print("======================================")

        print(f"System Voltage       : {self.voltage_kv:.2f} kV")
        print(f"System Impedance     : {self.impedance_percent:.2f} %")
        print(f"Base Impedance       : {z_base:.4f} Ohm")
        print(f"Fault Impedance      : {z_fault:.4f} Ohm")

        print("\nFault Currents")
        print("--------------------------------------")

        print(
            f"3-Phase Fault       : "
            f"{three_phase:.2f} A"
        )

        print(
            f"Line-to-Line Fault  : "
            f"{line_line:.2f} A"
        )

        print(
            f"Single Line-Ground  : "
            f"{single_line:.2f} A"
        )

        print("\nAnalysis Status      : COMPLETED")


# Main Program

print("===== Fault Analysis of Power System =====")

voltage = float(input("Enter system voltage (kV): "))
impedance = float(
    input("Enter system impedance (%): ")
)

if voltage <= 0 or impedance <= 0:
    print("Invalid input values!")
else:
    analysis = FaultAnalysis(
        voltage,
        impedance
    )

    analysis.display_results()
