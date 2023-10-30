#!/usr/bin/python3

csv_filename = f"{user_id}.csv"

with open(csv_filename, mode='w', newline='') as csv_file:
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header row to the CSV file
    writer.writeheader()

    # Fetch tasks and write them to the CSV file
    tasks = fetch_employee_tasks(user_id)  # You should implement the fetch_employee_tasks function
    for task in tasks:
        writer.writerow({
            "USER_ID": user_id,
            "USERNAME": task["username"],
            "TASK_COMPLETED_STATUS": str(task["completed"]),
            "TASK_TITLE": task["title"]
        })

print(f"Data has been exported to {csv_filename}")
