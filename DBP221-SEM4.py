import numpy as np
import pandas as pd

# 1. 50-100 хүртэл тоон утга бүхий нэг хэмжээст массив (вектор) үүсгэ.
array1 = np.arange(50, 101)

# 2. Арван ширхэг 1, арван ширхэг 0, арван ширхэг 6 тоо бүхий нэг хэмжээст массивууд (вектор) үүсгэ.
array2 = np.array([1, 0, 6] * 10)

# 3. 20-32 хүртэл тоон утга бүхий 3x4 хэмжээтэй массив үүсгэ.
array3 = np.arange(20, 33).reshape(3, 4)

# 4. Диагональ нь 1-ийн тоо, бусад нь 0 байх 3x3 хэмжээтэй массив үүсгэ.
array4 = np.eye(3)

# 5. Диагональ нь 1-5 хүртэл тоо, бусад нь 0 байх 5x5 хэмжээтэй массив үүсгэ.
array5 = np.diag(np.arange(1, 6))

# 6. Хоёр хэмжээст массив үүсгэж нийт элементүүдийн нийлбэр, багана, мөрийн нийлбэрийг хэвлэ.
total_elements = array1.size + array2.size
shape_array1 = array1.shape
shape_array2 = array2.shape

# 7. Спортын сайтуудын мэдээллийг ашиглан хөл бөмбөгийн спортын дурын 10 тоглогчийн сүүлийн арван жилийн цалин, нийт тоглолт, оруулсан гоалуудын талаар мэдээллийг цуглуулж тус бүрээр массив үүсгэ.
sports_data = {
    "Player Names": ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"],
    "Last 10 Years Salary": [1000000, 1500000, 800000, 2000000, 1200000, 2500000, 900000, 1800000, 700000, 3000000],
    "Total Games Played": [200, 220, 180, 240, 190, 260, 210, 230, 170, 250],
    "Goals Scored": [150, 180, 120, 200, 160, 220, 140, 175, 110, 230]
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(sports_data)

# Calculate statistics for each attribute
average_salary = df["Last 10 Years Salary"].mean()
max_games_played = df["Total Games Played"].max()
min_goals_scored = df["Goals Scored"].min()

# Print the results
print("1. Vector of numbers (50-100):\n", array1)
print("\n2. Vector of numbers (1, 0, 6):\n", array2)
print("\n3. 3x4 Matrix (20-32):\n", array3)
print("\n4. 3x3 Matrix (Diagonal 1s):\n", array4)
print("\n5. 5x5 Matrix (Diagonal 1-5):\n", array5)
print("\n6. Total Elements in array1 and array2:", total_elements)
print("   Shape of array1:", shape_array1)
print("   Shape of array2:", shape_array2)

print("\n7. Sports Data DataFrame:\n", df)
print("\n   Average Salary for All Players:", average_salary)
print("   Maximum Games Played by a Player:", max_games_played)
print("   Minimum Goals Scored by a Player:", min_goals_scored)

# Create a NumPy array from the dictionary values
sports_array = np.array(list(sports_data.values()))

# Calculate the sum of salaries, total games played, and goals scored for each player
sum_salaries = sports_array[1].sum(axis=1)
sum_total_games = sports_array[2].sum(axis=1)
sum_goals_scored = sports_array[3].sum(axis=1)

# Print the results
print("Sports Data Array:\n", sports_array)
print("Sum of Salaries for Each Player:\n", sum_salaries)
print("Sum of Total Games Played for Each Player:\n", sum_total_games)
print("Sum of Goals Scored for Each Player:\n", sum_goals_scored)