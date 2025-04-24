
    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = self._validate_name_property(value, "firstname")

import re


    def validate_string(self, value, field_name):
        pattern = r"^[a-zA-Z\s'-]+$"
        if re.fullmatch(pattern, value):
            return value
        else:
            raise ValueError(f"Invalid {field_name}: Please use only letters, spaces, hyphens, and apostrophes.")

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = self.validate_string(value, "firstname")



import phonenumbers

phone_number_str = "+52 867 712 3456"  # Example for Nuevo Laredo
try:
    parsed_number = phonenumbers.parse(phone_number_str)
    if phonenumbers.is_valid_number(parsed_number):
        print(f"{phone_number_str} is a valid phone number.")
    else:
        print(f"{phone_number_str} is not a valid phone number.")
except phonenumbers.NumberParseException as e:
    print(f"Error parsing phone number: {e}")
    
    
    #examples to validate a Bday
    import datetime

class Person:
    def __init__(self, name, birth_date_str, date_format="%Y-%m-%d"):
        self.name = name
        self.birth_date = self.validate_birth_date(birth_date_str, date_format)

    def validate_birth_date(self, date_string, format_string):
        """
        Validates if the given date string is a valid date according to the format
        and returns a datetime.date object if valid, otherwise raises ValueError.
        """
        try:
            birth_date = datetime.datetime.strptime(date_string, format_string).date()
            return birth_date
        except ValueError:
            raise ValueError(f"Invalid date format or date. Please use the format '{format_string}'.")

    @property
    def birth_date_str(self):
        return self.birth_date.strftime("%Y-%m-%d")  # Default format for display

    @birth_date_str.setter
    def birth_date_str(self, value):
        self.birth_date = self.validate_birth_date(value, "%Y-%m-%d")

# Example Usage:
try:
    person1 = Person("Alice", "1990-08-15")
    print(f"{person1.name}'s birth date: {person1.birth_date}")
    print(f"{person1.name}'s birth date (string): {person1.birth_date_str}")

    person2 = Person("Bob", "2000/02/29", "%Y/%m/%d")
    print(f"{person2.name}'s birth date: {person2.birth_date}")
    print(f"{person2.name}'s birth date (string, default format): {person2.birth_date_str}")

    person3 = Person("Charlie", "2023-02-29")  # Invalid date
except ValueError as e:
    print(f"Error creating person: {e}")

try:
    person1.birth_date_str = "1995-06-20"
    print(f"{person1.name}'s updated birth date: {person1.birth_date}")

    person1.birth_date_str = "invalid-date"  # This will raise a ValueError
except ValueError as e:
    print(f"Error updating birth date: {e}")