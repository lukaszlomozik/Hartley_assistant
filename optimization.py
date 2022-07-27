import pandas as pd
from itertools import product


class BruteForce:
    def __init__(self, file, coefficients, number_of_coef, step, goal):
        self.number_of_coef = number_of_coef
        self.data = pd.read_excel(file, str(self.number_of_coef))
        self.b = coefficients
        self.step = step
        self.goal = goal
        self.results = []

    def data_cleaning(self):
        for i, n in enumerate(self.data.keys()):
            if i >= self.number_of_coef:
                self.data = self.data.drop(columns=n)
        print(self.data)

    def calc_central_values(self):
        self.central_values = []
        for i, n in enumerate(self.data.keys()):
            self.central_values.append((self.data[n].max() + self.data[n].min()) / 2)
        print(f"central_values: {self.central_values}")

    def calc_units_variation(self):
        self.units_variation = []
        for i, n in enumerate(self.data.keys()):
            self.units_variation.append((self.data[n].max() - self.data[n].min()) / 2)
        print(f"units_variation: {self.units_variation}")

    def factors_generator(self):
        min_factor_value = []
        max_factor_value = []
        for i, n in enumerate(self.data.keys()):
            min_factor_value.append(self.data[n].min())
            max_factor_value.append(self.data[n].max())
        self.generated_factors = []
        for i in range(self.number_of_coef):
            n = min_factor_value[i]
            self.generated_factors.append([])
            while n <= max_factor_value[i]:
                self.generated_factors[i].append(n)
                n = n + self.step[i]

    def factors_coded(self):
        print("factors_coded")
        self.coded_factors = []
        for i in range(self.number_of_coef):
            self.coded_factors.append([])
            for n in range(len(self.generated_factors[i])):
                self.coded_factors[i].append(
                    (self.generated_factors[i][n] - self.central_values[i]) / self.units_variation[i])

    def substituting_variables(self):
        print("substituting_variables")
        if self.number_of_coef == 3:
            self.factors_combination = list(
                product(self.coded_factors[0], self.coded_factors[1], self.coded_factors[2],
                        repeat=1))
        if self.number_of_coef == 4:
            self.factors_combination = list(
                product(self.coded_factors[0], self.coded_factors[1], self.coded_factors[2], self.coded_factors[3],
                        repeat=1))
        if self.number_of_coef == 5:
            self.factors_combination = list(
                product(self.coded_factors[0], self.coded_factors[1], self.coded_factors[2], self.coded_factors[3],
                        self.coded_factors[4],
                        repeat=1))
        return self.factors_combination

    def calc_results(self, n):
        print("calc_results")
        self.results.append(self.calc_z_axis(input_level_factors=list(n)))

    def factors_decoded(self):
        print("factors_decoded")
        self.decoded_factors = []
        if self.goal == "Min":
            self.index = self.results.index(min(self.results))
            self.results = min(self.results)
        if self.goal == "Max":
            self.index = self.results.index(max(self.results))
            self.results = max(self.results)
        for i in range(self.number_of_coef):
            self.decoded_factors.append(
                (list(self.factors_combination[self.index])[i] * self.units_variation[i] + self.central_values[i]))

    def calc_z_axis(self, input_level_factors, decimal=4):
        keys = list(self.b.keys())
        bk = []
        bkk = []
        bkj = []
        product_bkx = []
        product_bkkx = []
        product_bkjx = []
        a = []
        for i, n in enumerate(keys):
            for z in range(1, self.number_of_coef + 1):
                if n == f"b{z}":
                    bk.append(n)
                elif n == f"b{z}{z}":
                    bkk.append(n)
            if (n not in bk) and (n not in bkk) and (n != "b0"):
                bkj.append(n)
                a.append(list(n))
        for i, n in enumerate(bk):
            product_bkx.append(round(self.b[n], decimal) * round(input_level_factors[i], decimal))
        for i, n in enumerate(bkk):
            product_bkkx.append(round(self.b[n], decimal) * round((input_level_factors[i]) ** 2, decimal))
        for i, n in enumerate(bkj):
            product_bkjx.append(
                round(self.b[n], decimal) * round(input_level_factors[int(a[i][1]) - 1] * input_level_factors[
                    int(a[i][2]) - 1], decimal))
        self.z_axis = (sum(product_bkx) + sum(product_bkkx) + sum(product_bkjx) + round(self.b["b0"], decimal))
        product_bkx.clear()
        product_bkkx.clear()
        product_bkjx.clear()
        return self.z_axis
