import pandas as pd


class DataLoad:

    def __init__(self, number_of_repetitions, number_of_coefficiens):
        print("dataload")
        self.number_of_repetitions = int(number_of_repetitions)
        self.number_of_coefficiens = int(number_of_coefficiens)

    def open_file(self, file='Szablon.xlsx'):
        try:
            self.data_frame = pd.read_excel(file)
            print(self.data_frame)
        except:
            return False
        return True

    def checking_amount_data(self):
        if (self.number_of_coefficiens + self.number_of_repetitions != len(self.data_frame.columns)) or (
                self.number_of_coefficiens == 3 and self.data_frame.index.stop != 11) or (
                self.number_of_coefficiens == 4 and self.data_frame.index.stop != 17) or (
                self.number_of_coefficiens == 5 and self.data_frame.index.stop != 27) or \
                self.data_frame.isna().sum().sum() > 0:
            return False
        else:
            return True

    def checking_content_data(self):
        for row in self.data_frame.values:
            for value in row:
                try:
                    float(value)
                except:
                    return False
        return True

    def loading_hartley_matrix(self, file):
        try:
            self.hm = pd.read_excel(file, str(self.number_of_coefficiens))
            test_data = abs(self.hm.values)
            print("\nhm:\n" + str(self.hm))
            return True
        except:
            return False

    def open_par(self, file):
        try:
            self.par = pd.read_excel(file)
            test_data = abs(self.par.values)
            print("\npar:\n" + str(self.par))
            return True
        except:
            return False
