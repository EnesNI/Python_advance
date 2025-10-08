from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height
        self.bmi = None
        self.category = None

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be positive.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {self.bmi:.2f}")
        print(f"Category: {self.category}")
        print("-" * 30)

# Adult class
class Adult(Person):
    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)
        self.get_bmi_category()

    def get_bmi_category(self):
        if self.bmi < 18.5:
            self.category = "Underweight"
        elif self.bmi < 24.9:
            self.category = "Normal weight"
        elif self.bmi < 29.9:
            self.category = "Overweight"
        else:
            self.category = "Obese"

# Child class
class Child(Person):
    def calculate_bmi(self):
        # Assume adjustment factor is internal; use same formula, but thresholds differ
        self.bmi = self.weight / (self.height ** 2)
        self.get_bmi_category()

    def get_bmi_category(self):
        if self.bmi < 14:
            self.category = "Underweight"
        elif self.bmi < 18:
            self.category = "Normal weight"
        elif self.bmi < 24:
            self.category = "Overweight"
        else:
            self.category = "Obese"

# BMIApp class
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person: Person):
        person.calculate_bmi()
        self.people.append(person)

    def collect_user_data(self):
        while True:
            print("\nEnter user information:")
            try:
                name = input("Name: ").strip()
                age = int(input("Age: "))
                weight = float(input("Weight (kg): "))
                height = float(input("Height (m): "))

                if age >= 18:
                    person = Adult(name, age, weight, height)
                else:
                    person = Child(name, age, weight, height)

                self.add_person(person)

            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            more = input("Add another person? (y/n): ").strip().lower()
            if more != 'y':
                break

    def print_results(self):
        print("\n--- BMI Results ---")
        for person in self.people:
            person.print_info()

    def run(self):
        print("=== Welcome to the BMI Calculator App ===")
        self.collect_user_data()
        self.print_results()
        print("=== Thank you for using the app! ===")

# Run the app
if __name__ == "__main__":
    app = BMIApp()
    app.run()
