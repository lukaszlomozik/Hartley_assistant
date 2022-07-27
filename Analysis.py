import pandas as pd
from math import sqrt, fabs
from scipy import stats
import itertools


class Analysis:
    def __init__(self, data_frame, level_of_significante, number_of_coefficiens, number_of_repetitions, hm, par):
        self.number_of_coefficiens = int(number_of_coefficiens)
        self.number_of_repetitions = int(number_of_repetitions)
        self.level_of_significante = float(level_of_significante)
        self.data = data_frame
        self.hm = hm
        self.n = len(self.hm.index)
        self.par = par
        print("\ndf:\n" + str(self.data))
        print("\nlevel_of_significante:\n" + str(self.level_of_significante))

    def matrix_exponentiation(self):
        hm_2 = self.hm.pow(2)
        self.hm_2 = hm_2.add_suffix("^2")
        print("\nhm_2:\n" + str(self.hm_2))

    def intra_matrix_multiplication(self):
        self.hm_3 = self.hm.copy()
        count = len(self.hm_3.columns) - 1
        q = 0
        while q < count:
            for i in range(count - q):
                self.hm_3["hm_x" + str(q + 1) + "x" + str(i + q + 2)] = self.hm_3["hm_x" + str(q + 1)] * self.hm_3[
                    "hm_x" + str(i + q + 2)]
            q = q + 1
        for i in range(count + 1):
            self.hm_3 = self.hm_3.drop(columns=["hm_x" + str(i + 1)])
        print("\nhm_3:\n" + str(self.hm_3))

    def average_samples(self):
        for i in range(self.number_of_coefficiens):
            self.data = self.data.drop(columns=[str(self.data.columns[0])])
        self.mean = self.data.mean(axis=1)
        print(self.data)
        print("\nmean:\n" + str(self.mean))

    def matrix_multiplication(self):
        self.hm = self.hm.join([self.hm_2, self.hm_3])
        self.mean_hm = self.hm.mul(self.mean, axis=0)
        print("\nmean_hm:\n" + str(self.mean_hm))

    def variance(self):
        self.var = self.data.var(axis=1)
        print("\nvar:\n" + str(self.var))

    def summation(self):
        self.sum = self.mean_hm.sum(axis=0)
        print("\nsum_all_mean:\n" + str(self.sum))
        self.sum_mean = self.mean.sum()
        print("\nsum_mean:\n" + str(self.sum_mean))
        self.sum_mean_2 = []
        for i in range(self.number_of_coefficiens):
            self.sum_mean_2.append(self.mean_hm[f"hm_x{i + 1}^2"].sum())
        self.sum_mean_2 = sum(self.sum_mean_2)
        print("\nsum_mean_2:\n" + str(self.sum_mean_2))

    def calculation_coefficients_values(self):
        n = self.n
        par = self.par
        print("\nn:\n" + str(n))
        self.regcoef = {}
        self.id = par[par["k"] == self.number_of_coefficiens].index.values
        print("\npar id:\n" + str(self.id))

        id = self.id
        self.regcoef["b0"] = float(par["a"][id] / n * self.sum_mean - (par["b"][id] / n) * self.sum_mean_2)

        coef_inter = {"b23": "hm_x2x3", "b13": "hm_x1x3", "b12": "hm_x1x2"}  # coefficients with interactions
        # (the order matters!)
        product_coef = []
        for i in range(1, self.number_of_coefficiens + 1):
            product_coef.append(i)
        product_coef = list(itertools.combinations(product_coef, 2))
        product_coef_bkj = []
        for i in range(len(product_coef)):
            product_coef_bkj.append("b" + str(list(product_coef[i])[0]) + str(list(product_coef[i])[1]))
        i = 1
        if self.number_of_coefficiens == 3:
            while i <= 3:
                self.regcoef[f"b{i}"] = float(
                    par["e"][id] / n * (self.sum[f"hm_x{i}"] - self.sum[(list(coef_inter.values())[i - 1])]))
                self.regcoef[list(coef_inter.keys())[i - 1]] = float(
                    par["f"][id] / n * self.sum[(list(coef_inter.values())[i - 1])] - par["e"][id] / n * self.sum[
                        f"hm_x{i}"])
                i += 1
        else:
            while i <= self.number_of_coefficiens:
                self.regcoef[f"b{i}"] = float(1 / par["2N"][id] * self.sum[f"hm_x{i}"])
                i += 1
            i = 0
            while i < len(product_coef_bkj):
                self.regcoef[product_coef_bkj[i]] = float(
                    1 / par["3N"][id] * self.sum[f"hm_x{list(product_coef_bkj[i])[1]}x{list(product_coef_bkj[i])[2]}"])
                i += 1
        i = 1
        while i <= self.number_of_coefficiens:
            self.regcoef[f"b{i}{i}"] = float(
                par["c"][id] / n * self.sum[f"hm_x{i}^2"] - (par["b"][id] / n) * self.sum_mean - (
                        par["d"][id] / n) * self.sum_mean_2)
            i += 1
        print("\nregcoef:\n" + str(self.regcoef))

    def tSudent_test(self):
        par = self.par
        n = self.n
        id = self.id
        tr = float(par["tr"][id])
        self.errors_var = (1 / n) * self.var.sum()
        print("errors_var: " + str(self.errors_var))
        self.b0kr = tr * (sqrt((par["a"][id] / (2 * n)) * self.errors_var))
        print("b0kr: " + str(self.b0kr))
        self.bkkr = tr * (sqrt(self.errors_var / (2 * par["2N"][id])))
        print("bkkr: " + str(self.bkkr))
        self.bkkkr = tr * (sqrt(((par["c"][id] - par["d"][id]) / (2 * n)) * self.errors_var))
        print("bkkkr: " + str(self.bkkkr))
        self.bkjkr = tr * (sqrt(self.errors_var / (2 * par["3N"][id])))
        print("bkjkr: " + str(self.bkjkr))

    def significance_test(self):
        sig = {}
        if fabs(self.regcoef["b0"]) > self.b0kr:
            sig["b0"] = "istotny"
        else:
            sig["b0"] = "nieistotny"
        for i in range(1, self.number_of_coefficiens + 1):
            if fabs(self.regcoef[f"b{i}"]) > self.bkkr:
                sig[f"b{i}"] = "istotny"
            else:
                sig[f"b{i}"] = "nieistotny"
            if fabs(self.regcoef[f"b{i}{i}"]) > self.bkkkr:
                sig[f"b{i}{i}"] = "istotny"
            else:
                sig[f"b{i}{i}"] = "nieistotny"
        for i, n in enumerate(self.regcoef):
            if n not in sig and self.regcoef[n] > self.bkjkr:
                sig[n] = "istotny"
            elif n not in sig and self.regcoef[n] < self.bkjkr:
                sig[n] = "nieistotny"
            else:
                continue
        self.sig = sig
        print("sig:\n" + str(self.sig))

    def resetting_irrelevant_coef(self):
        for i, n in enumerate(self.sig):
            if self.sig[n] == "nieistotny":
                self.regcoef[n] = 0
        print(self.regcoef)

    def calculation_regression_results(self):
        keys = list(self.regcoef.keys())
        bk = []
        bkk = []
        bkj = []
        product_bkx = []
        product_bkkx = []
        product_bkjx = []
        regression_results = {}
        for i, n in enumerate(keys):
            for z in range(1, self.number_of_coefficiens + 1):
                if n == f"b{z}":
                    bk.append(n)
                elif n == f"b{z}{z}":
                    bkk.append(n)
            if (n not in bk) and (n not in bkk) and (n != "b0"):
                bkj.append(n)
        for a in range(self.n):
            for i, n in enumerate(bk):
                product_bkx.append(self.regcoef[n] * self.hm[f"hm_x{list(n)[1]}"][a])
            for i, n in enumerate(bkk):
                product_bkkx.append(self.regcoef[n] * self.hm_2[f"hm_x{list(n)[1]}^2"][a])
            for i, n in enumerate(bkj):
                product_bkjx.append(self.regcoef[n] * self.hm_3[f"hm_x{list(n)[1]}x{list(n)[2]}"][a])
            regression_results[a] = (
                    sum(product_bkx) + sum(product_bkkx) + sum(product_bkjx) + self.regcoef["b0"])
            product_bkx = []
            product_bkkx = []
            product_bkjx = []
        print(f"regression_results: {regression_results}")
        self.regression_results = regression_results

    def evaluating_results(self):
        self.evaluation = ModelEvaluation()
        self.evaluation.computing_squared_deviations(self.regression_results, self.mean)
        self.evaluation.calculating_adequacy_variance(r=self.number_of_repetitions, n=self.n,
                                                      k=self.number_of_coefficiens)
        self.evaluation.calculating_degrees_freedom(self.number_of_repetitions, self.n, self.number_of_coefficiens)
        self.evaluation.calculating_critical_F_factor(sig_level=self.level_of_significante)
        self.evaluation.calculating_empirical_F_factor(errors_var=self.errors_var)
        self.evaluation.checking_regression_equation()

    def calc_z_axis(self, input_level_factors, decimal=6):
        keys = list(self.regcoef.keys())
        bk = []
        bkk = []
        bkj = []
        product_bkx = []
        product_bkkx = []
        product_bkjx = []
        a = []
        for i, n in enumerate(keys):
            for z in range(1, self.number_of_coefficiens + 1):
                if n == f"b{z}":
                    bk.append(n)
                elif n == f"b{z}{z}":
                    bkk.append(n)
            if (n not in bk) and (n not in bkk) and (n != "b0"):
                bkj.append(n)
                a.append(list(n))
        for i, n in enumerate(bk):
            product_bkx.append(round(self.regcoef[n], decimal) * input_level_factors[i])
        for i, n in enumerate(bkk):
            product_bkkx.append(round(self.regcoef[n], decimal) * (input_level_factors[i]) ** 2)
        for i, n in enumerate(bkj):
            product_bkjx.append(
                round(self.regcoef[n], 2) * input_level_factors[int(a[i][1]) - 1] * input_level_factors[
                    int(a[i][2]) - 1])
        self.z_axis = (sum(product_bkx) + sum(product_bkkx) + sum(product_bkjx) + round(self.regcoef["b0"], decimal))
        product_bkx.clear()
        product_bkkx.clear()
        product_bkjx.clear()
        return self.z_axis

    def calc_factors_combination(self):
        factors_amount = self.number_of_coefficiens
        input_factors = ["-1", "0", "1", "X", "Y"]
        product = list(itertools.product(input_factors, repeat=factors_amount))
        product_correct = []
        for i in range(len(product)):
            if product[i].count("X") == 1 and product[i].count("Y") == 1:
                product_correct.append(product[i])
        output = []
        for i in range(len(product_correct)):
            output.append(list(product_correct[i]))
        for i in range(len(output)):
            for n in range(len(output[i])):
                if output[i][n] == "X" or output[i][n] == "Y":
                    output[i][n] = "Y"
        for i in range(len(output)):
            for n in range(len(output[i])):
                if output[i][n] == "Y":
                    output[i][n] = "X"
                    break
        for i in range(len(output)):
            if output.count(output[i]) > 1:
                output[i] = None
        for a in range(output.count(None)):
            output.remove(None)
        return output


class ModelEvaluation:
    """r - number of repetitions, n - number of samples, k - number of coefficiens"""

    def computing_squared_deviations(self, prediction_data, input_data):
        self.pred_data = pd.Series(prediction_data)
        self.in_data = input_data
        self.dev = (self.in_data - self.pred_data).pow(2)
        self.sum_dev = sum(self.dev)
        print("\ndeviatons:\n" + str(self.dev))
        print("\nsum_deviatons:\n" + str(self.sum_dev))

    def calculating_adequacy_variance(self, r, n, k):
        self.adequacy_var = r * self.sum_dev / (n - k - 1)
        print("\nadequacy_var:\n" + str(self.adequacy_var))

    def calculating_degrees_freedom(self, r, n, k):
        self.f1 = n - k - 1
        self.f2 = n * (r - 1)
        print("\nf1:\n" + str(self.f1))
        print("\nf2:\n" + str(self.f2))

    def calculating_critical_F_factor(self, sig_level):
        self.crit_F_factor = stats.f.ppf(1 - sig_level, self.f1, self.f2)
        print("\ncrit_F_factor:\n" + str(self.crit_F_factor))

    def calculating_empirical_F_factor(self, errors_var):
        self.empi_F_factor = self.adequacy_var / errors_var
        print("\nempi_F_factor :\n" + str(self.empi_F_factor))

    def checking_regression_equation(self):
        if self.empi_F_factor < self.crit_F_factor:
            self.rating = "równanie regresji jest adekwatne"
            self.mark = "<"
        else:
            self.rating = "równanie regresji jest nieadekwatne"
            self.mark = ">"
