# Project Architecture

## Cloud Security & Threat Detection Platform

This project simulates a cloud security monitoring environment using Python and AWS-inspired security concepts.

### Security Workflow

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

### Components

- Security Events: Simulated authentication and administrative activity.
- Threat Detection: Identifies repeated failed logins and privilege changes.
- IAM Access Control: Simulates role-based permission checks.
- Network Security: Evaluates traffic against security rules.
- Incident Response: Generates recommended actions for detected threats.
- Security Assessment Report: Summarizes events, threats, severity, and recommendations.
- Automated Tests: Validates threat detection, IAM, and network security logic.
