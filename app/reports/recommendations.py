class RecommendationManager:
    """
    Generate recommendations based on MITRE tactics.
    """

    RULES = {

        "credential-access": [
            "Reset compromised credentials.",
            "Review privileged accounts.",
            "Inspect LSASS access.",
            "Enable MFA where possible."
        ],

        "execution": [
            "Inspect PowerShell logs.",
            "Review executed commands.",
            "Block malicious scripts."
        ],

        "persistence": [
            "Review Registry Run Keys.",
            "Inspect Scheduled Tasks.",
            "Check Startup folders."
        ],

        "privilege-escalation": [
            "Review administrator privileges.",
            "Inspect token manipulation.",
            "Audit local administrators."
        ],

        "lateral-movement": [
            "Review remote logins.",
            "Inspect SMB/RDP activity.",
            "Check Active Directory authentication."
        ],

        "defense-evasion": [
            "Inspect disabled security controls.",
            "Review antivirus logs.",
            "Check deleted event logs."
        ]
    }

    def get(self, tactics: list[str]) -> list[str]:

        recommendations = []

        for tactic in tactics:

            if tactic in self.RULES:

                recommendations.extend(
                    self.RULES[tactic]
                )

        return sorted(set(recommendations))