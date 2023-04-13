def assignment(annual_salary: float) -> float:
    MONTHS = 36
    COST_RANGE_APPROX = 100

    total_cost = 1_000_000
    portion_down_payment = 0.25
    min_required = total_cost * portion_down_payment

    start = 0
    end = 1
    steps = 0

    SAVE_EVERYHING = end

    TOO_LOW = -1
    TOO_HIGH = 1
    OK = 0

    def simulate(annual_salary: float, portion_saved: float) -> tuple[float, int]:
        nonlocal total_cost, portion_down_payment, min_required

        semi_annual_raise = 0.07
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

        return current_savings, current_month

    def simulation_analysis(simulation: tuple[float, int]) -> int:
        savings, current_month = simulation

        if current_month > MONTHS:
            return TOO_LOW
        elif current_month < MONTHS:
            return TOO_HIGH
        else:
            if savings > min_required + COST_RANGE_APPROX:
                return TOO_HIGH
            elif savings < min_required - COST_RANGE_APPROX:
                return TOO_LOW
            else:
                return OK

    if simulation_analysis(simulate(annual_salary, SAVE_EVERYHING)) != TOO_LOW:
        while True:
            steps += 1

            analysis = simulation_analysis(simulate(annual_salary, current := ((end - start) / 2) + start))

            if analysis == OK:
                break
            elif analysis == TOO_LOW:
                start = current
            elif analysis == TOO_HIGH:
                end = current

        # Uncomment to see bisection search steps if you need.
        # print(f'Steps in bisection search: {steps}')

        return current
    else:
        return -1

if __name__ == '__main__':
    annual_salary = float(input(r'Enter the starting salary: ')) or 150_000

    best_saving_rate = assignment(annual_salary)

    if best_saving_rate >= 0:
        print(f'Best savings rate: {best_saving_rate}')
    else:
        print('It is not possible to pay the down payment in three years.')
