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
                "failed_attempts": count
            })

    for event in events:
        if event["event"] == "permission_change":
            alerts.append({
                "type": "Privilege Change",
                "severity": "MEDIUM",
                "user": event["user"],
                "source_ip": event["source_ip"],
                "resource": event["resource"]
            })

    return alerts


def generate_response(alert):
    if alert["type"] == "Brute Force Login Attempt":
        return "Investigate the source IP and temporarily restrict the affected account."

    if alert["type"] == "Privilege Change":
        return "Verify the permission change and revert it if unauthorized."

    return "Review the event and determine whether further investigation is required."


def main():
    events = load_events()
    alerts = detect_threats(events)

    print("\n=== CLOUD SECURITY MONITORING PIPELINE ===\n")
    print(f"Security events analyzed: {len(events)}")
    print(f"Threats detected: {len(alerts)}\n")

    for number, alert in enumerate(alerts, start=1):
        action = generate_response(alert)

        print(f"Incident {number}")
        print(f"Threat: {alert['type']}")
        print(f"Severity: {alert['severity']}")
        print(f"User: {alert['user']}")
        print(f"Source IP: {alert['source_ip']}")
        print(f"Recommended Response: {action}")
        print("-" * 60)


if __name__ == "__main__":
    main()
