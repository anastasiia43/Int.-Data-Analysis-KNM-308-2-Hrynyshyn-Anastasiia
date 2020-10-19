import matplotlib.pyplot as plt
import math


def main_fun(database):
    x, y, list_plot = list(), list(), list()
    n = int(input("Enter number graph: "))
    for i in range(0, n):
        type_plot, cor_x, cor_y = entry_data(database)
        x.append(cor_x)
        y.append(cor_y)
        list_plot.append(type_plot)
    build_plot(x, y, n, list_plot, database)


def build_plot(x, y, n, list_plot, database):
    if math.ceil(n / 2) == 1:
        col = math.ceil(n / 2)
        row = n
    else:
        col = 2
        row = math.ceil(n / 2)

    fig, axs = plt.subplots(nrows=row, ncols=col, figsize=(20, 10))
    fig.suptitle('Lab 1')
    count = 0
    for i in range(0, row):
        if n - i * 2 != 1 and n != 2:
            m = 2
        else:
            m = 1
        for j in range(0, m):

            if list_plot[count] == "line":

                if n == 2:
                    line(database, axs[i], x[i])
                elif n == 1:
                    line(database, axs, x[i])
                else:
                    line(database, axs[i, j], x[count])

            elif list_plot[count] == "pie":
                if n == 2:
                    pie(database, axs[i], x[i])
                elif n == 1:
                    pie(database, axs, x[i])
                else:
                    pie(database, axs[i, j], x[count])

            elif list_plot[count] == "bar":
                if n == 2:
                    bar(database, axs[i], y[i], x[i])
                elif n == 1:
                    bar(database, axs, y[i], x[i])
                else:
                    bar(database, axs[i, j], y[count], x[count])

            elif list_plot[count] == "scatter":
                if n == 2:
                    scatter(database, axs[i], y[i], x[i])
                elif n == 1:
                    scatter(database, axs, y[i], x[i])
                else:
                    scatter(database, axs[i, j], y[count], x[count])

            elif list_plot[count] == "box":
                if n == 2:
                    box(database, axs[i], x[i])
                elif n == 1:
                    box(database, axs, x[i])
                else:
                    box(database, axs[i, j], x[count])

            elif list_plot[count] == "hist":
                if n == 2:
                    hist(database, axs[i], x[i])
                elif n == 1:
                    hist(database, axs, x[i])
                else:
                    hist(database, axs[i, j], x[count])

            count += 1
    plt.show()


def line(database, axs, x):
    axs.plot(database.groupby([x]).count())
    axs.set(xlabel=x, ylabel="Count")
    axs.xaxis.set_tick_params(rotation=90)


def pie(database, axs, x):
    database.groupby([x]).size().plot.pie(ax=axs)
    axs.set(xlabel=x, ylabel="")


def bar(database, axs, y, x):
    if y == 'none':
        axs.bar(database[x].unique(), database[x].value_counts(),
                label=database[x].name)
        axs.set(xlabel=x, ylabel="Count")
    else:
        axs.bar(database[x], database[y])
        axs.set(xlabel=x, ylabel=y)
    axs.xaxis.set_tick_params(rotation=90)


def scatter(database, axs, y, x):
    if y == 'none':
        axs.scatter(database[x].unique(), database[x].value_counts(),
                    label=database[x].name)
        axs.set(xlabel=x, ylabel="Count")
    else:
        axs.scatter(database[x], database[y])
        axs.set(xlabel=x, ylabel=y)
    axs.xaxis.set_tick_params(rotation=90)


def box(database, axs, x):
    axs.boxplot(database[x])
    axs.set(ylabel=x)


def hist(database, axs, x):
    axs.hist(database[x], edgecolor='black')
    axs.set(xlabel=x, ylabel="Count")
    axs.xaxis.set_tick_params(rotation=90)


def entry_data(data):
    type_plot = input("type plot (line/pie/bar/scatter/box/hist): ")
    x, y = "none", "none"

    name_cols = list()
    name_cols.append("day/month")
    for col in data.columns:
        name_cols.append(col)

    if type_plot == "pie" or type_plot == "line" or type_plot == "hist":
        print(*name_cols, sep=", ")
        while x not in name_cols:
            x = input("Input date: ")

    elif type_plot == "box":
        print(*name_cols[2:5], *name_cols[6:11], sep=", ")
        while x not in name_cols[2:5] and x not in name_cols[6:11]:
            x = input("Input data: ")

    elif type_plot == "scatter" or type_plot == "bar":
        print(*name_cols[1:], sep=", ")
        while x not in name_cols or (y not in name_cols and y != "none"):
            x = input("Input x: ")
            y = input("Input y (or none) : ")

    return type_plot, x, y
