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
    
    # Example usage
    audit_register.register_audit()
    audit_group.create_group()
    audit_planning.plan_audit()
    work_process.process_work()
    reporting.generate_report()

if __name__ == "__main__":
    main()
