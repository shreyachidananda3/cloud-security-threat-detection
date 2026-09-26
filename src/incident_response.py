def generate_response(alert):
    if alert["type"] == "Brute Force Login Attempt":
        return {
            "priority": "HIGH",
            "action": "Investigate the source IP and temporarily restrict the affected account."
        }

    if alert["type"] == "Privilege Change":
        return {
            "priority": "MEDIUM",
            "action": "Verify the permission change and revert it if unauthorized."
        }

    return {
        "priority": "LOW",
        "action": "Review the event and determine whether further investigation is required."
    }


def main():
    alerts = [
        {
            "type": "Brute Force Login Attempt",
            "user": "admin",
            "source_ip": "185.220.101.45"
        },
        {
            "type": "Privilege Change",
            "user": "admin",
            "source_ip": "185.220.101.45"
        }
    ]

    print("\n=== INCIDENT RESPONSE ENGINE ===\n")

    for number, alert in enumerate(alerts, start=1):
        response = generate_response(alert)

        print(f"Incident {number}")
        print(f"Threat: {alert['type']}")
        print(f"Priority: {response['priority']}")
        print(f"Recommended Action: {response['action']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
