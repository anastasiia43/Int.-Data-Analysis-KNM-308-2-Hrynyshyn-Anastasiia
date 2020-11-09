import numpy
import pandas
import kn308_anastasiia_hrynyshyn_plot


def parser(database):
    # date translation
    database['day/month'] = database['day/month'].astype(str) + '2019'
    database['day/month'] = pandas.to_datetime(database['day/month']).dt.strftime('%d-%m-%y')
    # time transfer
    database['Time'] = pandas.to_datetime(database['Time']).dt.strftime('%H:%M')
    #
    database['Temperature'] = pandas.to_numeric(database['Temperature'], errors='coerce')
    #
    database['Humidity'] = database['Humidity'].map(lambda x: x.rstrip('%'))
    database['Humidity'] = numpy.round(pandas.to_numeric(database['Humidity']) * 0.01, 3)
    #
    database['Wind Speed'] = database['Wind Speed'].map(lambda x: x.rstrip(' mph'))
    database['Wind Speed'] = pandas.to_numeric(database['Wind Speed'], errors='coerce')
    #
    database['Wind Gust'] = database['Wind Gust'].map(lambda x: x.rstrip(' mph'))
    database['Wind Gust'] = pandas.to_numeric(database['Wind Gust'], errors='coerce')
    #
    database['Pressure'] = numpy.round(pandas.to_numeric(database['Pressure'].str.replace(",", '.'), errors='coerce'),1)
    database['Precip Accum'] = pandas.to_numeric(database['Precip Accum'], errors='coerce')
    #
    database.set_index('day/month', inplace = True)

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


def main_fun(database):
    x, y, list_plot = list(), list(), list()
    n = int(input("Enter number graph: "))
    for i in range(0, n):
        type_plot, cor_x, cor_y = entry_data(database)
        x.append(cor_x)
        y.append(cor_y)
        list_plot.append(type_plot)
    kn308_anastasiia_hrynyshyn_plot.build_plot(x, y, n, list_plot, database)

if __name__ == '__main__':

    database = pandas.read_csv('../DATABASE.csv', delimiter=';')

    parser(database)
    main_fun(database)


