EMPLOYEE = 'EMPLOYEE'
BOT = 'BOT'
CUSTOMER = 'CUSTOMER'

E = int(input())
employees = []
for e in range(E):
    employees.append(input().lower().replace(' ', ''))

N = int(input())
for n in range(N):
    name = input().lower().replace(' ', '')

    category = CUSTOMER
    for eName in employees:
        if name == eName:
            category = EMPLOYEE
            break
        if abs(len(eName) - len(name)) > 1:
            continue
        if len(eName) > len(name):
            # char removed
            i, j = 0, 0
            charRemoved = False
            bot = True
            while i < len(eName):
                if j >= len(name):
                    break
                if eName[i] == name[j]:
                    i += 1
                    j += 1
                    continue
                if not charRemoved:
                    i += 1
                    charRemoved = True
                    continue
                bot = False
                break
            if bot:
                category = BOT
                break
        elif len(name) > len(eName):
            # char added
            i, j = 0, 0
            charAdded = False
            bot = True
            while i < len(eName):
                if j >= len(name):
                    break
                if eName[i] == name[j]:
                    i += 1
                    j += 1
                    continue
                if not charAdded:
                    j += 1
                    charAdded = True
                    continue
                bot = False
                break
            if bot:
                category = BOT
                break
        else:
            # char changed
            i, j = 0, 0
            charChanged = False
            bot = True
            while i < len(eName):
                if eName[i] == name[j]:
                    i += 1
                    j += 1
                    continue
                if not charChanged:
                    i += 1
                    j += 1
                    charChanged = True
                    continue
                bot = False
                break
            if bot:
                category = BOT
                break
    print(category)
