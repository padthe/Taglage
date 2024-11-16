from tabulate import tabulate


def print_train_data(trains):
    headers = ['Tågnummer', 'Annonserad tid', 'Beräknad tid', 'Operatör']
    table = [[train['Tågnummer'], train['Annonserad tid'], train['Beräknad tid'], train['Operatör']] for train in trains ]
    print(tabulate(table, headers=headers, tablefmt='grid'))
