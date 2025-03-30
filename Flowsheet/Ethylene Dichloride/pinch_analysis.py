import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Unit': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
    'Heat Duty (kW)': [40.01, 30.16, 14.86, -1720.29, 0.70, 11.51, 449.75]
}

df = pd.DataFrame(data)

Heating_system = df[df['Heat Duty (kW)'] > 0]
Cooling_system = df[df['Heat Duty (kW)'] < 0]

# Plot Pinch Analysis
plt.figure(figsize=(8,5))
plt.bar(Heating_system['Unit'], Heating_system['Heat Duty (kW)'], color='red', label='Heating System')
plt.bar(Cooling_system['Unit'], Cooling_system['Heat Duty (kW)'], color='blue', label='Cooling System')
plt.axhline(0, color='black', linewidth=1)
plt.xlabel("Unit Operasi")
plt.ylabel("Heat Duty (kW)")
plt.title("Pinch Analysis - Heat Integration")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Energy Efficiency
Heating_energy = Heating_system['Heat Duty (kW)'].sum()
Cooling_energy = abs(Cooling_system['Heat Duty (kW)'].sum())
Efficiency = Heating_energy / Cooling_energy * 100

print(f"Total Energi Pemanas: {Heating_energy:.2f} kW")
print(f"Total Energi Pendingin: {Cooling_energy:.2f} kW")
print(f"Efisiensi Pemanfaatan Energi: {Efficiency:.2f}%")
