# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

import pandas as pd

def gastos_verduleria():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo
    "verduleria.csv".
    Esta función debe informar la cantidad de productos comprados.
    '''
    #Tu código aca:
    df = pd.read_csv('datos/verduleria.csv')
    

    return df.shape[0]