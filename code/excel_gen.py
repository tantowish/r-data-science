import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Parameters
num_samples = 215
income_min = 1800000
income_max = 15000000
missing_income_percentage = 0.11  # 11% missing income

# Generate 'jenis_kelamin' with inconsistencies
gender_main = ['L', 'P']  # Most responses
gender_others = ['Laki-Laki', 'Perempuan']  # Inconsistent responses
gender = random.choices(gender_main, k=int(num_samples * 0.85)) + random.choices(gender_others, k=int(num_samples * 0.15))
random.shuffle(gender)  # Shuffle to mix the values
gender = gender[:num_samples]  # Ensure it's exactly 215

# Generate 'usia' with extreme values (e.g., very young or old)
age_normal = np.random.randint(18, 65, size=int(num_samples * 0.95))
age_extreme = np.random.randint(65, 100, size=int(num_samples * 0.05))  # Extreme values
age = np.concatenate((age_normal, age_extreme))
np.random.shuffle(age)  # Shuffle to mix the values
age = age[:num_samples]  # Ensure it's exactly 215

# Function to assign income based on age
def assign_income(age):
    if age < 30:
        return np.random.choice(np.arange(1800000, 12000000, 50000))  # Younger, lower range with 50,000 step
    elif 30 <= age <= 50:
        return np.random.choice(np.arange(5000000, 18000000, 50000))  # Mid-age, mid-range with 50,000 step
    else:
        return np.random.choice(np.arange(8000000, 20000000, 50000))  # Older, higher range with 50,000 step

# Apply the income function to each individual based on their age
income = np.array([assign_income(a) for a in age])

# Generate 'status' column
status = np.random.choice(['Teman', 'Keluarga', 'Tidak Ada Hubungan'], size=num_samples-1)

# Ensure all arrays are of equal length
print(len(gender), len(age), len(income), len(status))

# Create DataFrame
df = pd.DataFrame({
    'jenis_kelamin': gender,
    'usia': age,
    'penghasilan': income,
    'status': status
})

# One-hot encode the 'status' column
status_dummies = pd.get_dummies(df['status'], prefix='status')

# Concatenate the original DataFrame with the one-hot encoded DataFrame
df = pd.concat([df.drop('status', axis=1), status_dummies], axis=1)

# Save to Excel file
file_path = './sample_data.xlsx'
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")
