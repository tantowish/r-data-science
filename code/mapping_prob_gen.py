import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Define number of rows
n = 300

# Create data for AcademicStress (1-5 scale)
academic_stress = np.random.randint(1, 6, size=n)

# Create data for SelfEsteem (1-5 scale)
self_esteem = np.random.randint(1, 6, size=n)

# Create data for SleepQuality (PSQI index 0-21 scale)
sleep_quality = np.random.randint(0, 22, size=n)

# Introduce missing values by setting them to -1 (~10% missing)
for _ in range(int(0.1 * n)):
    academic_stress[random.randint(0, n-1)] = -1
    self_esteem[random.randint(0, n-1)] = -1
    sleep_quality[random.randint(0, n-1)] = -1

# Introduce inconsistent data (e.g., out of range values for stress and esteem)
academic_stress[random.sample(range(n), 5)] = np.random.randint(6, 10, size=5)
self_esteem[random.sample(range(n), 5)] = np.random.randint(6, 10, size=5)

# Introduce extreme values for SleepQuality
sleep_quality[random.sample(range(n), 5)] = np.random.randint(25, 40, size=5)

# Create a DataFrame
df = pd.DataFrame({
    'AcademicStress': academic_stress,
    'SelfEsteem': self_esteem,
    'SleepQuality': sleep_quality
})

# Save the DataFrame to CSV (comma-separated with integer values)
df.to_csv('dummy_data_sleep_quality_int.csv', index=False)

print("Data dummy (integer only) dengan missing values (-1), data tidak konsisten, dan nilai ekstrem berhasil dibuat dan disimpan sebagai CSV.")