import csv

class AuditGroup:
    def __init__(self):
        self.audit_list = self.read_audit_list()

    def read_audit_list(self):
        audit_list = []
        try:
            with open('Audit_List.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    audit_list.append(row)
        except FileNotFoundError:
            print("Audit_List.csv file not found.")
        return audit_list

    def display_audit_numbers(self):
        if not self.audit_list:
            print("No audits available.")
            return

        print("Available audits:")
        for audit in self.audit_list:
            print(f"Audit Number: {audit['Audit_Number']}, Audit Name: {audit['Audit_Name']}")

    def create_group(self):
        self.display_audit_numbers()
        if not self.audit_list:
            return

        audit_number = self.get_valid_audit_number()
        group_members = input("Enter group members (comma separated): ").split(',')

        # Updating the Audit List with group members
        self.update_audit_group(audit_number, group_members)

    def get_valid_audit_number(self):
        while True:
            audit_number = input("Enter audit number: ")
            if any(audit['Audit_Number'] == audit_number for audit in self.audit_list):
                return audit_number
            else:
                print("Wrong audit number. Please try again.")

    def update_audit_group(self, audit_number, group_members):
        updated_audit_list = []
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    row['Audit_Group'] = group_members
                updated_audit_list.append(row)

        with open('Audit_List.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=updated_audit_list[0].keys())
            writer.writeheader()
            writer.writerows(updated_audit_list)
        print(f"Audit group for audit number {audit_number} updated successfully.")
