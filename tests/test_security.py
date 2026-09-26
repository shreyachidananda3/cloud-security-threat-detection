import json
import sys

sys.path.append("src")

from threat_detector import detect_threats
from iam_security import check_access
from network_security import check_network_access


def load_events():
    with open("data/security_events.json", "r") as file:
        return json.load(file)


def load_users():
    with open("data/users.json", "r") as file:
        return json.load(file)


def load_rules():
    with open("data/network_rules.json", "r") as file:
        return json.load(file)


def test_threat_detection():
    events = load_events()
    alerts = detect_threats(events)

    assert len(alerts) == 2
    assert alerts[0]["severity"] == "HIGH"
    assert alerts[1]["severity"] == "MEDIUM"


def test_iam_access_control():
    users = load_users()

    assert check_access(users, "shreya", "read_logs") == "ALLOWED"
    assert check_access(users, "shreya", "change_permissions") == "DENIED"
    assert check_access(users, "guest", "manage_users") == "DENIED"


def test_network_security():
    rules = load_rules()

    assert check_network_access(
        rules, "192.168.1.25", 443, "HTTPS"
    ) == "ALLOW"

    assert check_network_access(
        rules, "185.220.101.45", 23, "TELNET"
    ) == "DENY"

    assert check_network_access(
        rules, "185.220.101.45", 3389, "RDP"
    ) == "DENY"


if __name__ == "__main__":
    test_threat_detection()
    test_iam_access_control()
    test_network_security()
    print("All security tests passed successfully.")
