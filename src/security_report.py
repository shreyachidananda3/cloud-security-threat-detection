import json

EVENTS_FILE = "data/security_events.json"


def load_events():
    with open(EVENTS_FILE, "r") as file:
        return json.load(file)


def analyze_events(events):
    failed_logins = 0
    permission_changes = 0

    for event in events:
        if event["event"] == "login_failed":
            failed_logins += 1
        elif event["event"] == "permission_change":
            permission_changes += 1

    threats = 0
    severity_levels = []

    if failed_logins >= 3:
        threats += 1
        severity_levels.append("HIGH")

    if permission_changes > 0:
        threats += permission_changes
        severity_levels.append("MEDIUM")

    return {
        "total_events": len(events),
        "failed_logins": failed_logins,
        "permission_changes": permission_changes,
        "threats_detected": threats,
        "severity_levels": severity_levels
    }


def generate_report(summary):
    print("\n==============================================")
    print("       CLOUD SECURITY ASSESSMENT REPORT")
    print("==============================================\n")

    print(f"Total Security Events: {summary['total_events']}")
    print(f"Failed Login Attempts: {summary['failed_logins']}")
    print(f"Permission Changes: {summary['permission_changes']}")
    print(f"Threats Detected: {summary['threats_detected']}")

    print("\nSeverity Levels:")
    for level in summary["severity_levels"]:
        print(f"- {level}")

    print("\nSecurity Recommendations:")

    if summary["failed_logins"] >= 3:
        print("- Investigate repeated failed login attempts.")
        print("- Review the affected account and source IP.")

    if summary["permission_changes"] > 0:
        print("- Review recent permission changes.")
        print("- Verify that administrative changes were authorized.")

    print("\n==============================================")


def main():
    events = load_events()
    summary = analyze_events(events)
    generate_report(summary)


if __name__ == "__main__":
    main()
