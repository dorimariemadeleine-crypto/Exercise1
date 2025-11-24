# A small helper function
def calculate_completion_rate(done, total):
    if total == 0:
        return 0
    else:
        return (done / total) * 100


# Daily Planner class
class DailyPlanner:
    def __init__(self, name, city, color, age):
        # Save basic information
        self.name = name
        self.city = city
        self.color = color
        self.age = age
        self.tasks = []      # List of tasks
        self.summary = {}    # Summary info

    def add_task(self, task, status="pending"):
        self.tasks.append((task, status))

    def complete_task(self, task_name):
        for i, (task, status) in enumerate(self.tasks):
            if task == task_name:
                self.tasks[i] = (task, "done")
                break
        else:
            print(f"Task '{task_name}' not found.")

    def show_tasks(self):
        print("=== Tasks ===")
        for task, status in self.tasks:
            print(f"- {task} [{status}]")

    def make_summary(self, done, left, best_task, energy):
        total = done + left
        rate = calculate_completion_rate(done, total)

        self.summary = {
            "Name": self.name,
            "City": self.city,
            "Favorite color": self.color,
            "Age": self.age,
            "Total tasks": total,
            "Completion rate": f"{rate:.1f}%",
            "Best task": best_task,
            "Energy level": energy
        }

    def show_summary(self):
        print("=== Daily Summary ===")
        for key, value in self.summary.items():
            print(f"- {key}: {value}")


# Main program
print("Welcome to the Daily Planner!")

name = input("What is your name? ")
if name == "":
    print("No name entered. I will use 'Guest'.")
    name = "Guest"
else:
    print(f"Hello {name}!")

city = input("Which city are you in now? ")
color = input("What is your favorite color? ")

# Age with validation
while True:
    try:
        age = int(input("How old are you? "))
        if age <= 0:
            print("Age must be positive.")
        else:
            break
    except ValueError:
        print("Please enter a number for age.")

# Create planner
planner = DailyPlanner(name, city, color, age)

# Sleep hours
hours = float(input("How many hours did you sleep last night? "))
print(f"That is {hours * 60} minutes of sleep.")

# Daily performance
done = int(input("How many tasks did you finish today? "))
left = int(input("How many tasks are still left? "))
best_task = input("Which task was most rewarding? ")
energy = int(input("Rate your energy today (1 to 10): "))

# Add tasks
planner.add_task("Study Python")
planner.add_task("Finish report")
planner.complete_task("Study Python")

# Make and show summary
planner.make_summary(done, left, best_task, energy)
planner.show_tasks()
planner.show_summary()

# More questions
hours_productive = float(input("How many productive hours today? "))
minutes_learning = int(input("Minutes spent learning something new? "))
gratitude = input("One thing you are grateful for today: ")

# Calculate tasks per hour
if hours_productive == 0:
    tasks_per_hour = done / 1.0
else:
    tasks_per_hour = done / hours_productive

print(f"You did about {tasks_per_hour:.2f} tasks per productive hour.")
print(f"You spent {minutes_learning} minutes learning and felt thankful for {gratitude}.")
print("Thanks for using the Daily Planner!")
