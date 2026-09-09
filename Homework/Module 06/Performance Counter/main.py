import pytest



class Employee:

    def __init__(self, name, department) -> None:
        self.name = name
        self.department = department

        self.base_score = 60.0

    def calculate_performance_score(self):
        return self.base_score

    def generate_report(self) -> str:
        report = f"\nREPORT\nEmployee name: {self.name}\nEmployee department: {self.department}"
        return report


class Manager(Employee):

    def __init__(self, name, department, team_size) -> None:
        super().__init__(name, department)
        self.team_size = team_size

    def calculate_performance_score(self):
        total_score = super().calculate_performance_score() + (self.team_size * 2) + 15
        return total_score

    def generate_report(self) -> str:
        base_report = super().generate_report()
        report = f"{base_report}\nTeam Size: {self.team_size}\n\nTotal Performance Scrore: {self.calculate_performance_score()}"
        return report    


class Developer(Employee):

    def __init__(self, name, department, reviews_count) -> None:
        super().__init__(name, department)
        self.reviews_count = reviews_count

    def calculate_performance_score(self):
        total_score = super().calculate_performance_score() + 25 + (self.reviews_count * 0.5)
        return total_score

    def generate_report(self) -> str:
        base_report = super().generate_report()
        report = f"{base_report}\n Reviews count: {self.reviews_count}\n\nTotal Performance score: {self.calculate_performance_score()}"
        return report


manager = Manager(name="Анна", department="Продуктовый", team_size=10)
report = manager.generate_report()
print(report)



def test_emoloyee_base_score():
    employee = Employee(name="Test1", department="Developer")
    assert employee.calculate_performance_score() == 60.0, "Base score should be 60.0"

def test_manager_performance_score():
    manager = Manager(name="Test2", department="Manager", team_size=10)
    assert manager.calculate_performance_score() == 95.0, "Manager performance score should be 95.0"

def test_developer_performance_score():
    developer = Developer(name="Test3", department="Developer", reviews_count=20)
    assert developer.calculate_performance_score() == 95.0, "Developer performance score should be 95.0"


"""
1. Dog is an Animal -> Dog(Animal)
2. Car has a Wheel -> Композиция
3. Square is not a Rectangle, Square has not Rectangle, получается, это ни то, ни то. Объекты между собой не дружат. Но вот если бы было Square и Line и Rectangle и Line, тогда это все дружило бы вместе. Или Square и Figure и Rectangle и Figure.
4. DatabaseLogger is a Logger -> DatabaseLogger(Logger)
5. Order is not a Customer, Order has a Customer -> Композиция.
"""