tasks = []

for i in range(1, 4):
    task = input(f"Enter task {i}: ")
    tasks.append(task)

print("\nYour tasks for today:")
for t in tasks:
    print(f"- {t}")
