class PasswordReport:
    def __init__(self, results: dict):
        self.results = results

    def display(self):
        print("Password Analysis Report")
        print("-" * 25)
        for key, value in self.results.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
