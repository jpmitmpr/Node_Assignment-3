from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_value

    def peek(self):
        return self.front.value if self.front else None

    def print_queue(self):
        current = self.front
        if not current:
            print("(empty)")
            return
        print("Waiting customers:")
        while current:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"Helped: {customer}")
            else:
                print("No customers to help.")

        elif choice == "3":
            customer = queue.peek()
            if customer:
                print(f"Next customer: {customer}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            queue.print_queue()

        elif choice == "5":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
