import random

class Nearby:

    def __init__(self, lo_bound, hi_bound, num):
        """
        This class generates a number of random numbers specified by the user and store them in a list.
        It also has a function to calculate the average value for the entire list.
        :param lo_bound: This is the lower bound of the random number
        :param hi_bound: This is the higher bound of the random number
        :param num: This is number of instances of random number to generate
        """
        self._lo_bound = lo_bound
        self._hi_bound = hi_bound
        self._num = num
        self._list = list()

    def get_lo_bound(self):
        return self._lo_bound

    def get_hi_bound(self):
        return self._hi_bound

    def get_num(self):
        return self._num

    def get_list(self):
        return self._list

    def simulate_list(self):
        """
        Generate instances of random number specified by the user.
        """
        for i in range(self.get_num()):
            rand_num = random.randint(self.get_lo_bound(), self.get_hi_bound())
            self.get_list().append(rand_num)

    def get_avg(self):
        """
        Calculates the average value for the simulated list.
        :return: The average value of the list
        """
        self.simulate_list()

        sum = 0
        for service_charge in self.get_list():
            sum = sum + service_charge

        return round(sum / self.get_num(), 2)


# ----------------------------------------------------------------------------------------------


class Refi:

    def __init__(self, loan_amount, current_rate, current_terms, new_rate, new_terms, app_fees):
        self._loan_amount = loan_amount
        self._current_rate = current_rate * 0.01
        self._current_terms = current_terms
        self._new_rate = new_rate * 0.01
        self._new_terms = new_terms
        self._app_fees = app_fees

    def get_loan_amount(self):
        return self._loan_amount

    def get_current_rate(self):
        return self._current_rate

    def get_current_terms(self):
        return self._current_terms

    def get_new_rate(self):
        return self._new_rate

    def get_new_terms(self):
        return self._new_terms

    def get_app_fees(self):
        return self._app_fees

    def get_current_payment(self):
        r = self.get_current_rate() / 12
        p = self.get_loan_amount()
        n = self.get_current_terms()

        current_payment = p * r * (1 + r) ** n / ((1 + r) ** n - 1)

        return round(current_payment, 2)

    def get_new_payment(self):
        r = self.get_new_rate() / 12
        p = self.get_loan_amount() + self.get_app_fees()
        n = self.get_new_terms()

        new_payment = p * r * (1 + r) ** n / ((1 + r) ** n - 1)

        return round(new_payment, 2)


# ----------------------------------------------------------------------------------------------

class ExtraPay:

    def __init__(self, loan_amount, loan_rate, loan_terms, extra_payment):
        self._loan_amount = loan_amount
        self._loan_rate = loan_rate * 0.01
        self._loan_terms = loan_terms  # remaining loan terms
        self._extra_payment = extra_payment  # extra payment towards principal

    def get_loan_amount(self):
        return self._loan_amount

    def get_loan_rate(self):
        return self._loan_rate

    def get_loan_terms(self):
        return self._loan_terms

    def get_extra_payment(self):
        return self._extra_payment

    def get_savings(self):
        r = self.get_loan_rate() / 12
        p1 = self.get_loan_amount()
        p2 = p1 - self.get_extra_payment()
        n = self.get_loan_terms()

        total_savings = (p1 - p2) * r * (1 + r) ** n / ((1 + r) ** n - 1) * n

        return round(total_savings, 2)

# ----------------------------------------------------------------------------------------------

class OilChange:

    def __init__(self, dealer_avg, DIY_cost, annual_mile):
        self._dealer_avg = dealer_avg
        self._DIY_cost = DIY_cost
        self._annual_mile = annual_mile


    def get_dealer_avg(self):
        return self._dealer_avg

    def get_DIY_cost(self):
        return self._DIY_cost

    def get_annual_mile(self):
        return self._annual_mile


    def get_num_of_oil_change(self):
        """
        Performing Oil change is recommended for every 3000 miles.
        User will give an estimate on annual mileage driven.
        Calculation will be rounded down to the whole number.
        """
        return self.get_annual_mile() // 3000

    def get_savings(self):
        # the DIY cost is for the engine oil material cost
        diff = self.get_dealer_avg() - self.get_DIY_cost()

        return diff * self.get_num_of_oil_change()