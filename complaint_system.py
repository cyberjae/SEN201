
class Complaint:
    def __init__(self, complaint_id, user_name, description, status="Open"):
        self.complaint_id = complaint_id
        self.user_name = user_name
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "complaint_id": self.complaint_id,
            "user_name": self.user_name,
            "description": self.description,
            "status": self.status
        }


class ComplaintManagementSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file)

    def load_complaints(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_complaints(self, complaints):
        with open(self.file_path, "w") as file:
            json.dump(complaints, file, indent=4)

    def register_complaint(self, user_name, description):
        complaints = self.load_complaints()
        complaint_id = len(complaints) + 1
        complaint = Complaint(complaint_id, user_name, description)
        complaints.append(complaint.to_dict())
        self.save_complaints(complaints)
        print("Complaint registered successfully!")

    def view_complaints(self):
        complaints = self.load_complaints()
        if not complaints:
            print("No complaints found.")
            return

        for c in complaints:
            print("\nComplaint ID:", c["complaint_id"])
            print("User Name:", c["user_name"])
            print("Description:", c["description"])
            print("Status:", c["status"])

    def update_complaint_status(self, complaint_id, new_status):
        complaints = self.load_complaints()
        for c in complaints:
            if c["complaint_id"] == complaint_id:
                c["status"] = new_status
                self.save_complaints(complaints)
                print("Complaint status updated!")
                return
        print("Complaint not found.")


def main():
    system = ComplaintManagementSystem(DATA_FILE)

    while True:
        print("\n--- Online Complaint Management System ---")
        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Update Complaint Status (Admin)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            description = input("Enter complaint description: ")
            system.register_complaint(name, description)

        elif choice == "2":
            system.view_complaints()

        elif choice == "3":
            complaint_id = int(input("Enter complaint ID: "))
            status = input("Enter new status (Open/In Progress/Resolved): ")
            system.update_complaint_status(complaint_id, status)

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
