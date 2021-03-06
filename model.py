import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date

engine = sqlalchemy.create_engine('postgresql://ejymphuvhamxdb:9ef0228e8e8f9dcbdef3cca0bc340898bc779a2c6cbecb97fca3a2ccb13b1f32@ec2-34-230-115-172.compute-1.amazonaws.com:5432/d7c6mq728i0v83', echo=True)
Base = declarative_base()


class DraexVent(Base):
    __tablename__ = 'DraexVent'
    factura = sqlalchemy.Column(sqlalchemy.String(length=36), primary_key=True, nullable=False)
    clave_cliente = sqlalchemy.Column(sqlalchemy.String(length=20)) #, sqlalchemy.ForeignKey(''))
    proforma = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=1)
    tipo = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=False, default='A')
    estatus = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=False, default='O')
    tipo_cambio = sqlalchemy.Column(sqlalchemy.Numeric)
    clave_moneda = sqlalchemy.Column(sqlalchemy.String(length=3), default='USD') #, sqlalchemy.ForeignKey(''))
    factor = sqlalchemy.Column(sqlalchemy.Numeric)
    descripcion = sqlalchemy.Column(sqlalchemy.String(length=250))
    fecha = sqlalchemy.Column(sqlalchemy.Date, nullable=False, default=datetime.strptime('14/11/2021', "%d/%m/%Y"))
    observaciones = sqlalchemy.Column(sqlalchemy.String(length=250))
    clave_incoterm = sqlalchemy.Column(sqlalchemy.String(length=3)) #, sqlalchemy.ForeignKey(''))
    procesocompleto = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    NoOficio = sqlalchemy.Column(sqlalchemy.String(length=30))
    FechaOficio = sqlalchemy.Column(sqlalchemy.Date)
    transferencia = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    constancia = sqlalchemy.Column(sqlalchemy.String(length=20))
    ITA = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    Adicional1 = sqlalchemy.Column(sqlalchemy.String(length=60))
    Adicional2 = sqlalchemy.Column(sqlalchemy.String(length=60))
    Adicional3 = sqlalchemy.Column(sqlalchemy.String(length=60))
    tipo_factura = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=False, default='B')
    agregar = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    porcentajepeso = sqlalchemy.Column(sqlalchemy.Numeric, default='0.0')
    patente = sqlalchemy.Column(sqlalchemy.String(length=4))
    descri_vehiculo = sqlalchemy.Column(sqlalchemy.String(length=250))
    manifiesto = sqlalchemy.Column(sqlalchemy.String(length=20))
    proporcion = sqlalchemy.Column(sqlalchemy.Numeric)
    validado = sqlalchemy.Column(sqlalchemy.Boolean)
    usuario = sqlalchemy.Column(sqlalchemy.String(length=10)) #, sqlalchemy.ForeignKey(''))
    guia_aerea = sqlalchemy.Column(sqlalchemy.String(length=50))
    edocument = sqlalchemy.Column(sqlalchemy.String(length=30))
    expconfiable = sqlalchemy.Column(sqlalchemy.String(length=50))
    clave_destina = sqlalchemy.Column(sqlalchemy.String(length=20))
    clave_transportista = sqlalchemy.Column(sqlalchemy.String(length=20)) #, sqlalchemy.ForeignKey(''))
    trailer = sqlalchemy.Column(sqlalchemy.String(length=30))
    remesa = sqlalchemy.Column(sqlalchemy.SmallInteger)
    vendido_por = sqlalchemy.Column(sqlalchemy.String(length=20))
    sellos = sqlalchemy.Column(sqlalchemy.String(length=30))
    id_consolidado = sqlalchemy.Column(sqlalchemy.String(20))
    bultos = sqlalchemy.Column(sqlalchemy.Numeric)
    isEXD = sqlalchemy.Column(sqlalchemy.Boolean)
    pedimento_aper = sqlalchemy.Column(sqlalchemy.String(length=30))


def WriteDraexVent(head):
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(head)
    session.commit()


class DraexVentmate(Base):
    __tablename__ = 'DraexVentmate'
    id_ventmate = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = sqlalchemy.Column(sqlalchemy.String(length=36), sqlalchemy.ForeignKey('DraexVent.factura'), nullable=False)
    clave_material = sqlalchemy.Column(sqlalchemy.String(length=30), nullable=False) #, sqlalchemy.ForeignKey(''))
    cantidad = sqlalchemy.Column(sqlalchemy.Numeric)
    valorusd = sqlalchemy.Column(sqlalchemy.Numeric)
    pedimento = sqlalchemy.Column(sqlalchemy.String(length=20)) #, sqlalchemy.ForeignKey(''))
    clave_fraccion = sqlalchemy.Column(sqlalchemy.String(length=20)) #, sqlalchemy.ForeignKey(''))
    clave_pais = sqlalchemy.Column(sqlalchemy.String(length=3)) #, sqlalchemy.ForeignKey(''))
    calculado = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    desperdicio = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    consumo = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    incorporacion = sqlalchemy.Column(sqlalchemy.Numeric)
    merma = sqlalchemy.Column(sqlalchemy.Numeric)
    clave_ppse = sqlalchemy.Column(sqlalchemy.String(length=20)) #, sqlalchemy.ForeignKey(''))
    tratamiento = sqlalchemy.Column(sqlalchemy.SmallInteger)
    pedimento2 = sqlalchemy.Column(sqlalchemy.String(length=20))
    fecha_pedimento = sqlalchemy.Column(sqlalchemy.Date)
    adu_secc = sqlalchemy.Column(sqlalchemy.String(length=4))
    constancia = sqlalchemy.Column(sqlalchemy.String(length=40))
    fecha_constancia = sqlalchemy.Column(sqlalchemy.Date)
    TLCdocumento = sqlalchemy.Column(sqlalchemy.String(length=20))
    TLCfecha = sqlalchemy.Column(sqlalchemy.Date)
    TLCadvalorem = sqlalchemy.Column(sqlalchemy.Numeric)
    TLCclave_fraccion = sqlalchemy.Column(sqlalchemy.String(length=20)) #, sqlalchemy.ForeignKey(''))
    TLCtipo = sqlalchemy.Column(sqlalchemy.SmallInteger)
    DestinoITA = sqlalchemy.Column(sqlalchemy.SmallInteger)
    capturado = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=1)
    descargado = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    incorporacionpendiente = sqlalchemy.Column(sqlalchemy.Numeric)
    mermapendiente = sqlalchemy.Column(sqlalchemy.Numeric)
    busquedacompleta = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    id_padre = sqlalchemy.Column(sqlalchemy.Integer)
    descargado2 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    id_padre2 = sqlalchemy.Column(sqlalchemy.Integer)
    explotado = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    agregar = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=0)
    peso_gross = sqlalchemy.Column(sqlalchemy.Numeric)
    tarimas = sqlalchemy.Column(sqlalchemy.Integer)
    iva = sqlalchemy.Column(sqlalchemy.Numeric)
    TLCclave_pais = sqlalchemy.Column(sqlalchemy.String(length=20))
    clave_empaque = sqlalchemy.Column(sqlalchemy.String(length=30))
    id_expoprod = sqlalchemy.Column(sqlalchemy.Integer)
    clave_destina = sqlalchemy.Column(sqlalchemy.String(length=20))
    entrega = sqlalchemy.Column(sqlalchemy.String(length=20))
    boxes = sqlalchemy.Column(sqlalchemy.String(length=50))
    va = sqlalchemy.Column(sqlalchemy.Numeric)
    usuario = sqlalchemy.Column(sqlalchemy.String(length=10))
    peso_neto = sqlalchemy.Column(sqlalchemy.Numeric)
    pedimento_comp = sqlalchemy.Column(sqlalchemy.String(length=20))
    num_identificador = sqlalchemy.Column(sqlalchemy.String(length=5))
    cr_generado = sqlalchemy.Column(sqlalchemy.Boolean)
    id_producto = sqlalchemy.Column(sqlalchemy.Integer)
    cantidad_despedicio = sqlalchemy.Column(sqlalchemy.Numeric)
    orden_produccion = sqlalchemy.Column(sqlalchemy.String(length=20))
    orden_fecha = sqlalchemy.Column(sqlalchemy.Date)
    archivo = sqlalchemy.Column(sqlalchemy.String(length=20))
    contrato = sqlalchemy.Column(sqlalchemy.String(length=50))
    corte = sqlalchemy.Column(sqlalchemy.String(length=50))
    descripcion_ped = sqlalchemy.Column(sqlalchemy.String(length=250))
    ensamblado = sqlalchemy.Column(sqlalchemy.Boolean)
    relacion_desca = sqlalchemy.Column(sqlalchemy.String(length=30))
    orden_venta = sqlalchemy.Column(sqlalchemy.String(length=30))
    adicional1 = sqlalchemy.Column(sqlalchemy.String(length=50))
    adicional2 = sqlalchemy.Column(sqlalchemy.String(length=50))
    adicional3 = sqlalchemy.Column(sqlalchemy.String(length=50))
    serie = sqlalchemy.Column(sqlalchemy.String(length=30))
    completar_proceso = sqlalchemy.Column(sqlalchemy.String(length=10))
    getid = sqlalchemy.Column(sqlalchemy.String(length=15))
    mermacomoporcentaje = sqlalchemy.Column(sqlalchemy.Boolean)
    merma_cantidadpendiente = sqlalchemy.Column(sqlalchemy.Numeric)
    clave_almacen = sqlalchemy.Column(sqlalchemy.String(length=10)) #, sqlalchemy.ForeignKey(''))
    ieps = sqlalchemy.Column(sqlalchemy.Numeric)
    secuencia = sqlalchemy.Column(sqlalchemy.Integer)
    pedimento_prov = sqlalchemy.Column(sqlalchemy.String(length=20))
    cost_center = sqlalchemy.Column(sqlalchemy.String(length=20))
    DesperdicioPendiente = sqlalchemy.Column(sqlalchemy.Numeric, nullable=False, default=0)
    Desperdicios = sqlalchemy.Column(sqlalchemy.Numeric)
    bln_desperdicio = sqlalchemy.Column(sqlalchemy.Boolean)


def WriteDraexVentmate(vmaterial):
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(vmaterial)
    session.commit()


class DraexMate(Base):
    __tablename__ = 'DraexMate'
    clave_material = sqlalchemy.Column(sqlalchemy.String(length=30), primary_key=True, nullable=False)
    clave_familia = sqlalchemy.Column(sqlalchemy.String(length=20))
    clave_categoria = sqlalchemy.Column(sqlalchemy.String(length=5))
    descripcion = sqlalchemy.Column(sqlalchemy.String(length=250), nullable=False)
    precio_unitario = sqlalchemy.Column(sqlalchemy.Numeric(precision=6))
    comprado = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    vendido = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    padre = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    hijo = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    tipo = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    clave_fraccion = sqlalchemy.Column(sqlalchemy.String(length=20))
    clave_fraccion3 = sqlalchemy.Column(sqlalchemy.String(length=20))
    adicional1 = sqlalchemy.Column(sqlalchemy.String(length=50))
    adicional2 = sqlalchemy.Column(sqlalchemy.String(length=50))
    adicional3 = sqlalchemy.Column(sqlalchemy.String(length=50))
    marca = sqlalchemy.Column(sqlalchemy.String(length=100))
    modelo = sqlalchemy.Column(sqlalchemy.String(length=50))
    depreciacion = sqlalchemy.Column(sqlalchemy.Integer)
    descripcion2 = sqlalchemy.Column(sqlalchemy.String(length=250))
    clave_fraccionusa = sqlalchemy.Column(sqlalchemy.String(length=20))
    clave_pais = sqlalchemy.Column(sqlalchemy.String(length=3))
    va = sqlalchemy.Column(sqlalchemy.Numeric(precision=6))
    clave_pais2 = sqlalchemy.Column(sqlalchemy.String(length=3))
    tipo_mate = sqlalchemy.Column(sqlalchemy.Integer)
    consignado = sqlalchemy.Column(sqlalchemy.Boolean)
    desensamble = sqlalchemy.Column(sqlalchemy.Boolean)
    regla2da = sqlalchemy.Column(sqlalchemy.Boolean)
    regimen = sqlalchemy.Column(sqlalchemy.String(length=2))
    actualizado = sqlalchemy.Column(sqlalchemy.Boolean)
    clave_r8a = sqlalchemy.Column(sqlalchemy.String(length=20))
    completar_proceso = sqlalchemy.Column(sqlalchemy.String(length=10))
    estatus_co = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    cert_origen = sqlalchemy.Column(sqlalchemy.String(length=20))
    fecha_co = sqlalchemy.Column(sqlalchemy.Date)
    isEXD = sqlalchemy.Column(sqlalchemy.Boolean)
    clave_desperdicio = sqlalchemy.Column(sqlalchemy.String(length=20))


def WriteDraexMate(material):
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(material)
    session.commit()
