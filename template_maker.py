import xlsxwriter


class MakeXlsFile:
    def __init__(self, number_factors, number_repetitions):
        self.number_factors = number_factors
        self.number_repetitions = number_repetitions
        self.data = None

    def create_file(self):
        self.workbook = xlsxwriter.Workbook('Szablon.xlsx')
        self.worksheet = self.workbook.add_worksheet(str(self.number_factors))

    def save_file(self):
        self.workbook.close()

    def make_columns(self):
        row = 0
        col = 0
        for i in range(1, self.number_factors + 1):
            self.worksheet.write(row, col, f"Czynnik{i}")
            col += 1
        for i in range(1, self.number_repetitions + 1):
            self.worksheet.write(row, col, f"Wynik{i}")
            col += 1
