import os
import model as m
from datetime import datetime


def main():
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    header = m.DraexVent(
        factura='DPA2606195',
        proforma=1,
        tipo='A',
        estatus='S',
        fecha=datetime.strptime('14/11/2021', "%d/%m/%Y"),
        procesocompleto=1,
        transferencia=0,
        tipo_factura='B',
        agregar=1,
        ITA=0
    )

    mate = m.DraexVentmate(
        factura='DPA2606195',
        clave_material='aslasdfasd'
    )

    m.WriteDraexVent(header)
    m.WriteDraexVentmate(mate)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

