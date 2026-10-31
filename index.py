class SmartSwitchMonitor:
    # Device mapping: Bit position -> Device Name
    DEVICES = {
        0: "Living Room Light",
        1: "Ceiling Fan",
        2: "Air Conditioner",
        3: "Kitchen Refrigerator",
        4: "Water Heater",
        5: "Porch Light",
        6: "Security Alarm",
        7: "Smart TV",
    }

    def __init__(self, initial_state: int = 0b00000000):
        self.state = initial_state & 0xFF  # Constrain to 8 bits

    def display_status(self):
        """Displays formatted binary, hex, and the individual device states."""
        binary_str = f"{self.state:08b}"
        print(f"\n{'='*45}")
        print(f"Current State: 0b{binary_str} | Decimal: {self.state} | Hex: 0x{self.state:02X}")
        print(f"{'='*45}")
        print(f"{'Bit':<4} | {'Status':<6} | {'Device Name'}")
        print(f"{'-'*45}")
        for bit, name in self.DEVICES.items():
            # Check bit status using bitwise AND with a mask (1 << bit)
            is_on = bool(self.state & (1 << bit))
            status = "ON [1]" if is_on else "OFF [0]"
            print(f"{bit:<4} | {status:<6} | {name}")
        print(f"{'='*45}\n")

    def turn_on(self, bit: int):
        """Turns ON a switch using Bitwise OR (|)."""
        mask = 1 << bit
        self.state |= mask
        print(f"-> Turned ON: {self.DEVICES.get(bit, 'Unknown')} (Mask: 0b{mask:08b})")

    def turn_off(self, bit: int):
        """Turns OFF a switch using Bitwise AND (&) with inverted mask (~)."""
        mask = 1 << bit
        self.state &= ~mask
        print(f"-> Turned OFF: {self.DEVICES.get(bit, 'Unknown')} (Mask: ~0b{mask:08b})")

    def toggle(self, bit: int):
        """Toggles a switch state using Bitwise XOR (^)."""
        mask = 1 << bit
        self.state ^= mask
        print(f"-> Toggled: {self.DEVICES.get(bit, 'Unknown')} (Mask: 0b{mask:08b})")

    def inspect_mask(self, mask: int):
        """Checks if all specified mask bits are active simultaneously."""
        print(f"\nChecking mask 0b{mask:08b} against current state 0b{self.state:08b}:")
        all_match = (self.state & mask) == mask
        any_match = (self.state & mask) != 0
        print(f" - Are ALL mask switches ON? {'Yes' if all_match else 'No'}")
        print(f" - Is AT LEAST ONE mask switch ON? {'Yes' if any_match else 'No'}")


# ----------------------------------------------------
# Example Classroom Walkthrough
# ----------------------------------------------------
if __name__ == "__main__":
    # Start with Living Room Light (bit 0) and Smart TV (bit 7) ON: 0b10000001 (129)
    monitor = SmartSwitchMonitor(0b10000001)
    monitor.display_status()

    # 1. Turn ON the Air Conditioner (bit 2) using bitwise OR
    monitor.turn_on(2)

    # 2. Toggle the Living Room Light (bit 0) using bitwise XOR
    monitor.toggle(0)

    # 3. Turn OFF the Smart TV (bit 7) using bitwise AND NOT
    monitor.turn_off(7)

    # Display updated state
    monitor.display_status()

    # 4. Use a bitmask to check if Climate Control (Fan [1] & AC [2]) is running
    climate_mask = (1 << 1) | (1 << 2)  # 0b00000110
    monitor.inspect_mask(climate_mask)