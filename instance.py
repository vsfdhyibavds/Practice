# Import datetime module to get current year calculation
from datetime import datetime


class Employee:
    def __init__(self, first_name, last_name, age, employment_start_year):
        # Initialize instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employment_start_year = employment_start_year

    def years_of_employment(self):
        """
        Calculates how many years the employee has been with the company
        Returns: Integer - Difference between current year and start year
        """
        current_year = datetime.now().year  # Get current year dynamically
        return current_year - self.employment_start_year

    def full_name(self):
        """
        Combines first and last names to create full name
        Returns: String - Full name in "First Last" format
        """
        return f"{self.first_name} {self.last_name}"

    def age_message(self):
        """
        Provides life-stage advice based on employee's age
        Returns: String - Custom message depending on age bracket
        """
        # Check age thresholds in descending order
        if self.age > 50:
            return "Need to call it quits Old timer and retire"
        elif self.age > 40:
            return "It's time to consider retiring"
        elif self.age > 30:
            return "It's about time to think about having Kids"
        elif self.age > 25:
            return "It's about time to consider marriage"
        else:
            return "No specific message for this age group"


# Example usage with comments:
if __name__ == "__main__":
    # Create an employee instance with sample data
    emp = Employee(
        first_name="John", last_name="Doe", age=32, employment_start_year=2022
    )

    # Demonstrate method outputs
    print("Employment Duration:", emp.years_of_employment())  # Current year - 2022
    print("Employee Name:", emp.full_name())  # "John Doe"
    print("Age Advice:", emp.age_message())  # Based on age 32
