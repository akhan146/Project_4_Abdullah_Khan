from domain.password import Password
from services.analyzer import BasicPasswordAnalyzer, AdvancedPasswordAnalyzer
from services.policy import PasswordPolicy
from services.generator import PasswordGenerator
from reports.report import PasswordReport
from persistence.storage import StorageManager


def run():
    policy = PasswordPolicy(min_length=10)
    generator = PasswordGenerator(policy)
    password = generator.generate()

    print(password)

    analyzers = [
        BasicPasswordAnalyzer(password),
        AdvancedPasswordAnalyzer(password)
    ]

    storage = StorageManager()

    for analyzer in analyzers:
        analysis = analyzer.analyze()
        report = PasswordReport(analysis)
        print()
        print(report)
        storage.save("latest_analysis.json", analysis)


if __name__ == "__main__":
    run()
