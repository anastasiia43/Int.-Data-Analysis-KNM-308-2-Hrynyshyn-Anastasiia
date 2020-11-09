import matplotlib.pyplot as plt
import math





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

            if list_plot[count] == "line" :

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



