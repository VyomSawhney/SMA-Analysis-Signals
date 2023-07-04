import csv
import os

def calculate_total(df):
    total = 0
    with open(df, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if len(rows) < 2:
            return total

        start_index = 0 if rows[0]['Signal'] == 'Long' else 1
        for i in range(start_index, len(rows), 2):
            current_open = float(rows[i]['Open'])
            if i + 1 < len(rows):
                next_open = float(rows[i + 1]['Open'])
            else:
                break

            if rows[i]['Signal'] == 'Short':
                total += next_open - current_open
            else:
                total += current_open - next_open

    return round(total, 2)

def calculate_average(df):
    total_open = 0
    count = 0
    with open(df, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_open += float(row['Open'])
            count += 1

    if count == 0:
        return 0

    average = total_open / count
    return round(average, 2)

file_name = input("Enter the CSV file name: ")

if not file_name.endswith('.csv'):
    file_name += '.csv'

if not os.path.exists(file_name):
    raise FileNotFoundError("The specified file does not exist.")


total = calculate_total(file_name)
average = calculate_average(file_name)

percent_difference = 100 * (total - average) / average if average != 0 else 0

print('Total:', total)
print('Average:', average)
print('Percent Difference:', round(percent_difference, 2), '%')