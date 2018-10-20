def calc_tax(salary, free, rule):
    salary -= free
    tax = 0
    for r in rule:
        if salary > r[0]:
            tax = salary * r[1] - r[2]
            break
    return tax

free_old = 3500
rule_old = [
    (80000, 0.45, 13505),
    (55000, 0.35, 5505),
    (35000, 0.3, 2755),
    (9000, 0.25, 1005),
    (4500, 0.2, 555),
    (1500, 0.1, 105),
    (0,0.03, 0)
]

free = 5000
rule = [
    (80000, 0.45, 15160),
    (55000, 0.35, 7160),
    (35000, 0.3, 4410),
    (25000, 0.25, 2660),
    (12000, 0.2, 1410),
    (3000, 0.1, 210),
    (0,0.03, 0)
]

income = eval(input('税前月收入：'))
insurance = eval(input('五险一金：'))
before = income - insurance
tax_old = calc_tax(before, free_old, rule_old)
tax = calc_tax(before, free, rule)
print('旧税率应纳税：%.2f 元，税后收入：%.2f 元' % (tax_old, before - tax_old))
print('新税率应纳税：%.2f 元，税后收入：%.2f 元' % (tax, before - tax))