# ai_monitoring.py
# Demonstrates AI-based anomaly detection in simulated system metrics with colored console output.

import random
import statistics
import time
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def generate_cpu_usage_data(samples=20):
    """Simulate CPU usage percentage readings."""
    return [random.uniform(20, 80) for _ in range(samples)]

def detect_anomaly(data):
    """Detect anomalies using mean ± 2*standard deviation."""
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    threshold_low = mean - 2 * stdev
    threshold_high = mean + 2 * stdev
    anomalies = [x for x in data if x < threshold_low or x > threshold_high]
    return anomalies, mean, stdev

print(Fore.CYAN + Style.BRIGHT + "\n=== AI-Based System Monitoring Simulation ===\n")

for i in range(3):
    time.sleep(1)
    cpu_data = generate_cpu_usage_data()
    anomalies, mean, stdev = detect_anomaly(cpu_data)

    print(Fore.YELLOW + f"Monitoring Cycle {i + 1}")
    print(Fore.WHITE + f"  Average CPU Usage: {mean:.2f}% | Standard Deviation: {stdev:.2f}%")

    if anomalies:
        print(Fore.RED + "  Detected Anomalies:")
        for val in anomalies:
            print(Fore.RED + f"   - Irregular reading: {val:.2f}%")
    else:
        print(Fore.GREEN + "  No anomalies detected. System operating normally.")

    print(Fore.WHITE + "-" * 60)

print(Fore.CYAN + Style.BRIGHT + "\nMonitoring completed successfully.\n")

# Summary:
# AI-based monitoring systems can leverage algorithms such as Isolation Forest, LSTM, or Autoencoders
# to automatically predict and detect unusual system activity patterns.
