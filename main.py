import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Message as ms
import view
import pandas as pd


class Main:
    def __init__(self):
        self.view = view.Ui_MainWindow()

    def opening_view(self):
        self.app = QtWidgets.QApplication(sys.argv)
        # apply_stylesheet(self.app, "dark_cyan.xml", light_secondary=True)
        MainWindow = QtWidgets.QMainWindow()
        self.view.setupUi(MainWindow)
        MainWindow.show()
        self.control_view_pushbuttons()
        # self.change_theme()
        sys.exit(self.app.exec_())

    def open_plots_view(self):
        try:
            self.plot_window = QtWidgets.QMainWindow()
            print('self.plot_window = QtWidgets.QMainWindow()')
            self.plot_window_ui = view.Ui_PlotWindow(self.view.coefficient_spinBox.value(), self.factors_name)
            print('self.plot_window_ui = view.Ui_PlotWindow(self.view.coefficient_spinBox.value(), self.factors_name)')
            self.plot_window_ui.setupUi(self.plot_window)
            self.plot_window.show()
            self.control_plotview_pushbuttons()
        except:
            ms.error_dialog("Brak danych")
            return

    def open_report_view(self):
        try:
            self.report_window = QtWidgets.QMainWindow()
            self.report_window_ui = view.ReportView(self.view.coefficient_spinBox.value(), self.factors_name)
            self.report_window_ui.setupUi(self.report_window)
            self.report_window.show()
            self.control_reportview_pushbuttons()
        except:
            ms.error_dialog("Brak danych")
            return

    def open_optimization_view(self):
        try:
            self.optimization_window = QtWidgets.QMainWindow()
            self.optimization_window_ui = view.OptimizationView(self.view.coefficient_spinBox.value(),
                                                                self.factors_name)
            self.optimization_window_ui.setupUi(self.optimization_window)
            self.optimization_window.show()
            self.control_optimization_pushbuttons()
        except:
            ms.error_dialog("Brak danych")
            return

    def display_results(self):
        res = self.an.evaluation
        self.results = res.pred_data
        frame = {'Dane rzeczywiste': self.an.mean, 'Wyniki regresji': self.results}
        results = pd.DataFrame(frame)
        self.view.textEdit.setText(f"{results}\n")
        self.view.textEdit.append(f"B????dy ??redniokwadratowe\n{res.dev}\n")
        self.view.textEdit.append(f"Suma b????d??w ??redniokwadratowych\n{round(res.sum_dev, 5)}\n")
        self.view.textEdit.append(f"Wariancja adekwatno??ci\n{round(res.adequacy_var, 5)}\n")
        self.view.textEdit.append("Test Fishera - Snedecora:\n")
        self.view.textEdit.append(f"Warto???? krytyczna wp????czynnika F\n{round(res.crit_F_factor, 5)}\n")
        self.view.textEdit.append(f"Warto???? empiryczna wp????czynnika F\n{round(res.empi_F_factor, 5)}\n")
        self.view.textEdit.append("Ocena adekwatno??ci modelu:")
        self.view.textEdit.append(
            f"poniewa?? {round(res.empi_F_factor, 5)} {res.mark} {round(res.crit_F_factor, 5)}")
        self.view.textEdit.append(f"\n{res.rating}")

    '''
    def change_theme(self):
        print(self.view.actions)
        self.view.actions[0].triggered.connect(lambda: load_theme(self.view.actions[0].objectName()))
        self.view.actions[1].triggered.connect(lambda: load_theme(self.view.actions[1].objectName()))
        self.view.actions[2].triggered.connect(lambda: load_theme(self.view.actions[2].objectName()))
        self.view.actions[3].triggered.connect(lambda: load_theme(self.view.actions[3].objectName()))
        self.view.actions[4].triggered.connect(lambda: load_theme(self.view.actions[4].objectName()))
        self.view.actions[5].triggered.connect(lambda: load_theme(self.view.actions[5].objectName()))
        self.view.actions[6].triggered.connect(lambda: load_theme(self.view.actions[6].objectName()))
        self.view.actions[7].triggered.connect(lambda: load_theme(self.view.actions[7].objectName()))
        self.view.actions[8].triggered.connect(lambda: load_theme(self.view.actions[8].objectName()))
        self.view.actions[9].triggered.connect(lambda: load_theme(self.view.actions[9].objectName()))
        self.view.actions[10].triggered.connect(lambda: load_theme(self.view.actions[10].objectName()))
        self.view.actions[11].triggered.connect(lambda: load_theme(self.view.actions[11].objectName()))
        self.view.actions[12].triggered.connect(lambda: load_theme(self.view.actions[12].objectName()))
        self.view.actions[13].triggered.connect(lambda: load_theme(self.view.actions[13].objectName()))
        self.view.actions[14].triggered.connect(lambda: load_theme(self.view.actions[14].objectName()))
        self.view.actions[15].triggered.connect(lambda: load_theme(self.view.actions[15].objectName()))

        def load_theme(theme):
            print(theme)
            apply_stylesheet(self.app, theme, light_secondary=True)
        '''

    def control_view_pushbuttons(self):
        self.view.load_pushButton.clicked.connect(lambda: self.load_data())
        self.view.analysis_pushButton.clicked.connect(lambda: self.make_analysis())
        self.view.scatterplot_pushButton.clicked.connect(lambda: self.make_scatter_plot())
        self.view.plot3d_pushButton.clicked.connect(lambda: self.open_plots_view())
        self.view.report_pushButton.clicked.connect(lambda: self.open_report_view())
        self.view.template_pushButton.clicked.connect(lambda: self.make_template())
        self.view.optimalization_pushButton.clicked.connect(lambda: self.open_optimization_view())

    def control_plotview_pushbuttons(self):
        self.plot_window_ui.pushButton.clicked.connect(lambda: self.make_3dplot())

    def control_reportview_pushbuttons(self):
        self.report_window_ui.pushButton.clicked.connect(lambda: self.make_report())

    def control_optimization_pushbuttons(self):
        self.optimization_window_ui.OK_pushButton.clicked.connect(lambda: self.optimization())

    def load_data(self):
        import Data
        self.data = Data.DataLoad(self.view.repetitions_spinBox.value(),
                                  self.view.coefficient_spinBox.value())
        self.data.open_file()
        self.data.loading_hartley_matrix('hartley_matrix.xlsx')
        self.data.open_par('hartley_parameters.xlsx')
        '''
        file = 'Szablon.xlsx'
        data_file = pd.read_excel(file)
        matrix_file = pd.read_excel("hartley_matrix.xlsx")
        par_file = pd.read_excel("hartley_parameters.xlsx")
        print(data_file)
        
        if self.data.data_frame is not None:
            if self.data.checking_amount_data():
                if self.data.checking_content_data():
                    if self.data.loading_hartley_matrix(matrix_file) and True not in self.data.hm.isnull().values:
                        if self.data.open_par(par_file):
                            self.loading_error = False
                            ms.message_dialog("Dane wczytano pomy??lnie")
                            print(self.data.data_frame)
                        else:
                            ms.error_dialog("B????d pliku parametr??w")
                            return
                    else:
                        ms.error_dialog("B????d pliku matrycy")
                        return
                else:
                    ms.error_dialog("Nieprawid??owe dane")
                    return
            else:
                ms.error_dialog("Nieprawid??owa ilo???? danych")
                return
        else:
            ms.error_dialog("Plik jest pusty")
            return
        '''
        self.factors_name = []
        for i in range(self.view.coefficient_spinBox.value()):
            self.factors_name.append(self.data.data_frame.keys()[i])

    def make_analysis(self):
        import Analysis
        try:
            self.an = Analysis.Analysis(self.data.data_frame, self.view.significante_doubleSpinBox.value(),
                                        self.view.coefficient_spinBox.value(),
                                        self.view.repetitions_spinBox.value(), self.data.hm, self.data.par)
        except:
            ms.error_dialog("Brak danych")
            return
        print('poprawnie wczyta??em dane do analizy')
        self.an.matrix_exponentiation()
        self.an.intra_matrix_multiplication()
        self.an.average_samples()
        self.an.matrix_multiplication()
        self.an.variance()
        self.an.summation()
        self.an.calculation_coefficients_values()
        self.an.tSudent_test()
        self.an.significance_test()
        self.an.resetting_irrelevant_coef()
        self.an.calculation_regression_results()
        self.an.evaluating_results()
        return self.display_results()

    def make_scatter_plot(self, do_report=False):
        try:
            import scatterplot as sc
            self.samples = self.data.data_frame.count(axis=0, numeric_only=True)[1]
            reg_res = list(self.an.regression_results.values())
            sc.make_plot(num_samples=self.samples, first_curve=reg_res, second_curve=self.an.mean,
                         leg_first_curve="Funkcja obiektu (z)", leg_second_curve='Rzeczywiste dane (x)',
                         do_report=do_report)
        except:
            ms.error_dialog("brak danych")
            return

    def make_3dplot(self):
        import plot3d
        print('import 3d')
        input_level_factors = []
        axis_name = {}
        for i in range(self.view.coefficient_spinBox.value()):
            input_level_factors.append(self.plot_window_ui.comboBox[f"comboBox_{i}"].currentText())
            axis_name[f"{self.factors_name[i]}"] = self.plot_window_ui.comboBox[f"comboBox_{i}"].currentText()
        print(input_level_factors)
        print(f"axis_name: {axis_name}")
        self.contr = plot3d.ControlInputLevel(input_level_factors)
        if not self.contr.control_levels():
            ms.error_dialog("Nieprawid??owe poziomy czynnik??w wej??ciowych")
            return
        else:
            plot = plot3d.MakePlot3D(input_level_factors, axis_name)
            plot.make_factors()
            factors_for_equation = self.an.calc_z_axis(plot.str_levels, decimal=2)
            factors_for_plots = self.an.calc_z_axis(plot.levels)
            plot.make_str_equation(factors_for_equation)
            plot.make_plot(factors_for_plots)

    def make_report(self):
        try:
            import report_maker
            print('report_maker')
            res = self.an.evaluation
            rpt = report_maker.Report()
            rpt.create_file()
            rpt.add_heading("B????d modelu")
            rpt.add_table(columns=["??rednia danych rzeczywistych", "Wynik funkcji regresji", "B????d ??redniokwadratowy"],
                          values=[list(self.an.mean), list(self.results), list(res.dev)], rd=4)
            rpt.add_text(f"\nSuma b????d??w ??redniokwadratowych: {round(res.sum_dev, 5)}")
            self.make_scatter_plot(do_report=True)
            rpt.add_picture("scatterplot.png")
            rpt.add_heading("Istotno???? modelu")
            rpt.add_text(f"Wariancja adekwatno??ci: {round(res.adequacy_var, 5)}")
            rpt.add_text("Ocena adekwatno??ci modelu:", bold=True)
            rpt.add_text(f"Warto???? krytyczna wp????czynnika F: {round(res.crit_F_factor, 5)}")
            rpt.add_text(f"Warto???? empiryczna wp????czynnika F: {round(res.empi_F_factor, 5)}")
            rpt.add_text(
                f"poniewa?? {round(res.empi_F_factor, 5)} {res.mark} {round(res.crit_F_factor, 5)} {res.rating}",
                bold=True)
            rpt.add_heading("Analiza wynik??w")

            comb = self.an.calc_factors_combination()
            axis_name = {}
            import plot3d
            loop_lenght = len(comb)
            for i in range(loop_lenght):
                for n in range(len(self.factors_name)):
                    axis_name[f"{self.factors_name[n]}"] = comb[i][n]
                plot = plot3d.MakePlot3D(input_level_factors=comb[i], axis_name=axis_name)
                plot.make_factors()
                factors_for_equation = self.an.calc_z_axis(plot.str_levels, decimal=2)
                factors_for_plots = self.an.calc_z_axis(plot.levels)
                plot.make_str_equation(factors_for_equation)
                plot.make_plot(factors_for_plots, do_report=True,
                               color=self.report_window_ui.comboBox.currentText(),
                               angle=int(self.report_window_ui.spinBox.value()),
                               width=int(self.report_window_ui.spinBox_2.value()),
                               height=int(self.report_window_ui.spinBox_3.value()))
                axis_name = {}
                self.report_window_ui.progressBar.setValue((i + 1) * 100 / loop_lenght)
                rpt.add_picture("plot3d.png")
            try:
                rpt.save_file("test.docx")
            except IOError:
                ms.error_dialog("Nie mo??na zapisa?? pliku! Zamknij plik raportu i spr??buj ponownie")
            ms.message_dialog("Generowanie raportu zako??czone")
        except:
            ms.error_dialog("Brak danych")

    def make_template(self):
        import template_maker
        temp = template_maker.MakeXlsFile(number_factors=self.view.coefficient_spinBox.value(),
                                          number_repetitions=self.view.repetitions_spinBox.value())
        temp.create_file()
        temp.make_columns()
        temp.save_file()
        ms.message_dialog("Utworzono szablon")

    def optimization(self):
        import optimization
        self.steps = [self.optimization_window_ui.variables_doubleSpinBox[f"variables_doubleSpinBox {i}"].value() for i
                      in
                      range(self.view.coefficient_spinBox.value())]
        if self.check_volatility_steps() is False:
            return
        opt_bf = optimization.BruteForce(file="exl.xlsx", coefficients=self.an.regcoef,
                                         number_of_coef=self.view.coefficient_spinBox.value(),
                                         step=self.steps, goal=self.optimization_window_ui.goal_comboBox.currentText())
        opt_bf.data_cleaning()
        opt_bf.calc_central_values()
        opt_bf.calc_units_variation()
        opt_bf.factors_generator()
        opt_bf.factors_coded()
        opt_bf.substituting_variables()
        for i, n in enumerate(opt_bf.factors_combination):
            print(n)
            opt_bf.calc_results(n)
            self.optimization_window_ui.progressBar.setValue((i + 1) * 100 / len(opt_bf.factors_combination))
        opt_bf.factors_decoded()
        if self.optimization_window_ui.goal_comboBox.currentText() == "Min":
            self.optimization_window_ui.textEdit.append(f"Funkcja osi??ga swoje minimum r??wne {opt_bf.results} \
            przy warto??ciach czynnik??w wej??ciowych:\n")
        if self.optimization_window_ui.goal_comboBox.currentText() == "Max":
            self.optimization_window_ui.textEdit.append(f"Funkcja osi??ga swoje maksimum r??wne {opt_bf.results}\
            przy warto??ciach czynnik??w wej??ciowych:\n")
        for i in range(len(opt_bf.decoded_factors)):
            self.optimization_window_ui.textEdit.append(
                f"{self.factors_name[i]} = {round(opt_bf.decoded_factors[i], 4)}")

    def check_volatility_steps(self):
        print("check_volatility_steps")
        text = "Mo??liwe, ??e ustawione kroki zmienno??ci znacznie wyd??u???? operacj??. Czy na pewno chcesz kontynuowa???"
        for i in self.steps:
            if i == 0:
                ms.error_dialog("Krok zmienno??ci nie mo??e by?? zerowy")
                return False
            if len(list(str(i))) >= 5:
                if ms.question_dialog(text) is True:
                    return True
                else:
                    return False


if __name__ == "__main__":
    main = Main()
    main.opening_view()
