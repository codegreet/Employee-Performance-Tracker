# Employee Performance Tracker (Quick Task Version)

employees = [
    {"name": "John Doe", "completed_tasks": 10, "incomplete_tasks": 2, "bugged_tasks": 1},
    {"name": "Jane Smith", "completed_tasks": 8, "incomplete_tasks": 1, "bugged_tasks": 3},
    {"name": "Alice Johnson", "completed_tasks": 12, "incomplete_tasks": 3, "bugged_tasks": 0},
    {"name": "Bob Brown", "completed_tasks": 7, "incomplete_tasks": 2, "bugged_tasks": 4}
]

# Calculate performance score
for emp in employees:
    emp["score"] = (emp["completed_tasks"] * 5) - (emp["incomplete_tasks"] * 2) - (emp["bugged_tasks"] * 3)

# Sort by score and assign rank
employees_sorted = sorted(employees, key=lambda x: x["score"], reverse=True)
for i, emp in enumerate(employees_sorted, start=1):
    emp["rank"] = i

# Display results
print("Rank  Name             Score")
for emp in employees_sorted:
    print(f"{emp['rank']:<5} {emp['name']:<15} {emp['score']}")