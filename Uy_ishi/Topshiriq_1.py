import numpy as np

matrix = np.random.uniform(1.01, 9.99, (10, 10))

mean = np.mean(matrix)
minimum = np.min(matrix)
maximum = np.max(matrix)
median = np.median(matrix)
std_dev = np.std(matrix)
variance = np.var(matrix)

diagonal = np.diagonal(matrix)

print("Massiv:")
print(matrix)
print("\nO'rtacha qiymat:", round(mean, 2))
print("Minimal element:", round(minimum, 2))
print("Maksimal element:", round(maximum, 2))
print("Median:", round(median, 2))
print("Standart og'ish:", round(std_dev, 2))
print("Dispersiya:", round(variance, 2))
print("\nAsosiy diagonal:")
print(np.round(diagonal, 2))