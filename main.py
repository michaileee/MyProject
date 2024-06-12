from audit_register import AuditRegister
from create_audit_group import AuditGroup
from audit_planning import AuditPlanning
from work_process import WorkProcess
from reporting import Reporting

def main():
    audit_register = AuditRegister()
    audit_group = AuditGroup()
    audit_planning = AuditPlanning()
    work_process = WorkProcess()
    reporting = Reporting()

    while True:
        try:
            choice = input(''' ::::::Audit Process Management ::::::: 
            1. Register Audit
            2. Create Audit Group
            3. Plan Audit
            4. Process Audit Work
            5. Generate Report
            6. Exit
            Choose Option: ''')

            if choice == '1':
                audit_register.register_audit()
            elif choice == '2':
                audit_group.create_group()
            elif choice == '3':
                audit_planning.plan_audit()
            elif choice == '4':
                work_process.process_work()
            elif choice == '5':
                reporting.generate_report()
            elif choice == '6':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
