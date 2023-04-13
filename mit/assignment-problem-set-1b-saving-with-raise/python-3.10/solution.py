def assignment(annual_salary: float, portion_saved: float, total_cost: float, semi_annual_raise: float) -> int:
    portion_down_payment = 0.25
    min_required = total_cost * portion_down_payment
    current_savings = 0
    rate = 0.04
    monthly_rate = rate / 12

    current_month = 0

    def invest(savings: float, rate: float) -> float:
        return savings * rate

    def apply_salary_raise() -> None:
        nonlocal annual_salary
        annual_salary += annual_salary * semi_annual_raise

    def mensal_salary() -> float:
        return annual_salary / 12

    def montly_saved() -> float:
        return mensal_salary() * portion_saved

    def save_money(amount: float) -> None:
        nonlocal current_month
        current_month += 1
        nonlocal current_savings

        if current_month % 6 == 0:
            apply_salary_raise()

        current_savings = current_savings + amount + invest(current_savings, monthly_rate)

    while current_savings < min_required:
        save_money(montly_saved())

    return current_month

if __name__ == '__main__':
    annual_salary = float(input(r'Enter your annual salary: ')) or 120_000
    portion_saved = float(input(r'Enter the percent of your salary to save (0% - 100%): ').replace('%', '')) / 100
    total_cost = float(input(r'Enter the cost of your dream home: '))
    semi_annual_raise = float(input(r'Enter the semi-annual raise (%):').replace('%', '')) / 100

    current_month = assignment(annual_salary, portion_saved, total_cost, semi_annual_raise)

    print(f'Number of months: {current_month}')
