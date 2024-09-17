class ExamEligibilityChecker:
    def __init__(self, age, attendance):
        self.age = age
        self.attendance = attendance
    
    def is_eligible(self):
        min_age = 18  # Minimum age required to sit for the exam
        min_attendance = 75  # Minimum attendance percentage required

        if self.age < min_age:
            return "Not eligible: You must be at least 18 years old."
        elif self.attendance < min_attendance:
            return f"Not eligible: You must have at least {min_attendance}% attendance. Your attendance is {self.attendance}%."
        else:
            return "Eligible: You meet all the criteria to sit for the exam."

    def display_result(self):
        result = self.is_eligible()
        print(result)

# Example usage
if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        attendance = float(input("Enter your attendance percentage: "))
        
        checker = ExamEligibilityChecker(age, attendance)
        checker.display_result()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
