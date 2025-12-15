class PasswordReport:
    def __init__(self, analysis: dict):
        self.analysis = analysis

    def __str__(self) -> str:
        lines = ["Password Analysis Report", "-" * 25]
        for key, value in self.analysis.items():
            lines.append(f"{key.replace('_', ' ').title()}: {value}")
        return "\n".join(lines)
