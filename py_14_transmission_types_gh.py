#!/usr/bin/env python3
"""
Chapter 14: Transmission Types (Asynchronous vs Synchronous)
Demonstrates different data transmission timing methods
"""

import time

def visualize_asynchronous_transmission(data_byte):
    """Visualize asynchronous transmission with start and stop bits"""
    print(f"\nAsynchronous Transmission of: {data_byte}")
    print("\nFrame structure:")
    print("START | D0 D1 D2 D3 D4 D5 D6 D7 | STOP")
    print("  0   | " + " ".join(data_byte) + "  |  1")
    print("\nTiming diagram:")
    print("      ┌──┐ ┌──┐    ┌──┐       ┌──────")
    print("      │  │ │  │    │  │       │")
    print("──────┘  └─┘  └────┘  └───────┘")
    print("START  Data bits...      STOP")
    
    total_bits = 1 + len(data_byte) + 1  # Start + Data + Stop
    print(f"\nTotal bits transmitted: {total_bits} (1 start + 8 data + 1 stop)")
    print(f"Overhead: {(2/total_bits)*100:.1f}%")

def visualize_synchronous_transmission(data_bytes):
    """Visualize synchronous transmission with clock"""
    print(f"\nSynchronous Transmission:")
    print(f"Data: {' '.join(data_bytes)} (continuous)")
    
    print("\nClock:  ▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁")
    
    data_line = "Data:   "
    for byte in data_bytes:
        for bit in byte:
            if bit == '1':
                data_line += "▄▄"
            else:
                data_line += "▁▁"
    
    print(data_line)
    print("\nNo start/stop bits - clock provides timing")
    print(f"Data bytes: {len(data_bytes)}")
    print(f"Total bits: {len(data_bytes) * 8}")

def calculate_transmission_efficiency(data_bits, overhead_bits):
    """Calculate transmission efficiency"""
    total = data_bits + overhead_bits
    efficiency = (data_bits / total) * 100
    return efficiency

def compare_transmission_methods(num_bytes):
    """Compare async vs sync transmission efficiency"""
    print(f"\nTransmitting {num_bytes} bytes:")
    
    # Asynchronous: 1 start + 8 data + 1 stop per byte
    async_data_bits = num_bytes * 8
    async_overhead = num_bytes * 2  # 2 bits overhead per byte
    async_total = async_data_bits + async_overhead
    async_efficiency = calculate_transmission_efficiency(async_data_bits, async_overhead)
    
    print(f"\nAsynchronous:")
    print(f"  Data bits:     {async_data_bits}")
    print(f"  Overhead bits: {async_overhead} (start + stop bits)")
    print(f"  Total bits:    {async_total}")
    print(f"  Efficiency:    {async_efficiency:.1f}%")
    
    # Synchronous: minimal overhead (just sync patterns at start)
    sync_data_bits = num_bytes * 8
    sync_overhead = 16  # Example: 16-bit sync pattern for entire transmission
    sync_total = sync_data_bits + sync_overhead
    sync_efficiency = calculate_transmission_efficiency(sync_data_bits, sync_overhead)
    
    print(f"\nSynchronous:")
    print(f"  Data bits:     {sync_data_bits}")
    print(f"  Overhead bits: {sync_overhead} (sync pattern)")
    print(f"  Total bits:    {sync_total}")
    print(f"  Efficiency:    {sync_efficiency:.1f}%")
    
    print(f"\nDifference: {sync_efficiency - async_efficiency:.1f}% more efficient")

def main():
    print("=" * 60)
    print("CHAPTER 14: Transmission Types")
    print("Asynchronous vs Synchronous Transmission")
    print("=" * 60)
    
    # Example 1: Asynchronous Transmission
    print("\n--- Example 1: Asynchronous Transmission ---")
    print("\nCharacteristics:")
    print("  • Each byte transmitted independently")
    print("  • Start bit signals beginning of byte")
    print("  • Stop bit(s) signal end of byte")
    print("  • No separate clock signal")
    print("  • Sender and receiver use agreed baud rate")
    print("  • Small gaps allowed between bytes")
    
    data_byte = "01000001"  # 'A' in ASCII
    visualize_asynchronous_transmission(data_byte)
    
    # Example 2: Asynchronous Frame Format
    print("\n--- Example 2: Asynchronous Frame Details ---")
    print("\nStandard UART frame format:")
    print("  1. Start bit:    Always 0 (marks beginning)")
    print("  2. Data bits:    5-9 bits (usually 8)")
    print("  3. Parity bit:   Optional (for error checking)")
    print("  4. Stop bit(s):  1 or 2 bits, always 1")
    
    print("\nExample: 8N1 (8 data, No parity, 1 stop)")
    print("  ┌─────────────────────────────────┐")
    print("  │ 0 │ D0 D1 D2 D3 D4 D5 D6 D7 │ 1 │")
    print("  └─────────────────────────────────┘")
    print("  Start      8 data bits        Stop")
    
    # Example 3: Synchronous Transmission
    print("\n--- Example 3: Synchronous Transmission ---")
    print("\nCharacteristics:")
    print("  • Continuous stream of data")
    print("  • Separate clock signal for timing")
    print("  • No start/stop bits per byte")
    print("  • Sender and receiver synchronized by clock")
    print("  • More efficient for large data blocks")
    print("  • Requires clock line or embedded clock")
    
    data_bytes = ["10101010", "11001100", "00110011"]
    visualize_synchronous_transmission(data_bytes)
    
    # Example 4: Clock Synchronization
    print("\n--- Example 4: Clock Synchronization ---")
    print("\nSynchronous transmission methods:")
    print("\n1. Separate Clock Line:")
    print("   Clock: ▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁")
    print("   Data:  ▄▄▁▁▄▁▁▁▄▁▄▄▁▁▄▄")
    print("   (Used in SPI, I2C)")
    
    print("\n2. Embedded Clock (Manchester encoding):")
    print("   Signal encodes both clock and data")
    print("   (Used in Ethernet)")
    
    print("\n3. Phase-Locked Loop (PLL):")
    print("   Receiver extracts clock from data transitions")
    print("   (Used in USB, SATA)")
    
    # Example 5: Efficiency Comparison
    print("\n--- Example 5: Transmission Efficiency ---")
    compare_transmission_methods(1)
    print()
    compare_transmission_methods(100)
    
    # Example 6: Real-world Protocols
    print("\n--- Example 6: Common Protocols ---")
    
    print("\nAsynchronous Protocols:")
    protocols_async = [
        ("UART/RS-232", "Serial communication, modems"),
        ("RS-485", "Industrial control systems"),
        ("MIDI", "Musical instrument digital interface")
    ]
    
    for protocol, use in protocols_async:
        print(f"  • {protocol:12s} - {use}")
    
    print("\nSynchronous Protocols:")
    protocols_sync = [
        ("SPI", "High-speed peripheral communication"),
        ("I2C", "Inter-chip communication"),
        ("USB", "Universal Serial Bus"),
        ("Ethernet", "Network communication"),
        ("SATA", "Storage device interface")
    ]
    
    for protocol, use in protocols_sync:
        print(f"  • {protocol:12s} - {use}")
    
    # Example 7: Advantages and Disadvantages
    print("\n--- Example 7: Comparison Summary ---")
    
    print("\nAsynchronous Transmission:")
    print("  Advantages:")
    print("    ✓ Simple implementation")
    print("    ✓ No clock synchronization needed")
    print("    ✓ Flexible timing between bytes")
    print("    ✓ Good for sporadic data")
    
    print("  Disadvantages:")
    print("    ✗ Lower efficiency (overhead per byte)")
    print("    ✗ Limited speed")
    print("    ✗ More susceptible to timing errors")
    
    print("\nSynchronous Transmission:")
    print("  Advantages:")
    print("    ✓ Higher efficiency (less overhead)")
    print("    ✓ Faster data rates")
    print("    ✓ Better for continuous data streams")
    print("    ✓ More reliable timing")
    
    print("  Disadvantages:")
    print("    ✗ Requires clock synchronization")
    print("    ✗ More complex hardware")
    print("    ✗ Extra clock line or encoding overhead")
    
    # Example 8: Timing Diagram Comparison
    print("\n--- Example 8: Timing Comparison ---")
    
    print("\nAsynchronous (UART) - sending 'AB':")
    print("Idle  Start Data    Stop Idle Start Data    Stop Idle")
    print("─────┐    ┌────────┐    ┌────┐    ┌────────┐    ┌─────")
    print("     └────┘        └────┘    └────┘        └────┘")
    print("      0  01000001   1         0  01000010   1")
    print("         'A' (65)                'B' (66)")
    
    print("\nSynchronous (with clock) - sending 'AB':")
    print("Clock: ▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁▄▁")
    print("Data:  ▁▄▁▁▁▁▁▁▁▄▁▄▁▁▁▁▁▁▄▁▄▁▁▁▁▁▁▄▁")
    print("       0 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0")
    print("       └─────'A'─────┘ └─────'B'─────┘")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Asynchronous: Independent bytes with start/stop bits")
    print("- Synchronous: Continuous stream with clock signal")
    print("- Asynchronous: Flexible, simple, lower efficiency")
    print("- Synchronous: Faster, more efficient, needs sync")
    print("- Choice depends on application requirements")
    print("=" * 60)

if __name__ == "__main__":
    main()
