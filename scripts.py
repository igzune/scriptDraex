from datetime import datetime
import pandas as pd
import json
import os
import shutil

import sqlalchemy.exc

import model
import asyncio


def ExcelToJson(file_name, headers):
    dir_excel = 'C:/python3_9_1/proyecto2/Draex/script/archivos/'
    dir_ex_read = 'C:/python3_9_1/proyecto2/Draex/script/archivos/Procesado/'
    df = pd.read_excel(dir_excel+file_name, sheet_name=0, header=headers)
    result = df.to_json(orient='index')
    js = json.loads(result)
    try:
        shutil.move(dir_excel + file_name, dir_ex_read)
        return js
    except shutil.Error:
        return f'The file {file_name} already exist in that directory {dir_ex_read}'


def WriteToDbJson(excel):
    mateJson = ExcelToJson(excel, 0)
    for x in mateJson:
        mate = model.DraexVentmate(
            factura=mateJson[x]['FACTURA'],
            clave_material=mateJson[x]['No PARTE HIJO'],
            incorporacion=mateJson[x]['INCORPORACION'],
            va=mateJson[x]['VA'],
            consumo=1,
            descargado=0,
            capturado=1,
            ensamblado=0
        )
        model.WriteDraexVentmate(mate)
    return f'The file {excel} was load to db. '


def MultiLoad():
    dirExcel = 'C:/python3_9_1/proyecto2/Draex/script/archivos/'
    # The variable filesX save the files names in a directory, and the variable save the files names with .xls or .xlsx.
    filesX = os.listdir(dirExcel)
    excelNames = [x for x in filesX if x[:2] != '~$' and x[-5:] == '.xlsx' or x[-4:] == '.xls']
    write = []
    for x in excelNames:
        try:
            result = WriteToDbJson(x)
            write.append(result)
        except sqlalchemy.exc.IntegrityError as e:
            return print('An error was popped up'+str(e.args)+x)
        else:
            return print(write)

# Del layout, se toma el No parte padre y el numero de factura, para buscar el id_ventmate de este y guardarlo en
# id_producto, esto por cada partida del layout de carga
