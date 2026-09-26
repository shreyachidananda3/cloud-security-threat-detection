# Cloud Security & Threat Detection Platform

A Python-based cloud security simulation that models common cloud security controls and threat detection workflows using AWS-inspired security concepts.

## Project Overview

This project demonstrates how security events can be analyzed, access permissions can be evaluated, network traffic can be checked against security rules, and recommended incident-response actions can be generated.

The project is implemented locally using Python and simulated security data. It does not require a live AWS environment.

## Security Capabilities

### Threat Detection
- Detects repeated failed login attempts
- Identifies potential brute-force activity
- Detects privilege and permission changes
- Assigns severity levels to detected threats

### Identity & Access Management
- Simulates role-based access control
- Evaluates user permissions
- Demonstrates least-privilege access concepts
- Identifies unauthorized permission requests

### Network Security
- Evaluates traffic against predefined network rules
- Allows approved HTTPS and internal SSH traffic
- Blocks insecure Telnet traffic
- Blocks public RDP access
- Denies unmatched network requests by default

### Incident Response
- Classifies detected security incidents
- Assigns response priorities
- Generates recommended investigation and remediation actions

### Security Assessment
- Summarizes security events
- Counts failed login attempts and permission changes
- Reports detected threats and severity levels
- Generates security recommendations

### Automated Security Testing
- Tests threat detection logic
- Tests IAM access control
- Tests network security rules

## Project Architecture

Security Events
       |
       v
Threat Detection
       |
       +-------------------+
       |                   |
       v                   v
IAM Access Control    Network Security
       |                   |
       +---------+---------+
                 |
                 v
        Incident Response
                 |
                 v
     Security Assessment Report

## Project Structure

cloud-security-threat-detection/
│
├── data/
│   ├── security_events.json
│   ├── users.json
│   └── network_rules.json
│
├── src/
│   ├── threat_detector.py
│   ├── incident_response.py
│   ├── security_pipeline.py
│   ├── iam_security.py
│   ├── network_security.py
│   └── security_report.py
│
├── tests/
│   └── test_security.py
│
├── docs/
│   └── architecture.md
│
├── screenshots/
├── notebooks/
├── README.md
└── .gitignore

## Technologies

- Python
- JSON
- Git & GitHub
- Security event analysis
- IAM concepts
- Network security concepts
- Threat detection
- Incident response
- Automated security testing

## Example Security Scenario

The simulated environment contains repeated failed login attempts from the same source IP followed by a privilege change.

The detection engine identifies:

-- HIGH: Repeated failed login / potential brute-force activity
- MEDIUM: Privilege change requiring authorization review

The incident-response component then generates recommended investigation and remediation actions.

## Testing

Run the automated security tests with:

python3 tests/test_security.py

Expected result:

All security tests passed successfully.

## Project Status

🚧 In development

Future improvements may include a security dashboard, expanded detection rules, additional simulated attack scenarios, and more automated security checks.

## Author

Shreya Chidananda

MS Cybersecurity
Stevens Institute of Technology