import secrets
import string

def standardize_name(name: str):
    return name.strip().lower().replace(" ", "")

def generate_employee_name():
    name_length = secrets.randbelow(50) + 20
    name = "".join([secrets.choice(string.ascii_letters) for _ in range(name_length)])
    if secrets.choice([True, False, False]):
        target_index = secrets.randbelow(len(name))
        name = name[:target_index] + " " + name[target_index:]
    return name.strip()


def mutate_name_at(name, target_index: int, mutation_type=None):
        if mutation_type is None:
            mutation_type = secrets.choice(['add', 'delete', 'replace'])
        if mutation_type == 'add':
            return name[:target_index] + secrets.choice(string.ascii_letters) + name[target_index:]
        elif mutation_type == 'delete':
            return name[:target_index] + name[target_index + 1:]
        else:
            return name[:target_index] + secrets.choice(string.ascii_letters) + name[target_index + 1:]


def mutate_name(name, num_mutations=1):
    original_name = name
    for _ in range(num_mutations):
        name = mutate_name_at(name, secrets.randbelow(len(name)))

    if name.lower() != original_name.lower():
        return name
    else:
        return mutate_name(name, num_mutations=num_mutations)


class ProblemTestCase:

    def __init__(self, num_employees: int, num_suspects: int) -> None:
        self._employees = list([generate_employee_name() for _ in range(num_employees)])
        self._std_employees = set([standardize_name(e) for e in self._employees])
        self._suspects = self.regenerate_suspects(num_suspects=num_suspects)

    def regenerate_suspects(self, num_suspects: int):
        suspects = []
        for _ in range(num_suspects):
            suspect_type = secrets.choice(['EMPLOYEE', 'BOT', 'CUSTOMER'])
            if suspect_type == 'EMPLOYEE':
                suspects.append((suspect_type, secrets.choice(self.employees)))
            elif suspect_type == "BOT":
                suspects.append((suspect_type, self.generate_bot()))
            else:
                suspects.append((suspect_type, self.generate_customer()))

            if secrets.choice([True, False]):
                suspects[-1] = suspects[-1][0], suspects[-1][1].swapcase()
        return suspects

    @property
    def employees(self):
        return self._employees

    def is_employee(self, name: str):
        return standardize_name(name) in self._std_employees


    @property
    def suspects(self):
        return [suspect[1] for suspect in self._suspects]

    @property
    def solutions(self):
        return [suspect[0] for suspect in self._suspects]

    def generate_bot(self):
        target_employee = secrets.choice(self.employees)
        bot_name = mutate_name(target_employee)
        if self.is_employee(bot_name):
            return self.generate_bot()
        else:
            return bot_name


    def generate_customer(self):
        return generate_employee_name()


def main():
    test_num = int(input("Test num:"))
    employees = int(input("Employees:"))
    suspects = int(input("Suspects:"))
    case = ProblemTestCase(employees, suspects)

    with open(f"./tests/{test_num}.in", "w") as f:
        f.write(str(employees) + "\n")
        for employee in case.employees:
            f.write(employee + "\n")
        f.write(str(suspects) + "\n")
        for suspect in case.suspects:
            f.write(suspect + "\n")

    with open(f"./tests/{test_num}.out", "w") as f:
        for solution in case.solutions:
            f.write(solution + "\n")



if __name__ == "__main__":
    main()


