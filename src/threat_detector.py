import json
from collections import Counter

LOG_FILE = "data/security_events.json"


def load_events():
    with open(LOG_FILE, "r") as file:
        return json.load(file)


def detect_threats(events):
    alerts = []

    failed_logins = Counter()

    for event in events:
        if event["event"] == "login_failed":
            key = (event["user"], event["source_ip"])
            failed_logins[key] += 1

    for (user, ip), count in failed_logins.items():
        if count >= 3:
            alerts.append({
                "type": "Brute Force Login Attempt",
                "severity": "HIGH",
                "user": user,
                "source_ip": ip,
                "failed_attempts": count,
                "recommendation": "Investigate the source IP and temporarily restrict the account."
            })

    for event in events:
        if event["event"] == "permission_change":
            alerts.append({
                "type": "Privilege Change",
                "severity": "MEDIUM",
                "user": event["user"],
                "source_ip": event["source_ip"],
                "resource": event["resource"],
                "recommendation": "Review the permission change and verify that it was authorized."
            })

    return alerts


def main():
    events = load_events()
    alerts = detect_threats(events)

    print("\n=== CLOUD SECURITY THREAT DETECTION ===\n")

    print(f"Total security events analyzed: {len(events)}")
    print(f"Threats detected: {len(alerts)}\n")

    if not alerts:
        print("No suspicious activity detected.")
        return

    for number, alert in enumerate(alerts, start=1):
        print(f"Alert {number}")
        print(f"Type: {alert['type']}")
        print(f"Severity: {alert['severity']}")
        print(f"User: {alert['user']}")
        print(f"Source IP: {alert['source_ip']}")

        if "failed_attempts" in alert:
            print(f"Failed attempts: {alert['failed_attempts']}")

        if "resource" in alert:
            print(f"Resource: {alert['resource']}")

        print(f"Recommendation: {alert['recommendation']}")
        print("-" * 50)


if __name__ == "__main__":
    main()