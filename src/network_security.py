import json
import ipaddress

RULES_FILE = "data/network_rules.json"


def load_rules():
    with open(RULES_FILE, "r") as file:
        return json.load(file)


def check_network_access(rules, source_ip, port, protocol):
    for rule in rules:
        network = ipaddress.ip_network(rule["source"])

        if (
            ipaddress.ip_address(source_ip) in network
            and port == rule["port"]
            and protocol == rule["protocol"]
        ):
            return rule["action"]

    return "DENY"


def main():
    rules = load_rules()

    traffic_requests = [
        ("192.168.1.25", 443, "HTTPS"),
        ("192.168.1.25", 22, "SSH"),
        ("185.220.101.45", 23, "TELNET"),
        ("185.220.101.45", 3389, "RDP"),
        ("185.220.101.45", 443, "HTTPS")
    ]

    print("\n=== NETWORK SECURITY SIMULATION ===\n")

    for source_ip, port, protocol in traffic_requests:
        result = check_network_access(
            rules,
            source_ip,
            port,
            protocol
        )

        print(f"Source IP: {source_ip}")
        print(f"Port: {port}")
        print(f"Protocol: {protocol}")
        print(f"Access: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()
