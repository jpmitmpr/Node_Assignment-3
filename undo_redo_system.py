class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value

    def peek(self):
        return self.top.value if self.top else None

    def print_stack(self):
        current = self.top
        if not current:
            print("(empty)")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":  # Perform Action
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo stack
            print(f"Action performed: {action}")

        elif choice == "2":  # Undo
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo.")

        elif choice == "3":  # Redo
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo.")

        elif choice == "4":  # View Undo Stack
            print("Undo Stack:")
            undo_stack.print_stack()

        elif choice == "5":  # View Redo Stack
            print("Redo Stack:")
            redo_stack.print_stack()

        elif choice == "6":  # Exit
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run_undo_redo()