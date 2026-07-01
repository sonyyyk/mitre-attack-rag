class RiskManager:
    """
    Calculate incident risk.
    """

    HIGH = {
        "credential-access",
        "privilege-escalation",
        "lateral-movement"
    }

    MEDIUM = {
        "execution",
        "persistence",
        "defense-evasion"
    }

    def calculate(
        self,
        tactics: list[str]
    ) -> str:

        if any(t in self.HIGH for t in tactics):
            return "HIGH"

        if any(t in self.MEDIUM for t in tactics):
            return "MEDIUM"

        return "LOW"