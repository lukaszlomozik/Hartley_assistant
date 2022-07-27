import numpy as np
import matplotlib.pyplot as plt
from sympy import var
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class ControlInputLevel:
    def __init__(self, input_level_factors):
        self.input = input_level_factors

    def control_levels(self):
        if self.input.count("X") > 1 or self.input.count("X") < 1 or self.input.count("Y") > 1 or self.input.count(
                "Y") < 1:
            return False
        else:
            return True


class MakePlot3D:

    def __init__(self, input_level_factors, axis_name):
        self.levels = input_level_factors
        self.str_levels = []
        self.levels_legends = []
        self.axis_name = axis_name

        print(f"levels_{self.levels}")
        print(f"self.axis_name_{self.axis_name}")

    def make_factors(self):
        x = np.linspace(-1, 1, 50)
        y = np.linspace(-1, 1, 50)
        self.X, self.Y = np.meshgrid(x, y)
        for i, n in enumerate(self.levels):
            if n == "X":
                self.levels[i] = self.X
                self.str_levels.insert(i, var("x"))
            elif n == "Y":
                self.levels[i] = self.Y
                self.str_levels.insert(i, var("y"))
            else:
                self.levels[i] = int(n)
                self.str_levels.insert(i, int(n))
                self.levels_legends.insert(i, int(n))
        return

    def make_str_equation(self, z_axis):
        equation = list(str(z_axis))
        for n, i in enumerate(equation):
            if n != len(equation) - 1:
                if equation[n] == "x" and equation[n + 1] == "*" and equation[n + 2] == "*":
                    equation[n] = "$x^2$"
                    equation.pop(n + 1)
                    equation.pop(n + 1)
                    equation.pop(n + 1)
                if equation[n] == "y" and equation[n + 1] == "*" and equation[n + 2] == "*":
                    equation[n] = "$y^2$"
                    equation.pop(n + 1)
                    equation.pop(n + 1)
                    equation.pop(n + 1)
        for n, i in enumerate(equation):
            if equation[n] == "*":
                equation.pop(n)
        str_equation = ""
        for i in equation:
            str_equation += i
        self.str_equation = str_equation

    def make_plot(self, z_axis, do_report=False, color="viridis", width=6, height=6, angle=20):
        fig = plt.figure(figsize=[width, height])
        ax = fig.add_subplot(1, 1, 1, projection='3d', azim=-130, elev=angle)

        surf = ax.plot_surface(self.X, self.Y, z_axis, rstride=1, cstride=1,
                               cmap=color)
        y = 0.2
        for i, n in enumerate(self.axis_name):
            if self.axis_name[n] != "X" and self.axis_name[n] != "Y":
                ax.text2D(1.0, y, f"{self.axis_name[n]} = {list(self.axis_name.keys())[i]}", transform=ax.transAxes,
                          fontsize=11.5)
                y = y - 0.05
            elif self.axis_name[n] == "X":
                ax.set_xlabel(n, fontsize=13, labelpad=5)
            elif self.axis_name[n] == "Y":
                ax.set_ylabel(n, fontsize=13, labelpad=5)
        ax.zaxis.set_rotate_label(False)
        ax.set_zlabel("t", fontsize=13, labelpad=5)
        fig.colorbar(surf, shrink=0.5, aspect=10, pad=0.1)
        plt.title(f"Z = {self.str_equation}", pad=20, fontsize=11.5)
        if do_report:
            plt.savefig("plot3d.png")
            plt.close()
        else:
            plt.show()
