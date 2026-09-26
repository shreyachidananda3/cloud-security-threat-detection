import json

USERS_FILE = "data/users.json"


def load_users():
    with open(USERS_FILE, "r") as file:
        return json.load(file)


def check_access(users, username, permission):
    for user in users:
        if user["username"] == username:
            if permission in user["permissions"]:
                return "ALLOWED"
            return "DENIED"

    return "USER NOT FOUND"


def main():
    users = load_users()

    access_requests = [
        ("shreya", "read_logs"),
        ("shreya", "change_permissions"),
        ("admin", "change_permissions"),
        ("guest", "view_reports"),
        ("guest", "manage_users")
    ]

    print("\n=== IAM ACCESS CONTROL SIMULATION ===\n")

    for username, permission in access_requests:
        result = check_access(users, username, permission)

        print(f"User: {username}")
        print(f"Requested Permission: {permission}")
        print(f"Access: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()
