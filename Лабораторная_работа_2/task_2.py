salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_salary = 0
total_spend = 0
for month in range(months):
    total_salary += salary
    total_spend += spend
    spend *= 1 + increase

money_capital = round(total_spend - total_salary)
# но я бы использовал math.ceil(), чтобы копейки не откидывать

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
