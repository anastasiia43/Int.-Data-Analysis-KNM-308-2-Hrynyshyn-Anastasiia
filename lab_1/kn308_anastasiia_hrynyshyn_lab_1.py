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


if __name__ == '__main__':

    database = pandas.read_csv('../DATABASE.csv', delimiter=';')

    parser(database)
    kn308_anastasiia_hrynyshyn_plot.main_fun(database)
