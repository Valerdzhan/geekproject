
# выручка
revenue = int(input('Enter revenue: '))
# издержки
costs = int(input('Enter costs: '))

# прибыль — выручка больше издержек, или убыток — издержки больше выручки
if revenue > costs:
    print('Profit! =)')
    # вычисляем прибыль
    profit = revenue - costs
    # вычисляем рентабельность
    profitability = profit / revenue
    empoyees = int(input('Enter the number of employees: '))
    # прибыль фирмы в расчете на одного сотрудника
    empoyees_profit = profit / empoyees
    print('Profit empoyees: {}'.format(empoyees_profit))
else:
    print('Lesion! =(')


