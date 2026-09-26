# Security Findings & Remediation

## Finding 1: Repeated Failed Login Attempts

**Severity:** High

**Observation:**  
The simulated security logs contain three consecutive failed login attempts for the administrator account from the same source IP address.

**Security Risk:**  
Repeated authentication failures may indicate a brute-force or unauthorized access attempt.

**Recommended Remediation:**  
- Investigate the source IP address.
- Review authentication activity for the affected account.
- Temporarily restrict the account if the activity is confirmed as unauthorized.
- Consider implementing stronger authentication controls and rate limiting.

---

## Finding 2: Privilege Change

**Severity:** Medium

**Observation:**  
A permission change affecting the administrator role was identified in the simulated security events.

**Security Risk:**  
Unauthorized privilege changes could provide excessive access to sensitive resources.

**Recommended Remediation:**  
- Verify that the permission change was authorized.
- Review who initiated the change.
- Revert unauthorized changes.
- Apply least-privilege access principles.

---

## Finding 3: Public Remote Access Controls

**Severity:** Medium

**Observation:**  
The network security simulation blocks public Telnet and RDP traffic.

**Security Risk:**  
Exposing insecure or unnecessary remote-access services to public networks can increase the attack surface.

**Recommended Remediation:**  
- Keep Telnet blocked.
- Restrict remote desktop access to trusted networks or approved users.
- Regularly review network access rules.
- Follow a default-deny approach for unmatched traffic.

---

## Overall Assessment

The simulated environment identified authentication, privilege-management, and network-security risks.

The project demonstrates security monitoring, access-control evaluation, network-rule analysis, threat detection, and recommended incident-response actions using simulated data.