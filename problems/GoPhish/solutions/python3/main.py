#!/usr/bin/env python3


from typing import List


def standardize_name(name: str) -> str:
    return name.strip().lower().replace(" ", "")


def contains_single_deletion(shorter: str, longer: str) -> bool:
    for i, character in enumerate(shorter):
        if character != longer[i]:
            remaining_shorter = shorter[i:]
            remaining_longer = longer[i+1:]
            return remaining_shorter == remaining_longer
    return True # i.e., the last character in `longer` was the one added


class Employee:

    def __init__(self, name: str) -> None:
        self.name = name

    def is_off_by_one(self, suspect: str) -> bool:
        if len(suspect) == len(self.name):
            differences = 0
            for i, character in enumerate(self.name):
                if character != suspect[i]:
                    differences += 1
                if differences > 1:
                    return False  # Same length, but off by more than one character.
            return differences == 1
        elif len(suspect) - len(self.name) == 1:
            return contains_single_deletion(self.name, suspect)
        elif len(self.name) - len(suspect) == 1:
            return contains_single_deletion(suspect, self.name)
        else:
            return False


class EmployeeList:

    def __init__(self, employees: List[Employee]):
        self.employees = employees
        self.employees_name_cache = set([e.name for e in employees])

    def classify(self, suspect: str):
        if suspect in self.employees_name_cache:
            return "EMPLOYEE"
        for employee in self.employees:
            if employee.is_off_by_one(suspect):
                return "BOT"
        return "CUSTOMER"


def main():
    num_employees = int(input())
    employees_raw = []
    for i in range(num_employees):
        employees_raw.append(
            Employee(standardize_name(input()))
        )
    employees = EmployeeList(employees_raw)

    num_suspects = int(input())
    for i in range(num_suspects):
        suspect = standardize_name(input())
        print(employees.classify(suspect))


if __name__ == "__main__":
    main()