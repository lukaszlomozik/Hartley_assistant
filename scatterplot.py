import matplotlib.pyplot as plt


def make_plot(num_samples, first_curve, second_curve, leg_first_curve, leg_second_curve, do_report):
    print("scatter_chart")

    plt.plot(range(0, num_samples, 1), first_curve, ".-r")
    max_y_axis = [max(first_curve), max(second_curve)]
    max_y = (max(max_y_axis)) + 0.1 * (max(max_y_axis))
    min_y_axis = [min(first_curve), min(second_curve)]
    min_y = (min(min_y_axis)) - 0.1 * (min(min_y_axis))
    plt.plot(range(0, num_samples, 1), second_curve, ".-g")
    plt.axis(
        [-1, num_samples, min_y, max_y])
    plt.legend((leg_first_curve, leg_second_curve),
               loc='upper right')
    plt.title("Wykres rozrzutu")
    if do_report:
        plt.savefig("scatterplot.png")
        plt.close()
    else:
        plt.show()
    """
    plt.savefig("line_plot2.png")
    ui.scatter_chart_plot_2.setPixmap(QtGui.QPixmap("line_plot2.png"))
    ui.scatter_chart_plot_2.setScaledContents(True)
    ui.scatter_chart_plot_2.setObjectName("scatter_chart")
    ui.scatter_chart_plot_2.setMargin(-20)
    if plot:
        plt.show()
    else:
        plt.close()
    """
