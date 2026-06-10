import csv


file = open("students.csv", "w")
writer = csv.writer(file)

writer.writerow(["name", "marks"])
writer.writerow(["Ram", 80])
writer.writerow(["Sita", 90])
writer.writerow(["Hari", 75])
writer.writerow(["Gita", 85])

file.close()

print("CSV file created and data written ")


file = open("students.csv", "r")
reader = csv.DictReader(file)

total_marks = 0
count = 0

for row in reader:
    total_marks += float(row["marks"])
    count += 1

file.close()


average = total_marks / count

print("\nTotal Students:", count)
print("Average Marks:", average)