from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        t = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        curr_tasks_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {curr_tasks_len - len(self.tasks)} tasks."

    def view_section(self) -> str:
        tasks_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_details}"




















