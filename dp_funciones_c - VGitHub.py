# -----------------------------------------------------------------------------
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # #    INDICE   # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#   DEBIDO A LAS CONSTANTES MEJORAS INTRODUCIDAS, A LAS CORRECCIONES, Y A LA
#   INCORPORACION DE NUEVAS FUNCIONES, EL SIGUIENTE INDICE ESTA DESACTUALIZADO
# 
# -----------------------------------------------------------------------------
#                               CODIGOS GENERALES
# -----------------------------------------------------------------------------
# Identificador de cliente:    Linea 50.
# Identificador de usuarios
# Interfaz_composicion:        Linea 340
# Interfaz_honorario:          Linea 565
# Interfaz_rendimiento:        Linea 800
# usuario                      Linea 1040
# Rendimiento de todo el plazo Linea 1040

# -----------------------------------------------------------------------------
#                                BULLMARKET
# -----------------------------------------------------------------------------
# Split.                       Linea 1260.
# Composicion de cartera (cambio liq) Linea 1270.
# Honorarios                   Linea 2080
# Rendimiento un periodo       Linea 2450

# -----------------------------------------------------------------------------
#                                IEB
# -----------------------------------------------------------------------------
# Split.                       Linea 3590
# Composicion de cartera       Linea 2790
# Honorarios                   Linea 4450
# Rendimiento un periodo       Linea 4840

# -----------------------------------------------------------------------------
#                                BALANZ
# -----------------------------------------------------------------------------
# Composicion de cartera       Linea 6000
# Honorarios                   Linea 4060
# Rendimineto un periodo       Linea 6740

# -----------------------------------------------------------------------------
#                 OTROS, CONCATENACION, MOVIMIENTOS y GRAFICAS
# -----------------------------------------------------------------------------
# Otros - Retiros y depositos
# Concatenacion
# Ultimas lineas. Estan los de las tres alycs.
# Graficas de las tres alycs
# Rendimiento neto de las tres alycs

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def cliente(alyc='', nombre_cliente='', numero_interno=0, dni=0, usuario = 1):
    
    """
    ---------------------------------------------------------------------------
                                  ¿QUE HACE EL CODIGO?
    Genera un dataframe o tabla con informacion sobre el nombre del cliente, el
    numero de cliente (comitente), y si corresponde, la fecha de movimientos (dato
    clave en el caso de los clientes de bull).
    
    El codigo requiere la definicion de dos datos, la alyc donde se encuentra 
    la cuenta del cliente y un identificador del cliente, su nombre, numero interno,
    o dni. Respecto de estos identificadores, el codigo prioriza la busqueda de
    datos utilizando el nombre completo del cliente, y si este no se tipea o se
    tipea mal, busca a partir del numero interno, pero si con este sucede lo mismo,
    entonces busca utilizando el dni del cliente.
    
    Si algun parametro clave se escribe mal o no se tipea, el codigo dara aviso.
    ---------------------------------------------------------------------------
    
    Parametros
    ----------
    alyc : tipo string.
    
        DESCRIPCION.
        Es el nombre de la alyc. Puede ser Bull, Ieb, o Balanz. No importa como
        se escriba el nombre, si con mayusculas o acentos.
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre completo del cliente tal cual figura en la comitente (este
        es el que figura en nuestros archivos). No importa si se escribe con ma
        yusculas o acentos.
        Valor por defecto: ''.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero interno que la empresa asigna a cada cliente.
        Valor por defecto: 0.
        
    dni : tipo integer.
    
        DESCRIPCION.
        Es el numero de dni del cliente. Debe escribirse sin puntos separadores. 
        Valor por defecto: 0.
        
    Resultado
    -------
    Genera un dataframe o tabla con informacion sobre el nombre del cliente, el
    numero de cliente (comitente), y si corresponde, la fecha de movimientos (dato
    clave en el caso de los clientes de bull)
    
    
    """
    
    from unidecode import unidecode
    import pandas as pd
    import os
    import warnings


    # Ignorar la advertencia específica
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl.worksheet.header_footer")
    
    # -----------------------------------------------------------------------------
    try:
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
            
        directorio_clientes=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS'
        nombre_archivo_clientes='Base de Datos de Clientes'
        
        direccion_directorio_bull=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket'
        # ACLARACION: Solo usamos lo de BULL porque el objetivo es conocer la 'fecha de  
        # movimientos' y con IEB y Balanz la misma no existe.
        
        
        # -----------------------------------------------------------------------------
        # Tratamiento del nombre del cliente introducido
        nombre_cliente = nombre_cliente.title()
        nombre_cliente = unidecode(nombre_cliente)
        
        alyc = alyc.title()
        alyc = unidecode(alyc)
        
        dni = float(dni)
        
        # -----------------------------------------------------------------------------
        listado_clientes=pd.read_excel(f'{directorio_clientes}/{nombre_archivo_clientes}.xlsx',
                                        header = 0)
        listado_clientes.set_index('numero_interno',inplace=True)
        listado_clientes.dropna(subset=['nombre','comitente'],inplace = True)
        
        for i in listado_clientes.index:
            listado_clientes.loc[i,'nombre'] = str(listado_clientes.loc[i,'nombre'])
            listado_clientes.loc[i,'alyc'] = str(listado_clientes.loc[i,'alyc'])
            
        for i in listado_clientes.index:
            listado_clientes.loc[i,'nombre'] = listado_clientes.loc[i,'nombre'].title()
            listado_clientes.loc[i,'nombre'] = unidecode(listado_clientes.loc[i,'nombre'])
        
        for i in listado_clientes.index:
            listado_clientes.loc[i,'alyc'] = listado_clientes.loc[i,'alyc'].title()
            listado_clientes.loc[i,'alyc'] = unidecode(listado_clientes.loc[i,'alyc'])
            
            
        try: # BLOQUE POR SI TENEMOS DEFINIDO CORRECTAMENTE EL NOMBRE DEL CLIENTE
            cliente = listado_clientes.loc[(listado_clientes.nombre==nombre_cliente) & (
                                        listado_clientes.alyc==alyc)].copy()
            
            numero_cliente = int(cliente.comitente.iloc[0])
            dia_corte = int(listado_clientes.loc[listado_clientes.nombre == nombre_cliente].iloc[0,3])
            
            # -----------------------------------------------------------------------------
            # Ruta del directorio donde se realiza la busqueda
            if alyc=='Bull':
                directorio = f'{direccion_directorio_bull}\{nombre_cliente} ({numero_cliente})'
            
                nombre_archivo2=[]
            
                # Recorre todos los archivos y directorios dentro del directorio
                for nombre_archivo in os.listdir(directorio):
                    ruta_archivo = os.path.join(directorio, nombre_archivo)
                    
                    # Verifica si es un archivo (y no un directorio)
                    if os.path.isfile(ruta_archivo):
                        nombre_archivo2.append(nombre_archivo)
                
                fecha_movimientos=''
                for i in nombre_archivo2:
                    if i[:16]=='Cuenta Corriente':
                        fecha_movimientos=i[-13:-5]
                        break
                
                if fecha_movimientos=='':
                    fecha_movimientos = 'No hay movimientos'
                    
                
            elif alyc=='Ieb':
                fecha_movimientos = 'no corresponde'
                
            elif alyc=='Balanz':
                fecha_movimientos = 'no corresponde'
                
            else:
                ''
                    
            datos = pd.DataFrame()
            datos['Datos del cliente'] = str()
            datos.loc['nombre cliente'] = nombre_cliente
            datos.loc['numero cliente'] = numero_cliente
            datos.loc['fecha movimientos'] = fecha_movimientos
            datos.loc['Dia de corte'] = dia_corte
            
        except:
            try: # BLOQUE POR SI SOLO TENEMOS DEFINIDO CORRECTAMENTE EL NUMERO INTERNO DEL CLIENTE
                cliente = listado_clientes.loc[(listado_clientes.index==numero_interno) & (
                                            listado_clientes.alyc==alyc)].copy()
                            
                numero_cliente = int(cliente.comitente.iloc[0])
                nombre_cliente = cliente.nombre.iloc[0]
                dia_corte = int(listado_clientes.loc[listado_clientes.index == numero_interno].iloc[0,3])
                
                # Incorporamos la capacidad para identificar si tiene o no fondo de retiro
                # Esto solo fue incorporado para usar con numero_interno.
                fondo_retiro = cliente.loc[numero_interno, 'Fondo de retiro']
                if fondo_retiro > 0: 
                    fondo_retiro_bis = 'si'
                    
                else:
                    fondo_retiro_bis = 'no'
                 
                # -----------------------------------------------------------------------------
                # Ruta del directorio donde se realiza la busqueda
                if alyc=='Bull':
                    directorio = f'{direccion_directorio_bull}\{nombre_cliente} ({numero_cliente})'
                
                    nombre_archivo2=[]
                    
                    # Recorre todos los archivos y directorios dentro del directorio
                    for nombre_archivo in os.listdir(directorio):
                        ruta_archivo = os.path.join(directorio, nombre_archivo)
                        
                        # Verifica si es un archivo (y no un directorio)
                        if os.path.isfile(ruta_archivo):
                            nombre_archivo2.append(nombre_archivo)
                   
                    fecha_movimientos=''
                    for i in nombre_archivo2:
                        if i[:16]=='Cuenta Corriente':
                            fecha_movimientos=i[-13:-5]
                            break
                        
                    if fecha_movimientos=='':
                        fecha_movimientos = 'No hay movimientos'
                    
                elif alyc=='Ieb':
                    fecha_movimientos = 'no corresponde'
                    
                elif alyc=='Balanz':
                    fecha_movimientos = 'no corresponde'
                    
                else:
                    ''
                        
                datos = pd.DataFrame()
                datos['Datos del cliente'] = str()
                datos.loc['nombre cliente'] = nombre_cliente
                datos.loc['numero cliente'] = numero_cliente
                datos.loc['fecha movimientos'] = fecha_movimientos
                datos.loc['Dia de corte'] = dia_corte
                datos.loc['Fondo de retiro'] = fondo_retiro_bis
                
            except:
                try: # BLOQUE POR SI SOLO TENEMOS DEFINIDO CORRECTAMENTE EL DNI DEL CLIENTE
                    
                    cliente = listado_clientes.loc[(listado_clientes.dni==dni) & (
                                                listado_clientes.alyc==alyc)].copy()
                    
                    numero_cliente = cliente.comitente.iloc[0]
                    nombre_cliente = cliente.nombre.iloc[0]
                    dia_corte = int(listado_clientes.loc[listado_clientes.dni == dni].iloc[0,3])
                    
                    # -----------------------------------------------------------------------------
                    # Ruta del directorio donde se realiza la busqueda
                    if alyc=='Bull':
                        directorio = f'{direccion_directorio_bull}\{nombre_cliente} ({numero_cliente})'
                    
                        nombre_archivo2=[]
                    
                        # Recorre todos los archivos y directorios dentro del directorio
                        for nombre_archivo in os.listdir(directorio):
                            ruta_archivo = os.path.join(directorio, nombre_archivo)
                            
                            # Verifica si es un archivo (y no un directorio)
                            if os.path.isfile(ruta_archivo):
                                nombre_archivo2.append(nombre_archivo)
                        
                        fecha_movimientos=''
                        for i in nombre_archivo2:
                            if i[:16]=='Cuenta Corriente':
                                fecha_movimientos=i[-13:-5]
                                break
                            
                        if fecha_movimientos=='':
                            fecha_movimientos = 'No hay movimientos'
                            
                    elif alyc=='Ieb':
                        fecha_movimientos = 'no corresponde'
                        
                    elif alyc=='Balanz':
                        fecha_movimientos = 'no corresponde'
                        
                    else:
                        ''
                    
                    datos = pd.DataFrame()
                    datos['Datos del cliente'] = str()
                    datos.loc['nombre cliente'] = nombre_cliente
                    datos.loc['numero cliente'] = numero_cliente
                    datos.loc['fecha movimientos'] = fecha_movimientos
                    datos.loc['Dia de corte'] = dia_corte
                    
                except:
                    ''
                    datos = """El nombre de cliente, numero interno, y/o dni,
no se han escrito, o se han escrito mal"""
                                    

    except:
        datos = 'Introduzca un usuario válido: Numero entre 1 y 6'



    return datos






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def interfaz_composicion():
    
    import tkinter as tk
    import pandas as pd
    import sys
    from pandastable import Table
    from unidecode import unidecode
    from datetime import datetime as dt
    from PIL import Image, ImageTk
    
    
    def mostrar_tabla():
        fecha_cierre = entry1.get()
        alyc=entry2.get()
        numero_interno = entry3.get()
        nombre_cliente = entry4.get()
        dni = entry5.get()
        usuario = entry6.get()
        
        # Corrigiendo strings e integers para adecuarlos para la formula
        alyc = alyc.title()
        alyc = unidecode(alyc)
        if (alyc=='Bull') or (alyc=='Ieb') or (alyc=='Balanz'): 
            alyc = alyc
            
        else:
            alyc = ''
            
        if nombre_cliente!='':
            nombre_cliente = nombre_cliente.title()
            nombre_cliente = unidecode(nombre_cliente)
        
        else:
            nombre_cliente=''
        
        dni = int(dni)     
        if dni == 0:
            dni = 0
        
        numero_interno = float(numero_interno)    
        if numero_interno == float(0):
            numero_interno = float(0)
        
        try:
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')   
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            control = 0
            
        except:
            df = 'Error en el formato de la fecha de cierre'
            control = 1
        
        usuario = int(usuario) 
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        try:
            directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
            sys.path.append(f'{directorio_funciones}')
            import dp_funciones_c as fc
            
            # Crear un DataFrame a partir del diccionario
            if control == 0:
                if alyc == 'Bull':
                    df = fc.composicion_cartera_bull(fecha_cierre = fecha_cierre, alyc = alyc, 
                                                    numero_interno = numero_interno, 
                                                    dni = dni, nombre_cliente = nombre_cliente,
                                                    usuario = usuario)
                elif alyc == 'Ieb':
                    df = fc.composicion_cartera_ieb(fecha_cierre = fecha_cierre, alyc = alyc, 
                                                   numero_interno = numero_interno, 
                                                   dni = dni, nombre_cliente = nombre_cliente,
                                                   usuario = usuario)
                    
                elif alyc == 'Balanz':
                    df = fc.composicion_cartera_bal(fecha_cierre = fecha_cierre, alyc = alyc, 
                                                   numero_interno = numero_interno, 
                                                   dni = dni, nombre_cliente = nombre_cliente,
                                                   usuario = usuario)
                else: 
                    df = 'Error al introducir el nombre de la ALYC'
                    
            elif control == 1:
                df = df
                
            else:
                ''
        except:
            df = 'Introduzca un usuario válido: Entre 1 y 6'
                
        # Obtener el tipo de datos en df
        if isinstance(df, pd.DataFrame):
            # Crear una ventana emergente
            ventana_tabla = tk.Toplevel()
            ventana_tabla.title("Información para el cobro de los honorarios")
    
            # Crear la tabla utilizando pandastable
            tabla = Table(ventana_tabla, dataframe=df, showtoolbar=False, showstatusbar=False)
            tabla.show()
            
            # Establecer el índice correcto en la tabla
            tabla.model.df = df.astype(object).apply(pd.to_numeric, errors='ignore')
            tabla.model.df = tabla.model.df.reset_index()
            tabla.redraw()  
            
        elif isinstance(df, str):
            ventana_texto = tk.Toplevel()
            ventana_texto.title("Error al introducir los datos del cliente o el ALYC")
    
            etiqueta_texto = tk.Label(ventana_texto, text=df)
            etiqueta_texto.pack()
    
    ventana = tk.Tk()
    ventana.title("Composición de la cartera")
    
    usuarios = ['Y','YY','YYY','Y_Y','YY_YY','YYY_YYY']
    auxiliar = ['--','','--','','','']
    for i in range(len(usuarios)):
        try:
            # Cargar la imagen del logo
            imagen = Image.open(f"C:/Users\{usuarios[i]}\Dropbox{auxiliar[i]}\HONORARIOS\Icono.png")
            logo = ImageTk.PhotoImage(imagen)
            
            # Crear el widget Label para el logo y colocarlo detrás de los demás widgets
            label_logo = tk.Label(ventana, image=logo)
            label_logo.place(x=0, y=0)
            label_logo.lower()  # Colocar el logo detrás de los demás widgets
        
        except:
            ''
    
    texto_explicativo = """
    -------------------------------------------------------------------------------------
    INFORMACION PARA EL CALCULO DE LA COMPOSICION DE LA CARTERA
    -------------------------------------------------------------------------------------
    Al ejecutar el cálculo obtenemos la composición de la cartera a fecha de 
    cierre
    Los que se deben completar:    
    - FECHA DE CIERRE -
    -
    - ALYC -
    -
    - IDENTIFICADOR DEL CLIENTE -
    Hay tres identificadores de cliente: 1) Número interno del cliente, 2) Nombre
    del cliente, y 3) DNI. Basta con utilizar uno. Si se usan los tres, el código
    buscará dando prioridad al nombre. La segunda prioridad es el número interno,
    y en última instancia se busca por DNI.
    -------------------------------------------------------------------------------------
    """
    etiqueta_explicativa = tk.Label(ventana, text=texto_explicativo, bg="#e6e6e6", fg="black",
                                    font=("Century Gothic", 9))
    etiqueta_explicativa.place(x=1, y=1)
    
    label1 = tk.Label(ventana, text="Fecha de cierre (yyyy-mm-dd)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label1.place(x=490, y=20)
    
    entry1 = tk.Entry(ventana)
    entry1.insert(tk.END, "2023-09-29")
    entry1.place(x=500, y=46)
    
    label2 = tk.Label(ventana, text="ALYC (bull, ieb, o balanz)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label2.place(x=490, y=72)
    
    entry2 = tk.Entry(ventana)
    entry2.insert(tk.END, "")
    entry2.place(x=500, y=98)
    
    label3 = tk.Label(ventana, text="[Opcional] Número interno (empresa)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label3.place(x=490, y=124)
    
    entry3 = tk.Entry(ventana)
    entry3.insert(tk.END, float(0))
    entry3.place(x=500, y=150)
    
    label4 = tk.Label(ventana, text="[Opcional] Nombre del cliente (Comitente)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label4.place(x=490, y=176)
    
    entry4 = tk.Entry(ventana)
    entry4.insert(tk.END, "")
    entry4.place(x=500, y=202)
    
    label5 = tk.Label(ventana, text="[Opcional] DNI (sin puntos ni comas)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label5.place(x=490, y=228)
    
    entry5 = tk.Entry(ventana)
    entry5.insert(tk.END, 0)
    entry5.place(x=500, y=254)
    
    label6 = tk.Label(ventana, text="Introduzca el tipo de usuario (entre 1 y 6)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label6.place(x=0, y=524)
    
    entry6 = tk.Entry(ventana)
    entry6.insert(tk.END, 1)
    entry6.place(x=5, y=550)
    
    boton = tk.Button(ventana, text="CALCULAR COMPOSICION", command=mostrar_tabla,
                      font=("Century Gothic", 8, "bold"))
    boton.place(x=500, y=280)
    
    # Incrementar el tamaño de la interfaz a 800x600 píxeles
    ventana.geometry("800x600")
    
    ventana.mainloop()

# honorario=interfaz_composicion()






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def interfaz_honorario():
    
    import tkinter as tk
    import pandas as pd
    import sys
    from pandastable import Table
    from unidecode import unidecode
    from datetime import datetime as dt
    from PIL import Image, ImageTk
    
    
    def mostrar_tabla():
        fecha_cierre = entry1.get()
        alyc=entry2.get()
        numero_interno = entry3.get()
        nombre_cliente = entry4.get()
        dni = entry5.get()
        usuario = entry6.get()
        
        # Corrigiendo strings e integers para adecuarlos para la formula
        alyc = alyc.title()
        alyc = unidecode(alyc)
        if (alyc=='Bull') or (alyc=='Ieb') or (alyc=='Balanz'): 
            alyc = alyc
            
        else:
            alyc = ''
            
        if nombre_cliente!='':
            nombre_cliente = nombre_cliente.title()
            nombre_cliente = unidecode(nombre_cliente)
        
        else:
            nombre_cliente=''
        
        dni = int(dni)     
        if dni == 0:
            dni = 0
        
        numero_interno = float(numero_interno)    
        if numero_interno == float(0):
            numero_interno = float(0)
        
        try:
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')   
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            control = 0
            
        except:
            df = 'Error en el formato de la fecha de cierre'
            control = 1
        
        usuario = int(usuario) 
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        try:
            directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
            sys.path.append(f'{directorio_funciones}')
            import dp_funciones_c as fc
            
            # Crear un DataFrame a partir del diccionario
            if control == 0:
                if alyc == 'Bull':
                    df = fc.honorario(fecha_cierre = fecha_cierre, alyc = alyc, 
                                      numero_interno = numero_interno, 
                                      dni = dni, nombre_cliente = nombre_cliente,
                                      usuario = usuario)
                    if type(df) == str:
                        df = df
                        
                    else:
                        for i in range(3,len(df)):
                            monto = df.iloc[i,0]
                            monto = float(monto[2:])
                            monto = "{:,}".format(monto)
                            monto = f'$ {monto}'
                            df.iloc[i,0] = monto  
                    
                elif alyc == 'Ieb':
                    df = fc.honorario_ieb(fecha_cierre = fecha_cierre, alyc = alyc, 
                                          numero_interno = numero_interno, 
                                          dni = dni, nombre_cliente = nombre_cliente,
                                          usuario = usuario)
                    if type(df) == str:
                        df = df
                        
                    else:
                        for i in range(3,len(df)):
                            monto = df.iloc[i,0]
                            monto = float(monto[2:])
                            monto = "{:,}".format(monto)
                            monto = f'$ {monto}'
                            df.iloc[i,0] = monto  
                    
                elif alyc == 'Balanz':
                    df = fc.honorario_bal(fecha_cierre = fecha_cierre, alyc = alyc, 
                                          numero_interno = numero_interno, 
                                          dni = dni, nombre_cliente = nombre_cliente,
                                          usuario = usuario)
                    if type(df) == str:
                        df = df
                        
                    else:
                        for i in range(3,len(df)):
                            monto = df.iloc[i,0]
                            monto = float(monto[2:])
                            monto = "{:,}".format(monto)
                            monto = f'$ {monto}'
                            df.iloc[i,0] = monto  
                    
                else: 
                    df = 'Error al introducir el nombre de la ALYC'
                    
            elif control == 1:
                df = df
                
            else:
                ''
        except:
            df = 'Introduzca un usuario válido: Entre 1 y 6'
                
        # Obtener el tipo de datos en df
        if isinstance(df, pd.DataFrame):
            # Crear una ventana emergente
            ventana_tabla = tk.Toplevel()
            ventana_tabla.title("Información para el cobro de los honorarios")
    
            # Crear la tabla utilizando pandastable
            tabla = Table(ventana_tabla, dataframe=df, showtoolbar=False, showstatusbar=False)
            tabla.show()
            
            # Establecer el índice correcto en la tabla
            tabla.model.df = df.astype(object).apply(pd.to_numeric, errors='ignore')
            tabla.model.df = tabla.model.df.reset_index()
            tabla.redraw()  
            
        elif isinstance(df, str):
            ventana_texto = tk.Toplevel()
            ventana_texto.title("Error al introducir los datos del cliente o el ALYC")
    
            etiqueta_texto = tk.Label(ventana_texto, text=df)
            etiqueta_texto.pack()
    
    ventana = tk.Tk()
    ventana.title("Calculo de honorarios")
    
    usuarios = ['Y','YY','YYY','Y_Y','YY_YY','YYY_YYY']
    auxiliar = ['--','','--','','','']
    for i in range(len(usuarios)):
        try:
            # Cargar la imagen del logo
            imagen = Image.open(f"C:/Users\{usuarios[i]}\Dropbox{auxiliar[i]}\HONORARIOS\Icono.png")
            logo = ImageTk.PhotoImage(imagen)
            
            # Crear el widget Label para el logo y colocarlo detrás de los demás widgets
            label_logo = tk.Label(ventana, image=logo)
            label_logo.place(x=0, y=0)
            label_logo.lower()  # Colocar el logo detrás de los demás widgets
        
        except:
            ''

    texto_explicativo = """
    -------------------------------------------------------------------------------------
    INFORMACION PARA EL CALCULO DE LOS HONORARIOS
    -------------------------------------------------------------------------------------
    Al ejecutar la aplicación obtenemos los honorarios a cobrar
    Los que se deben completar:
        
    - FECHA DE CIERRE -
    -
    - ALYC -
    -
    - IDENTIFICADOR DEL CLIENTE -
    Hay tres identificadores de cliente: 1) Número interno del cliente, 2) Nombre
    del cliente, y 3) DNI. Basta con utilizar uno. Si se usan los tres, el código
    buscará dando prioridad al nombre. La segunda prioridad es el número interno,
    y en última instancia se busca por DNI.
    -------------------------------------------------------------------------------------
    """
    etiqueta_explicativa = tk.Label(ventana, text=texto_explicativo, bg="#e6e6e6", fg="black",
                                    font=("Century Gothic", 9))
    etiqueta_explicativa.place(x=1, y=1)
    
    label1 = tk.Label(ventana, text="Fecha de cierre (yyyy-mm-dd)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label1.place(x=490, y=20)
    
    entry1 = tk.Entry(ventana)
    entry1.insert(tk.END, "2023-09-29")
    entry1.place(x=500, y=46)
    
    label2 = tk.Label(ventana, text="ALYC (bull, ieb, o balanz)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label2.place(x=490, y=72)
    
    entry2 = tk.Entry(ventana)
    entry2.insert(tk.END, "")
    entry2.place(x=500, y=98)
    
    label3 = tk.Label(ventana, text="[Opcional] Número interno (empresa)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label3.place(x=490, y=124)
    
    entry3 = tk.Entry(ventana)
    entry3.insert(tk.END, float(0))
    entry3.place(x=500, y=150)
    
    label4 = tk.Label(ventana, text="[Opcional] Nombre del cliente (Comitente)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label4.place(x=490, y=176)
    
    entry4 = tk.Entry(ventana)
    entry4.insert(tk.END, "")
    entry4.place(x=500, y=202)
    
    label5 = tk.Label(ventana, text="[Opcional] DNI (sin puntos ni comas)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label5.place(x=490, y=228)
    
    entry5 = tk.Entry(ventana)
    entry5.insert(tk.END, 0)
    entry5.place(x=500, y=254)
    
    label6 = tk.Label(ventana, text="Introduzca el tipo de usuario (entre 1 y 6)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label6.place(x=0, y=524)
    
    entry6 = tk.Entry(ventana)
    entry6.insert(tk.END, 1)
    entry6.place(x=5, y=550)
    
    boton = tk.Button(ventana, text="CALCULAR HONORARIOS", command=mostrar_tabla,
                      font=("Century Gothic", 8, "bold"))
    boton.place(x=500, y=280)
    
    # Incrementar el tamaño de la interfaz a 800x600 píxeles
    ventana.geometry("800x600")
    
    ventana.mainloop()

# honorario=interfaz_honorario()






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def interfaz_rendimiento():
    
    import tkinter as tk
    import pandas as pd
    import sys
    from pandastable import Table
    from unidecode import unidecode
    from datetime import datetime as dt
    from PIL import Image, ImageTk
    
    
    def mostrar_tabla():
        fecha_cierre = entry1.get()
        dias = entry7.get()
        alyc=entry2.get()
        numero_interno = entry3.get()
        nombre_cliente = entry4.get()
        dni = entry5.get()
        usuario = entry6.get()
        
        # Corrigiendo strings e integers para adecuarlos para la formula
        alyc = alyc.title()
        alyc = unidecode(alyc)
        if (alyc=='Bull') or (alyc=='Ieb') or (alyc=='Balanz'): 
            alyc = alyc
            
        else:
            alyc = ''
            
        if nombre_cliente!='':
            nombre_cliente = nombre_cliente.title()
            nombre_cliente = unidecode(nombre_cliente)
        
        else:
            nombre_cliente=''
        
        dni = int(dni)     
        if dni == 0:
            dni = 0
        
        numero_interno = float(numero_interno)    
        if numero_interno == float(0):
            numero_interno = float(0)
        
        try:
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')   
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            control = 0
            
        except:
            df = 'Error en el formato de la fecha de cierre'
            control = 1
        
        usuario = int(usuario) 
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
            
        dias = int(dias)
        if dias == int(30):
            dias = int(30)
        
        try:
            directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
            sys.path.append(f'{directorio_funciones}')
            import dp_funciones_c as fc
            
            # Crear un DataFrame a partir del diccionario
            if control == 0:
                if alyc == 'Bull':
                    df = fc.rendimientos_bruto_neto(fecha_cierre = fecha_cierre, 
                                    alyc = alyc, numero_interno = numero_interno, 
                                    dni = dni, nombre_cliente = nombre_cliente,
                                    usuario = usuario, dias = dias)
                    
                elif alyc == 'Ieb':
                    ''
                    df = fc.rendimientos_bruto_neto_ieb(fecha_cierre = fecha_cierre, 
                                    alyc = alyc, numero_interno = numero_interno, 
                                    dni = dni, nombre_cliente = nombre_cliente,
                                    usuario = usuario, dias = dias)
                    
                elif alyc == 'Balanz':
                    ''
                    df = fc.rendimientos_bruto_neto_bal(fecha_cierre = fecha_cierre, 
                                    alyc = alyc, numero_interno = numero_interno, 
                                    dni = dni, nombre_cliente = nombre_cliente,
                                    usuario = usuario, dias = dias)
                    
                else: 
                    df = 'Error al introducir el nombre de la ALYC'
                    
            elif control == 1:
                df = df
                
            else:
                ''
        except:
            df = 'Introduzca un usuario válido: Entre 1 y 6'
                
        # Obtener el tipo de datos en df
        if isinstance(df, pd.DataFrame):
            # Crear una ventana emergente
            ventana_tabla = tk.Toplevel()
            ventana_tabla.title("Información para el cálculo del rendimiento")
    
            # Crear la tabla utilizando pandastable
            tabla = Table(ventana_tabla, dataframe=df, showtoolbar=False, showstatusbar=False)
            tabla.show()
            
            # Establecer el índice correcto en la tabla
            tabla.model.df = df.astype(object).apply(pd.to_numeric, errors='ignore')
            tabla.model.df = tabla.model.df.reset_index()
            tabla.redraw()  
            
        elif isinstance(df, str):
            ventana_texto = tk.Toplevel()
            ventana_texto.title("Error al introducir los datos del cliente o el ALYC")
    
            etiqueta_texto = tk.Label(ventana_texto, text=df)
            etiqueta_texto.pack()
    
    ventana = tk.Tk()
    ventana.title("Calculo de rendimientos")
    
    usuarios = ['Y','YY','YYY','Y_Y','YY_YY','YYY_YYY']
    auxiliar = ['--','','--','','','']
    for i in range(len(usuarios)):
        try:
            # Cargar la imagen del logo
            imagen = Image.open(f"C:/Users\{usuarios[i]}\Dropbox{auxiliar[i]}\HONORARIOS\Icono.png")
            logo = ImageTk.PhotoImage(imagen)
            
            # Crear el widget Label para el logo y colocarlo detrás de los demás widgets
            label_logo = tk.Label(ventana, image=logo)
            label_logo.place(x=0, y=0)
            label_logo.lower()  # Colocar el logo detrás de los demás widgets
        
        except:
            ''

    texto_explicativo = """
    -------------------------------------------------------------------------------------
    INFORMACION PARA EL CALCULO DE LOS HONORARIOS
    -------------------------------------------------------------------------------------
    Al ejecutar la aplicación obtenemos el rendimiento del período especificado
    Se debe completar lo siguiente:
    - FECHA DE CIERRE -
    -
    - ALYC -
    -
    - IDENTIFICADOR DEL CLIENTE -
    -
    - PLAZO (DIAS)
    Hay tres identificadores de cliente: 1) Número interno del cliente, 2) Nombre
    del cliente, y 3) DNI. Basta con utilizar uno. Si se usan los tres, el código
    buscará dando prioridad al nombre. La segunda prioridad es el número interno,
    y en última instancia se busca por DNI.
    -------------------------------------------------------------------------------------
    """
    etiqueta_explicativa = tk.Label(ventana, text=texto_explicativo, bg="#e6e6e6", fg="black",
                                    font=("Century Gothic", 8))
    etiqueta_explicativa.place(x=1, y=1)
    
    label1 = tk.Label(ventana, text="Fecha de cierre (yyyy-mm-dd)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label1.place(x=490, y=20)
    
    entry1 = tk.Entry(ventana)
    entry1.insert(tk.END, "2023-09-29")
    entry1.place(x=500, y=46)
    
    label2 = tk.Label(ventana, text="ALYC (bull, ieb, o balanz)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label2.place(x=490, y=72)
    
    entry2 = tk.Entry(ventana)
    entry2.insert(tk.END, "")
    entry2.place(x=500, y=98)
    
    label3 = tk.Label(ventana, text="[Opcional] Número interno (empresa)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label3.place(x=490, y=124)
    
    entry3 = tk.Entry(ventana)
    entry3.insert(tk.END, float(0))
    entry3.place(x=500, y=150)
    
    label4 = tk.Label(ventana, text="[Opcional] Nombre del cliente (Comitente)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label4.place(x=490, y=176)
    
    entry4 = tk.Entry(ventana)
    entry4.insert(tk.END, "")
    entry4.place(x=500, y=202)
    
    label5 = tk.Label(ventana, text="[Opcional] DNI (sin puntos ni comas)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label5.place(x=490, y=228)
    
    entry5 = tk.Entry(ventana)
    entry5.insert(tk.END, 0)
    entry5.place(x=500, y=254)
    
    label6 = tk.Label(ventana, text="Introduzca el tipo de usuario (entre 1 y 6)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label6.place(x=0, y=524)
    
    entry6 = tk.Entry(ventana)
    entry6.insert(tk.END, 1)
    entry6.place(x=5, y=550)
    
    label7 = tk.Label(ventana, text="Introduzca el plazo (cantidad de días)", bg="#e6e6e6", fg="black",
                      font=("Century Gothic", 8, "bold"))
    label7.place(x=240, y=524)
    
    entry7 = tk.Entry(ventana)
    entry7.insert(tk.END, int(30))
    entry7.place(x=250, y=550)
    
    boton = tk.Button(ventana, text="CALCULAR HONORARIOS", command=mostrar_tabla,
                      font=("Century Gothic", 8, "bold"))
    boton.place(x=500, y=280)
    
    # Incrementar el tamaño de la interfaz a 800x600 píxeles
    ventana.geometry("800x600")
    
    ventana.mainloop()






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def rendimiento_bruto_completo(fecha, usuario = 1, dni = 0, numero_interno = 0,
                               nombre_cliente = '', alyc = ''):
    """
    ---------------------------------------------------------------------------
                              ¿PARA QUE SIRVE ESTE CODIGO?
    Halla la TIR o rendimiento bruto mensual de la cartera del cliente. El plazo
    esta predefinido en el archivo excel 'calendario', quien debera modificarse
    cuando se desee analizar un periodo distinto. 
    ---------------------------------------------------------------------------
                               ACLARACIONES ADICIONALES
    1) Este codigo es utilizado para situaciones donde el cliente realiza, durante
    el mes, menos de 50 depositos y menos de 50 retiros. De exceder estas canti-
    dades, el codigo se 'rompera' (dejara de funcionar).
    
    2) El codigo es dependiente del archivo excel 'calendario', el cual debe
    modificarse a gusto (su primera hoja) para definir el periodo de interes.
    ---------------------------------------------------------------------------
    Paramentros
    ----------
    fecha : tipo string.
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
        DESCRIPCION.
        Es la alyc donde el cliente tiene su cuenta: Bull, Ieb, o Balanz. 
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco aurelio'.
        
    dni : tipo integer.
        DESCRIPCION.
        Es el dni del cliente.   
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
        DESCRIPCION.
        Es el numero interno asignado por la empresa al cliente.  
        Valor por defecto: 0.
        
    usuario :
        DESCRIPCION.
        Es un numero entero entre 1 y 5 que indica el ordenador desde el que se
        accede al dropbox de la empresa         
        
        
    Resultado
    -------
    rendimiento : tipo DataFrame
        DESCRIPCION.
        Es una tabla con el rendimiento bruto mensual de la cartera del cliente.

    """ 

    try:
        # usuario = 4 
        
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
    
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        import pandas as pd
        from datetime import datetime as dt
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        from unidecode import unidecode
       
        
        # Normalizacion de los valores de los parametros introducidos
        alyc = alyc.title()
        alyc = unidecode(alyc)
        nombre_cliente = nombre_cliente.title()
        nombre_cliente = unidecode(nombre_cliente)
        
    
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                    numero_interno = numero_interno, dni = dni,
                                    usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
            
        controlador = type(datos_cliente)==str
        if controlador == False:
            # Sub parametros - direcciones
            directorio = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
            archivo = 'calendario'
            
            directorio_clientes = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS'
            archivo_clientes = 'Base de Datos de Clientes'
            
            
            # Importamos el archivo de clientes y nos quedamos con su fecha de alta
            clientes = pd.read_excel(f'{directorio_clientes}/{archivo_clientes}.xlsx')
            clientes.set_index('numero_interno', inplace = True)
            
            fecha_alta = clientes.loc[numero_interno,'Alta de Cliente']
            
            
            # Importamos archivo calentario y tomamos su mascara para fechas entre el alta
            # y la fecha elegida al inicio ('fecha')
            calendario = pd.read_excel(f'{directorio}/{archivo}.xlsx')
            calendario['aux'] = 0
            calendario.set_index('fecha final',inplace = True)
            
            calendario.loc[fecha_alta] = 0
            
            calendario.sort_index(ascending = True, inplace = True)
            
            fecha = dt.strptime(fecha,'%Y-%m-%d')
            
            calendario = calendario.loc[calendario.index <= fecha].copy()
            calendario = calendario.loc[calendario.index >= fecha_alta].copy()
            
            
            # Construimos la tabla de fechas que utilizaremos para los rendimientos
            calendario2 = calendario.iloc[1:,:].copy()
            calendario2['fecha_inicial'] = calendario.iloc[:-1,:].index
            
            calendario2.drop('aux', axis = 1, inplace = True)
            
            calendario2['dias'] = int(0)
            for i in range(len(calendario2)):
                calendario2.iloc[i,1] = (calendario2.index[i] - calendario2.iloc[i,0]).days
                
            
            # Calculamos los rendimientos y construimos la tabla que los contendra
            tabla_rend = calendario2.copy()
            tabla_rend.drop('dias', axis = 1, inplace = True)
            tabla_rend['Rendimiento'] = float(0)
            
            for i in range(len(calendario2)):
                fecha_cierre = dt.strftime(calendario2.index[i], '%Y-%m-%d')
                dias = int(calendario2.iloc[i,-1])
                
                if alyc == 'Bull':
                    rendimiento = fc.rendimientos_bruto_neto(fecha_cierre = fecha_cierre,
                                                              usuario = usuario, alyc = alyc, 
                                                              numero_interno = numero_interno,
                                                              dias = dias, dni = dni,
                                                              nombre_cliente = nombre_cliente)
                    tabla_rend.iloc[i,1] = rendimiento.iloc[0,0]
                    
                elif alyc == 'Ieb':
                    rendimiento = fc.rendimientos_bruto_neto_ieb(fecha_cierre = fecha_cierre,
                                                              usuario = usuario, alyc = alyc, 
                                                              numero_interno = numero_interno,
                                                              dias = dias, dni = dni,
                                                              nombre_cliente = nombre_cliente)
                    tabla_rend.iloc[i,1] = rendimiento.iloc[0,0]
                    
                elif alyc == 'Balanz':
                    rendimiento = fc.rendimientos_bruto_neto_bal(fecha_cierre = fecha_cierre,
                                                              usuario = usuario, alyc = alyc, 
                                                              numero_interno = numero_interno,
                                                              dias = dias, dni = dni,
                                                              nombre_cliente = nombre_cliente)
                    tabla_rend.iloc[i,1] = rendimiento.iloc[0,0]
                    
                else:
                    tabla_rend = 'Se ha equivocado de alyc. Es Bull, Ieb, o Balanz'
            
            
        else:
            tabla_rend = datos_cliente
    
    
    except:
        tabla_rend = 'Introduzca un usuario válido: Numero entero entre 1 y 6'
    
    
    return tabla_rend





# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def split_bull(fecha_cierre, alyc = '', nombre_cliente = '', numero_interno = 0, 
               dni = 0, tipo_calculo = 'rendimiento', usuario = 1):
    """
    ---------------------------------------------------------------------------
                           ¿PARA QUE SIRVE ESTE CODIGO?
    Se obtiene la cantidad de papeles que se deben adicionar a la cartera debido 
    al split generado.
    
    ---------------------------------------------------------------------------
    Parameters
    ----------
    fecha_cierre : Tipo String.
        DESCRIPTION. Indica el momento donde deseamos conocer los papeles extras. 
        Por ejemplo: '2023-02-24'. 
                     
    alyc : Tipo String.
        DESCRIPTION. Es el nombre de la alyc donde el cliente tiene cuenta. Es
        Bull, Ieb, o Balanz. No importa si lo escribimos en mayusculas o con 
        acentos.The default is ''.
        
    nombre_cliente : Tipo String.
        DESCRIPTION. Es el nombre del cliente tal cual figura en su cuenta 
        comitente. No importa si se escribe con mayusculas y acentos. 
        Valor por defecto: ''.
        
    numero_interno : Tipo integer
        DESCRIPTION. Es el numero de la cuenta en ALYC que corresponde 
        al cliente. Valor por defecto: 0.
        
    dni : Tipo integer
        DESCRIPTION. Es el numero de la cuenta en ALYC que corresponde 
        al cliente. Valor por defecto: 0.
        
    tipo_calculo : Tipo string
        DESCRIPTION. El valor por defecto es 'rendimiento', pero tambien puede
        escribirse 'tenencia'. Ambos son dos maneras de obtener la composicion
        de la cartera a fecha de cierre. El primero tiene en cuenta la concerta
        cion, es decir, al comprar o vender un papel, no importa si la operacion
        se liquida, importa que se inicio. El segundo solo tiene en cuenta las 
        operaciones que se han liquidado.

    """
    
    # -----------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------
    try:        
        
        # -----------------------------------------------------------------------------
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        import pandas as pd
        from datetime import datetime as dt
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        

        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni, 
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
        
        # Estos son parametros, pero no es necesario modificarlos, puede pensarse que
        # sus valores estan fijados por defecto.                  
        tenencia_inicial=f'Tenencia 31-12-22 {nombre_cliente}'
        transferencia_alyc='Transferencias entre alycs y div en especie'
        archivo_split = 'SPLITs'
        ubicacion_split = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})'
        # -----------------------------------------------------------------------------
        movimiento_pesos=f'Cuenta Corriente PESOS {fecha_movimientos}' 
        movimiento_usd=f'Cuenta Corriente DOLARES {fecha_movimientos}' 
        movimiento_ccl=f'Cuenta Corriente DOLARES CABLE {fecha_movimientos}' 
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
 
        
        # ----------------------------- PRIMERA PARTE ---------------------------------
        #                       IMPORTACION DE ARCHIVOS EXCEL
        # -----------------------------------------------------------------------------
        # Se importan los archivos con los movimientos de la cuenta. Sobre cada uno se
        # toma la máscara que contiene movimientos en fechas previas o iguales a la fecha
        # de cierre. Y se ordenan cronológicamente las operaciones.
        # -----------------------------------------------------------------------------
        # Se transforma la fecha de cierre al tipo datetime
        fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
        
        
        # Se importa el archivo split y se toma la mascara conforme a la fecha de cierre
        archivo_split = pd.read_excel(f'{ubicacion_split}\{archivo_split}.xlsx')
        archivo_split.set_index("Fecha", inplace=True)
        archivo_split = archivo_split.loc[archivo_split.index<=fecha_cierre].copy()
        archivo_split.sort_index(inplace=True)
        
        
        # Definimos el dataframe donde se guardaran los papeles extra
        papeles = pd.DataFrame()
        
        
        # Se controla el dataframe 'papeles' segun la mascara 'archivo_split' este o no vacia.
        if archivo_split.empty:
            papeles = papeles
            
        else:
            for i in range(len(archivo_split.index)):
                papeles.loc[i,'Especie'] = archivo_split.iloc[i,2]
                papeles.loc[i,'Cantidad'] = int(0)
                papeles.loc[i,'Fecha acreditacion'] = str()
            
            papeles.set_index('Especie',inplace=True)
        
        for i in range(len(archivo_split.index)):
            fecha_split = archivo_split.index[i]
            fecha_split = fecha_split.to_pydatetime()
        
            # Importamos la tenencia inicial, eliminamos la columna de precios, y tomamos
            # solo los tickets, la liquidez no (pues queda sujeta al saldo, quien cambia
            # automaticamente). En simultaneo, usamos 'try - except' por si el archivo de 
            # tenencia inicial no existe.
            try:
                cartera_inicial_1=pd.read_excel(f'{directorio_origen}\{tenencia_inicial}.xlsx'
                                              ).set_index('Especie')
                cartera_inicial_1.drop(cartera_inicial_1.columns[-1],axis=1,inplace=True)
                cartera_inicial=cartera_inicial_1.iloc[:-4].copy()
            
            except:
                cartera_inicial=0
         
            
            # Importamos el archivo en pesos y lo ordenamos cronologiamente por columna "Liquida",
            # y recalculamos el saldo. El 'Try - except' es para contemplar la situacion donde
            # # este archivo no existe. Adicionalmente, se identifican las cauciones dentro 
            # de la tabla de bullmarket que quedan fuera de la mascara por fecha de cierre. 
            # El opuesto del importe de estas cauciones se sumara al saldo liquido en pesos.
            try:   
                archivo_pesos=fc.concatenacion_movimientos_bull(moneda = 'Pesos', alyc = alyc, 
                                                                dni = dni,
                                                                nombre_cliente = nombre_cliente, 
                                                                numero_interno = numero_interno,
                                                                usuario = usuario)
                
                if tipo_calculo == 'rendimiento':
                    # Se toma la mascara de acuerdo a la fecha de cierre y las 'operaciones locas'
                    # que implican cambios en la liquidez y cantidad de papales; y también, las
                    # 'operaciones_relocas' que también implican cambios en la liquidez.
                    operaciones_locas=archivo_pesos.loc[(archivo_pesos.Operado<=fecha_split) &
                                                    (archivo_pesos.index>fecha_split) &
                                                    (archivo_pesos.Comprobante!='COMPRA CAUCION TERMINO')].copy()
                    
                    if len(operaciones_locas)>0:
                        importe_operaciones=operaciones_locas.Importe.sum()
                    else:
                        importe_operaciones=0
                    
                    operaciones_relocas=archivo_pesos.loc[(archivo_pesos.index<fecha_split)].copy()
                    
                    if len(operaciones_relocas)>0:
                        operaciones_relocas=operaciones_relocas.loc[(operaciones_relocas.Comprobante=='ENT GAR PESOS') |
                                                            (operaciones_relocas.Comprobante=='DEV GAR PESOS')].copy()
                    else:
                        operaciones_relocas=pd.DataFrame()
                
                    if len(operaciones_relocas)>0:
                        importe_operaciones2=operaciones_relocas.Importe.sum()*-1
                    else:
                        importe_operaciones2=0
                    
                    archivo_pesos=archivo_pesos.loc[archivo_pesos.index<=fecha_split].copy()
                    
                elif tipo_calculo == 'tenencia':
                    # Se toma la mascara de acuerdo a la fecha de cierre 
                    operaciones_locas=archivo_pesos.loc[(archivo_pesos.Operado<fecha_cierre) &
                                                    (archivo_pesos.index>fecha_cierre)].copy() 
                    
                    if len(operaciones_locas)>0:
                        importe_operaciones=operaciones_locas.Importe.sum()*-1
                    else:
                        importe_operaciones=0
                        
                    operaciones_relocas=archivo_pesos.loc[(archivo_pesos.index<=fecha_cierre)].copy()
                    
                    if len(operaciones_relocas)>0:
                        operaciones_relocas=operaciones_relocas.loc[(operaciones_relocas.Comprobante=='ENT GAR PESOS') |
                                                            (operaciones_relocas.Comprobante=='DEV GAR PESOS')].copy()
                    else:
                        operaciones_relocas=pd.DataFrame()
        
                    if len(operaciones_relocas)>0:
                        importe_operaciones2=operaciones_relocas.Importe.sum()*-1
                    else:
                        importe_operaciones2=0
                    
                    archivo_pesos=archivo_pesos.loc[archivo_pesos.index<=fecha_cierre].copy()
            
            except:
                archivo_pesos=pd.DataFrame()
                operaciones_locas=pd.DataFrame()
            
            
            # Importamos el archivo en dolares y se ordena cronologicamente por columna "Liquida"
            # recalculando el saldo. El 'Try - except' es para contemplar la situacion donde
            # este archivo no existe.
            try:
                archivo_usd=fc.concatenacion_movimientos_bull(moneda = 'Dolares', alyc = alyc, 
                                                              dni = dni,
                                                              nombre_cliente = nombre_cliente, 
                                                              numero_interno = numero_interno,
                                                              usuario = usuario)
                   
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_usd=archivo_usd.loc[archivo_usd.index<=fecha_split].copy()
            
            except:
                archivo_usd=pd.DataFrame()
            
            
            # Importamos el archivo en dolares cable. El 'Try - except' es para contemplar
            # la situacion donde este archivo no existe. 
            try:
                archivo_ccl=fc.concatenacion_movimientos_bull(moneda = 'Dolares cable', alyc = alyc, 
                                                              dni = dni,
                                                              nombre_cliente = nombre_cliente, 
                                                              numero_interno = numero_interno,
                                                              usuario = usuario) 
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_ccl=archivo_ccl.loc[archivo_ccl.index<=fecha_split].copy()
            
            except:
                archivo_ccl=pd.DataFrame()
            
            
            # Traemos el archivo que contiene las transferencias entre alycs.
            try:
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')
                archivo_transf_alyc.set_index("Liquida", inplace=True)   
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.index<=fecha_split].copy()
                
            except:
                archivo_transf_alyc = pd.DataFrame()
                
                
                
            
            # ----------------------------- SEGUNDA PARTE ---------------------------------
            #     COMPOSICIONES PARCIALES DE CARTERA - MOVIMIENTOS EN PESOS Y DOLARES 
            # -----------------------------------------------------------------------------
            # Armamos los dataframes agrupando de acuerdo a los tickets, compras/ventas, y 
            # calculando las cantidades mantenidas hasta la fecha de cierre (inclusive). 
            # Esto se hace con los tres archivos, movimientos en pesos, en usd, y en ccl.  
            # -----------------------------------------------------------------------------
            # Movimientos en pesos, eliminamos las cauciones, quienes se tratan mas adelante.
            
            if tipo_calculo == 'rendimiento':
                if archivo_pesos.empty:
                    cartera_pesos=pd.DataFrame()
                    cartera_pesos2=pd.DataFrame()  
                    
                else:
                    cartera_pesos=archivo_pesos.groupby('Especie').Cantidad.sum()
                    cartera_pesos=pd.DataFrame(cartera_pesos)
                    
                    if len(operaciones_locas)>0:
                        cartera_pesos2=operaciones_locas.groupby('Especie').Cantidad.sum()
                        cartera_pesos2=pd.DataFrame(cartera_pesos2)
                    else:
                        cartera_pesos2=pd.DataFrame()
                    
                    if len(cartera_pesos.loc[cartera_pesos.index=='VARIAS'])>0:
                        cartera_pesos.drop('VARIAS',axis=0,inplace=True)
                        
            elif tipo_calculo == 'tenencia':
                if archivo_pesos.empty:
                    cartera_pesos=pd.DataFrame()
                    
                else:
                    cartera_pesos=archivo_pesos.groupby('Especie').Cantidad.sum()
                    cartera_pesos=pd.DataFrame(cartera_pesos)
                    
                    if len(cartera_pesos.loc[cartera_pesos.index=='VARIAS'])>0:
                        cartera_pesos.drop('VARIAS',axis=0,inplace=True)
            
            
            # Cartera por tenencia
            if archivo_transf_alyc.empty:
                cartera_trans_alyc = pd.DataFrame()
            
            else:
                cartera_trans_alyc = archivo_transf_alyc.groupby('Especie').Cantidad.sum()
                cartera_trans_alyc = pd.DataFrame(cartera_trans_alyc)
            
            
            # Movimientos en dolares (mep y ccl)
            # Estos movimientos pueden no existir antes de la fecha de cierre, por ende, los
            # dataframes correspondientes estaran vacios. Debemos tener en cuenta esta posibi-
            # lidad para evitar que el codigo se rompa. 
            if len(archivo_usd.index)>0:
                cartera_usd=archivo_usd.groupby('Especie').Cantidad.sum()
                cartera_usd=pd.DataFrame(cartera_usd)
                saldo_usd=archivo_usd.loc[:,'Saldo'].iloc[-1]
                
            else:
                cartera_usd=0
                saldo_usd=0
            
            if len(archivo_ccl.index)>0:
                cartera_ccl=archivo_ccl.groupby('Especie').Cantidad.sum()
                cartera_ccl=pd.DataFrame(cartera_ccl)
                saldo_ccl=archivo_ccl.Saldo.iloc[-1]
            else:
                cartera_ccl=0
                saldo_ccl=0
            
            
            # Se incorpora la tenencia de euros a la liquidez en dolares, por ende, esta 
            # divisa se cotiza como dolares mep. Ademas, eliminamos este ticket de la tenencia
            # inicial 
            if type(cartera_inicial)!=type(0): 
                if len(cartera_inicial.loc[cartera_inicial.index=='EUR'])>0:
                    cartera_inicial.drop('EUR',axis=0,inplace=True)
            
            
            
            
            # ----------------------------- TERCERA PARTE ---------------------------------
            #       COMPOSICIONES PARCIALES DE CARTERA - INTEGRANDO LOS MOVIMIENTOS 
            # -----------------------------------------------------------------------------
            # Fusionamos las carteras en un nuevo vector llamado 'cartera' (recordar que los
            # movimientos en mep y ccl pueden no existir)
            if (type(cartera_usd)==type(0))&(type(cartera_ccl)==type(0)):
                cartera=pd.DataFrame(cartera_pesos)
                cartera=pd.DataFrame(cartera)
                
            elif (type(cartera_usd)==type(0))&(type(cartera_ccl)!=type(0)):
                cartera=pd.concat([cartera_pesos,cartera_ccl],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            elif (type(cartera_usd)!=type(0))&(type(cartera_ccl)==type(0)):
                cartera=pd.concat([cartera_pesos,cartera_usd],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            else:
                cartera=pd.concat([cartera_pesos,cartera_usd,cartera_ccl],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            
            if tipo_calculo == 'rendimiento':
                # Ahora fusionamos la cartera con las 'operaciones locas' halladas en la primera parte.
                if cartera.empty:
                    cartera=cartera_pesos2.copy()
                
                elif cartera_pesos2.empty:
                    cartera=cartera
                
                else:
                    cartera=pd.concat([cartera_pesos2,cartera],ignore_index=False)
                    cartera=cartera.groupby(cartera.index).Cantidad.sum()
                    cartera=pd.DataFrame(cartera)
            
            
            # Se fusiona la 'cartera' con 'cartera_trans_alyc'
            if cartera_trans_alyc.empty:
                cartera = cartera
                
            else:
                cartera = pd.concat([cartera,cartera_trans_alyc],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            
            
            # ----------------------------- CUARTA PARTE ----------------------------------
            #   COMPOSICION PARCIAL DE CARTERA - UNION ENTRE TENENCIA INICIAL Y MOVIMIENTOS
            # -----------------------------------------------------------------------------
            # Concatenamos los dataframes y nos quedamos con las cantidades positivas 
            if (type(cartera_inicial)!=type(0))&(type(cartera)!=type(0)):
                cartera=pd.concat([cartera,cartera_inicial],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                cartera=cartera.loc[cartera.Cantidad>0].copy()
            
            elif (type(cartera_inicial)!=type(0))&(type(cartera)==type(0)):
                cartera=cartera_inicial.copy()
                
            elif (type(cartera_inicial)==type(0))&(type(cartera)!=type(0)):
                cartera=cartera.copy()
                
            else:
                cartera=pd.DataFrame()
            
            
            # Se elimina la fila 'ccl' en caso de existir
            if len(cartera)>0:
                ccl=cartera.loc[cartera.index=='ccl'].copy()
            
                if len(ccl)==1:
                    cartera.drop('ccl',axis=0,inplace=True)
            
            
            # Control de errores por si no existen splits 
            if papeles.empty:
                papeles = papeles
                
            else:
                try: # Control de errores por si el papel que hace el split no se tiene 
                     # en cartera
                    # Cantidad de papeles
                    ticket = archivo_split.iloc[i,2]
                    papeles_extra = cartera.loc[ticket,'Cantidad'] * archivo_split.iloc[i,1]
                    
                    papeles_extra = int(papeles_extra)
                    
                    papeles.loc[ticket,'Cantidad'] = papeles_extra
                    
                    # Fechas
                    papeles.loc[ticket,'Fecha acreditacion'] = archivo_split.iloc[i,3]
                    
                    # Si recalculan las cantidades por si no corresponden
                    fecha_acreditacion = archivo_split.iloc[i,3]
                    
                    if fecha_cierre < fecha_acreditacion:
                        papeles.loc[ticket,'Cantidad'] = 0
                        
                    papeles.drop('Fecha acreditacion',axis=1,inplace=True) 
                    
                except:
                    papeles = papeles
             
    except:
        papeles = 'Introduzca un usuario válido: Numero entero entre 1 y 6'


    return papeles






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def composicion_cartera_bull(fecha_cierre, alyc = '', nombre_cliente = '',
                             numero_interno = 0, dni = 0, usuario = 1, 
                             tipo_calculo='rendimiento'):
    """  
    Aclaraciones
    -----------
    Cualquier SPLIT debe introducirse "a mano" en el archivo excel correspondiente
    figurando como un ingreso de papeles que represente dicho split, sin alterar
    el saldo de la cartera.
    
    Las fechas de las operaciones que se tienen en cuenta son las correspondientes
    a la concertacion, no a la liquidacion.
    
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    dni : tipo integer.
    
        DESCRIPCION
        Es el dni del cliente.
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    tipo_calculo : tipo string. Valor por defecto: 'rendimiento'
    
        DESCRIPCION.
        Este parametro toma dos valores en concreto, 'rendimiento' y 'tenencia'. 
        Ambos son para el calculo del valor de la cartera, pero el primero es 
        para el caso del analisis de rendimiento, y el segundo es para el caso
        de la tenencia valorizada. La diferencia se encuentra entre la concertacion 
        y liquidacion, el primer caso valora de acuerdo a la concertacion; el 
        segundo de acuerdo a la liquidacion.

        
    Resultado
    -------
    cartera : tipo DataFrame.
       
       DESCRIPCION.
       Se obtiene la composicion (precio y cantidad) de la cartera a fecha de 
       cierre. Adicionalmente, se identifican las operaciones mep realizadas. 
       Esta información es vital para calcular el valor final o inicial de la 
       cartera.     
    """
    # -----------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------
    try:
        # usuario = 4 
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        import pandas as pd
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        import math
        
    
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                    numero_interno = numero_interno, dni = dni,
                                    usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
        
        # Estos son parametros, pero no es necesario modificarlos, puede pensarse que
        # sus valores estan fijados por defecto.      
        # Obtenemos los momentos clave
        inicio_año = '2023-01-01' 
        
        tenencia_inicial=f'Tenencia 31-12-22 {nombre_cliente}'
        transferencia_alyc='Transferencias entre alycs y div en especie'
        
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})'
        # -----------------------------------------------------------------------------
        movimiento_pesos=f'Cuenta Corriente PESOS {fecha_movimientos}' 
        movimiento_usd=f'Cuenta Corriente DOLARES {fecha_movimientos}' 
        movimiento_ccl=f'Cuenta Corriente DOLARES CABLE {fecha_movimientos}' 
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
            
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            #                       IMPORTACION DE ARCHIVOS EXCEL
            # -----------------------------------------------------------------------------
            # Se importan los archivos con los movimientos de la cuenta. Sobre cada uno se
            # toma la máscara que contiene movimientos en fechas previas o iguales a la fecha
            # de cierre. Y se ordenan cronológicamente las operaciones.
            # -----------------------------------------------------------------------------
            # Se transforma la fecha de cierre al tipo datetime
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            inicio_año=dt.strptime(inicio_año,'%Y-%m-%d')
            
            # Importamos la tenencia inicial, eliminamos la columna de precios, y tomamos
            # solo los tickets, la liquidez no (pues queda sujeta al saldo, quien cambia
            # automaticamente). En simultaneo, usamos 'try - except' por si el archivo de 
            # tenencia inicial no existe.
            try:
                cartera_inicial_1=pd.read_excel(f'{directorio_origen}\{tenencia_inicial}.xlsx'
                                              ).set_index('Especie')
                cartera_inicial_1.drop(cartera_inicial_1.columns[-1],axis=1,inplace=True)
                cartera_inicial=cartera_inicial_1.iloc[:-4].copy()
            
            except:
                cartera_inicial=0
            
            
            # Importamos el archivo en pesos y lo ordenamos cronologiamente por columna "Liquida",
            # y recalculamos el saldo. El 'Try - except' es para contemplar la situacion donde
            # este archivo no existe. Adicionalmente, se identifican las cauciones dentro 
            # de la tabla de bullmarket que quedan fuera de la mascara por fecha de cierre. 
            # El opuesto del importe de estas cauciones se sumara al saldo liquido en pesos.
            try:   
                archivo_pesos = fc.concatenacion_movimientos_bull(moneda = 'Pesos', alyc = alyc, 
                                                                  dni = dni,
                                                                  nombre_cliente = nombre_cliente, 
                                                                  numero_interno = numero_interno, 
                                                                  usuario = usuario)
                archivo_pesos = archivo_pesos.loc[archivo_pesos.Operado >= inicio_año].copy()
                
                # Mascaras para calculo de liquidez en pesos
                cauciones_y_div = archivo_pesos.loc[(archivo_pesos.index <= fecha_cierre)].copy()
                cauciones_y_div = cauciones_y_div.loc[(cauciones_y_div.Especie == 'VARIAS') |
                                                      (cauciones_y_div.Comprobante == 'DIVIDENDOS')].copy()
                
                cauciones_y_div_locos = archivo_pesos.loc[(archivo_pesos.Operado <= fecha_cierre) &
                                                          (archivo_pesos.index > fecha_cierre)].copy()
                cauciones_y_div_locos = cauciones_y_div_locos.loc[(cauciones_y_div_locos.Especie == 'VARIAS') |
                                                                  (cauciones_y_div_locos.Comprobante == 'DIVIDENDOS')].copy()
                
                compras_y_ventas = archivo_pesos.loc[(archivo_pesos.index <= fecha_cierre)].copy()
                compras_y_ventas = compras_y_ventas.loc[(compras_y_ventas.Especie != 'VARIAS') &
                                                        (compras_y_ventas.Comprobante != 'DIVIDENDOS')].copy()
                
                compras_y_ventas_locas = archivo_pesos.loc[(archivo_pesos.Operado <= fecha_cierre) &
                                                          (archivo_pesos.index > fecha_cierre)].copy()
                compras_y_ventas_locas = compras_y_ventas_locas.loc[(compras_y_ventas_locas.Especie != 'VARIAS') &
                                                                    (compras_y_ventas_locas.Comprobante != 'DIVIDENDOS')].copy()
                
                # Se toma la mascara de acuerdo a la fecha de cierre y las 'operaciones locas'
                # que implican cambios en la liquidez y cantidad de papales; y también, las
                # 'operaciones_relocas' que también implican cambios en la liquidez.
                operaciones_locas=archivo_pesos.loc[(archivo_pesos.Operado<=fecha_cierre) &
                                                (archivo_pesos.index>fecha_cierre) &
                                                (archivo_pesos.Comprobante!='COMPRA CAUCION TERMINO')].copy()
                
                archivo_pesos=archivo_pesos.loc[archivo_pesos.index<=fecha_cierre].copy()
            
            except:
                archivo_pesos = pd.DataFrame()
                operaciones_locas = pd.DataFrame()
                cauciones = pd.DataFrame()
                cauciones_bis = pd.DataFrame()
            
            
            # Importamos el archivo en dolares y se ordena cronologicamente por columna "Liquida"
            # recalculando el saldo. El 'Try - except' es para contemplar la situacion donde
            # este archivo no existe.
            try:
                archivo_usd = fc.concatenacion_movimientos_bull(moneda = 'Dolares', alyc = alyc, 
                                                                  dni = dni,
                                                                  nombre_cliente = nombre_cliente, 
                                                                  numero_interno = numero_interno, 
                                                                  usuario = usuario)
                archivo_usd = archivo_usd.loc[archivo_usd.index >= inicio_año].copy()
                
                operaciones_locas_usd=archivo_usd.loc[(archivo_usd.Operado<=fecha_cierre) &
                                                (archivo_usd.index>fecha_cierre)].copy()
                
                if len(operaciones_locas_usd)>0:
                    importe_operaciones_usd=operaciones_locas_usd.Importe.sum()
                else:
                    importe_operaciones_usd=0
                   
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_usd=archivo_usd.loc[archivo_usd.index<=fecha_cierre].copy()
            
            except:
                archivo_usd=pd.DataFrame()
                importe_operaciones_usd = 0
            
            
            # Importamos el archivo en dolares cable. El 'Try - except' es para contemplar
            # la situacion donde este archivo no existe. 
            try:
                archivo_ccl = fc.concatenacion_movimientos_bull(moneda = 'Dolares cable', alyc = alyc, 
                                                                  dni = dni,
                                                                  nombre_cliente = nombre_cliente, 
                                                                  numero_interno = numero_interno, 
                                                                  usuario = usuario)
                archivo_ccl = archivo_ccl.loc[archivo_ccl.index >= inicio_año].copy()   
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_ccl=archivo_ccl.loc[archivo_ccl.index<=fecha_cierre].copy()
            
            except:
                archivo_ccl=pd.DataFrame()
            
            
            # Traemos el archivo que contiene las transferencias entre alycs.
            try:
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')
                archivo_transf_alyc.set_index("Liquida", inplace=True)   
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.index<=fecha_cierre].copy()
                
            except:
                archivo_transf_alyc = pd.DataFrame()
            
            
            
            
            # ----------------------------- SEGUNDA PARTE ---------------------------------
            #     COMPOSICIONES PARCIALES DE CARTERA - MOVIMIENTOS EN PESOS Y DOLARES 
            # -----------------------------------------------------------------------------
            # Armamos los dataframes agrupando de acuerdo a los tickets, compras/ventas, y 
            # calculando las cantidades mantenidas hasta la fecha de cierre (inclusive). 
            # Esto se hace con los tres archivos, movimientos en pesos, en usd, y en ccl.  
            # -----------------------------------------------------------------------------
            # Movimientos en pesos, eliminamos las cauciones, quienes se tratan mas adelante.
            if archivo_pesos.empty:
                cartera_pesos=pd.DataFrame()
                cartera_pesos2=pd.DataFrame()
                
                if type(cartera_inicial)==type(0):
                    liquidez_pesos=0
                else:
                    liquidez_pesos=cartera_inicial_1.loc['liquidez_pesos','Cantidad']
                
            else:
                cartera_pesos=archivo_pesos.groupby('Especie').Cantidad.sum()
                cartera_pesos=pd.DataFrame(cartera_pesos)
                
                if len(operaciones_locas)>0:
                    cartera_pesos2=operaciones_locas.groupby('Especie').Cantidad.sum()
                    cartera_pesos2=pd.DataFrame(cartera_pesos2)
                else:
                    cartera_pesos2=pd.DataFrame()
                
                if len(cartera_pesos.loc[cartera_pesos.index=='VARIAS'])>0:
                    cartera_pesos.drop('VARIAS',axis=0,inplace=True)
                
            
            # Armamos cuatro mascaras que nos permitiran obtener la liquidez    
            if archivo_pesos.empty == False:
                liq_cauciones_y_div = cauciones_y_div.Importe.sum()
                
                liq_cauciones_y_div_locos = cauciones_y_div_locos.Importe.sum()
                
                liq_compras_y_ventas = compras_y_ventas.Importe.sum()
                
                liq_compras_y_ventas_locas = compras_y_ventas_locas.Importe.sum()
                
                liquidez_pesos = (liq_cauciones_y_div + liq_cauciones_y_div_locos) + (
                                  liq_compras_y_ventas + liq_compras_y_ventas_locas)
            
            
            # Ajustamos la liquidez en pesos de acuerdo a la existencia de saldos en pesos
            # antes del 01-01-23 (inicio del año 2023)
            if (type(cartera_inicial) != type(0)) & (archivo_pesos.empty == False):
                saldo_inicial = archivo_pesos.Saldo.iloc[0] + archivo_pesos.Importe.iloc[0] * -1
                
                liquidez_pesos = liquidez_pesos + saldo_inicial
                
            
            # Cartera por tenencia
            if archivo_transf_alyc.empty:
                cartera_trans_alyc = pd.DataFrame()
            
            else:
                cartera_trans_alyc = archivo_transf_alyc.groupby('Especie').Cantidad.sum()
                cartera_trans_alyc = pd.DataFrame(cartera_trans_alyc)
            
            
            # Se calcula la tenencia por split.
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            papeles_split = fc.split_bull(fecha_cierre = fecha_cierre, alyc = alyc, dni = dni,
                                          nombre_cliente = nombre_cliente, 
                                          numero_interno = numero_interno,
                                          tipo_calculo = tipo_calculo,
                                          usuario = usuario)
            
            
            # Se reconvierte la 'fecha de cierre' a formato datetime.
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Movimientos en dolares (mep y ccl)
            # Estos movimientos pueden no existir antes de la fecha de cierre, por ende, los
            # dataframes correspondientes estaran vacios. Debemos tener en cuenta esta posibi-
            # lidad para evitar que el codigo se rompa. 
            if len(archivo_usd.index)>0:
                cartera_usd = archivo_usd.groupby('Especie').Cantidad.sum()
                cartera_usd = pd.DataFrame(cartera_usd)
                saldo_usd = archivo_usd.loc[:,'Saldo'].iloc[-1] + importe_operaciones_usd
                
                if len(operaciones_locas_usd)>0:
                    papeles_locos_usd = pd.DataFrame()
                    papeles_locos_usd['Especie'] = operaciones_locas_usd.Especie
                    papeles_locos_usd['Cantidad'] = operaciones_locas_usd.Cantidad
                    papeles_locos_usd.reset_index(inplace=True)
                    papeles_locos_usd.drop('Liquida',axis=1,inplace=True)
                    papeles_locos_usd.set_index('Especie', inplace=True)
                    
                    cartera_usd = pd.concat([cartera_usd, papeles_locos_usd],ignore_index=False)
                    cartera_usd=cartera_usd.groupby(cartera_usd.index).Cantidad.sum()
                    cartera_usd=pd.DataFrame(cartera_usd)
                
            else:
                cartera_usd=0
                saldo_usd=0
                
            if len(archivo_ccl.index)>0:
                cartera_ccl=archivo_ccl.groupby('Especie').Cantidad.sum()
                cartera_ccl=pd.DataFrame(cartera_ccl)
                saldo_ccl=archivo_ccl.Saldo.iloc[-1]
            else:
                cartera_ccl=0
                saldo_ccl=0
            
            
            # Liquidez en dolares
            try:
                tenencia_inicial_usdtotal=cartera_inicial_1.loc['liquidez_usd','Cantidad']
                tenencia_inicial_ccl=cartera_inicial_1.loc['ccl','Cantidad']
            
            except:
                tenencia_inicial_usdtotal=0
                tenencia_inicial_ccl=0
            
            if (saldo_usd!=0) & (saldo_ccl!=0):
                liquidez_usd=saldo_usd+saldo_ccl
            
            elif (tenencia_inicial_usdtotal!=0) & (saldo_usd==0) & (saldo_ccl!=0):
                if archivo_usd.empty:
                    liquidez_usd = tenencia_inicial_usdtotal - tenencia_inicial_ccl + saldo_ccl 
                    
                else:
                    liquidez_usd = saldo_usd + saldo_ccl 
            
            elif (tenencia_inicial_usdtotal!=0) & (saldo_usd!=0) & (saldo_ccl==0):
                if archivo_ccl.empty:
                    liquidez_usd = tenencia_inicial_usdtotal - (tenencia_inicial_usdtotal
                            - tenencia_inicial_ccl) + saldo_usd 
                
                else:
                    liquidez_usd = saldo_usd + saldo_ccl
            
            elif (tenencia_inicial_usdtotal==0) & (saldo_usd!=0) & (saldo_ccl==0):
                liquidez_usd = saldo_usd
            
            elif (tenencia_inicial_usdtotal==0) & (saldo_usd==0) & (saldo_ccl!=0):
                liquidez_usd = saldo_ccl
            
            elif (tenencia_inicial_usdtotal==0) & (saldo_usd==0) & (saldo_ccl==0):
                liquidez_usd = 0
            
            else:
                liquidez_usd = tenencia_inicial_usdtotal                                   
                                                                              
            
            # Se incorpora la tenencia de euros a la liquidez en dolares, por ende, esta 
            # divisa se cotiza como dolares mep. Ademas, eliminamos este ticket de la tenencia
            # inicial 
            if type(cartera_inicial)!=type(0): 
                if len(cartera_inicial.loc[cartera_inicial.index=='EUR'])>0:
                    cartera_inicial.drop('EUR',axis=0,inplace=True)
            
            
            
            
            # ----------------------------- TERCERA PARTE ---------------------------------
            #       COMPOSICIONES PARCIALES DE CARTERA - INTEGRANDO LOS MOVIMIENTOS 
            # -----------------------------------------------------------------------------
            # Fusionamos las carteras en un nuevo vector llamado 'cartera' (recordar que los
            # movimientos en mep y ccl pueden no existir)
            if (type(cartera_usd)==type(0))&(type(cartera_ccl)==type(0)):
                cartera=pd.DataFrame(cartera_pesos)
                cartera=pd.DataFrame(cartera)
                
            elif (type(cartera_usd)==type(0))&(type(cartera_ccl)!=type(0)):
                cartera=pd.concat([cartera_pesos,cartera_ccl],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            elif (type(cartera_usd)!=type(0))&(type(cartera_ccl)==type(0)):
                cartera=pd.concat([cartera_pesos,cartera_usd],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            else:
                cartera=pd.concat([cartera_pesos,cartera_usd,cartera_ccl],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            
            # Ahora fusionamos la cartera con las 'operaciones locas' halladas en la primera parte.
            if cartera.empty:
                cartera=cartera_pesos2.copy()
            
            elif cartera_pesos2.empty:
                cartera=cartera
            
            else:
                cartera=pd.concat([cartera_pesos2,cartera],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            
            # Se fusiona la 'cartera' con 'cartera_trans_alyc'
            if cartera_trans_alyc.empty:
                cartera = cartera
                
            else:
                cartera = pd.concat([cartera,cartera_trans_alyc],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                
            
            # Se fusiona la 'cartera' con 'papeles_split'.
            if papeles_split.empty:
                cartera = cartera
            
            else: 
                cartera = pd.concat([cartera,papeles_split],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)       
            
            
            
            
            # ----------------------------- CUARTA PARTE ----------------------------------
            #  COMPOSICION PARCIAL DE CARTERA - UNION ENTRE TENENCIA INICIAL Y MOVIMIENTOS
            # -----------------------------------------------------------------------------
            # Concatenamos los dataframes y nos quedamos con las cantidades positivas 
            if (type(cartera_inicial)!=type(0))&(type(cartera)!=type(0)):
                cartera=pd.concat([cartera,cartera_inicial],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                cartera=cartera.loc[cartera.Cantidad>0].copy()
            
            elif (type(cartera_inicial)!=type(0))&(type(cartera)==type(0)):
                cartera=cartera_inicial.copy()
                
            elif (type(cartera_inicial)==type(0))&(type(cartera)!=type(0)):
                cartera=cartera.copy()
                
            else:
                cartera=pd.DataFrame()
            
            
            # Se elimina la fila 'ccl' en caso de existir
            if len(cartera)>0:
                ccl=cartera.loc[cartera.index=='ccl'].copy()
            
                if len(ccl)==1:
                    cartera.drop('ccl',axis=0,inplace=True)
                
            
            # Tomamos los papeles con cantidades positivas. Existen pagos de dividendos que 
            # son en bonos, sin embargo, bullmarket no los refleja en sus archivos de movimientos
            # por ende, solo sabes de su existencia cuando son vendidos, operacion que genera
            # una cantidad negativa en dicho ticket. 
            if len(cartera)==0:
                cartera=pd.DataFrame()
            else:
                cartera=cartera.loc[cartera.Cantidad>0].copy() 
            
            
            
            
            # ----------------------------- QUINTA PARTE ----------------------------------
            #     PAUSAMOS LA IDENTIFICACION DE LA CARTERA PARA GENERAR VECTOR MEP  
            # -----------------------------------------------------------------------------
            # Incorporamos las ventas MEP para identificar posibles retiros de dolares. Esto
            # se resuelve en dos grandes pasos: 1) eliminacion de operaciones rechazadas, y 
            # 2) construccion del vector mep.
            #
            # Tomamos la mascara cuyos registros implican una salida de dolares por MEP y 
            # una entrada de dolares por rechazo de la orden de salida.
            if len(archivo_usd.index)>0:
                mascara_mep=archivo_usd.loc[(archivo_usd.Comprobante=='ORD PAGO DOLARES') | 
                                        (archivo_usd.Comprobante=='RECIBO DE COBRO DOLARES') & 
                                        (archivo_usd.Referencia!='CREDITO CTA. CTE.')].copy()
            else:
                mascara_mep=pd.DataFrame()
            
            
            # Ahora eliminamos las operaciones rechazadas, considerando la posibilidad de que 
            # no existan operaciones mep.
            if len(mascara_mep.index)>0:
                
                # Montos rechazados
                rechazos=mascara_mep.loc[mascara_mep.Comprobante=='RECIBO DE COBRO DOLARES'].Importe
                rechazos=pd.DataFrame(rechazos)
                
                for i in rechazos.Importe:
                    
                    # Identificando lo rechazado y devuelto
                    a=mascara_mep.loc[mascara_mep.Importe==i*-1].iloc[0].Numero
                    b=mascara_mep.loc[mascara_mep.Importe==i].iloc[0].Comprobante
                    
                    # Drop de lo rechazado y devuelto
                    mascara_mep=mascara_mep.drop(mascara_mep[mascara_mep['Numero']==a].index)
                    mascara_mep=mascara_mep.drop(mascara_mep[mascara_mep['Comprobante']==b].index)
                    
            else:    
                mascara_mep=0
            
            
            # Creamos vector de operaciones mep, quien contiene: fecha, ticket, y nominales
            oper_mep=[]
            
            if type(mascara_mep)==type(0):
                oper_mep=0
            else:
                oper_mep=pd.DataFrame(oper_mep)
                oper_mep['Especie']=mascara_mep.Especie
                oper_mep['Cantidad']=mascara_mep.Importe
            
            
            # Al vector de operaciones mep le colocamos los mismos nombres de columnas que 
            # tendra el vector "cartera". Al proceso lo ajustamos por si no existen estas ope-
            # raciones.
            if type(oper_mep)==type(0):
                oper_mep=0
            else:
                oper_mep.reset_index(inplace=True)
                oper_mep.set_index('Cantidad',inplace=True)
                oper_mep.reset_index(inplace=True)
                oper_mep.set_index('Especie',inplace=True)
                oper_mep=oper_mep.rename(columns={'Liquida':fecha_cierre})
            
            
            # Generamos una tercer columna donde se pondra la fecha de la operacion mep
            if type(oper_mep)==type(0):
                oper_mep=0
            else:
                oper_mep['fecha mep']=oper_mep[fecha_cierre]
                oper_mep[fecha_cierre]=0
            
            
            # Incorporamos la columna donde colocaremos los precios de cada papel y del
            # dolar mep. Tambien se crea la columna 'fecha mep' donde se ubicara en las
            # siguientes lineas la fecha donde se realiza cada operacion mep.
            if cartera.empty:
                cartera['Cantidad']=0
                cartera[fecha_cierre]=0
                cartera['fecha mep']=0
            else:
                cartera[fecha_cierre]=0
                cartera['fecha mep']=0
               
            
            
            
            # ------------------------------ SEXTA PARTE ----------------------------------
            #             SE UNIFICA LA CARTERA CON EL VECTOR MEP + LIQUIDEZ
            # -----------------------------------------------------------------------------
            # Incoporamos las operaciones mep nucleadas en el vector "oper_mep", ajustando
            # para el caso donde no existen
            if type(oper_mep)==type(0):
                cartera=cartera
            else:
                cartera=pd.concat([cartera,oper_mep],ignore_index=False)
            
            
            # Incorporamos los saldos liquidos en pesos y en dolares al vector "cartera". Se
            # incorpora la fila 'PRECIO MEP' donde colocaremos a mano el precio MEP de la 
            # fecha de cierre
            cartera.loc['liquidez_usd']=float(0)
            cartera.loc['liquidez_usd','Cantidad']=liquidez_usd
            
            cartera.loc['PRECIO MEP']=float(0)
            
            cartera.loc['liquidez_pesos']=float(1)
            cartera.loc['liquidez_pesos','Cantidad']=liquidez_pesos
            cartera.loc['liquidez_pesos','fecha mep']=float(0)
            
            
            
            
            # --------------------------- SEPTIMA PARTE -----------------------------------
            #            SE COLOCAN LOS PRECIOS A CADA UNO DE LOS PAPELES
            # -----------------------------------------------------------------------------
            # Creamos una cartera donde solo esten los tickets de las acciones
            mep=cartera.loc[cartera.index=='MEP'].copy()
            
            if mep.empty==True:
                cartera2=cartera.drop(['PRECIO MEP','liquidez_pesos'])
            
            else:
                cartera2=cartera.drop(['liquidez_usd','PRECIO MEP','liquidez_pesos','MEP'])
            
            
            # Importamos el archivo en pesos
            archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                          ,sheet_name='Hoja 2').set_index('fecha')
            
            
            # Resolvemos la fecha de cierre por si no existen precios en dicho momento
            fecha_cierre2=fecha_cierre
            for i in range(60):
                
                if len(archivo_precios.loc[archivo_precios.index==(fecha_cierre-timedelta(days=i))])==0:
                    fecha_cierre2=fecha_cierre-timedelta(days=i)
                    
                else:
                    fecha_cierre2=fecha_cierre-timedelta(days=i)
                
                if len(archivo_precios.loc[archivo_precios.index==fecha_cierre2])==1:
                    break
            
            
            # Colocamos los precios de las acciones y dolar mep, si el papel no esta en la
            # serie excel de precios, entonces como precio colocamos el valor 0 (cero)
            cartera[fecha_cierre] = cartera[fecha_cierre].astype(float)
            for i in cartera2.index:
                try:
                    precio=archivo_precios.loc[fecha_cierre2,i]
                    if math.isnan(precio):
                        cartera.loc[i,fecha_cierre] = 0
                    
                    else:
                        cartera.loc[i,fecha_cierre] = precio
                    
                except:
                    cartera.loc[i,fecha_cierre]=0    
            
            
            # Se genera el vector de precios MEP vigentes en las fechas donde se hace la 
            # operacion MEP. Se lo ajusta por si no existen dichas operaciones.   
            vector_mep=pd.DataFrame()
            vector_mep['precio']=float(0)
            
            if len(cartera.loc[cartera.index=='MEP'])>0:  
                
                if len(cartera.loc[cartera.index=='MEP'])>1:
                    
                    for i in range(len(cartera.loc['MEP','fecha mep'])):
                        vector_mep.loc[cartera.loc['MEP','fecha mep'].iloc[i]]=float(0)
                
                    for i in range(len(vector_mep)):
                        try:
                            vector_mep.iloc[i,0]=archivo_precios.loc[vector_mep.index[i],'dolar_mep']
                        
                        except:
                            fecha=vector_mep.index[i]
                            for j in range(60):
                                
                                if len(archivo_precios.loc[archivo_precios.index==(vector_mep.index[i]-timedelta(days=j))])==0:
                                    fecha=vector_mep.index[i]-timedelta(days=j)
                                    
                                else:
                                    fecha=vector_mep.index[i]-timedelta(days=j)
                                
                                if len(archivo_precios.loc[archivo_precios.index==fecha])==1:
                                    break
                            
                            
                            vector_mep.iloc[i,0]=archivo_precios.loc[fecha,'dolar_mep']
                            
                else:
                    vector_mep.loc[cartera.loc['MEP','fecha mep']]=float(0)
                    
                    fecha=vector_mep.index[0]
                    for j in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(vector_mep.index[0]-timedelta(days=j))])==0:
                            fecha=vector_mep.index[0]-timedelta(days=j)
                            
                        else:
                            fecha=vector_mep.index[0]-timedelta(days=j)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha])==1:
                            break
                        
                    vector_mep.iloc[0,0]=archivo_precios.loc[fecha,'dolar_mep']
                    
            
            # Cambiamos el indice de la cartera temporalmente (para colocar el precio del mep)
            cartera.reset_index(inplace=True)
            cartera.set_index('fecha mep',inplace=True)
            
            
            # Colocamos el precio del dolar mep segun la fecha donde se lo opero
            for i in cartera.index:
                if i != 0:        
                    if vector_mep.empty:
                        ''
                        
                    else:
                        cartera.loc[i,fecha_cierre]=vector_mep.loc[i,'precio']
              
            
            # Devolvemos el indice a la normalidad
            cartera.reset_index(inplace=True)
            cartera.set_index(fecha_cierre,inplace=True)
            
            cartera.reset_index(inplace=True)
            cartera.set_index('Cantidad',inplace=True)
            
            if cartera.columns[-1]=='index':    
                cartera=cartera.rename(columns={'index':'Especie'})
                cartera.reset_index(inplace=True)
                cartera.set_index('Especie',inplace=True)
            
            cartera.reset_index(inplace=True)
            cartera.set_index('Especie',inplace=True)
            
            
            # Colocamos el precio MEP actual 
            cartera.loc['liquidez_usd',fecha_cierre]=archivo_precios.loc[fecha_cierre2,'dolar_mep']
            cartera.loc['PRECIO MEP',fecha_cierre]=archivo_precios.loc[fecha_cierre2,'dolar_mep']
            
            
            # Tomamos la mascara de la cartera para la cual los valores en la columna 'cantidad" 
            # son diferentes a cero. 
            cartera3 = cartera.iloc[:-3,:].copy()
            cartera4 = cartera.iloc[-3:,:].copy()
            cartera3 = cartera3.loc[cartera3['Cantidad']!=0].copy()
            
            cartera = pd.concat([cartera3,cartera4])
            cartera = pd.DataFrame(cartera)
            
            
            cartera = cartera
            
        else:
            cartera = datos_cliente

    except:
       cartera = 'Introduzca un usuario válido: Numero entero entre 1 y 6'


    return cartera






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def honorario(fecha_cierre, alyc='', nombre_cliente='', numero_interno=0, dni=0,
              usuario = 1, alicuota1 = 0.005, alicuota2 = 0.0025, sumafija = 1_500,
              alicuota = 0.015/12, ctte_adm = 'no'):

    """ 
    ---------------------------------------------------------------------------
                               ¿PARA QUE SIRVE?
    Es util para obtener los honorarios de la cartera. 
    ---------------------------------------------------------------------------
                               ¿COMO FUNCIONA? 
    Utiliza la función 'composicion_carteraF', con la cual se obtiene la carte-
    ra del cliente con cuenta en bullmarket en la fecha de cierre indicada.  
    A parte de esta se calcula su valor y se aplican la alicuota que corresponde.
    ---------------------------------------------------------------------------
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene cuenta. Puede ser Bull, Ieb, o Balanz. 
        No importa si el nombre de la alyc se escribe con mayusculas o acentos.  
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, el que figura en la cuenta comitente. Puede 
        escribirse con mayusculas y acentos. 
        Ejemplo: 'Marco Aurelio'.
    
    dni : tipo integer.
    
        DESCRIPCION.
        Es el dni del cliente. No debe escribirse con separadores, puntos o comas.
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa le asigno al cliente.  
        Valor por defecto: 0.
        
    ctte_adm : tipo string.
    
        DESCRIPCION.
        Permite obtener los retiros y depositos considerando las transferencias 
        de papeles en determinadas circunstancias. Admite uno de tres valores: 
        1) 'si', en este caso se consideran solo las transferencias entre cttes
        administradas por catalaxia; 2) 'no', en este caso se considera todo lo 
        no sea una transferencia hecha entre cttes administradas por catalaxia; 
        y 3) '', en este caso si considera todo tipo de transferencia. 
        Valor por defecto: 'no'.
        
        
    Resultado
    -------
    honorario : tipo DataFrame.
       
       DESCRIPCION.
       Es una tabla con el valor de cartera, los honorarios totales, y la fecha
       correspondiente.

    """
    
    
    try:
        # usuario = 4 
        # -----------------------------------------------------------------------------
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
           
        # ----------------------------------------------------------------------------
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        import pandas as pd
        from datetime import datetime as dt   
        from datetime import timedelta
        
        
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
            fondo_retiro = datos_cliente.loc['Fondo de retiro', 'Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            fondo_retiro = ''
        
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})'
        movimiento_pesos=f'Cuenta Corriente PESOS {fecha_movimientos}' 
        
        directorio_clasificador=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        nombre_clasificador='- Categorias de papeles para calculo de honorarios'
        
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # -----------------------------------------------------------------------------
            #    SE OBTIENEN LOS VALORES BRUTOS SOBRE LOS QUE SE CALCULAN LOS HONORARIOS
            # -----------------------------------------------------------------------------
            # Se importa la cartera con tickets, cantidades, precios, mep, y saldo liquido
            # que corresponde a la fecha de cierre.
            try:
                cartera=fc.composicion_cartera_bull(fecha_cierre=fecha_cierre, alyc=alyc,
                                                    dni=dni, numero_interno=numero_interno,
                                                    nombre_cliente=nombre_cliente, 
                                                    usuario = usuario)
                
                mep=cartera.iloc[-2,1]
            
                cartera['monto']=cartera.Cantidad*cartera.iloc[:,1]
            
            except:
                cartera=pd.DataFrame()
            
            if cartera.empty:
                portafolio=pd.DataFrame()
                
            else:
                # Se corrige por la presencia de operaciones MEP
                if len(cartera.loc[cartera.index=='MEP'])>0:
                    cartera.drop('MEP',axis=0,inplace=True)
                
                cartera.drop('PRECIO MEP',inplace=True)
                cartera.drop(['Cantidad','fecha mep'],axis=1,inplace=True)
                cartera.drop(cartera.columns[0],axis=1,inplace=True)
            
            
            # Tomamos la mascara con solo valores positivos
            cartera = cartera.loc[cartera.monto > 0].copy()    
            
            
            # Identificamos los papeles en cartera para elegir la alicuota que corresponde
            clasificador=pd.read_excel(
                f'{directorio_clasificador}/{nombre_clasificador}.xlsx').set_index('papel')
            
            cartera['categoria']=str(0)
            
            for i in cartera.index:
                cartera.loc[i,'categoria']=clasificador.loc[i,'clasificacion']
            
            
            # Agrupamos el monto de la cartera de acuerdo a esta categorizacion y calculamos
            # su participacion
            cartera2=cartera.groupby('categoria').sum()
            cartera2['porcentaje']=cartera2.monto/cartera2.monto.sum()
            
            
            
            # -----------------------------------------------------------------------------
            #    SE OBTIENEN LOS VALORES NETOS SOBRE LOS QUE SE CALCULAN LOS HONORARIOS
            # -----------------------------------------------------------------------------
            # Identificamos los depositos hechos durante el ultimo mes. Para esto debemos 
            # definir el periodo de tiempo entre la fecha de cierre y el ultimo cobro de honorarios.
            
            # El punto de partida es la fecha de cierre, momento donde queremos cobrar los
            # honorarios. Utilizandola junto con el 'dia de corte' del dataframe 'datos_cliente'
            # definimos la fecha del ultimo cobro de honorarios.
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Objetivo: definir puntas del periodo: 1) fecha de cierre es punta final, 2) 
            # fecha ultimo cobro es punta inicial. Esta ultima debe definirse e implica iden-
            # tificar si dada la fecha de cierre hay o no cambio de mes. Si el dia de la 
            # fecha de cierre es menor o igual al dia de fecha de cobro entonces hay cambio 
            # de mes, si es mayor entonces no lo hay. 
            # Con el siguiente condicional identificamos si cambiamos o no de mes
            if fecha_cierre.day <= datos_cliente.iloc[3,0]:
                # Cambiamos el mes del siguiente modo
                try:    
                    # Controlando los dias por febrero 
                    if (datos_cliente.iloc[3,0] > 28) & (fecha_cierre.month == 3):
                        fecha_ultimo_cobro = fecha_cierre.replace(month = 2, day = 28)
                    
                    # Controlando los dias por meses con 31 dias
                    elif datos_cliente.iloc[3,0] == 31:
                        fecha_ultimo_cobro = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                                  day = 30)
                        
                    # Sin necesidad de controles sobre los dias
                    else:
                        fecha_ultimo_cobro = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                                  day = datos_cliente.iloc[3,0])
                    
                except ValueError:
                    # Cambio de año por tener fecha de cierre en enero y de ultimo cobro en diciembre
                    fecha_ultimo_cobro = fecha_cierre.replace(year = fecha_cierre.year-1, month = 12,
                                                              day = datos_cliente.iloc[3,0])
                    
            else:
                # Al no cambiar de mes solo hay que modificar el dia
                fecha_ultimo_cobro = fecha_cierre.replace(day = datos_cliente.iloc[3,0])
            
            
            # Definimos la proxima fecha de cobro de honorarios, tomando como punto de 
            # partida la 'fecha_cierre'
            # Controlando el mes por cambio de año  
            if fecha_ultimo_cobro.month == 12:
                fecha_prox_cobro = fecha_ultimo_cobro.replace(month = 1, 
                                                              year = fecha_ultimo_cobro.year + 1)
            
            # Controlando los dias por meses con 31 dias
            elif (fecha_ultimo_cobro.day == 31) & (fecha_ultimo_cobro.month != 1):
                fecha_prox_cobro = fecha_ultimo_cobro.replace(month = fecha_ultimo_cobro.month + 1, 
                                                              day = 30)
                
            # Controlando por mes de febrero
            elif (fecha_ultimo_cobro.month == 1) & (fecha_ultimo_cobro.day > 28):
                fecha_prox_cobro = fecha_ultimo_cobro.replace(month = 2, day = 28)
                
            else:
                fecha_prox_cobro = fecha_ultimo_cobro.replace(month = fecha_ultimo_cobro.month + 1)
               
            dias_plazo = (fecha_prox_cobro - fecha_ultimo_cobro).days
               
            
            # Obtenemos los movimientos del periodo de interes
            fecha_ultimo_cobro = dt.strftime(fecha_ultimo_cobro,'%Y-%m-%d')
            fecha_cierre = dt.strftime(fecha_cierre,'%Y-%m-%d')
            
            movimientos = fc.depositos_retiros_bull(fecha_cierre = fecha_cierre,
                                                    fecha_inicial = fecha_ultimo_cobro,
                                                    usuario = usuario,
                                                    numero_interno = numero_interno,
                                                    ctte_adm = ctte_adm)
            
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_ultimo_cobro = dt.strptime(fecha_ultimo_cobro,'%Y-%m-%d')
            
            
            # Teniendo los movimientos y las fechas ajustamos los depositos y los retiros
            # Los depositos ajustados son los que restamos del valor de la cartera
            # Los retiros ajustados son los que sumamos al valor de la cartera
            movimientos['depositos_ajus'] = float(0)
            movimientos['retiros_ajus'] = float(0)
            
            for i in movimientos.index:
                movimientos.loc[i,'depositos_ajus'] = movimientos.loc[i,'depositos'] * (
                                                    (movimientos.fecha[i]- fecha_ultimo_cobro).days) / dias_plazo     
                
                movimientos.loc[i,'retiros_ajus'] = movimientos.loc[i,'retiros'] * (
                                                    (movimientos.fecha[i]- fecha_ultimo_cobro).days) / dias_plazo
                
            total_depositos_ajustados = movimientos['depositos_ajus'].sum() # Monto a restar de la cartera
            total_retiros_ajustados = movimientos['retiros_ajus'].sum() # Monto a sumar a la cartera
            
            
            # Obtenemos el valor bruto de cartera
            valor_bruto = cartera2.monto.sum()
            
            
            # El valor neto de la cartera se obtiene restandole los depositos ajustados y 
            # sumandole los retiros ajustados. Sin embargo, la operacion debe distribuirse equi-
            # tativamente entre las diferentes categorias de activos (renta fija, variable, liquidez).
            if len(cartera) > 0: 
                if cartera.iloc[-1,0]<0:
                    cartera2.drop('liquidez',axis=0,inplace=True)
                    cartera2['porcentaje']=cartera2['porcentaje']/cartera2['porcentaje'].sum()
                    
                    for i in cartera2.index:
                        cartera2.loc[i,'monto']=cartera2.loc[i,'monto'] + (
                                    total_retiros_ajustados - total_depositos_ajustados) * cartera2.loc[i,'porcentaje']
                 
                     
                else:
                    for i in cartera2.index:
                        cartera2.loc[i,'monto'] = cartera2.loc[i,'monto'] + (
                                    total_retiros_ajustados - total_depositos_ajustados) * cartera2.loc[i,'porcentaje']
            
                    cartera2 = cartera2.loc[cartera2.monto > 0].copy()
            
            
            # -----------------------------------------------------------------------------
            #                       SE CALCULA EL HONORARIO
            # -----------------------------------------------------------------------------
            # Los honorarios se calculan dependiendo de si la comitente esta invertida
            # en un fondo de retiro o no.
            honorario = 0
            
            if fondo_retiro == 'si': # Caso donde hay cartera de fondo de retiro
                alicuota = 0.015 / 12 
                valor_bruto_ajustado = valor_bruto - total_depositos_ajustados + total_retiros_ajustados
                
                honorario = valor_bruto_ajustado * alicuota * 1.21 
                
                
            else: # Caso donde no se tiene cartera de fondo de retiro
                alicuota1 = 0.005
                alicuota2 = 0.0025
                sumafija = 1_500
                
                valor_bruto_ajustado = valor_bruto - total_depositos_ajustados + total_retiros_ajustados
                
                
                if valor_bruto_ajustado/mep >= 10_000:    
                    
                    honorario_excedente = (valor_bruto_ajustado/mep - 10_000) * alicuota2 * mep
                    honorario_base = 10_000 * mep * alicuota1 + sumafija 
            
                    honorario = (honorario_base + honorario_excedente) * 1.21
                    
                    
                elif (valor_bruto_ajustado/mep >= 1_000) & (valor_bruto_ajustado/mep < 10_000):
                    if len(cartera2.loc[cartera2.index=='liquidez'])>0:
                        if cartera2.loc['liquidez','porcentaje']>=0.25:
                            honorario_liq = cartera2.loc['liquidez','monto']*alicuota2
                            valor_liquidez = round(cartera2.loc['liquidez','monto'],2)
                        
                        else:
                            honorario_liq = cartera2.loc['liquidez','monto']*alicuota1
                            valor_liquidez = round(cartera2.loc['liquidez','monto'],2)
                    
                    else: 
                        honorario_liq = 0
                        valor_liquidez = 0
                    
                    if len(cartera2.loc[cartera2.index=='renta fija'])>0:
                        if cartera2.loc['renta fija','porcentaje']>=0.1:
                            honorario_rf = cartera2.loc['renta fija','monto']*alicuota2
                            valor_rentaf = round(cartera2.loc['renta fija','monto'],2)
                            
                        else:
                            honorario_rf = cartera2.loc['renta fija','monto']*alicuota1
                            valor_rentaf = round(cartera2.loc['renta fija','monto'],2)
                    
                    else:
                        honorario_rf = 0
                        valor_rentaf = 0
                    
                    if len(cartera2.loc[cartera2.index=='renta variable'])>0:
                        honorario_rv = cartera2.loc['renta variable','monto']*alicuota1
                        valor_rentav = round(cartera2.loc['renta variable','monto'],2)
                        
                    else:
                        honorario_rv = 0
                        valor_rentav = 0
                
                    honorario = (honorario_rv + honorario_rf + honorario_liq + sumafija) * 1.21
                        
                else:
                    honorario = 0
                
            
            # Para calcular los honorarios proporcionales utilizamos 'dias_plazo', o sea,
            # la cantidad de dias entre la ultima fecha de cobro de honorarios y la proxima.
            # Tambien calculamos la cantidad de dias que pasaron entre la fecha de cierre 
            # y el ultimo cobro de honorarios.
            dias_trans = (fecha_cierre - fecha_ultimo_cobro).days
            
            
            # Si corresponde, aplicamos proporcionalidad sobre los honorarios
            if fecha_cierre != fecha_prox_cobro:
                honorario = honorario * dias_trans/ dias_plazo
            
            
            # Se crea un DataFrame que contiene el honorario y el valor de cartera
            if fondo_retiro == 'si':
                portafolio2={'Cartera: Fondo de retiro':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Valor imponible':[f'$ {round(valor_bruto_ajustado,2)}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
            else:
                if valor_bruto_ajustado/mep>=10_000:
                    portafolio2={'Cartera cuyo valor supera los 10 mil usd':[''],
                                  'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                                'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                                'Valor imponible':[f'$ {round(valor_bruto_ajustado,2)}'],
                                'Honorarios totales':[f'$ {round(honorario,2)}']}
                    
                    portafolio2=pd.DataFrame(portafolio2).T
                    portafolio2=portafolio2.rename(columns={0:''})
                
                elif (valor_bruto_ajustado/mep>=1_000) & (valor_bruto_ajustado/mep<10_000):
                    portafolio2={'Cartera cuyo valor se encuentra entre los mil y 10 mil usd':[''],
                                  'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                                'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                                'Valor imponible liquidez':[f'$ {valor_liquidez}'],
                                'Valor imponible renta fija':[f'$ {valor_rentaf}'],
                                'Valor imponible renta variable':[f'$ {valor_rentav}'],
                                'Honorarios totales':[f'$ {round(honorario,2)}'],
                                'Honorario liquidez':[f'$ {round(honorario_liq,2)}'],
                                'Honorarios renta fija':[f'$ {round(honorario_rf,2)}'],
                                'Honorarios renta variable':[f'$ {round(honorario_rv,2)}']}
                    
                    portafolio2=pd.DataFrame(portafolio2).T
                    portafolio2=portafolio2.rename(columns={0:''})
                
                else:
                    portafolio2={'Cartera cuyo valor es inferior a los mil usd':[''],
                                  'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                                'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                                'Honorarios totales':[f'$ {round(honorario,2)}']}
                    
                    portafolio2=pd.DataFrame(portafolio2).T
                    portafolio2=portafolio2.rename(columns={0:''})
                
                
                # Se crea un DataFrame que contiene el honorario y el valor de cartera
                portafolio={'valor cartera':[valor_bruto],'honorarios':[honorario],
                                                                        'fecha':[fecha_cierre]}
                portafolio=pd.DataFrame(portafolio).T
                portafolio=portafolio.rename(columns={0:'valores&fechas'})
              
            portafolio2 = portafolio2
                
        else:
            portafolio2 = datos_cliente

    except:
        portafolio2 = 'Introduzca un usuario válido: entero entre 1 y 6'

        
    
    return portafolio2






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def rendimientos_bruto_neto(fecha_cierre, dias, alyc = '', nombre_cliente = '',
                            numero_interno = 0, dni = 0, puntos_basicos = 0.1, 
                            usuario = 1):
    """
    ---------------------------------------------------------------------------
                              ¿PARA QUE SIRVE ESTE CODIGO?
    Para hallar la TIR bruta y neta de honorarios de la cartera. Asimismo, se 
    indica la fecha inicial y final del periodo analizado, pues de este modo 
    el resultado de la funcion puede utilizarse junto a otras funciones. 
    ---------------------------------------------------------------------------
                               ¿COMO FUNCIONA EL CODIGO? 
    Se calcula el valor inicial y final de la cartera, junto con los honorarios
    (si corresponden). Tambien, se obtienen los retiros y depositos en pesos y 
    dolares (aqui se incluyen las operaciones por dolar mep).
    A partir de esta informacion, se obtiene el rendimiento como la TIR de un
    polinomio donde se minimiza el error de calculo. Este se se define como la 
    diferencia entre el valor final e inicial de la cartera, ajustando la dife-
    rencia por los retiros y depositos. Algebraicamente:
                      error = SF - (VF[depositos]-VF[retiros]) 
    ---------------------------------------------------------------------------
                               ACLARACIONES ADICIONALES
    Este codigo es utilizado para situaciones donde el cliente realiza, durante
    el mes, menos de 50 depositos y menos de 50 retiros. De exceder estas canti-
    dades, el codigo se 'rompera' (dejara de funcionar).
    ---------------------------------------------------------------------------
    Paramentros
    ----------
    fecha_cierre : tipo string.
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
        DESCRIPCION.
        Es la alyc donde el cliente tiene su cuenta: Bull, Ieb, o Balanz. 
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    dni : tipo integer.
        DESCRIPCION.
        Es el dni del cliente.   
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
        DESCRIPCION.
        Es el numero interno asignado por la empresa al cliente.  
        Valor por defecto: 0.
        
    puntos_basicos : TYPE float
        DESCRIPCION. 
        Valor por defecto: 0.5.
        Define el incremental del iterador utilizado para hallar la TIR. En otras
        palabras, la TIR crece en 0.5 puntos basicos en el siguiente calculo.
        
    dias : tipo integer
        DESCRIPCION. 
        Valor por defecto: 30.
        Define la cantidad de dias del plazo de analisis. En otras palabras, 
        son la cantidad de dias que se restan a la fecha de cierre.              
        
        
    Resultado
    -------
    rendimiento : tipo DataFrame
        DESCRIPCION.
        Es una tabla con el rendimiento bruto y neto mensual de la cartera ana-
        lizada, junto con la fecha inicial y final del periodo correspondiente.

    """ 
    try:
        # usuario = 4 
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        import numpy as np
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
      
        puntos_basicos = 0.1
        
        
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
            dia_corte = datos_cliente.loc['Dia de corte','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
            
        # -----------------------------------------------------------------------------
        # Sub Parametros
        # Estos son parametros, pero no es necesario modificarlos.                  
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})'
        
        movimiento_pesos=f'Cuenta Corriente PESOS {fecha_movimientos}' 
        movimiento_usd=f'Cuenta Corriente DOLARES {fecha_movimientos}' 
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        transferencia_alyc='Transferencias entre alycs y div en especie'
        
        directorio_clientes=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS'
        nombre_archivo_clientes='Base de Datos de Clientes'
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            # Obtenemos el valor final e inicial de la cartera ajustando por palanca,
            # los honorarios del periodo, y el plazo correspondiente
            # -----------------------------------------------------------------------------
            # Obtenemos los momentos clave
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial=fecha_cierre-timedelta(days=dias)
            
            
            # Transformamos las fechas a formato string
            fecha_cierre=dt.strftime(fecha_cierre, '%Y-%m-%d')
            fecha_inicial=dt.strftime(fecha_inicial, '%Y-%m-%d')
            
            
            # Calculamos el VALOR DE LA CARTERA
            # Calculamos el valor inicial de la cartera controlando la palanca.
            cartera_inicio = fc.composicion_cartera_bull(fecha_cierre = fecha_inicial,
                                                          alyc = alyc, dni = dni,
                                                          nombre_cliente = nombre_cliente,
                                                          numero_interno = numero_interno,
                                                          usuario = usuario)
            
            cartera_inicio['monto'] = cartera_inicio.Cantidad * cartera_inicio.iloc[:,1]
            
            cartera_inicio = cartera_inicio.loc[cartera_inicio.index != 'MEP'].copy()
                    
            # Calculamos el valor final de la cartera controlando la palanca.
            cartera_final = fc.composicion_cartera_bull(fecha_cierre = fecha_cierre,
                                                        alyc = alyc, 
                                                        dni = dni,
                                                        nombre_cliente = nombre_cliente,
                                                        numero_interno = numero_interno,
                                                        usuario = usuario)
            
            cartera_final['monto'] = cartera_final.Cantidad * cartera_final.iloc[:,1]
                
            cartera_final = cartera_final.loc[cartera_final.index != 'MEP'].copy()
            
            # Calculamos los valores iniciales y finales de la cartera    
            valor_cierre = cartera_final.monto.sum()
            valor_inicial = cartera_inicio.monto.sum()


            # Calculamos los HONORARIOS
            # Recuerde que los mismos se calculan en diferentes fechas dependiendo 
            # del cliente. En otras palabras, no siempre se calculan a fin de mes. 
            # La fecha de corte difiere, y cuando el cliente se dio de baja tenemos 
            # que ir a la base de datos de clientes y darle un valor positivo.     
            # fecha_corte = f'{fecha_cierre[:7]}-{dia_corte}'
            fecha_cierre = dt.strptime(fecha_cierre, '%Y-%m-%d')
            
            if fecha_cierre.day >= dia_corte: # no cambia el mes para la fecha de corte
                fecha_corte = dt.strptime(f'{fecha_cierre.year}-{fecha_cierre.month}-{dia_corte}', '%Y-%m-%d')
            
            elif fecha_cierre.day < dia_corte: # cambia el mes para la fecha de corte
                try:    
                    # Controlando los dias por febrero 
                    if (datos_cliente.iloc[3,0] > 28) & (fecha_cierre.month == 3):
                        fecha_corte = fecha_cierre.replace(month = 2, day = 28)
                    
                    # Controlando los dias por meses con 31 dias
                    elif datos_cliente.iloc[3,0] == 31:
                        fecha_corte = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                           day = 30)
                        
                    # Sin necesidad de controles sobre los dias
                    else:
                        fecha_corte = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                           day = datos_cliente.iloc[3,0])
                    
                except ValueError:
                    # Cambio de año por tener fecha de cierre en enero y de ultimo cobro en diciembre
                    fecha_corte = fecha_cierre.replace(year = fecha_cierre.year-1, month = 12,
                                                       day = datos_cliente.iloc[3,0])
                        
            fecha_corte = dt.strftime(fecha_corte, "%Y-%m-%d")
            
            portafolio_fecha_corte = fc.honorario(fecha_cierre = fecha_corte, 
                                                  alyc = alyc, 
                                                  numero_interno = numero_interno,
                                                  usuario = usuario,
                                                  ctte_adm = 'no')
            
            if len(portafolio_fecha_corte) == 11:
                honorario_cierre = float(portafolio_fecha_corte.iloc[7,0][2:])
                
            elif len(portafolio_fecha_corte) == 6:
                honorario_cierre = float(portafolio_fecha_corte.iloc[5,0][2:])
            
            elif len(portafolio_fecha_corte) == 5:
                honorario_cierre = float(portafolio_fecha_corte.iloc[4,0][2:])
            
            
            # Calculamos la cantidad de dias entre la fecha de cierre y el momento
            # donde se cobran los honorarios.
            fecha_corte = dt.strptime(fecha_corte, "%Y-%m-%d")
            
            plazo_honorario = (fecha_cierre - fecha_corte).days
            
            fecha_cierre = dt.strftime(fecha_cierre, "%Y-%m-%d")
            
            
            # ----------------------------- SEGUNDA PARTE ---------------------------------
            # Se obtiene el dataframe con los movimientos (depositos, retiros, y transferencias)
            # -----------------------------------------------------------------------------
            movimientos = fc.depositos_retiros_bull(fecha_cierre = fecha_cierre, 
                                                    fecha_inicial = fecha_inicial, 
                                                    alyc = alyc, 
                                                    usuario = usuario,
                                                    numero_interno = numero_interno,
                                                    ctte_adm = '')
     
            movimientos['plazo'] = int(0)
     
            fecha_cierre = dt.strptime(fecha_cierre, "%Y-%m-%d")
     
            movimientos['plazo'] = (fecha_cierre - movimientos.iloc[:, 0]).dt.days
            movimientos.reset_index(inplace = True)
            movimientos.drop('index', axis = 1, inplace = True)
     
            fecha_cierre = dt.strftime(fecha_cierre, "%Y-%m-%d")

            
            # --------------------------- TERCERA PARTE -----------------------------------
            # Se calcula la TIR BRUTA de la cartera 
            # -----------------------------------------------------------------------------
            lista_b_error = []
            listado_b_tir = []

            for tir in np.arange(-1,1,puntos_basicos/10000):
                
                termino_dep = 0 # elemento que acumula la suma de todos los depositos capitalizados 
                termino_ret = 0 # elemento que acumula la suma de todos los retiros capitalizados   
                
                valor_inicial_bis = valor_inicial
                
                for i in range(len(movimientos)):
                    # Obteniendo depositos, retiros, y plazos
                    monto_dep = movimientos.depositos[i]
                    monto_ret = movimientos.retiros[i]
                    plazo = movimientos.plazo[i]
               
                    # Acumulacion de los depositos y retiros capitalizados
                    termino_dep = termino_dep + monto_dep * (1 + tir) ** plazo  
                    termino_ret = termino_ret + monto_ret * (1 + tir) ** plazo   

                # Capitalización del valor inicial
                valor_inicial_bis = valor_inicial_bis * (1+tir) ** dias
                
                # Calculo del error
                error = valor_cierre + termino_ret - (valor_inicial_bis + termino_dep)

                lista_b_error.append(error)
                listado_b_tir.append(tir)
                
            lista_b = pd.DataFrame()    
            lista_b['tir_diaria'] = listado_b_tir
            lista_b['error'] = lista_b_error
            lista_b['error_abs']=lista_b['error'].abs()
            lista_b.sort_values(by='error_abs',inplace=True)
            lista_b.drop(axis=1,columns='error_abs',inplace=True)

            # Ahora corregimos este listado para evitar problemas del tipo "controversia del
            # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
            # cobran honorarios. El asunto se resuelve en tres pasos:
            # PRIMERO. Slicing 10 primeros con errores mas pequeños
            lista_b = lista_b.iloc[:10,:]

            # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
            lista_b.sort_values(by='tir_diaria',inplace=True)
            lista_b = lista_b.iloc[:5,:]

            # TERCERO. Ordenamos de menor a mayor por error absoluto
            lista_b['error_abs'] = lista_b['error'].abs()
            lista_b.sort_values(by='error_abs',inplace=True)
            lista_b.drop(axis=1,columns='error_abs',inplace=True)



            # ----------------------------- CUARTA PARTE ----------------------------------
            # Se calcula la TIR neta de la cartera 
            # -----------------------------------------------------------------------------
            lista_n_error = []
            listado_n_tir = []

            for tir in np.arange(-1,1,puntos_basicos/10000):
                
                termino_dep = 0 # elemento que acumula la suma de todos los depositos capitalizados 
                termino_ret = 0 # elemento que acumula la suma de todos los retiros capitalizados   
                
                valor_inicial_bis = valor_inicial
                honorario = honorario_cierre 
                
                for i in range(len(movimientos)):                
                    # Obteniendo depositos, retiros, y plazos
                    monto_dep = movimientos.depositos[i]
                    monto_ret = movimientos.retiros[i]
                    plazo = movimientos.plazo[i]
               
                    # Acumulacion de los depositos y retiros capitalizados
                    termino_dep = termino_dep + monto_dep * (1 + tir) ** plazo  
                    termino_ret = termino_ret + monto_ret * (1 + tir) ** plazo 
                    
                # Capitalizacion del valor inicial y de los honorarios
                valor_inicial_bis = valor_inicial_bis * (1+tir) ** dias
                honorario = honorario * (1+tir) ** plazo_honorario
                
                # Calculo del error
                error = valor_cierre + termino_ret - (valor_inicial_bis + termino_dep) - honorario

                lista_n_error.append(error)
                listado_n_tir.append(tir)
                
            lista_n = pd.DataFrame()    
            lista_n['tir_diaria'] = listado_n_tir
            lista_n['error'] = lista_n_error
            lista_n['error_abs']=lista_n['error'].abs()
            lista_n.sort_values(by='error_abs',inplace=True)
            lista_n.drop(axis=1,columns='error_abs',inplace=True)

            # Ahora corregimos este listado para evitar problemas del tipo "controversia del
            # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
            # cobran honorarios. El asunto se resuelve en tres pasos:
            # PRIMERO. Slicing 10 primeros con errores mas pequeños
            lista_n = lista_n.iloc[:10,:]

            # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
            lista_n.sort_values(by='tir_diaria',inplace=True)
            lista_n = lista_n.iloc[:5,:]

            # TERCERO. Ordenamos de menor a mayor por error absoluto
            lista_n['error_abs'] = lista_n['error'].abs()
            lista_n.sort_values(by='error_abs',inplace=True)
            lista_n.drop(axis=1,columns='error_abs',inplace=True)

            
            
            # ----------------------------- QUINTA PARTE ----------------------------------
            # Se crea un diccionario que contiene el resultado
            # -----------------------------------------------------------------------------
            # Resultado
            tir_d_bruta = lista_b.iloc[0,0]
            tir_d_neta = lista_n.iloc[0,0]
           
            
            tir_a_bruta = np.exp(dias * np.log(1 + tir_d_bruta)) - 1
            tir_a_neta = np.exp(dias * np.log(1 + tir_d_neta)) - 1
            
            
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial = dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            rendimientos = {'Rend período':[tir_a_bruta, tir_a_neta],
                            'Fecha inicial':[f'{fecha_inicial}','-'],
                            'Fecha final':[f'{fecha_cierre}','-'],
                            'Valor inicial':[f'{valor_inicial}','-'],
                            'Valor final':[f'{valor_cierre}','-'],
                            'Honorarios':[f'{honorario_cierre}','-']}
            
            rendimiento = pd.DataFrame(rendimientos).T
            rendimiento = rendimiento.rename(columns = {0:'Rendimiento bruto',1:'Rendimiento neto'})
            
            
        else:
            rendimiento = datos_cliente

    except:
        rendimiento = 'Introduzca un usuario válido: entero entre 1 y 6'

    
    return rendimiento






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def split_ieb(fecha_cierre, alyc = '', nombre_cliente = '', numero_interno = 0, dni = 0,
              tipo_calculo = 'rendimiento', usuario = 1):
    """
    ---------------------------------------------------------------------------
                           ¿PARA QUE SIRVE ESTE CODIGO?
    Se obtiene la cantidad de papeles que se deben adicionar a la cartera debido 
    al split generado.
    
    ---------------------------------------------------------------------------
    Parameters
    ----------
    fecha_cierre : Tipo String.
        DESCRIPTION. Indica el momento donde deseamos conocer los papeles extras. 
        Por ejemplo: '2023-02-24'. 
                     
    alyc : Tipo String.
        DESCRIPTION. Es el nombre de la alyc donde el cliente tiene cuenta. Es
        Bull, Ieb, o Balanz. No importa si lo escribimos en mayusculas o con 
        acentos.The default is ''.
        
    nombre_cliente : Tipo String.
        DESCRIPTION. Es el nombre del cliente tal cual figura en su cuenta 
        comitente. No importa si se escribe con mayusculas y acentos. 
        Valor por defecto: ''.
        
    numero_interno : Tipo integer
        DESCRIPTION. Es el numero de la cuenta en ALYC que corresponde 
        al cliente. Valor por defecto: 0.
        
    dni : Tipo integer
        DESCRIPTION. Es el numero de la cuenta en ALYC que corresponde 
        al cliente. Valor por defecto: 0.
        
    tipo_calculo : Tipo string
        DESCRIPTION. El valor por defecto es 'rendimiento', pero tambien puede
        escribirse 'tenencia'. Ambos son dos maneras de obtener la composicion
        de la cartera a fecha de cierre. El primero tiene en cuenta la concerta
        cion, es decir, al comprar o vender un papel, no importa si la operacion
        se liquida, importa que se inicio. El segundo solo tiene en cuenta las 
        operaciones que se han liquidado.

    """
    # -----------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------

    if usuario == 1: 
        sub_directorio = 'Y'
        auxiliar = '--'
    elif usuario == 2:
        sub_directorio = 'YY'
        auxiliar = '--'
    elif usuario == 3:
        sub_directorio = 'YYY'
        auxiliar = ''
    elif usuario == 4:
        sub_directorio = 'Y_Y'
        auxiliar = ''
    elif usuario == 5:
        sub_directorio = 'YY_YY'
        auxiliar = ''
    elif usuario == 6:
        sub_directorio = 'YYY_YYY'
        auxiliar = ''

    directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'

    import pandas as pd
    from datetime import datetime as dt
    import sys
    sys.path.append(f'{directorio_funciones}')
    import dp_funciones_c as fc


    try:
   
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
        
        # Estos son parametros, pero no es necesario modificarlos, puede pensarse que
        # sus valores estan fijados por defecto.                  
        tenencia_inicial=f'Tenencia 31-12-22 {nombre_cliente}'
        transferencia_alyc='Transferencias entre alycs y div en especie'
        archivo_split = 'SPLITs'
        ubicacion_split = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})'
        directorio_orgien2 = ubicacion_split
        # -----------------------------------------------------------------------------
        movimiento_pesos='Movimientos de Pesos' 
        
        nombre_ticket='Tabla de conversion ticket vs IEB'
  
        
        # ----------------------------- PRIMERA PARTE ---------------------------------
        #                       IMPORTACION DE ARCHIVOS EXCEL
        # -----------------------------------------------------------------------------
        # Se importan los archivos con los movimientos de la cuenta. Sobre cada uno se
        # toma la mÃ¡scara que contiene movimientos en fechas previas o iguales a la fecha
        # de cierre. Y se ordenan cronolÃ³gicamente las operaciones.
        # -----------------------------------------------------------------------------
        # Se transforma la fecha de cierre al tipo datetime
        fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
        
        
        # Se importa el archivo split y se toma la mascara conforme a la fecha de cierre
        archivo_split = pd.read_excel(f'{ubicacion_split}\{archivo_split}.xlsx')
        archivo_split.set_index("Fecha", inplace=True)
        archivo_split = archivo_split.loc[archivo_split.index<=fecha_cierre].copy()
        archivo_split.sort_index(inplace=True)
        
        # Definimos el dataframe donde se guardaran los papeles extra
        papeles = pd.DataFrame()
        
        
        # Se controla el dataframe 'papeles' segun la mascara 'archivo_split' este o no vacia.
        if archivo_split.empty:
            papeles = papeles
            
        else:
            for i in range(len(archivo_split.index)):
                papeles.loc[i,'Especie'] = archivo_split.iloc[i,2]
                papeles.loc[i,'Cantidad'] = int(0)
                papeles.loc[i,'Fecha acreditacion'] = str()
                
            papeles.set_index('Especie',inplace=True)
          
        for i in range(len(archivo_split.index)):
            fecha_split = archivo_split.index[i]
            fecha_split = fecha_split.to_pydatetime()
              
            # Importamos el archivo en pesos. El 'Try - except' es para contemplar la situacion 
            # donde el mismo no existe. Adicionalmente, se identifican las cauciones dentro 
            # de la tabla de IEB que quedan fuera de la mascara por fecha de cierre. 
            # El opuesto del importe de estas cauciones se sumara al saldo liquido en pesos.
            try:       
                # Se lo importa y se lo limpia.    
                archivo_pesos = fc.concatenacion_movimientos_ieb(moneda = 1, alyc = alyc, dni = dni,
                                                                  nombre_cliente = nombre_cliente, 
                                                                  numero_interno = numero_interno,
                                                                  usuario = usuario)
                
                if tipo_calculo=='rendimiento':
                    # Para la liquidez en pesos se toma la siguiente mascara 
                    operaciones_locas=archivo_pesos.loc[(archivo_pesos.Operado<=fecha_split) &
                                                    (archivo_pesos.index>fecha_split)].copy()
                    
                    operaciones_locas_papeles=operaciones_locas.loc[operaciones_locas.Especie!='ESPECIES VARIAS'].copy()
                   
                    if len(operaciones_locas)>0:
                        importe_operaciones=operaciones_locas.Importe.sum()
                    else:
                        importe_operaciones=0
                        
                    if len(operaciones_locas_papeles)>0:
                        papeles_locos=operaciones_locas_papeles.groupby('Especie').Cantidad.sum()
                        papeles_locos=pd.DataFrame(papeles_locos)
                        
                    else:
                        papeles_locos=pd.DataFrame()
                    
                elif tipo_calculo=='tenencia':
                    importe_operaciones=0
                    papeles_locos=pd.DataFrame()
                    
                else:
                    print('Tipo de calculo mal especificado, elija rendimiento o tenencia.')
                    
                archivo_pesos=archivo_pesos.loc[archivo_pesos.index<=fecha_split].copy()
                
            except:
                archivo_pesos=pd.DataFrame()
        
        
            # Se importa el archivo por transferencias de papeles entre alyc y dividendos 
            # en especies 
            try:
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')
                archivo_transf_alyc.set_index('Liquida',inplace = True)
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.index<=fecha_split].copy()
        
            except:
                archivo_transf_alyc = pd.DataFrame()
            
        
        
        
            # ----------------------------- SEGUNDA PARTE ---------------------------------
            #                   CARTERA Y LIQUIDEZ EN PESOS Y EN DOLARES 
            # -----------------------------------------------------------------------------
            # Armamos los dataframes agrupando de acuerdo a los tickets, compras/ventas, y 
            # calculando las cantidades mantenidas hasta la fecha de cierre (inclusive). 
            # Esto se hace con los tres archivos, movimientos en pesos, en usd, y en ccl.  
            # -----------------------------------------------------------------------------
            # Movimientos en pesos, eliminamos las cauciones, quienes se tratan mas adelante.
            if archivo_pesos.empty:
                cartera=pd.DataFrame() 
                liquidez_pesos=0 # Falta la linea de codigo donde se eliminan cauciones
                
            else:
                cartera=archivo_pesos.groupby('Especie').Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                cartera=cartera.loc[cartera.index != 'ESPECIES VARIAS'].copy()
        
            
            # Fusionamos la 'cartera' con los 'papeles locos'.
            if cartera.empty:
                cartera = cartera
            
            else:
                cartera=pd.concat([cartera,papeles_locos],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
        
            
            # Se define la cartera por transferencia
            if archivo_transf_alyc.empty:
                cartera_trans_alyc = pd.DataFrame()
        
            else:
                cartera_trans_alyc = archivo_transf_alyc.groupby('Especie').Cantidad.sum()
                cartera_trans_alyc = pd.DataFrame(cartera_trans_alyc)
        
            
            # Se fusiona la 'cartera_trans_alyc' con 'cartera'.
            if cartera_trans_alyc.empty:
                cartera = cartera
                
            else:
                cartera=pd.concat([cartera,cartera_trans_alyc],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                cartera=cartera.loc[cartera.Cantidad>0].copy()
                
        
           
            
            # ----------------------------- TERCERA PARTE ---------------------------------
            #                  REEMPLAZANDO EL NOMBRE POR EL TICKET
            # -----------------------------------------------------------------------------
            ticket=pd.read_excel(f'{directorio_orgien2}/{nombre_ticket}.xlsx').set_index('IEB')
        
            cartera['ticket']=str(0)
        
            if cartera.empty:
                cartera = cartera
            
            else:
                try:
                    for j in cartera.index:
                        cartera.loc[j,'ticket']=ticket.loc[j,'TICKET']
                    
                    cartera.reset_index(inplace=True)
                    cartera.set_index('ticket',inplace=True)
                    cartera.drop('Especie',axis=1,inplace=True)
            
                except:
                    print('Hay que actualizar el excel donde están los Tickets con sus nombres')
              
            
            # Control de errores por si no existen splits 
            if papeles.empty:
                papeles = papeles
                
            else:
                try: # Control de errores por si el papel que hace el split no se tiene 
                     # en cartera
                    # Cantidad de papeles
                    ticket = archivo_split.iloc[i,2]
                    papeles_extra = cartera.loc[ticket,'Cantidad'] * archivo_split.iloc[i,1]
                    
                    papeles_extra = int(papeles_extra)
                    
                    papeles.loc[ticket,'Cantidad'] = papeles_extra
                    
                    # Fechas
                    papeles.loc[ticket,'Fecha acreditacion'] = archivo_split.iloc[i,3]
                    
                    # Si recalculan las cantidades por si no corresponden
                    fecha_acreditacion = archivo_split.iloc[i,3]
                    
                    if fecha_cierre < fecha_acreditacion:
                        papeles.loc[ticket,'Cantidad'] = 0
                        
                    papeles.drop('Fecha acreditacion',axis=1,inplace=True) 
                    
                except:
                    papeles = papeles

    except:
        papeles = 'Introduzca un usuario válido: 1, 2, 3, 4 o 5 (intente con cualquiera)'


    return papeles







# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def composicion_cartera_ieb(fecha_cierre, alyc = '', nombre_cliente ='', 
                            numero_interno = 0, dni = 0, tipo_calculo = 'rendimiento',
                            usuario = 1):
    """  
    Aclaraciones
    -----------
    Cualquier SPLIT debe introducirse "a mano" en el archivo excel correspondiente
    figurando como un ingreso de papeles que represente dicho split, sin alterar
    el saldo de la cartera.
    
    Las fechas de las operaciones que se tienen en cuenta son las correspondientes
    a la concertacion, no a la liquidacion.
    
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente tal cual aparece en la comitente que tiene en 
        la alyc. Puede escribirse con mayusculas y acentos, o sin ellos (es indis-
        tinto).
        Valor por defecto: ''.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Corresponde al numero asignado por la empresa.
        Valor por defecto: 0.
        
    alyc : tipo string. 
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la comitente. Puede ser Bull, Ieb, o
        Balanz.
        Valor por defecto: ''.
    
    dni : tipo string. 
    
        DESCRIPCION.
        Es el dni del cliente. Tiene que escribirse sin puntos ni comas.
        Valor por defecto: ''.
        
    tipo_calculo : tipo string
        
        DESCRIPCION
        Dos valores son posibles: 'rendimiento' y 'tenencia'. El rendimiento se
        utiliza para calcular el valor de la cartera con el fin de obtener los
        honorarios y el rendimiento en cierto periodo, mientras que tenencia se 
        utiliza para conocer el valor de la cartera en cierto momento.
        
        
    Resultado
    -------
    cartera : tipo DataFrame.
       
       DESCRIPCION.
       Se obtiene la composicion (precio y cantidad) de la cartera a fecha de 
       cierre. Adicionalmente, se identifican las operaciones mep realizadas. 
       Esta información es vital, para calcular el valor final o inicial de la 
       cartera.     

    """
    try:
        
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
            
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'
        
        # -----------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------
        import pandas as pd
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        

        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
        
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        # Estos son parametros, pero no es necesario modificarlos, puede pensarse que
        # sus valores estan fijados por defecto.                  
        
        directorio_origen = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})'
        directorio_orgien2 = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        # -----------------------------------------------------------------------------
        movimiento_pesos='Movimientos de Pesos' 
        movimiento_usd='Movimientos de Moneda Extranjera' 
        movimiento_divyren='Movimientos Dividendos y Rentas Cobradas' 
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        nombre_ticket='Tabla de conversion ticket vs IEB'
        
        transferencia_alyc='Transferencias entre alycs y div en especie'
        

        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            #                       IMPORTACION DE ARCHIVOS EXCEL
            # -----------------------------------------------------------------------------
            # Se importan los archivos con los movimientos de la cuenta. Sobre cada uno se
            # toma la máscara que contiene movimientos en fechas previas o iguales a la fecha
            # de cierre. Y se ordenan cronológicamente las operaciones.
            # -----------------------------------------------------------------------------
            # Se transforma la fecha de cierre al tipo datetime
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Importamos el archivo en pesos. El 'Try - except' es para contemplar la situacion 
            # donde el mismo no existe. Adicionalmente, se identifican las cauciones dentro 
            # de la tabla de IEB que quedan fuera de la mascara por fecha de cierre. 
            # El opuesto del importe de estas cauciones se sumara al saldo liquido en pesos.
            try:   
                
                # Se lo importa y se lo limpia.    
                archivo_pesos = fc.concatenacion_movimientos_ieb(moneda = 1, alyc = alyc, dni = dni,
                                                                 nombre_cliente = nombre_cliente, 
                                                                 numero_interno = numero_interno,
                                                                 usuario = usuario)
                
                if tipo_calculo=='rendimiento':
                    # Para la liquidez en pesos se toma la siguiente mascara 
                    operaciones_locas=archivo_pesos.loc[(archivo_pesos.Operado<=fecha_cierre) &
                                                    (archivo_pesos.index>fecha_cierre)].copy()
                    
                    operaciones_locas_papeles=operaciones_locas.loc[operaciones_locas.Especie!='ESPECIES VARIAS'].copy()
                    
                    if len(operaciones_locas)>0:
                        importe_operaciones=operaciones_locas.Importe.sum()
                    else:
                        importe_operaciones=0
                        
                    if len(operaciones_locas_papeles)>0:
                        papeles_locos=operaciones_locas_papeles.groupby('Especie').Cantidad.sum()
                        papeles_locos=pd.DataFrame(papeles_locos)
                        
                    else:
                        papeles_locos=pd.DataFrame()
                    
                elif tipo_calculo=='tenencia':
                    importe_operaciones=0
                    papeles_locos=pd.DataFrame()
                    
                else:
                    print('Tipo de calculo mal especificado, elija rendimiento o tenencia.')
                    
                archivo_pesos=archivo_pesos.loc[archivo_pesos.index<=fecha_cierre].copy()
            
            except:
                archivo_pesos=pd.DataFrame()
            
            
            # Importamos el archivo en dolares. El 'Try - except' es para contemplar la 
            # situacion donde el mismo no existe.
            try:
                # Se lo importa y se lo limpia.
                archivo_usd = fc.concatenacion_movimientos_ieb(moneda = 2, alyc = alyc, dni = dni,
                                                               nombre_cliente = nombre_cliente, 
                                                               numero_interno = numero_interno,
                                                               usuario = usuario)
                   
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_usd=archivo_usd.loc[archivo_usd.index<=fecha_cierre]
                
                
                # Identificamos la transformacion de DOLARUSA A USD
                dolarusa_a_usd = archivo_usd.loc[archivo_usd[archivo_usd.columns[2]] != 'NCCD'].copy()
                
                liquidez_usd1 = dolarusa_a_usd.Importe.sum()
            
            except:
                archivo_usd=pd.DataFrame()
            
                liquidez_usd1=0
                
                dolarusa_a_usd = 0
            
            
            # Importamos el archivo en dolares cable. El 'Try - except' es para contemplar
            # la situacion donde este archivo no existe. 
            try:
                archivo_usd_extra = fc.concatenacion_movimientos_ieb(moneda = 3, alyc = alyc, dni = dni,
                                                                     nombre_cliente = nombre_cliente, 
                                                                     numero_interno = numero_interno,
                                                                     usuario = usuario)
                
                # Se toma la mascara de acuerdo a la fecha de cierre y al 'DOLARUSA'
                archivo_usd_extra = archivo_usd_extra.loc[archivo_usd_extra.index<=fecha_cierre].copy()
                archivo_usd_extra = archivo_usd_extra.loc[archivo_usd_extra[archivo_usd_extra.columns[3]
                                                                                ] == 'DOLARUSA'].copy()
                
                liquidez_usd2 = archivo_usd_extra['Divi/renta'].sum() 
            
            except:
                archivo_usd_extra = pd.DataFrame()
                
                liquidez_usd2=0
            
            
            # Se importa el archivo por transferencias de papeles entre alyc y dividendos 
            # en especies 
            try:
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')
                archivo_transf_alyc.set_index('Liquida',inplace = True)
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.index<=fecha_cierre].copy()
            
            except:
                archivo_transf_alyc = pd.DataFrame()
                
                
            
            
            # ----------------------------- SEGUNDA PARTE ---------------------------------
            #                   CARTERA Y LIQUIDEZ EN PESOS Y EN DOLARES 
            # -----------------------------------------------------------------------------
            # Armamos los dataframes agrupando de acuerdo a los tickets, compras/ventas, y 
            # calculando las cantidades mantenidas hasta la fecha de cierre (inclusive). 
            # Esto se hace con los tres archivos, movimientos en pesos, en usd, y en ccl.  
            # -----------------------------------------------------------------------------
            # Movimientos en pesos, eliminamos las cauciones, quienes se tratan mas adelante.
            if archivo_pesos.empty:
                cartera=pd.DataFrame() 
                liquidez_pesos=0 # Falta la linea de codigo donde se eliminan cauciones
                
            else:
                cartera=archivo_pesos.groupby('Especie').Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                # cartera=cartera.loc[cartera.Cantidad>0].copy()
            
                liquidez_pesos=archivo_pesos.loc[:,'Saldo'].iloc[0]+importe_operaciones
            
            
            # Movimientos en dolares. Solo importa el saldo, pues las compras y ventas de 
            # papeles tambien se registran en el archivo en pesos. 
            liquidez_usd = liquidez_usd1 + liquidez_usd2
            
            
            # Se calcula la tenencia por split.
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            papeles_split = fc.split_ieb(fecha_cierre = fecha_cierre, alyc = alyc, dni = dni,
                                          nombre_cliente = nombre_cliente, 
                                          numero_interno = numero_interno, 
                                          tipo_calculo = tipo_calculo,
                                          usuario = usuario)
            
            
            # Se reconvierte la 'fecha de cierre' a formato datetime.
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Fusionamos la 'cartera' con los 'papeles locos'.
            if cartera.empty:
                cartera = cartera
            
            else:
                cartera=pd.concat([cartera,papeles_locos],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
            
            
            # Se define la cartera por transferencia
            if archivo_transf_alyc.empty:
                cartera_trans_alyc = pd.DataFrame()
            
            else:
                cartera_trans_alyc = archivo_transf_alyc.groupby('Especie').Cantidad.sum()
                cartera_trans_alyc = pd.DataFrame(cartera_trans_alyc)
            
            
            # Se fusiona la 'cartera_trans_alyc' con 'cartera'.
            if cartera_trans_alyc.empty:
                cartera = cartera
                # cartera=cartera.loc[cartera.Cantidad>0].copy()
                
            else:
                cartera=pd.concat([cartera,cartera_trans_alyc],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                # cartera=cartera.loc[cartera.Cantidad>0].copy()
            
            if len(cartera.loc[cartera.index=='ESPECIES VARIAS']):
                cartera.drop(index='ESPECIES VARIAS',inplace=True)
                
                
            
            # ----------------------------- TERCERA PARTE ---------------------------------
            #                  REEMPLAZANDO EL NOMBRE POR EL TICKET
            # -----------------------------------------------------------------------------
            ticket=pd.read_excel(f'{directorio_orgien2}/{nombre_ticket}.xlsx').set_index('IEB')
            
            if cartera.empty == False:
                cartera['ticket']=str(0)
            
            if cartera.empty:
                cartera = cartera
            
            else:
                try:
                    for i in cartera.index:
                        cartera.loc[i,'ticket']=ticket.loc[i,'TICKET']
                    
                    cartera.reset_index(inplace=True)
                    cartera.set_index('ticket',inplace=True)
                    cartera.drop('Especie',axis=1,inplace=True)
            
                except:
                    print('Hay que actualizar el excel donde están los Tickets con sus nombres')
            
            
            # Ahora que se tienen los tickets se fusiona la 'cartera' con 'papeles_split'.
            if cartera.empty:
                cartera = cartera
                
            else:
                cartera=pd.concat([cartera,papeles_split],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                cartera=cartera.loc[cartera.Cantidad>0].copy()
            
            
            
            # ------------------------------ CUARTA PARTE ---------------------------------
            #                  SE UNIFICA LA CARTERA CON LA LIQUIDEZ
            # -----------------------------------------------------------------------------
            # Incorporamos los saldos liquidos en pesos y en dolares al vector "cartera".
            if (cartera.empty) & (liquidez_pesos == 0):
                cartera = cartera
                
            else:
                cartera.loc['liquidez_usd']=float(0)
                cartera.loc['liquidez_usd','Cantidad']=liquidez_usd
                
                cartera.loc['liquidez_pesos']=float(0)
                cartera.loc['liquidez_pesos','Cantidad']=liquidez_pesos
            
            
            
            
            # --------------------------- QUINTA PARTE ------------------------------------
            #            SE COLOCAN LOS PRECIOS A CADA UNO DE LOS PAPELES
            # -----------------------------------------------------------------------------
            # Creamos la columna donde se colocaran los precios, indicada por la fecha de cierre
            if cartera.empty:
                cartera = cartera
            
            else:
                cartera[fecha_cierre]=1
                
                # Creamos una cartera donde solo esten los tickets de las acciones
                cartera2=cartera.iloc[:-2,:].copy()
                
                # Importamos el archivo en pesos
                archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                              ,sheet_name='Hoja 2').set_index('fecha')
                
                
                # Resolvemos la fecha de cierre por si no existen precios en dicho momento
                fecha_cierre2=fecha_cierre
                for i in range(60):
                    
                    if len(archivo_precios.loc[archivo_precios.index==(fecha_cierre-timedelta(days=i))])==0:
                        fecha_cierre2=fecha_cierre-timedelta(days=i)
                        
                    else:
                        fecha_cierre2=fecha_cierre-timedelta(days=i)
                    
                    if len(archivo_precios.loc[archivo_precios.index==fecha_cierre2])==1:
                        break
                
                
                # Colocamos los precios de las acciones y dolar mep, si el papel no esta en la
                # serie excel de precios, entonces como precio colocamos el valor 0 (cero)
                cartera[fecha_cierre]=float(0)
                for i in cartera2.index:
                    try:
                        precio=archivo_precios.loc[fecha_cierre2,i]
                        cartera.loc[i,fecha_cierre]=precio
                    
                    except:
                        cartera.loc[i,fecha_cierre]=float(0)   
                
                cartera.loc['liquidez_usd',fecha_cierre]=archivo_precios.loc[fecha_cierre2,'dolar_mep']
                cartera.loc['liquidez_pesos',fecha_cierre]=float(1)
               
            
        else:
            cartera = datos_cliente

    except:
        cartera = 'Introduzca un usuario válido: entero entre 1 y 6'

   
    return cartera






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def honorario_ieb(fecha_cierre, dni = 0, alyc = '', nombre_cliente = '', 
                  numero_interno = 0, usuario = 1):
   
    """ 
    ---------------------------------------------------------------------------
                               ¿PARA QUE SIRVE?
    Es util para obtener los honorarios de la cartera. 
    ---------------------------------------------------------------------------
                               ¿COMO FUNCIONA? 
    Utiliza la función 'composicion_carteraF', con la cual se obtiene la carte-
    ra del cliente con cuenta en bullmarket en la fecha de cierre indicada.  
    A parte de esta se calcula su valor y se aplican la alicuota que corresponde.
    ---------------------------------------------------------------------------
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Valor por defecto: ''.
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es el nombre de la alyc donde el cliente tiene su comitente. Puede ser
        Bull, Ieb, o Balanz.
        Valor por defecto: ''.
    
    dni : tipo integer.
    
        DESCRIPCION.
        Es el numero de dni del cliente, sin puntos ni comas. 
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero asignado por la empresa.
        Valor por defecto: 0.    
                 
    Resultado
    -------
    honorario : tipo DataFrame.
       
       DESCRIPCION.
       Se obtiene el honorario que corresponde al momento indicado en la fecha
       de cierre.

    """


    try:
        # usuario = 4 # 
        
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'
        
        # ----------------------------------------------------------------------------
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        import pandas as pd
        from datetime import datetime as dt   
    
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni, 
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
            
        
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})'
        
        movimiento_pesos='Movimientos de Pesos' 
        
        directorio_clasificador=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        nombre_clasificador='- Categorias de papeles para calculo de honorarios'
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # -----------------------------------------------------------------------------
            #         SE OBTIENE LA CARTERA, SE OBTIENE SU VALOR, Y SE CLASIFICA
            # -----------------------------------------------------------------------------
            # Se importa la cartera con tickets, cantidades, precios, mep, y saldo liquido
            # que corresponde a la fecha de cierre.
            try:
                cartera=fc.composicion_cartera_ieb(fecha_cierre = fecha_cierre, alyc = alyc,
                                                   nombre_cliente = nombre_cliente, dni = dni,
                                                   numero_interno = numero_interno,
                                                   usuario = usuario)
                
                cartera['monto']=cartera.Cantidad*cartera.iloc[:,1]  
                
                # Ajustamos la variable 'cartera' para calcular el activo de la cuenta
                # en lugar del patrimonio neto. En otras palabras, solo modificamos dicha
                # variable si la liquidez es negativa, convirtiendola en cero (el monto por 
                # el cual el cliente esta apalancado se encuentra invertido en los diferentes 
                # valores negociables)
                if cartera.loc['liquidez_pesos','monto'] < 0:
                    cartera.loc['liquidez_pesos','monto'] = 0
                
                
                # Se clasifican los papeles de la cartera
                clasificador=pd.read_excel(
                    f'{directorio_clasificador}/{nombre_clasificador}.xlsx').set_index('papel')
            
                cartera['categoria']=str(0)
                
                for i in cartera.index:
                    cartera.loc[i,'categoria']=clasificador.loc[i,'clasificacion']
                
                # Agrupamos el monto de la cartera de acuerdo a esta categorizacion y calculamos
                # su participacion
                cartera2=cartera.groupby('categoria').sum()
                cartera2['porcentaje']=cartera2.monto/cartera2.monto.sum()
                
            except:
                cartera=pd.DataFrame()
                
                cartera2=pd.DataFrame()
            
            
            
            
            # -----------------------------------------------------------------------------
            #              SE CALCULA EL VALOR BRUTO Y NETO DE LA CARTERA
            # -----------------------------------------------------------------------------
            # Identificamos los depositos hechos durante el ultimo mes. Para esto debemos 
            # definir el periodo de tiempo entre la fecha de cierre y el ultimo cobro de honorarios.
            
            # El punto de partida es la fecha de cierre, momento donde queremos cobrar los
            # honorarios. Utilizandola junto con el 'dia de corte' del dataframe 'datos_cliente'
            # definimos la fecha del ultimo cobro de honorarios.
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Objetivo: definir puntas del periodo: 1) fecha de cierre es punta final, 2) 
            # fecha ultimo cobro es punta inicial. Esta ultima debe definirse e implica iden-
            # tificar si dada la fecha de cierre hay o no cambio de mes. Si el dia de la 
            # fecha de cierre es menor o igual al dia de fecha de cobro entonces hay cambio 
            # de mes, si es mayor entonces no lo hay. 
            # Con el siguiente condicional identificamos si cambiamos o no de mes
            if fecha_cierre.day <= datos_cliente.iloc[3,0]:
                # Cambiamos el mes del siguiente modo
                try:    
                    # Controlando los dias por febrero 
                    if (datos_cliente.iloc[3,0] > 28) & (fecha_cierre.month == 3):
                        fecha_ultimo_cobro = fecha_cierre.replace(month = 2, day = 28)
                    
                    # Controlando los dias por meses con 31 dias
                    elif datos_cliente.iloc[3,0] == 31:
                        fecha_ultimo_cobro = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                                  day = 30)
                        
                    # Sin necesidad de controles sobre los dias
                    else:
                        fecha_ultimo_cobro = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                                  day = datos_cliente.iloc[3,0])
                    
                except ValueError:
                    # Cambio de año por tener fecha de cierre en enero y de ultimo cobro en diciembre
                    fecha_ultimo_cobro = fecha_cierre.replace(year = fecha_cierre.year-1, month = 12,
                                                              day = datos_cliente.iloc[3,0])
                    
            else:
                # Al no cambiar de mes solo hay que modificar el dia
                fecha_ultimo_cobro = fecha_cierre.replace(day = datos_cliente.iloc[3,0])
            
            
            # Ahora se procede a identificar los depositos realizados entre el ultimo cobro
            # de honorarios y la fecha de cierre
            # Depositos en pesos
            dias_transcurridos = (fecha_cierre - fecha_ultimo_cobro).days
            
            if cartera.empty:
                archivo_pesos=pd.DataFrame()
                
                depositos=pd.DataFrame()
            
                valor_depositos=0
                
            else:
                try:   
                    
                    # Se lo importa y se lo limpia.    
                    archivo_pesos = fc.concatenacion_movimientos_ieb(moneda = 1, alyc = alyc, dni = dni,
                                                                      nombre_cliente = nombre_cliente, 
                                                                      numero_interno = numero_interno,
                                                                      usuario = usuario)
                  
                    archivo_pesos=archivo_pesos.loc[(archivo_pesos.index<=fecha_cierre) &
                                                    (archivo_pesos.index>=fecha_ultimo_cobro)].copy()
                    
                    depositos=archivo_pesos.loc[(archivo_pesos.Referencia=='TRANSFERENCIA RECIBIDA WEB') | 
                                                (archivo_pesos.Referencia=='TRANSF.RECIBIDA')].copy()
                    
                    if depositos.empty:
                        valor_depositos=0
                    else:
                        depositos=depositos[['Operado','Importe']]
                        depositos.reset_index(inplace=True)
                        depositos.set_index('Operado',inplace=True)
                        depositos.drop('Liquida',axis=1,inplace=True)
                        
                        depositos['dias_corridos']=int(0)
                        for i in depositos.index:
                            depositos.loc[i,'dias_corridos']=(fecha_cierre-i).days
                            
                        depositos['Importe_ajus']= -1 * (depositos.dias_corridos - dias_transcurridos
                                                      ) * depositos.Importe / dias_transcurridos
                        
                        valor_depositos=depositos.Importe_ajus.sum()
                       
                except:
                    archivo_pesos=pd.DataFrame()
                    
                    depositos=pd.DataFrame()
                
                    valor_depositos=0
            
            
            # Obtenemos el valor neto y bruto de cartera
            if cartera2.empty:
                valor_bruto=float(0)
                
            else:    
                valor_bruto=cartera2.monto.sum()
                
                for i in cartera2.index:
                    cartera2.loc[i,'monto']=cartera2.loc[i,'monto'] - cartera2.loc[i,'porcentaje']*valor_depositos
                
            
            
            
            # -----------------------------------------------------------------------------
            #                       SE CALCULA EL HONORARIO
            # -----------------------------------------------------------------------------
            # Se calculan los honorarios
            honorario=0
            
            alicuota1=0.005
            
            alicuota2=0.0025
            
            sumafija=1_500
            
            if cartera.empty:
                mep = 1
            
            else:
                mep=cartera.iloc[-2,1]
            
            if valor_bruto/mep>=10_000:
                honorario = (valor_bruto - valor_depositos) * alicuota2 * 1.21
             
            elif (valor_bruto/mep>=1_000) & (valor_bruto/mep<10_000):
                if len(cartera2.loc[cartera2.index=='liquidez'])>0:
                    if cartera2.loc['liquidez','porcentaje']>=0.25:
                        honorario_liq = cartera2.loc['liquidez','monto']*alicuota2
                        valor_liquidez = round(cartera2.loc['liquidez','monto'],2)
                        
                    else:
                        honorario_liq = cartera2.loc['liquidez','monto']*alicuota1
                        valor_liquidez = round(cartera2.loc['liquidez','monto'],2)
                        
                else: 
                    honorario_liq = 0
                    valor_liquidez = 0
                
                if len(cartera2.loc[cartera2.index=='renta fija'])>0:
                    if cartera2.loc['renta fija','porcentaje']>=0.1:
                        honorario_rf = cartera2.loc['renta fija','monto']*alicuota2
                        valor_rentaf = round(cartera2.loc['renta fija','monto'],2)
                        
                    else:
                        honorario_rf = cartera2.loc['renta fija','monto']*alicuota1
                        valor_rentaf = round(cartera2.loc['renta fija','monto'],2)
                
                else:
                    honorario_rf = 0
                    valor_rentaf = 0
                
                if len(cartera2.loc[cartera2.index=='renta variable'])>0:
                    honorario_rv = cartera2.loc['renta variable','monto']*alicuota1
                    valor_rentav = round(cartera2.loc['renta variable','monto'],2)
                    
                else:
                    honorario_rv = 0
                    valor_rentav = 0
            
                honorario = (honorario_rv + honorario_rf + honorario_liq + sumafija) * 1.21
                
            else:
                honorario=0
                
                
            # Para calcular los honorarios proporcionales debemos definir una fecha de cierre
            # ideal que represente el momento donde se cumple exactamente un mes desde el 
            # ultimo cobro. 
            # Controlando el mes por cambio de año  
            if fecha_ultimo_cobro.month == 12:
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = 1, 
                                                                year = fecha_ultimo_cobro.year + 1)
            
            # Controlando los dias por meses con 31 dias
            elif (fecha_ultimo_cobro.day == 31) & (fecha_ultimo_cobro.month != 1):
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = fecha_ultimo_cobro.month + 1, 
                                                                day = 30)
                
            # Controlando por mes de febrero
            elif (fecha_ultimo_cobro.month == 1) & (fecha_ultimo_cobro.day > 28):
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = 2, day = 28)
                
            else:
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = fecha_ultimo_cobro.month + 1)
                    
            periodo_ideal = (fecha_cierre_ideal - fecha_ultimo_cobro).days
            periodo_transcurrido = (fecha_cierre - fecha_ultimo_cobro).days
            
            
            # Si corresponde, aplicamos proporcionalidad sobre los honorarios
            if fecha_cierre.day != fecha_ultimo_cobro.day:
                honorario = honorario * (periodo_transcurrido)/ periodo_ideal   
                
            
            # Se crea un DataFrame que contiene el honorario y el valor de cartera
            if valor_bruto/mep>=10_000:
                portafolio2={'Cartera cuyo valor supera los 10 mil usd':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Valor imponible':[f'$ {round(valor_bruto - valor_depositos,2)}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
            elif (valor_bruto/mep>=1_000) & (valor_bruto/mep<10_000):
                portafolio2={'Cartera cuyo valor se encuentra entre los mil y 10 mil usd':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Valor imponible liquidez':[f'$ {valor_liquidez}'],
                            'Valor imponible renta fija':[f'$ {valor_rentaf}'],
                            'Valor imponible renta variable':[f'$ {valor_rentav}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}'],
                            'Honorario liquidez':[f'$ {round(honorario_liq,2)}'],
                            'Honorarios renta fija':[f'$ {round(honorario_rf,2)}'],
                            'Honorarios renta variable':[f'$ {round(honorario_rv,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
            else:
                portafolio2={'Cartera cuyo valor es inferior a los mil usd':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
        
        
        else:
            portafolio2 = datos_cliente
                
    except:
        portafolio2 = 'Introduzca un usuario válido: entero entre 1 y 6'
    
    return portafolio2






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def rendimientos_bruto_neto_ieb(fecha_cierre, alyc = '', dni = 0, nombre_cliente = '',
                                numero_interno = 0, puntos_basicos = 0.1, dias = 30,
                                usuario = 1):
    """
    ---------------------------------------------------------------------------
                              ¿PARA QUE SIRVE ESTE CODIGO?
    Para hallar la TIR bruta y neta de honorarios de la cartera. Asimismo, se 
    indica la fecha inicial y final del periodo analizado, pues de este modo 
    el resultado de la funcion puede utilizarse junto a otras funciones. 
    ---------------------------------------------------------------------------
                               ¿COMO FUNCIONA EL CODIGO? 
    Se calcula el valor inicial y final de la cartera, junto con los honorarios
    (si corresponden). Tambien, se obtienen los retiros y depositos en pesos y 
    dolares (aqui se incluyen las operaciones por dolar mep).
    A partir de esta informacion, se obtiene el rendimiento como la TIR de un
    polinomio donde se minimiza el error de calculo. Este se se define como la 
    diferencia entre el valor final e inicial de la cartera, ajustando la dife-
    rencia por los retiros y depositos. Algebraicamente:
                      error = SF - (VF[depositos]-VF[retiros]) 
    ---------------------------------------------------------------------------
                               ACLARACIONES ADICIONALES
    Este codigo es utilizado para situaciones donde el cliente realiza, durante
    el mes, menos de 50 depositos y menos de 50 retiros. De exceder estas canti-
    dades, el codigo se 'rompera' (dejara de funcionar).
    ---------------------------------------------------------------------------
    Paramentros
    ----------
    fecha_cierre : tipo string.
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    nombre_cliente : tipo string.
        DESCRIPCION.
        Es el nombre del cliente, el registrado en su comitente. Puede escribirse
        con mayusculas y acentos, es indistinto.  .
        Valor por defecto: ''.
        
    dni : tipo integer.
        DESCRIPCION.
        Es el numero de dni del cliente, sin puntos ni comas.
        Valor por defecto: 0.
        
    alyc : tipo string.
        DESCRIPCION.
        Es el nombre de la alyc donde el cliente tiene su comitente. Puede ser 
        Bull, Ieb, o Balanz.   .
        Valor por defecto: ''.
        
    numero_interno : tipo integer.
        DESCRIPCION.
        Es el numero asignado por la empresa. 
        Valor por defecto: 0.
        
    puntos_basicos : tipo float
        DESCRIPCION. 
        Valor por defecto: 0.5.
        Define el incremental del iterador utilizado para hallar la TIR. En otras
        palabras, la TIR crece en 0.5 puntos basicos en el siguiente calculo.
        
    dias : tipo integer
        DESCRIPCION. 
        Valor por defecto: 30.
        Define la cantidad de dias del plazo de analisis. En otras palabras, 
        son la cantidad de dias que se restan a la fecha de cierre.              
           

    Resultado
    -------
    rendimiento : tipo DataFrame
        DESCRIPCION.
        Es una tabla con el rendimiento bruto y neto mensual de la cartera ana-
        lizada, junto con la fecha inicial y final del periodo correspondiente.

    """ 
    try:    
       
        
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        import numpy as np
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
            dia_corte = datos_cliente.loc['Dia de corte','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
        
        
        # -----------------------------------------------------------------------------
        # Sub Parametros
        # Estos son parametros, pero no es necesario modificarlos.                  
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})'
        # -----------------------------------------------------------------------------
        movimiento_pesos='Movimientos de Pesos' 
        movimiento_usd='Movimientos de Moneda Extranjera' 
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        transferencia_alyc='Transferencias entre alycs y div en especie'
        
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            # Se calcula el 'vector_portafolio', que contiene el valor de la cartera en
            # cada momento, los honorarios, y las fechas de dichos momentos.
            # -----------------------------------------------------------------------------
            # Obtenemos los momentos clave
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial=fecha_cierre-timedelta(days=dias)
            
            
            # Transformamos las fechas a formato string
            fecha_cierre=dt.strftime(fecha_cierre, '%Y-%m-%d')
            fecha_inicial=dt.strftime(fecha_inicial, '%Y-%m-%d')
            
            
            # Obtenemos la composicion de las carteras a inicio y final del periodo 
            # de analisis. De esto nos quedamos con la liquidez en pesos solo si es
            # negativa. Lo hacemos asi para ajustar el valor de cartera que obtenemos
            # con la funcion honorarios.
            saldo_liq_pesos_inicio = fc.composicion_cartera_ieb(fecha_cierre = fecha_inicial,
                                                                  alyc = alyc, dni = dni,
                                                                  nombre_cliente = nombre_cliente,
                                                                  numero_interno = numero_interno,
                                                                  usuario = usuario)
            if saldo_liq_pesos_inicio.empty == False:
                saldo_liq_pesos_inicio = saldo_liq_pesos_inicio.loc['liquidez_pesos','Cantidad']
                
            else:
                saldo_liq_pesos_inicio = 0
            
            saldo_liq_pesos_final = fc.composicion_cartera_ieb(fecha_cierre = fecha_cierre,
                                                                  alyc = alyc, dni = dni,
                                                                  nombre_cliente = nombre_cliente,
                                                                  numero_interno = numero_interno,
                                                                  usuario = usuario)
            if saldo_liq_pesos_final.empty == False:
                saldo_liq_pesos_final = saldo_liq_pesos_final.loc['liquidez_pesos','Cantidad']
                
            else:
                saldo_liq_pesos_final = 0
            
            
            # Calculamos los honorarios de cierre junto con valores iniciales y finales
            portafolio_cierre=fc.honorario_ieb(fecha_cierre = fecha_cierre, dni = dni, 
                                                alyc = alyc, nombre_cliente = nombre_cliente,
                                                numero_interno = numero_interno,
                                                usuario = usuario)
            
            portafolio_inicial=fc.honorario_ieb(fecha_cierre = fecha_inicial, dni = dni, 
                                                alyc = alyc, nombre_cliente = nombre_cliente,
                                                numero_interno = numero_interno,
                                                usuario = usuario)
            
            valor_cierre=float(portafolio_cierre.iloc[3,0][2:])
            valor_inicial=float(portafolio_inicial.iloc[3,0][2:])
            
            if saldo_liq_pesos_inicio < 0:
                valor_inicial = valor_inicial + saldo_liq_pesos_inicio
                
            if saldo_liq_pesos_final < 0:
                valor_cierre = valor_cierre + saldo_liq_pesos_final
            
            
            # Se obtienen los plazos
            plazo_cierre=(portafolio_cierre.iloc[2,0]-portafolio_cierre.iloc[2,0]).days
            
            plazo_inicial=(portafolio_cierre.iloc[2,0]-portafolio_inicial.iloc[2,0]).days
            
            
            # Calculamos los honorarios. Recuerde que los mismos se calculan en diferentes
            # fechas dependiendo el cliente. En otras palabras, no se calculan a finales de 
            # cada mes (no necesariamente). Cuando al cliente no se le cobran honorarios
            # porque ya no es cliente (pero tal vez queremos estudiar los rendimientos que
            # tuvo cuando sí lo fue, entonces "dia_corte" va a ser igual a cero, en estos
            # casos tomamos como fecha de corte la fecha de cierre)  
            if dia_corte == 0:
                fecha_corte = fecha_cierre
            
            else:
                fecha_corte = f'{fecha_cierre[:7]}-{dia_corte}'
                
                # Controlamos para fechas de febrero que no existen:
                # Si el try funciona entonces usamos la fecha de corte señalada arriba.
                # Si el try no funciona se utiliza el resultado del except.
                try:
                    fecha_corte_prueba = dt.strptime(fecha_corte,'%Y-%m-%d')
                    
                except:
                    fecha_corte = f'{fecha_cierre[:7]}-28'
            
            portafolio_fecha_corte = fc.honorario_ieb(fecha_cierre=fecha_corte, alyc=alyc, 
                                                      nombre_cliente=nombre_cliente,
                                                      numero_interno=numero_interno,
                                                      dni=dni,usuario = usuario)
            if len(portafolio_fecha_corte) == 11:
                honorario_cierre = float(portafolio_fecha_corte.iloc[7,0][2:])
                
            elif len(portafolio_fecha_corte) == 6:
                honorario_cierre = float(portafolio_fecha_corte.iloc[5,0][2:])
            
            elif len(portafolio_fecha_corte) == 5:
                honorario_cierre = float(portafolio_fecha_corte.iloc[4,0][2:])
            
            
            
            
            # ----------------------------- TERCERA PARTE ---------------------------------
            #          SE IDENTIFICAN LOS DEPOSITOS Y RETIROS EN PESOS Y EN USD
            # -----------------------------------------------------------------------------
            # Se transforma la fecha de cierre al tipo datetime
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial=dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            
            # Importamos los movimientos en pesos 
            try:   
                # Se lo importa y se lo limpia.    
                archivo_pesos = fc.concatenacion_movimientos_ieb(moneda = 1, alyc = alyc, dni = dni,
                                                                 nombre_cliente = nombre_cliente, 
                                                                 numero_interno = numero_interno,
                                                                 usuario = usuario)
            
                archivo_pesos=archivo_pesos.loc[(archivo_pesos.index<=fecha_cierre) & (
                                                    archivo_pesos.index>=fecha_inicial)].copy()
            
                pesos_depositos=archivo_pesos.loc[(archivo_pesos[archivo_pesos.columns[1]]=='COBW') |
                                                  (archivo_pesos[archivo_pesos.columns[1]]=='COBR')].copy()
                
                pesos_retiros=archivo_pesos.loc[archivo_pesos[archivo_pesos.columns[1]]=='PAGW'].copy()
            
            except:
                archivo_pesos=pd.DataFrame()
                
                pesos_depositos=pd.DataFrame()
            
                pesos_retiros=pd.DataFrame()
                
            
            # Importamos las transferencias y nos quedamos con las correspondientes mascaras
            try: 
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')    
                archivo_transf_alyc.set_index('Liquida', inplace =True)
                
                archivo_transf_alyc = archivo_transf_alyc.loc[
                                    (archivo_transf_alyc[archivo_transf_alyc.columns[1]] == 'TRANSFERENCIA') &
                                    (archivo_transf_alyc.index <= portafolio_cierre.iloc[2,0]) &
                                    (archivo_transf_alyc.index >= portafolio_inicial.iloc[2,0])].copy()
                
                # Identificamos las transferencias desde y hacia la alyc.
                trans_desde_alycs = archivo_transf_alyc.loc[archivo_transf_alyc.Importe > 0].copy()
                
                trans_hacia_alycs = archivo_transf_alyc.loc[archivo_transf_alyc.Importe < 0].copy() 
                
            except:
                trans_desde_alycs = pd.DataFrame()
                trans_hacia_alycs = pd.DataFrame()
               
                
            # Importamos los movimientos en pesos dólares
            try:   
                # Se lo importa y se lo limpia.    
                archivo_usd = fc.concatenacion_movimientos_ieb(moneda = 2, alyc = alyc, dni = dni,
                                                               nombre_cliente = nombre_cliente, 
                                                               numero_interno = numero_interno,
                                                               usuario = usuario)
            
                archivo_usd=archivo_usd.loc[(archivo_usd.index<=fecha_cierre)].copy()
                archivo_usd=archivo_usd.loc[(archivo_usd.index>=fecha_inicial)].copy()
            
                usd_depositos=archivo_usd.loc[(archivo_usd[archivo_usd.columns[1]]=='COUW') |
                                              (archivo_usd[archivo_usd.columns[1]]=='COME')].copy()
                
                usd_retiros=archivo_usd.loc[(archivo_usd[archivo_usd.columns[2]]=='PAUW') |
                                            (archivo_usd[archivo_usd.columns[2]]=='PAME')].copy()
            
            except:
                archivo_usd=pd.DataFrame()
                
                usd_depositos=pd.DataFrame()
            
                usd_retiros=pd.DataFrame()
            
            
            
            
            # ------------------------------ CUARTA PARTE ---------------------------------
            #               SE ARMAN LOS VECTORES DE DEPOSITOS Y RETIROS
            # -----------------------------------------------------------------------------
            # Vectores de depositos y retiros en pesos
            depositos_pesos=pd.DataFrame()
            depositos_pesos['monto']=float(0)
            depositos_pesos['plazo']=int(0)
            depositos_pesos['depositos_pesos']=int(0)
            
            for i in range(50):
                depositos_pesos.loc[i]=float(0)  
                depositos_pesos.loc[i,'depositos_pesos']=i
            
            depositos_pesos.set_index('depositos_pesos',inplace=True)
            
            for i in range(len(pesos_depositos)):
                depositos_pesos.iloc[i,0]=pesos_depositos.loc[:,'Importe'].iloc[i]
                depositos_pesos.iloc[i,1]=(fecha_cierre-pesos_depositos.index[i]).days
                
                if (depositos_pesos.iloc[i,1] == dias):
                    depositos_pesos.iloc[i,0] = 0
            
            retiros_pesos=pd.DataFrame()
            retiros_pesos['monto']=float(0)
            retiros_pesos['plazo']=int(0)
            retiros_pesos['retiros_pesos']=int(0)
            
            for i in range(50):
                retiros_pesos.loc[i]=float(0)  
                retiros_pesos.loc[i,'retiros_pesos']=i    
            
            retiros_pesos.set_index('retiros_pesos',inplace=True)
            
            for i in range(len(pesos_retiros)):
                retiros_pesos.iloc[i,0]=pesos_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_pesos.iloc[i,1]=(fecha_cierre-pesos_retiros.index[i]).days
                
                if (retiros_pesos.iloc[i,1] == dias):
                    retiros_pesos.iloc[i,0] = 0
              
            
            # Vector de transferencia desde otras ALYCS
            alycs_trans_desde=pd.DataFrame()
            alycs_trans_desde['monto']=float(0)
            alycs_trans_desde['plazo']=int(0)
            alycs_trans_desde['alycs_trans_desde']=int(0)
            
            for i in range(50):
                alycs_trans_desde.loc[i]=float(0) 
                alycs_trans_desde.loc[i,'alycs_trans_desde']=i
            
            alycs_trans_desde.set_index('alycs_trans_desde',inplace=True)
            
            for i in range(len(trans_desde_alycs)):
                alycs_trans_desde.iloc[i,0]=trans_desde_alycs.loc[:,'Importe'].iloc[i]
                alycs_trans_desde.iloc[i,1]=(fecha_cierre-trans_desde_alycs.index[i]).days 
                
                if (alycs_trans_desde.iloc[i,1] == dias):
                    alycs_trans_desde.iloc[i,0] = 0
                 
            
            # Vector de transferencia hacia otras ALYCS
            alycs_trans_hacia=pd.DataFrame()
            alycs_trans_hacia['monto']=float(0)
            alycs_trans_hacia['plazo']=int(0)
            alycs_trans_hacia['alycs_trans_hacia']=int(0)
            
            for i in range(50):
                alycs_trans_hacia.loc[i]=float(0) 
                alycs_trans_hacia.loc[i,'alycs_trans_hacia']=i
            
            alycs_trans_hacia.set_index('alycs_trans_hacia',inplace=True)
            
            for i in range(len(trans_hacia_alycs)):
                alycs_trans_hacia.iloc[i,0]=trans_hacia_alycs.loc[:,'Importe'].iloc[i]*-1
                alycs_trans_hacia.iloc[i,1]=(fecha_cierre-trans_hacia_alycs.index[i]).days 
                 
                if (alycs_trans_hacia.iloc[i,1] == dias):
                    alycs_trans_hacia.iloc[i,0] = 0
            
            # Vectores de depositos y retiros en usd
            depositos_usd=pd.DataFrame()
            depositos_usd['monto']=float(0)
            depositos_usd['plazo']=int(0)
            depositos_usd['depositos_usd']=int(0)
            
            for i in range(50):
                depositos_usd.loc[i]=float(0)  
                depositos_usd.loc[i,'depositos_usd']=i
            
            depositos_usd.set_index('depositos_usd',inplace=True)
            
            for i in range(len(usd_depositos)):
                depositos_usd.iloc[i,0]=usd_depositos.loc[:,'Importe'].iloc[i]
                depositos_usd.iloc[i,1]=(fecha_cierre-usd_depositos.index[i]).days
                
                if (depositos_usd.iloc[i,1] == dias):
                    depositos_usd.iloc[i,0] = 0
            
            retiros_usd=pd.DataFrame()
            retiros_usd['monto']=float(0)
            retiros_usd['plazo']=int(0)
            retiros_usd['retiros_usd']=int(0)
            
            for i in range(50):
                retiros_usd.loc[i]=float(0)  
                retiros_usd.loc[i,'retiros_usd']=i    
            
            retiros_usd.set_index('retiros_usd',inplace=True)
            
            for i in range(len(usd_retiros)):
                retiros_usd.iloc[i,0]=usd_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_usd.iloc[i,1]=(fecha_cierre-usd_retiros.index[i]).days 
                
                if (retiros_usd.iloc[i,1] == dias):
                    retiros_usd.iloc[i,0] = 0
                
            
            
            
            # ------------------------------ QUINTA PARTE ---------------------------------
            #             DEPOSITOS Y RETIROS EN DOLARES SE TRADUCEN A PESOS MEP
            # -----------------------------------------------------------------------------
            # Importamos el archivo de precios
            if (len(depositos_usd.loc[depositos_usd.monto>0])>0) or (
                                        len(retiros_usd.loc[retiros_usd.monto>0])>0):
                archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                            ,sheet_name='Hoja 2').set_index('fecha')
            else:
                archivo_precios = pd.DataFrame()
                
            
            # Depositos en usd a pesos
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in usd_depositos.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                for i in range(len(usd_depositos)):
                    depositos_usd.iloc[i,0]=precio_dolar[i]*depositos_usd.iloc[i,0]
            
            
            # Retiros en usd a pesos
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in usd_retiros.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                for i in range(len(usd_retiros)):
                    retiros_usd.iloc[i,0]=precio_dolar[i]*retiros_usd.iloc[i,0]
            
            
            
            
            # ----------------------------- SEPTIMA PARTE ----------------------------------
            # Los calculos obtenidos se vuelcan en nuevas variables que los contendran. Estas
            # variables son parte de los terminos de la formula para calcular el rendimiento
            # de la cartera.
            # -----------------------------------------------------------------------------
            # Depositos en pesos (d)
            d1=depositos_pesos.iloc[0,0] ; dias_d1=depositos_pesos.iloc[0,1]
            d2=depositos_pesos.iloc[1,0] ; dias_d2=depositos_pesos.iloc[1,1]
            d3=depositos_pesos.iloc[2,0] ; dias_d3=depositos_pesos.iloc[2,1]
            d4=depositos_pesos.iloc[3,0] ; dias_d4=depositos_pesos.iloc[3,1]
            d5=depositos_pesos.iloc[4,0] ; dias_d5=depositos_pesos.iloc[4,1]
            d6=depositos_pesos.iloc[5,0] ; dias_d6=depositos_pesos.iloc[5,1]
            d7=depositos_pesos.iloc[6,0] ; dias_d7=depositos_pesos.iloc[6,1]
            d8=depositos_pesos.iloc[7,0] ; dias_d8=depositos_pesos.iloc[7,1]
            d9=depositos_pesos.iloc[8,0] ; dias_d9=depositos_pesos.iloc[8,1]
            d10=depositos_pesos.iloc[9,0] ; dias_d10=depositos_pesos.iloc[9,1]
            d11=depositos_pesos.iloc[10,0] ; dias_d11=depositos_pesos.iloc[10,1]
            d12=depositos_pesos.iloc[11,0] ; dias_d12=depositos_pesos.iloc[11,1]
            d13=depositos_pesos.iloc[12,0] ; dias_d13=depositos_pesos.iloc[12,1]
            d14=depositos_pesos.iloc[13,0] ; dias_d14=depositos_pesos.iloc[13,1]
            d15=depositos_pesos.iloc[14,0] ; dias_d15=depositos_pesos.iloc[14,1]
            d16=depositos_pesos.iloc[15,0] ; dias_d16=depositos_pesos.iloc[15,1]
            d17=depositos_pesos.iloc[16,0] ; dias_d17=depositos_pesos.iloc[16,1]
            d18=depositos_pesos.iloc[17,0] ; dias_d18=depositos_pesos.iloc[17,1]
            d19=depositos_pesos.iloc[18,0] ; dias_d19=depositos_pesos.iloc[18,1]
            d20=depositos_pesos.iloc[19,0] ; dias_d20=depositos_pesos.iloc[19,1]
            d21=depositos_pesos.iloc[20,0] ; dias_d21=depositos_pesos.iloc[20,1]
            d22=depositos_pesos.iloc[21,0] ; dias_d22=depositos_pesos.iloc[21,1]
            d23=depositos_pesos.iloc[22,0] ; dias_d23=depositos_pesos.iloc[22,1]
            d24=depositos_pesos.iloc[23,0] ; dias_d24=depositos_pesos.iloc[23,1]
            d25=depositos_pesos.iloc[24,0] ; dias_d25=depositos_pesos.iloc[24,1]
            d26=depositos_pesos.iloc[25,0] ; dias_d26=depositos_pesos.iloc[25,1]
            d27=depositos_pesos.iloc[26,0] ; dias_d27=depositos_pesos.iloc[26,1]
            d28=depositos_pesos.iloc[27,0] ; dias_d28=depositos_pesos.iloc[27,1]
            d29=depositos_pesos.iloc[28,0] ; dias_d29=depositos_pesos.iloc[28,1]
            d30=depositos_pesos.iloc[29,0] ; dias_d30=depositos_pesos.iloc[29,1]
            d31=depositos_pesos.iloc[30,0] ; dias_d31=depositos_pesos.iloc[30,1]
            d32=depositos_pesos.iloc[31,0] ; dias_d32=depositos_pesos.iloc[31,1]
            d33=depositos_pesos.iloc[32,0] ; dias_d33=depositos_pesos.iloc[32,1]
            d34=depositos_pesos.iloc[33,0] ; dias_d34=depositos_pesos.iloc[33,1]
            d35=depositos_pesos.iloc[34,0] ; dias_d35=depositos_pesos.iloc[34,1]
            d36=depositos_pesos.iloc[35,0] ; dias_d36=depositos_pesos.iloc[35,1]
            d37=depositos_pesos.iloc[36,0] ; dias_d37=depositos_pesos.iloc[36,1]
            d38=depositos_pesos.iloc[37,0] ; dias_d38=depositos_pesos.iloc[37,1]
            d39=depositos_pesos.iloc[38,0] ; dias_d39=depositos_pesos.iloc[38,1]
            d40=depositos_pesos.iloc[39,0] ; dias_d40=depositos_pesos.iloc[39,1]
            d41=depositos_pesos.iloc[40,0] ; dias_d41=depositos_pesos.iloc[40,1]
            d42=depositos_pesos.iloc[41,0] ; dias_d42=depositos_pesos.iloc[41,1]
            d43=depositos_pesos.iloc[42,0] ; dias_d43=depositos_pesos.iloc[42,1]
            d44=depositos_pesos.iloc[43,0] ; dias_d44=depositos_pesos.iloc[43,1]
            d45=depositos_pesos.iloc[44,0] ; dias_d45=depositos_pesos.iloc[44,1]
            d46=depositos_pesos.iloc[45,0] ; dias_d46=depositos_pesos.iloc[45,1]
            d47=depositos_pesos.iloc[46,0] ; dias_d47=depositos_pesos.iloc[46,1]
            d48=depositos_pesos.iloc[47,0] ; dias_d48=depositos_pesos.iloc[47,1]
            d49=depositos_pesos.iloc[48,0] ; dias_d49=depositos_pesos.iloc[48,1]
            d50=depositos_pesos.iloc[49,0] ; dias_d50=depositos_pesos.iloc[49,1]
            
            
            # Depositos en dolares (d_usd)
            d_usd1=depositos_usd.iloc[0,0] ; dias_d_usd1=depositos_usd.iloc[0,1]
            d_usd2=depositos_usd.iloc[1,0] ; dias_d_usd2=depositos_usd.iloc[1,1]
            d_usd3=depositos_usd.iloc[2,0] ; dias_d_usd3=depositos_usd.iloc[2,1]
            d_usd4=depositos_usd.iloc[3,0] ; dias_d_usd4=depositos_usd.iloc[3,1]
            d_usd5=depositos_usd.iloc[4,0] ; dias_d_usd5=depositos_usd.iloc[4,1]
            d_usd6=depositos_usd.iloc[5,0] ; dias_d_usd6=depositos_usd.iloc[5,1]
            d_usd7=depositos_usd.iloc[6,0] ; dias_d_usd7=depositos_usd.iloc[6,1]
            d_usd8=depositos_usd.iloc[7,0] ; dias_d_usd8=depositos_usd.iloc[7,1]
            d_usd9=depositos_usd.iloc[8,0] ; dias_d_usd9=depositos_usd.iloc[8,1]
            d_usd10=depositos_usd.iloc[9,0] ; dias_d_usd10=depositos_usd.iloc[9,1]
            d_usd11=depositos_usd.iloc[10,0] ; dias_d_usd11=depositos_usd.iloc[10,1]
            d_usd12=depositos_usd.iloc[11,0] ; dias_d_usd12=depositos_usd.iloc[11,1]
            d_usd13=depositos_usd.iloc[12,0] ; dias_d_usd13=depositos_usd.iloc[12,1]
            d_usd14=depositos_usd.iloc[13,0] ; dias_d_usd14=depositos_usd.iloc[13,1]
            d_usd15=depositos_usd.iloc[14,0] ; dias_d_usd15=depositos_usd.iloc[14,1]
            d_usd16=depositos_usd.iloc[15,0] ; dias_d_usd16=depositos_usd.iloc[15,1]
            d_usd17=depositos_usd.iloc[16,0] ; dias_d_usd17=depositos_usd.iloc[16,1]
            d_usd18=depositos_usd.iloc[17,0] ; dias_d_usd18=depositos_usd.iloc[17,1]
            d_usd19=depositos_usd.iloc[18,0] ; dias_d_usd19=depositos_usd.iloc[18,1]
            d_usd20=depositos_usd.iloc[19,0] ; dias_d_usd20=depositos_usd.iloc[19,1]
            d_usd21=depositos_usd.iloc[20,0] ; dias_d_usd21=depositos_usd.iloc[20,1]
            d_usd22=depositos_usd.iloc[21,0] ; dias_d_usd22=depositos_usd.iloc[21,1]
            d_usd23=depositos_usd.iloc[22,0] ; dias_d_usd23=depositos_usd.iloc[22,1]
            d_usd24=depositos_usd.iloc[23,0] ; dias_d_usd24=depositos_usd.iloc[23,1]
            d_usd25=depositos_usd.iloc[24,0] ; dias_d_usd25=depositos_usd.iloc[24,1]
            d_usd26=depositos_usd.iloc[25,0] ; dias_d_usd26=depositos_usd.iloc[25,1]
            d_usd27=depositos_usd.iloc[26,0] ; dias_d_usd27=depositos_usd.iloc[26,1]
            d_usd28=depositos_usd.iloc[27,0] ; dias_d_usd28=depositos_usd.iloc[27,1]
            d_usd29=depositos_usd.iloc[28,0] ; dias_d_usd29=depositos_usd.iloc[28,1]
            d_usd30=depositos_usd.iloc[29,0] ; dias_d_usd30=depositos_usd.iloc[29,1]
            d_usd31=depositos_usd.iloc[30,0] ; dias_d_usd31=depositos_usd.iloc[30,1]
            d_usd32=depositos_usd.iloc[31,0] ; dias_d_usd32=depositos_usd.iloc[31,1]
            d_usd33=depositos_usd.iloc[32,0] ; dias_d_usd33=depositos_usd.iloc[32,1]
            d_usd34=depositos_usd.iloc[33,0] ; dias_d_usd34=depositos_usd.iloc[33,1]
            d_usd35=depositos_usd.iloc[34,0] ; dias_d_usd35=depositos_usd.iloc[34,1]
            d_usd36=depositos_usd.iloc[35,0] ; dias_d_usd36=depositos_usd.iloc[35,1]
            d_usd37=depositos_usd.iloc[36,0] ; dias_d_usd37=depositos_usd.iloc[36,1]
            d_usd38=depositos_usd.iloc[37,0] ; dias_d_usd38=depositos_usd.iloc[37,1]
            d_usd39=depositos_usd.iloc[38,0] ; dias_d_usd39=depositos_usd.iloc[38,1]
            d_usd40=depositos_usd.iloc[39,0] ; dias_d_usd40=depositos_usd.iloc[39,1]
            d_usd41=depositos_usd.iloc[40,0] ; dias_d_usd41=depositos_usd.iloc[40,1]
            d_usd42=depositos_usd.iloc[41,0] ; dias_d_usd42=depositos_usd.iloc[41,1]
            d_usd43=depositos_usd.iloc[42,0] ; dias_d_usd43=depositos_usd.iloc[42,1]
            d_usd44=depositos_usd.iloc[43,0] ; dias_d_usd44=depositos_usd.iloc[43,1]
            d_usd45=depositos_usd.iloc[44,0] ; dias_d_usd45=depositos_usd.iloc[44,1]
            d_usd46=depositos_usd.iloc[45,0] ; dias_d_usd46=depositos_usd.iloc[45,1]
            d_usd47=depositos_usd.iloc[46,0] ; dias_d_usd47=depositos_usd.iloc[46,1]
            d_usd48=depositos_usd.iloc[47,0] ; dias_d_usd48=depositos_usd.iloc[47,1]
            d_usd49=depositos_usd.iloc[48,0] ; dias_d_usd49=depositos_usd.iloc[48,1]
            d_usd50=depositos_usd.iloc[49,0] ; dias_d_usd50=depositos_usd.iloc[49,1]
            
            
            # Retiros en pesos (r)
            r1=retiros_pesos.iloc[0,0] ; dias_r1=retiros_pesos.iloc[0,1]
            r2=retiros_pesos.iloc[1,0] ; dias_r2=retiros_pesos.iloc[1,1]
            r3=retiros_pesos.iloc[2,0] ; dias_r3=retiros_pesos.iloc[2,1]
            r4=retiros_pesos.iloc[3,0] ; dias_r4=retiros_pesos.iloc[3,1]
            r5=retiros_pesos.iloc[4,0] ; dias_r5=retiros_pesos.iloc[4,1]
            r6=retiros_pesos.iloc[5,0] ; dias_r6=retiros_pesos.iloc[5,1]
            r7=retiros_pesos.iloc[6,0] ; dias_r7=retiros_pesos.iloc[6,1]
            r8=retiros_pesos.iloc[7,0] ; dias_r8=retiros_pesos.iloc[7,1]
            r9=retiros_pesos.iloc[8,0] ; dias_r9=retiros_pesos.iloc[8,1]
            r10=retiros_pesos.iloc[9,0] ; dias_r10=retiros_pesos.iloc[9,1]
            r11=retiros_pesos.iloc[10,0] ; dias_r11=retiros_pesos.iloc[10,1]
            r12=retiros_pesos.iloc[11,0] ; dias_r12=retiros_pesos.iloc[11,1]
            r13=retiros_pesos.iloc[12,0] ; dias_r13=retiros_pesos.iloc[12,1]
            r14=retiros_pesos.iloc[13,0] ; dias_r14=retiros_pesos.iloc[13,1]
            r15=retiros_pesos.iloc[14,0] ; dias_r15=retiros_pesos.iloc[14,1]
            r16=retiros_pesos.iloc[15,0] ; dias_r16=retiros_pesos.iloc[15,1]
            r17=retiros_pesos.iloc[16,0] ; dias_r17=retiros_pesos.iloc[16,1]
            r18=retiros_pesos.iloc[17,0] ; dias_r18=retiros_pesos.iloc[17,1]
            r19=retiros_pesos.iloc[18,0] ; dias_r19=retiros_pesos.iloc[18,1]
            r20=retiros_pesos.iloc[19,0] ; dias_r20=retiros_pesos.iloc[19,1]
            r21=retiros_pesos.iloc[20,0] ; dias_r21=retiros_pesos.iloc[20,1]
            r22=retiros_pesos.iloc[21,0] ; dias_r22=retiros_pesos.iloc[21,1]
            r23=retiros_pesos.iloc[22,0] ; dias_r23=retiros_pesos.iloc[22,1]
            r24=retiros_pesos.iloc[23,0] ; dias_r24=retiros_pesos.iloc[23,1]
            r25=retiros_pesos.iloc[24,0] ; dias_r25=retiros_pesos.iloc[24,1]
            r26=retiros_pesos.iloc[25,0] ; dias_r26=retiros_pesos.iloc[25,1]
            r27=retiros_pesos.iloc[26,0] ; dias_r27=retiros_pesos.iloc[26,1]
            r28=retiros_pesos.iloc[27,0] ; dias_r28=retiros_pesos.iloc[27,1]
            r29=retiros_pesos.iloc[28,0] ; dias_r29=retiros_pesos.iloc[28,1]
            r30=retiros_pesos.iloc[29,0] ; dias_r30=retiros_pesos.iloc[29,1]
            r31=retiros_pesos.iloc[30,0] ; dias_r31=retiros_pesos.iloc[30,1]
            r32=retiros_pesos.iloc[31,0] ; dias_r32=retiros_pesos.iloc[31,1]
            r33=retiros_pesos.iloc[32,0] ; dias_r33=retiros_pesos.iloc[32,1]
            r34=retiros_pesos.iloc[33,0] ; dias_r34=retiros_pesos.iloc[33,1]
            r35=retiros_pesos.iloc[34,0] ; dias_r35=retiros_pesos.iloc[34,1]
            r36=retiros_pesos.iloc[35,0] ; dias_r36=retiros_pesos.iloc[35,1]
            r37=retiros_pesos.iloc[36,0] ; dias_r37=retiros_pesos.iloc[36,1]
            r38=retiros_pesos.iloc[37,0] ; dias_r38=retiros_pesos.iloc[37,1]
            r39=retiros_pesos.iloc[38,0] ; dias_r39=retiros_pesos.iloc[38,1]
            r40=retiros_pesos.iloc[39,0] ; dias_r40=retiros_pesos.iloc[39,1]
            r41=retiros_pesos.iloc[40,0] ; dias_r41=retiros_pesos.iloc[40,1]
            r42=retiros_pesos.iloc[41,0] ; dias_r42=retiros_pesos.iloc[41,1]
            r43=retiros_pesos.iloc[42,0] ; dias_r43=retiros_pesos.iloc[42,1]
            r44=retiros_pesos.iloc[43,0] ; dias_r44=retiros_pesos.iloc[43,1]
            r45=retiros_pesos.iloc[44,0] ; dias_r45=retiros_pesos.iloc[44,1]
            r46=retiros_pesos.iloc[45,0] ; dias_r46=retiros_pesos.iloc[45,1]
            r47=retiros_pesos.iloc[46,0] ; dias_r47=retiros_pesos.iloc[46,1]
            r48=retiros_pesos.iloc[47,0] ; dias_r48=retiros_pesos.iloc[47,1]
            r49=retiros_pesos.iloc[48,0] ; dias_r49=retiros_pesos.iloc[48,1]
            r50=retiros_pesos.iloc[49,0] ; dias_r50=retiros_pesos.iloc[49,1]
            
            
            # Retiros por dolar mep (dm)
            dm1=retiros_usd.iloc[0,0] ; dias_dm1=retiros_usd.iloc[0,1]
            dm2=retiros_usd.iloc[1,0] ; dias_dm2=retiros_usd.iloc[1,1]
            dm3=retiros_usd.iloc[2,0] ; dias_dm3=retiros_usd.iloc[2,1]
            dm4=retiros_usd.iloc[3,0] ; dias_dm4=retiros_usd.iloc[3,1]
            dm5=retiros_usd.iloc[4,0] ; dias_dm5=retiros_usd.iloc[4,1]
            dm6=retiros_usd.iloc[5,0] ; dias_dm6=retiros_usd.iloc[5,1]
            dm7=retiros_usd.iloc[6,0] ; dias_dm7=retiros_usd.iloc[6,1]
            dm8=retiros_usd.iloc[7,0] ; dias_dm8=retiros_usd.iloc[7,1]
            dm9=retiros_usd.iloc[8,0] ; dias_dm9=retiros_usd.iloc[8,1]
            dm10=retiros_usd.iloc[9,0] ; dias_dm10=retiros_usd.iloc[9,1]
            dm11=retiros_usd.iloc[10,0] ; dias_dm11=retiros_usd.iloc[10,1]
            dm12=retiros_usd.iloc[11,0] ; dias_dm12=retiros_usd.iloc[11,1]
            dm13=retiros_usd.iloc[12,0] ; dias_dm13=retiros_usd.iloc[12,1]
            dm14=retiros_usd.iloc[13,0] ; dias_dm14=retiros_usd.iloc[13,1]
            dm15=retiros_usd.iloc[14,0] ; dias_dm15=retiros_usd.iloc[14,1]
            dm16=retiros_usd.iloc[15,0] ; dias_dm16=retiros_usd.iloc[15,1]
            dm17=retiros_usd.iloc[16,0] ; dias_dm17=retiros_usd.iloc[16,1]
            dm18=retiros_usd.iloc[17,0] ; dias_dm18=retiros_usd.iloc[17,1]
            dm19=retiros_usd.iloc[18,0] ; dias_dm19=retiros_usd.iloc[18,1]
            dm20=retiros_usd.iloc[19,0] ; dias_dm20=retiros_usd.iloc[19,1]
            dm21=retiros_usd.iloc[20,0] ; dias_dm21=retiros_usd.iloc[20,1]
            dm22=retiros_usd.iloc[21,0] ; dias_dm22=retiros_usd.iloc[21,1]
            dm23=retiros_usd.iloc[22,0] ; dias_dm23=retiros_usd.iloc[22,1]
            dm24=retiros_usd.iloc[23,0] ; dias_dm24=retiros_usd.iloc[23,1]
            dm25=retiros_usd.iloc[24,0] ; dias_dm25=retiros_usd.iloc[24,1]
            dm26=retiros_usd.iloc[25,0] ; dias_dm26=retiros_usd.iloc[25,1]
            dm27=retiros_usd.iloc[26,0] ; dias_dm27=retiros_usd.iloc[26,1]
            dm28=retiros_usd.iloc[27,0] ; dias_dm28=retiros_usd.iloc[27,1]
            dm29=retiros_usd.iloc[28,0] ; dias_dm29=retiros_usd.iloc[28,1]
            dm30=retiros_usd.iloc[29,0] ; dias_dm30=retiros_usd.iloc[29,1]
            dm31=retiros_usd.iloc[30,0] ; dias_dm31=retiros_usd.iloc[30,1]
            dm32=retiros_usd.iloc[31,0] ; dias_dm32=retiros_usd.iloc[31,1]
            dm33=retiros_usd.iloc[32,0] ; dias_dm33=retiros_usd.iloc[32,1]
            dm34=retiros_usd.iloc[33,0] ; dias_dm34=retiros_usd.iloc[33,1]
            dm35=retiros_usd.iloc[34,0] ; dias_dm35=retiros_usd.iloc[34,1]
            dm36=retiros_usd.iloc[35,0] ; dias_dm36=retiros_usd.iloc[35,1]
            dm37=retiros_usd.iloc[36,0] ; dias_dm37=retiros_usd.iloc[36,1]
            dm38=retiros_usd.iloc[37,0] ; dias_dm38=retiros_usd.iloc[37,1]
            dm39=retiros_usd.iloc[38,0] ; dias_dm39=retiros_usd.iloc[38,1]
            dm40=retiros_usd.iloc[39,0] ; dias_dm40=retiros_usd.iloc[39,1]
            dm41=retiros_usd.iloc[40,0] ; dias_dm41=retiros_usd.iloc[40,1]
            dm42=retiros_usd.iloc[41,0] ; dias_dm42=retiros_usd.iloc[41,1]
            dm43=retiros_usd.iloc[42,0] ; dias_dm43=retiros_usd.iloc[42,1]
            dm44=retiros_usd.iloc[43,0] ; dias_dm44=retiros_usd.iloc[43,1]
            dm45=retiros_usd.iloc[44,0] ; dias_dm45=retiros_usd.iloc[44,1]
            dm46=retiros_usd.iloc[45,0] ; dias_dm46=retiros_usd.iloc[45,1]
            dm47=retiros_usd.iloc[46,0] ; dias_dm47=retiros_usd.iloc[46,1]
            dm48=retiros_usd.iloc[47,0] ; dias_dm48=retiros_usd.iloc[47,1]
            dm49=retiros_usd.iloc[48,0] ; dias_dm49=retiros_usd.iloc[48,1]
            dm50=retiros_usd.iloc[49,0] ; dias_dm50=retiros_usd.iloc[49,1]
            
            
            # Entrada de papeles por transferencias desde otra/s alyc/s (depositos)
            te1=alycs_trans_desde.iloc[0,0] ; dias_te1=alycs_trans_desde.iloc[0,1]
            te2=alycs_trans_desde.iloc[1,0] ; dias_te2=alycs_trans_desde.iloc[1,1]
            te3=alycs_trans_desde.iloc[2,0] ; dias_te3=alycs_trans_desde.iloc[2,1]
            te4=alycs_trans_desde.iloc[3,0] ; dias_te4=alycs_trans_desde.iloc[3,1]
            te5=alycs_trans_desde.iloc[4,0] ; dias_te5=alycs_trans_desde.iloc[4,1]
            te6=alycs_trans_desde.iloc[5,0] ; dias_te6=alycs_trans_desde.iloc[5,1]
            te7=alycs_trans_desde.iloc[6,0] ; dias_te7=alycs_trans_desde.iloc[6,1]
            te8=alycs_trans_desde.iloc[7,0] ; dias_te8=alycs_trans_desde.iloc[7,1]
            te9=alycs_trans_desde.iloc[8,0] ; dias_te9=alycs_trans_desde.iloc[8,1]
            te10=alycs_trans_desde.iloc[9,0] ; dias_te10=alycs_trans_desde.iloc[9,1]
            te11=alycs_trans_desde.iloc[10,0] ; dias_te11=alycs_trans_desde.iloc[10,1]
            te12=alycs_trans_desde.iloc[11,0] ; dias_te12=alycs_trans_desde.iloc[11,1]
            te13=alycs_trans_desde.iloc[12,0] ; dias_te13=alycs_trans_desde.iloc[12,1]
            te14=alycs_trans_desde.iloc[13,0] ; dias_te14=alycs_trans_desde.iloc[13,1]
            te15=alycs_trans_desde.iloc[14,0] ; dias_te15=alycs_trans_desde.iloc[14,1]
            te16=alycs_trans_desde.iloc[15,0] ; dias_te16=alycs_trans_desde.iloc[15,1]
            te17=alycs_trans_desde.iloc[16,0] ; dias_te17=alycs_trans_desde.iloc[16,1]
            te18=alycs_trans_desde.iloc[17,0] ; dias_te18=alycs_trans_desde.iloc[17,1]
            te19=alycs_trans_desde.iloc[18,0] ; dias_te19=alycs_trans_desde.iloc[18,1]
            te20=alycs_trans_desde.iloc[19,0] ; dias_te20=alycs_trans_desde.iloc[19,1]
            te21=alycs_trans_desde.iloc[20,0] ; dias_te21=alycs_trans_desde.iloc[20,1]
            te22=alycs_trans_desde.iloc[21,0] ; dias_te22=alycs_trans_desde.iloc[21,1]
            te23=alycs_trans_desde.iloc[22,0] ; dias_te23=alycs_trans_desde.iloc[22,1]
            te24=alycs_trans_desde.iloc[23,0] ; dias_te24=alycs_trans_desde.iloc[23,1]
            te25=alycs_trans_desde.iloc[24,0] ; dias_te25=alycs_trans_desde.iloc[24,1]
            te26=alycs_trans_desde.iloc[25,0] ; dias_te26=alycs_trans_desde.iloc[25,1]
            te27=alycs_trans_desde.iloc[26,0] ; dias_te27=alycs_trans_desde.iloc[26,1]
            te28=alycs_trans_desde.iloc[27,0] ; dias_te28=alycs_trans_desde.iloc[27,1]
            te29=alycs_trans_desde.iloc[28,0] ; dias_te29=alycs_trans_desde.iloc[28,1]
            te30=alycs_trans_desde.iloc[29,0] ; dias_te30=alycs_trans_desde.iloc[29,1]
            te31=alycs_trans_desde.iloc[30,0] ; dias_te31=alycs_trans_desde.iloc[30,1]
            te32=alycs_trans_desde.iloc[31,0] ; dias_te32=alycs_trans_desde.iloc[31,1]
            te33=alycs_trans_desde.iloc[32,0] ; dias_te33=alycs_trans_desde.iloc[32,1]
            te34=alycs_trans_desde.iloc[33,0] ; dias_te34=alycs_trans_desde.iloc[33,1]
            te35=alycs_trans_desde.iloc[34,0] ; dias_te35=alycs_trans_desde.iloc[34,1]
            te36=alycs_trans_desde.iloc[35,0] ; dias_te36=alycs_trans_desde.iloc[35,1]
            te37=alycs_trans_desde.iloc[36,0] ; dias_te37=alycs_trans_desde.iloc[36,1]
            te38=alycs_trans_desde.iloc[37,0] ; dias_te38=alycs_trans_desde.iloc[37,1]
            te39=alycs_trans_desde.iloc[38,0] ; dias_te39=alycs_trans_desde.iloc[38,1]
            te40=alycs_trans_desde.iloc[39,0] ; dias_te40=alycs_trans_desde.iloc[39,1]
            te41=alycs_trans_desde.iloc[40,0] ; dias_te41=alycs_trans_desde.iloc[40,1]
            te42=alycs_trans_desde.iloc[41,0] ; dias_te42=alycs_trans_desde.iloc[41,1]
            te43=alycs_trans_desde.iloc[42,0] ; dias_te43=alycs_trans_desde.iloc[42,1]
            te44=alycs_trans_desde.iloc[43,0] ; dias_te44=alycs_trans_desde.iloc[43,1]
            te45=alycs_trans_desde.iloc[44,0] ; dias_te45=alycs_trans_desde.iloc[44,1]
            te46=alycs_trans_desde.iloc[45,0] ; dias_te46=alycs_trans_desde.iloc[45,1]
            te47=alycs_trans_desde.iloc[46,0] ; dias_te47=alycs_trans_desde.iloc[46,1]
            te48=alycs_trans_desde.iloc[47,0] ; dias_te48=alycs_trans_desde.iloc[47,1]
            te49=alycs_trans_desde.iloc[48,0] ; dias_te49=alycs_trans_desde.iloc[48,1]
            te50=alycs_trans_desde.iloc[49,0] ; dias_te50=alycs_trans_desde.iloc[49,1]
            
            
            # Salida de papeles por transferencias desde otra/s alyc/s (retiros)
            ts1=alycs_trans_hacia.iloc[0,0] ; dias_ts1=alycs_trans_hacia.iloc[0,1]
            ts2=alycs_trans_hacia.iloc[1,0] ; dias_ts2=alycs_trans_hacia.iloc[1,1]
            ts3=alycs_trans_hacia.iloc[2,0] ; dias_ts3=alycs_trans_hacia.iloc[2,1]
            ts4=alycs_trans_hacia.iloc[3,0] ; dias_ts4=alycs_trans_hacia.iloc[3,1]
            ts5=alycs_trans_hacia.iloc[4,0] ; dias_ts5=alycs_trans_hacia.iloc[4,1]
            ts6=alycs_trans_hacia.iloc[5,0] ; dias_ts6=alycs_trans_hacia.iloc[5,1]
            ts7=alycs_trans_hacia.iloc[6,0] ; dias_ts7=alycs_trans_hacia.iloc[6,1]
            ts8=alycs_trans_hacia.iloc[7,0] ; dias_ts8=alycs_trans_hacia.iloc[7,1]
            ts9=alycs_trans_hacia.iloc[8,0] ; dias_ts9=alycs_trans_hacia.iloc[8,1]
            ts10=alycs_trans_hacia.iloc[9,0] ; dias_ts10=alycs_trans_hacia.iloc[9,1]
            ts11=alycs_trans_hacia.iloc[10,0] ; dias_ts11=alycs_trans_hacia.iloc[10,1]
            ts12=alycs_trans_hacia.iloc[11,0] ; dias_ts12=alycs_trans_hacia.iloc[11,1]
            ts13=alycs_trans_hacia.iloc[12,0] ; dias_ts13=alycs_trans_hacia.iloc[12,1]
            ts14=alycs_trans_hacia.iloc[13,0] ; dias_ts14=alycs_trans_hacia.iloc[13,1]
            ts15=alycs_trans_hacia.iloc[14,0] ; dias_ts15=alycs_trans_hacia.iloc[14,1]
            ts16=alycs_trans_hacia.iloc[15,0] ; dias_ts16=alycs_trans_hacia.iloc[15,1]
            ts17=alycs_trans_hacia.iloc[16,0] ; dias_ts17=alycs_trans_hacia.iloc[16,1]
            ts18=alycs_trans_hacia.iloc[17,0] ; dias_ts18=alycs_trans_hacia.iloc[17,1]
            ts19=alycs_trans_hacia.iloc[18,0] ; dias_ts19=alycs_trans_hacia.iloc[18,1]
            ts20=alycs_trans_hacia.iloc[19,0] ; dias_ts20=alycs_trans_hacia.iloc[19,1]
            ts21=alycs_trans_hacia.iloc[20,0] ; dias_ts21=alycs_trans_hacia.iloc[20,1]
            ts22=alycs_trans_hacia.iloc[21,0] ; dias_ts22=alycs_trans_hacia.iloc[21,1]
            ts23=alycs_trans_hacia.iloc[22,0] ; dias_ts23=alycs_trans_hacia.iloc[22,1]
            ts24=alycs_trans_hacia.iloc[23,0] ; dias_ts24=alycs_trans_hacia.iloc[23,1]
            ts25=alycs_trans_hacia.iloc[24,0] ; dias_ts25=alycs_trans_hacia.iloc[24,1]
            ts26=alycs_trans_hacia.iloc[25,0] ; dias_ts26=alycs_trans_hacia.iloc[25,1]
            ts27=alycs_trans_hacia.iloc[26,0] ; dias_ts27=alycs_trans_hacia.iloc[26,1]
            ts28=alycs_trans_hacia.iloc[27,0] ; dias_ts28=alycs_trans_hacia.iloc[27,1]
            ts29=alycs_trans_hacia.iloc[28,0] ; dias_ts29=alycs_trans_hacia.iloc[28,1]
            ts30=alycs_trans_hacia.iloc[29,0] ; dias_ts30=alycs_trans_hacia.iloc[29,1]
            ts31=alycs_trans_hacia.iloc[30,0] ; dias_ts31=alycs_trans_hacia.iloc[30,1]
            ts32=alycs_trans_hacia.iloc[31,0] ; dias_ts32=alycs_trans_hacia.iloc[31,1]
            ts33=alycs_trans_hacia.iloc[32,0] ; dias_ts33=alycs_trans_hacia.iloc[32,1]
            ts34=alycs_trans_hacia.iloc[33,0] ; dias_ts34=alycs_trans_hacia.iloc[33,1]
            ts35=alycs_trans_hacia.iloc[34,0] ; dias_ts35=alycs_trans_hacia.iloc[34,1]
            ts36=alycs_trans_hacia.iloc[35,0] ; dias_ts36=alycs_trans_hacia.iloc[35,1]
            ts37=alycs_trans_hacia.iloc[36,0] ; dias_ts37=alycs_trans_hacia.iloc[36,1]
            ts38=alycs_trans_hacia.iloc[37,0] ; dias_ts38=alycs_trans_hacia.iloc[37,1]
            ts39=alycs_trans_hacia.iloc[38,0] ; dias_ts39=alycs_trans_hacia.iloc[38,1]
            ts40=alycs_trans_hacia.iloc[39,0] ; dias_ts40=alycs_trans_hacia.iloc[39,1]
            ts41=alycs_trans_hacia.iloc[40,0] ; dias_ts41=alycs_trans_hacia.iloc[40,1]
            ts42=alycs_trans_hacia.iloc[41,0] ; dias_ts42=alycs_trans_hacia.iloc[41,1]
            ts43=alycs_trans_hacia.iloc[42,0] ; dias_ts43=alycs_trans_hacia.iloc[42,1]
            ts44=alycs_trans_hacia.iloc[43,0] ; dias_ts44=alycs_trans_hacia.iloc[43,1]
            ts45=alycs_trans_hacia.iloc[44,0] ; dias_ts45=alycs_trans_hacia.iloc[44,1]
            ts46=alycs_trans_hacia.iloc[45,0] ; dias_ts46=alycs_trans_hacia.iloc[45,1]
            ts47=alycs_trans_hacia.iloc[46,0] ; dias_ts47=alycs_trans_hacia.iloc[46,1]
            ts48=alycs_trans_hacia.iloc[47,0] ; dias_ts48=alycs_trans_hacia.iloc[47,1]
            ts49=alycs_trans_hacia.iloc[48,0] ; dias_ts49=alycs_trans_hacia.iloc[48,1]
            ts50=alycs_trans_hacia.iloc[49,0] ; dias_ts50=alycs_trans_hacia.iloc[49,1]
            
            
            
            
            # ---------------------------- OCTAVA PARTE -----------------------------------
            # Se calcula la TIR BRUTA de la cartera para el trimestre
            # -----------------------------------------------------------------------------
            lista_error_b=[]
            lista_tir_b=[] # Esta en porcentaje
            
            for tir in np.arange(-1,1,puntos_basicos/10000):
                
                                # FLUJO DE FONDOS PARA LA OBTENCION DEL RENDIMIENTO BRUTO
                error = valor_cierre - (
                                
                                  # SALDO AL INICIO DEL TRIMESTRE
                                  valor_inicial*(1+tir)**plazo_inicial +
                                 
                                  # DEPOSITOS DE PESOS DEL CLIENTE
                                  d1*(1+tir)**dias_d1 + d2*(1+tir)**dias_d2 + d3*(1+tir)**dias_d3 +
                                  d4*(1+tir)**dias_d4 + d5*(1+tir)**dias_d5 + d6*(1+tir)**dias_d6 +
                                  d7*(1+tir)**dias_d7 + d8*(1+tir)**dias_d8 + d9*(1+tir)**dias_d9 +
                                  d10*(1+tir)**dias_d10 + d11*(1+tir)**dias_d11 + d12*(1+tir)**dias_d12 +
                                  d13*(1+tir)**dias_d13 + d14*(1+tir)**dias_d14 + d15*(1+tir)**dias_d15 +
                                  d16*(1+tir)**dias_d16 + d17*(1+tir)**dias_d17 + d18*(1+tir)**dias_d18 +
                                  d19*(1+tir)**dias_d19 + d20*(1+tir)**dias_d20 + d21*(1+tir)**dias_d21 +
                                  d22*(1+tir)**dias_d22 + d23*(1+tir)**dias_d23 + d24*(1+tir)**dias_d24 +
                                  d25*(1+tir)**dias_d25 + d26*(1+tir)**dias_d26 + d27*(1+tir)**dias_d27 +
                                  d28*(1+tir)**dias_d28 + d29*(1+tir)**dias_d29 + d30*(1+tir)**dias_d30 +
                                  d31*(1+tir)**dias_d31 + d32*(1+tir)**dias_d32 + d33*(1+tir)**dias_d33 +
                                  d34*(1+tir)**dias_d34 + d35*(1+tir)**dias_d35 + d36*(1+tir)**dias_d36 +
                                  d37*(1+tir)**dias_d37 + d38*(1+tir)**dias_d38 + d39*(1+tir)**dias_d39 +
                                  d40*(1+tir)**dias_d40 + d41*(1+tir)**dias_d41 + d42*(1+tir)**dias_d42 +
                                  d43*(1+tir)**dias_d43 + d44*(1+tir)**dias_d44 + d45*(1+tir)**dias_d45 +
                                  d46*(1+tir)**dias_d46 + d47*(1+tir)**dias_d47 + d48*(1+tir)**dias_d48 +
                                  d49*(1+tir)**dias_d49 + d50*(1+tir)**dias_d50 +  
                               
                                  # DEPOSITOS DE DOLARES DEL CLIENTE
                                  d_usd1*(1+tir)**dias_d_usd1 + d_usd2*(1+tir)**dias_d_usd2 + d_usd3*(1+tir)**dias_d_usd3 +
                                  d_usd4*(1+tir)**dias_d_usd4 + d_usd5*(1+tir)**dias_d_usd5 + d_usd6*(1+tir)**dias_d_usd6 +
                                  d_usd7*(1+tir)**dias_d_usd7 + d_usd8*(1+tir)**dias_d_usd8 + d_usd9*(1+tir)**dias_d_usd9 +
                                  d_usd10*(1+tir)**dias_d_usd10 + d_usd11*(1+tir)**dias_d_usd11 + d_usd12*(1+tir)**dias_d_usd12 +
                                  d_usd13*(1+tir)**dias_d_usd13 + d_usd14*(1+tir)**dias_d_usd14 + d_usd15*(1+tir)**dias_d_usd15 +
                                  d_usd16*(1+tir)**dias_d_usd16 + d_usd17*(1+tir)**dias_d_usd17 + d_usd18*(1+tir)**dias_d_usd18 +
                                  d_usd19*(1+tir)**dias_d_usd19 + d_usd20*(1+tir)**dias_d_usd20 + d_usd21*(1+tir)**dias_d_usd21 +
                                  d_usd22*(1+tir)**dias_d_usd22 + d_usd23*(1+tir)**dias_d_usd23 + d_usd24*(1+tir)**dias_d_usd24 +
                                  d_usd25*(1+tir)**dias_d_usd25 + d_usd26*(1+tir)**dias_d_usd26 + d_usd27*(1+tir)**dias_d_usd27 +
                                  d_usd28*(1+tir)**dias_d_usd28 + d_usd29*(1+tir)**dias_d_usd29 + d_usd30*(1+tir)**dias_d_usd30 +
                                  d_usd31*(1+tir)**dias_d_usd31 + d_usd32*(1+tir)**dias_d_usd32 + d_usd33*(1+tir)**dias_d_usd33 +
                                  d_usd34*(1+tir)**dias_d_usd34 + d_usd35*(1+tir)**dias_d_usd35 + d_usd36*(1+tir)**dias_d_usd36 +
                                  d_usd37*(1+tir)**dias_d_usd37 + d_usd38*(1+tir)**dias_d_usd38 + d_usd39*(1+tir)**dias_d_usd39 +
                                  d_usd40*(1+tir)**dias_d_usd40 + d_usd41*(1+tir)**dias_d_usd41 + d_usd42*(1+tir)**dias_d_usd42 +
                                  d_usd43*(1+tir)**dias_d_usd43 + d_usd44*(1+tir)**dias_d_usd44 + d_usd45*(1+tir)**dias_d_usd45 +
                                  d_usd46*(1+tir)**dias_d_usd46 + d_usd47*(1+tir)**dias_d_usd47 + d_usd48*(1+tir)**dias_d_usd48 +
                                  d_usd49*(1+tir)**dias_d_usd49 + d_usd50*(1+tir)**dias_d_usd50 +
                                  
                                  # TRANSFERENCIAS DE PAPELES DESDE OTRAS ALYCS (DEPOSITOS)
                                  te1*(1+tir)**dias_te1 + te2*(1+tir)**dias_te2 + te3*(1+tir)**dias_te3 +
                                  te4*(1+tir)**dias_te4 + te5*(1+tir)**dias_te5 + te6*(1+tir)**dias_te6 +
                                  te7*(1+tir)**dias_te7 + te8*(1+tir)**dias_te8 + te9*(1+tir)**dias_te9 +
                                  te10*(1+tir)**dias_te10 + te11*(1+tir)**dias_te11 + te12*(1+tir)**dias_te12 +
                                  te13*(1+tir)**dias_te13 + te14*(1+tir)**dias_te14 + te15*(1+tir)**dias_te15 +
                                  te16*(1+tir)**dias_te16 + te17*(1+tir)**dias_te17 + te18*(1+tir)**dias_te18 +
                                  te19*(1+tir)**dias_te19 + te20*(1+tir)**dias_te20 + te21*(1+tir)**dias_te21 +
                                  te22*(1+tir)**dias_te22 + te23*(1+tir)**dias_te23 + te24*(1+tir)**dias_te24 +
                                  te25*(1+tir)**dias_te25 + te26*(1+tir)**dias_te26 + te27*(1+tir)**dias_te27 +
                                  te28*(1+tir)**dias_te28 + te29*(1+tir)**dias_te29 + te30*(1+tir)**dias_te30 +
                                  te31*(1+tir)**dias_te31 + te32*(1+tir)**dias_te32 + te33*(1+tir)**dias_te33 +
                                  te34*(1+tir)**dias_te34 + te35*(1+tir)**dias_te35 + te36*(1+tir)**dias_te36 +
                                  te37*(1+tir)**dias_te37 + te38*(1+tir)**dias_te38 + te39*(1+tir)**dias_te39 +
                                  te40*(1+tir)**dias_te40 + te41*(1+tir)**dias_te41 + te42*(1+tir)**dias_te42 +
                                  te43*(1+tir)**dias_te43 + te44*(1+tir)**dias_te44 + te45*(1+tir)**dias_te45 +
                                  te46*(1+tir)**dias_te46 + te47*(1+tir)**dias_te47 + te48*(1+tir)**dias_te48 +
                                  te49*(1+tir)**dias_te49 + te50*(1+tir)**dias_te50 -                                        
                                 
                                  # RETIROS DE PESOS DEL CLIENTE
                                  r1*(1+tir)**dias_r1 - r2*(1+tir)**dias_r2 - r3*(1+tir)**dias_r3 -
                                  r4*(1+tir)**dias_r4 - r5*(1+tir)**dias_r5 - r6*(1+tir)**dias_r6 -
                                  r7*(1+tir)**dias_r7 - r8*(1+tir)**dias_r8 - r9*(1+tir)**dias_r9 -
                                  r10*(1+tir)**dias_r10 - r11*(1+tir)**dias_r11 - r12*(1+tir)**dias_r12 -
                                  r13*(1+tir)**dias_r13 - r14*(1+tir)**dias_r14 - r15*(1+tir)**dias_r15 -
                                  r16*(1+tir)**dias_r16 - r17*(1+tir)**dias_r17 - r18*(1+tir)**dias_r18 -
                                  r19*(1+tir)**dias_r19 - r20*(1+tir)**dias_r20 - r21*(1+tir)**dias_r21 -
                                  r22*(1+tir)**dias_r22 - r23*(1+tir)**dias_r23 - r24*(1+tir)**dias_r24 -
                                  r25*(1+tir)**dias_r25 - r26*(1+tir)**dias_r26 - r27*(1+tir)**dias_r27 -
                                  r28*(1+tir)**dias_r28 - r29*(1+tir)**dias_r29 - r30*(1+tir)**dias_r30 -
                                  r31*(1+tir)**dias_r31 - r32*(1+tir)**dias_r32 - r33*(1+tir)**dias_r33 -
                                  r34*(1+tir)**dias_r34 - r35*(1+tir)**dias_r35 - r36*(1+tir)**dias_r36 -
                                  r37*(1+tir)**dias_r37 - r38*(1+tir)**dias_r38 - r39*(1+tir)**dias_r39 -
                                  r40*(1+tir)**dias_r40 - r41*(1+tir)**dias_r41 - r42*(1+tir)**dias_r42 -
                                  r43*(1+tir)**dias_r43 - r44*(1+tir)**dias_r44 - r45*(1+tir)**dias_r45 -
                                  r46*(1+tir)**dias_r46 - r47*(1+tir)**dias_r47 - r48*(1+tir)**dias_r48 -
                                  r49*(1+tir)**dias_r49 - r50*(1+tir)**dias_r50 -
                                  
                                  # RETIROS DE DOLARES (POR DOLAR MEP)
                                  dm1*(1+tir)**dias_dm1 - dm2*(1+tir)**dias_dm2 - dm3*(1+tir)**dias_dm3 -
                                  dm4*(1+tir)**dias_dm4 - dm5*(1+tir)**dias_dm5 - dm6*(1+tir)**dias_dm6 -
                                  dm7*(1+tir)**dias_dm7 - dm8*(1+tir)**dias_dm8 - dm9*(1+tir)**dias_dm9 -
                                  dm10*(1+tir)**dias_dm10 - dm11*(1+tir)**dias_dm11 - dm12*(1+tir)**dias_dm12 -
                                  dm13*(1+tir)**dias_dm13 - dm14*(1+tir)**dias_dm14 - dm15*(1+tir)**dias_dm15 -
                                  dm16*(1+tir)**dias_dm16 - dm17*(1+tir)**dias_dm17 - dm18*(1+tir)**dias_dm18 -
                                  dm19*(1+tir)**dias_dm19 - dm20*(1+tir)**dias_dm20 - dm21*(1+tir)**dias_dm21 -
                                  dm22*(1+tir)**dias_dm22 - dm23*(1+tir)**dias_dm23 - dm24*(1+tir)**dias_dm24 -
                                  dm25*(1+tir)**dias_dm25 - dm26*(1+tir)**dias_dm26 - dm27*(1+tir)**dias_dm27 -
                                  dm28*(1+tir)**dias_dm28 - dm29*(1+tir)**dias_dm29 - dm30*(1+tir)**dias_dm30 -
                                  dm31*(1+tir)**dias_dm31 - dm32*(1+tir)**dias_dm32 - dm33*(1+tir)**dias_dm33 -
                                  dm34*(1+tir)**dias_dm34 - dm35*(1+tir)**dias_dm35 - dm36*(1+tir)**dias_dm36 -
                                  dm37*(1+tir)**dias_dm37 - dm38*(1+tir)**dias_dm38 - dm39*(1+tir)**dias_dm39 -
                                  dm40*(1+tir)**dias_dm40 - dm41*(1+tir)**dias_dm41 - dm42*(1+tir)**dias_dm42 -
                                  dm43*(1+tir)**dias_dm43 - dm44*(1+tir)**dias_dm44 - dm45*(1+tir)**dias_dm45 -
                                  dm46*(1+tir)**dias_dm46 - dm47*(1+tir)**dias_dm47 - dm48*(1+tir)**dias_dm48 -
                                  dm49*(1+tir)**dias_dm49 - dm50*(1+tir)**dias_dm50 -
                                  
                                  # TRANSFERENCIAS DE PAPELES HACIA OTRAS ALYCS (RETIROS)
                                  ts1*(1+tir)**dias_ts1 - ts2*(1+tir)**dias_ts2 - ts3*(1+tir)**dias_ts3 -
                                  ts4*(1+tir)**dias_ts4 - ts5*(1+tir)**dias_ts5 - ts6*(1+tir)**dias_ts6 -
                                  ts7*(1+tir)**dias_ts7 - ts8*(1+tir)**dias_ts8 - ts9*(1+tir)**dias_ts9 -
                                  ts10*(1+tir)**dias_ts10 - ts11*(1+tir)**dias_ts11 - ts12*(1+tir)**dias_ts12 - 
                                  ts13*(1+tir)**dias_ts13 - ts14*(1+tir)**dias_ts14 - ts15*(1+tir)**dias_ts15 -
                                  ts16*(1+tir)**dias_ts16 - ts17*(1+tir)**dias_ts17 - ts18*(1+tir)**dias_ts18 -
                                  ts19*(1+tir)**dias_ts19 - ts20*(1+tir)**dias_ts20 - ts21*(1+tir)**dias_ts21 -
                                  ts22*(1+tir)**dias_ts22 - ts23*(1+tir)**dias_ts23 - ts24*(1+tir)**dias_ts24 -
                                  ts25*(1+tir)**dias_ts25 - ts26*(1+tir)**dias_ts26 - ts27*(1+tir)**dias_ts27 -
                                  ts28*(1+tir)**dias_ts28 - ts29*(1+tir)**dias_ts29 - ts30*(1+tir)**dias_ts30 -
                                  ts31*(1+tir)**dias_ts31 - ts32*(1+tir)**dias_ts32 - ts33*(1+tir)**dias_ts33 -
                                  ts34*(1+tir)**dias_ts34 - ts35*(1+tir)**dias_ts35 - ts36*(1+tir)**dias_ts36 -
                                  ts37*(1+tir)**dias_ts37 - ts38*(1+tir)**dias_ts38 - ts39*(1+tir)**dias_ts39 -
                                  ts40*(1+tir)**dias_ts40 - ts41*(1+tir)**dias_ts41 - ts42*(1+tir)**dias_ts42 -
                                  ts43*(1+tir)**dias_ts43 - ts44*(1+tir)**dias_ts44 - ts45*(1+tir)**dias_ts45 -
                                  ts46*(1+tir)**dias_ts46 - ts47*(1+tir)**dias_ts47 - ts48*(1+tir)**dias_ts48 -
                                  ts49*(1+tir)**dias_ts49 - ts50*(1+tir)**dias_ts50 
                                  
                                  
                                  )
                
                lista_tir_b.append(tir)
                lista_error_b.append(error)
                
            listado_b=pd.DataFrame()
            listado_b['error']=lista_error_b
            listado_b['tir']=lista_tir_b
            listado_b['error_abs']=listado_b['error'].abs()
            listado_b.sort_values(by='error_abs',inplace=True)
            listado_b.drop(axis=1,columns='error_abs',inplace=True)
            
            
            # Ahora corregimos este listado para evitar problemas del tipo "controversia del
            # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
            # cobran honorarios. El asunto se resuelve en tres pasos:
            # PRIMERO. Slicing 10 primeros con errores mas pequeños
            listado_b=listado_b.iloc[:10,:]
            
            
            # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
            listado_b.sort_values(by='tir',inplace=True)
            listado_b=listado_b.iloc[:5,:]
            
            
            # TERCERO. Ordenamos de menor a mayor por error absoluto
            listado_b['error_abs']=listado_b['error'].abs()
            listado_b.sort_values(by='error_abs',inplace=True)
            listado_b.drop(axis=1,columns='error_abs',inplace=True)
            
            
            
            
            # ----------------------------- NOVENA PARTE ----------------------------------
            # Se calcula la TIR neta de la cartera para el trimestre
            # -----------------------------------------------------------------------------
            lista_error_n=[]
            lista_tir_n=[] # Esta en porcentaje
            
            for tir in np.arange(-1,1,puntos_basicos/10000):
                
                                # FLUJO DE FONDOS PARA LA OBTENCION DEL RENDIMIENTO NETO
                error = ( valor_cierre - honorario_cierre ) - (
                                
                                    # SALDO AL INICIO DEL TRIMESTRE
                                    valor_inicial*(1+tir)**plazo_inicial +
                                  
                                    # DEPOSITOS DE PESOS DEL CLIENTE
                                    d1*(1+tir)**dias_d1 + d2*(1+tir)**dias_d2 + d3*(1+tir)**dias_d3 +
                                    d4*(1+tir)**dias_d4 + d5*(1+tir)**dias_d5 + d6*(1+tir)**dias_d6 +
                                    d7*(1+tir)**dias_d7 + d8*(1+tir)**dias_d8 + d9*(1+tir)**dias_d9 +
                                    d10*(1+tir)**dias_d10 + d11*(1+tir)**dias_d11 + d12*(1+tir)**dias_d12 +
                                    d13*(1+tir)**dias_d13 + d14*(1+tir)**dias_d14 + d15*(1+tir)**dias_d15 +
                                    d16*(1+tir)**dias_d16 + d17*(1+tir)**dias_d17 + d18*(1+tir)**dias_d18 +
                                    d19*(1+tir)**dias_d19 + d20*(1+tir)**dias_d20 + d21*(1+tir)**dias_d21 +
                                    d22*(1+tir)**dias_d22 + d23*(1+tir)**dias_d23 + d24*(1+tir)**dias_d24 +
                                    d25*(1+tir)**dias_d25 + d26*(1+tir)**dias_d26 + d27*(1+tir)**dias_d27 +
                                    d28*(1+tir)**dias_d28 + d29*(1+tir)**dias_d29 + d30*(1+tir)**dias_d30 +
                                    d31*(1+tir)**dias_d31 + d32*(1+tir)**dias_d32 + d33*(1+tir)**dias_d33 +
                                    d34*(1+tir)**dias_d34 + d35*(1+tir)**dias_d35 + d36*(1+tir)**dias_d36 +
                                    d37*(1+tir)**dias_d37 + d38*(1+tir)**dias_d38 + d39*(1+tir)**dias_d39 +
                                    d40*(1+tir)**dias_d40 + d41*(1+tir)**dias_d41 + d42*(1+tir)**dias_d42 +
                                    d43*(1+tir)**dias_d43 + d44*(1+tir)**dias_d44 + d45*(1+tir)**dias_d45 +
                                    d46*(1+tir)**dias_d46 + d47*(1+tir)**dias_d47 + d48*(1+tir)**dias_d48 +
                                    d49*(1+tir)**dias_d49 + d50*(1+tir)**dias_d50 +  
                                
                                    # DEPOSITOS DE DOLARES DEL CLIENTE
                                    d_usd1*(1+tir)**dias_d_usd1 + d_usd2*(1+tir)**dias_d_usd2 + d_usd3*(1+tir)**dias_d_usd3 +
                                    d_usd4*(1+tir)**dias_d_usd4 + d_usd5*(1+tir)**dias_d_usd5 + d_usd6*(1+tir)**dias_d_usd6 +
                                    d_usd7*(1+tir)**dias_d_usd7 + d_usd8*(1+tir)**dias_d_usd8 + d_usd9*(1+tir)**dias_d_usd9 +
                                    d_usd10*(1+tir)**dias_d_usd10 + d_usd11*(1+tir)**dias_d_usd11 + d_usd12*(1+tir)**dias_d_usd12 +
                                    d_usd13*(1+tir)**dias_d_usd13 + d_usd14*(1+tir)**dias_d_usd14 + d_usd15*(1+tir)**dias_d_usd15 +
                                    d_usd16*(1+tir)**dias_d_usd16 + d_usd17*(1+tir)**dias_d_usd17 + d_usd18*(1+tir)**dias_d_usd18 +
                                    d_usd19*(1+tir)**dias_d_usd19 + d_usd20*(1+tir)**dias_d_usd20 + d_usd21*(1+tir)**dias_d_usd21 +
                                    d_usd22*(1+tir)**dias_d_usd22 + d_usd23*(1+tir)**dias_d_usd23 + d_usd24*(1+tir)**dias_d_usd24 +
                                    d_usd25*(1+tir)**dias_d_usd25 + d_usd26*(1+tir)**dias_d_usd26 + d_usd27*(1+tir)**dias_d_usd27 +
                                    d_usd28*(1+tir)**dias_d_usd28 + d_usd29*(1+tir)**dias_d_usd29 + d_usd30*(1+tir)**dias_d_usd30 +
                                    d_usd31*(1+tir)**dias_d_usd31 + d_usd32*(1+tir)**dias_d_usd32 + d_usd33*(1+tir)**dias_d_usd33 +
                                    d_usd34*(1+tir)**dias_d_usd34 + d_usd35*(1+tir)**dias_d_usd35 + d_usd36*(1+tir)**dias_d_usd36 +
                                    d_usd37*(1+tir)**dias_d_usd37 + d_usd38*(1+tir)**dias_d_usd38 + d_usd39*(1+tir)**dias_d_usd39 +
                                    d_usd40*(1+tir)**dias_d_usd40 + d_usd41*(1+tir)**dias_d_usd41 + d_usd42*(1+tir)**dias_d_usd42 +
                                    d_usd43*(1+tir)**dias_d_usd43 + d_usd44*(1+tir)**dias_d_usd44 + d_usd45*(1+tir)**dias_d_usd45 +
                                    d_usd46*(1+tir)**dias_d_usd46 + d_usd47*(1+tir)**dias_d_usd47 + d_usd48*(1+tir)**dias_d_usd48 +
                                    d_usd49*(1+tir)**dias_d_usd49 + d_usd50*(1+tir)**dias_d_usd50 +
                                    
                                    # TRANSFERENCIAS DE PAPELES DESDE OTRAS ALYCS (DEPOSITOS)
                                    te1*(1+tir)**dias_te1 + te2*(1+tir)**dias_te2 + te3*(1+tir)**dias_te3 +
                                    te4*(1+tir)**dias_te4 + te5*(1+tir)**dias_te5 + te6*(1+tir)**dias_te6 +
                                    te7*(1+tir)**dias_te7 + te8*(1+tir)**dias_te8 + te9*(1+tir)**dias_te9 +
                                    te10*(1+tir)**dias_te10 + te11*(1+tir)**dias_te11 + te12*(1+tir)**dias_te12 +
                                    te13*(1+tir)**dias_te13 + te14*(1+tir)**dias_te14 + te15*(1+tir)**dias_te15 +
                                    te16*(1+tir)**dias_te16 + te17*(1+tir)**dias_te17 + te18*(1+tir)**dias_te18 +
                                    te19*(1+tir)**dias_te19 + te20*(1+tir)**dias_te20 + te21*(1+tir)**dias_te21 +
                                    te22*(1+tir)**dias_te22 + te23*(1+tir)**dias_te23 + te24*(1+tir)**dias_te24 +
                                    te25*(1+tir)**dias_te25 + te26*(1+tir)**dias_te26 + te27*(1+tir)**dias_te27 +
                                    te28*(1+tir)**dias_te28 + te29*(1+tir)**dias_te29 + te30*(1+tir)**dias_te30 +
                                    te31*(1+tir)**dias_te31 + te32*(1+tir)**dias_te32 + te33*(1+tir)**dias_te33 +
                                    te34*(1+tir)**dias_te34 + te35*(1+tir)**dias_te35 + te36*(1+tir)**dias_te36 +
                                    te37*(1+tir)**dias_te37 + te38*(1+tir)**dias_te38 + te39*(1+tir)**dias_te39 +
                                    te40*(1+tir)**dias_te40 + te41*(1+tir)**dias_te41 + te42*(1+tir)**dias_te42 +
                                    te43*(1+tir)**dias_te43 + te44*(1+tir)**dias_te44 + te45*(1+tir)**dias_te45 +
                                    te46*(1+tir)**dias_te46 + te47*(1+tir)**dias_te47 + te48*(1+tir)**dias_te48 +
                                    te49*(1+tir)**dias_te49 + te50*(1+tir)**dias_te50 -  
                                  
                                    # RETIROS DE PESOS DEL CLIENTE
                                    r1*(1+tir)**dias_r1 - r2*(1+tir)**dias_r2 - r3*(1+tir)**dias_r3 -
                                    r4*(1+tir)**dias_r4 - r5*(1+tir)**dias_r5 - r6*(1+tir)**dias_r6 -
                                    r7*(1+tir)**dias_r7 - r8*(1+tir)**dias_r8 - r9*(1+tir)**dias_r9 -
                                    r10*(1+tir)**dias_r10 - r11*(1+tir)**dias_r11 - r12*(1+tir)**dias_r12 -
                                    r13*(1+tir)**dias_r13 - r14*(1+tir)**dias_r14 - r15*(1+tir)**dias_r15 -
                                    r16*(1+tir)**dias_r16 - r17*(1+tir)**dias_r17 - r18*(1+tir)**dias_r18 -
                                    r19*(1+tir)**dias_r19 - r20*(1+tir)**dias_r20 - r21*(1+tir)**dias_r21 -
                                    r22*(1+tir)**dias_r22 - r23*(1+tir)**dias_r23 - r24*(1+tir)**dias_r24 -
                                    r25*(1+tir)**dias_r25 - r26*(1+tir)**dias_r26 - r27*(1+tir)**dias_r27 -
                                    r28*(1+tir)**dias_r28 - r29*(1+tir)**dias_r29 - r30*(1+tir)**dias_r30 -
                                    r31*(1+tir)**dias_r31 - r32*(1+tir)**dias_r32 - r33*(1+tir)**dias_r33 -
                                    r34*(1+tir)**dias_r34 - r35*(1+tir)**dias_r35 - r36*(1+tir)**dias_r36 -
                                    r37*(1+tir)**dias_r37 - r38*(1+tir)**dias_r38 - r39*(1+tir)**dias_r39 -
                                    r40*(1+tir)**dias_r40 - r41*(1+tir)**dias_r41 - r42*(1+tir)**dias_r42 -
                                    r43*(1+tir)**dias_r43 - r44*(1+tir)**dias_r44 - r45*(1+tir)**dias_r45 -
                                    r46*(1+tir)**dias_r46 - r47*(1+tir)**dias_r47 - r48*(1+tir)**dias_r48 -
                                    r49*(1+tir)**dias_r49 - r50*(1+tir)**dias_r50 -
                                   
                                    # RETIROS DE DOLARES (POR DOLAR MEP)
                                    dm1*(1+tir)**dias_dm1 - dm2*(1+tir)**dias_dm2 - dm3*(1+tir)**dias_dm3 -
                                    dm4*(1+tir)**dias_dm4 - dm5*(1+tir)**dias_dm5 - dm6*(1+tir)**dias_dm6 -
                                    dm7*(1+tir)**dias_dm7 - dm8*(1+tir)**dias_dm8 - dm9*(1+tir)**dias_dm9 -
                                    dm10*(1+tir)**dias_dm10 - dm11*(1+tir)**dias_dm11 - dm12*(1+tir)**dias_dm12 -
                                    dm13*(1+tir)**dias_dm13 - dm14*(1+tir)**dias_dm14 - dm15*(1+tir)**dias_dm15 -
                                    dm16*(1+tir)**dias_dm16 - dm17*(1+tir)**dias_dm17 - dm18*(1+tir)**dias_dm18 -
                                    dm19*(1+tir)**dias_dm19 - dm20*(1+tir)**dias_dm20 - dm21*(1+tir)**dias_dm21 -
                                    dm22*(1+tir)**dias_dm22 - dm23*(1+tir)**dias_dm23 - dm24*(1+tir)**dias_dm24 -
                                    dm25*(1+tir)**dias_dm25 - dm26*(1+tir)**dias_dm26 - dm27*(1+tir)**dias_dm27 -
                                    dm28*(1+tir)**dias_dm28 - dm29*(1+tir)**dias_dm29 - dm30*(1+tir)**dias_dm30 -
                                    dm31*(1+tir)**dias_dm31 - dm32*(1+tir)**dias_dm32 - dm33*(1+tir)**dias_dm33 -
                                    dm34*(1+tir)**dias_dm34 - dm35*(1+tir)**dias_dm35 - dm36*(1+tir)**dias_dm36 -
                                    dm37*(1+tir)**dias_dm37 - dm38*(1+tir)**dias_dm38 - dm39*(1+tir)**dias_dm39 -
                                    dm40*(1+tir)**dias_dm40 - dm41*(1+tir)**dias_dm41 - dm42*(1+tir)**dias_dm42 -
                                    dm43*(1+tir)**dias_dm43 - dm44*(1+tir)**dias_dm44 - dm45*(1+tir)**dias_dm45 -
                                    dm46*(1+tir)**dias_dm46 - dm47*(1+tir)**dias_dm47 - dm48*(1+tir)**dias_dm48 -
                                    dm49*(1+tir)**dias_dm49 - dm50*(1+tir)**dias_dm50 -
                                    
                                    # TRANSFERENCIAS DE PAPELES HACIA OTRAS ALYCS (RETIROS)
                                    ts1*(1+tir)**dias_ts1 - ts2*(1+tir)**dias_ts2 - ts3*(1+tir)**dias_ts3 -
                                    ts4*(1+tir)**dias_ts4 - ts5*(1+tir)**dias_ts5 - ts6*(1+tir)**dias_ts6 -
                                    ts7*(1+tir)**dias_ts7 - ts8*(1+tir)**dias_ts8 - ts9*(1+tir)**dias_ts9 -
                                    ts10*(1+tir)**dias_ts10 - ts11*(1+tir)**dias_ts11 - ts12*(1+tir)**dias_ts12 - 
                                    ts13*(1+tir)**dias_ts13 - ts14*(1+tir)**dias_ts14 - ts15*(1+tir)**dias_ts15 -
                                    ts16*(1+tir)**dias_ts16 - ts17*(1+tir)**dias_ts17 - ts18*(1+tir)**dias_ts18 -
                                    ts19*(1+tir)**dias_ts19 - ts20*(1+tir)**dias_ts20 - ts21*(1+tir)**dias_ts21 -
                                    ts22*(1+tir)**dias_ts22 - ts23*(1+tir)**dias_ts23 - ts24*(1+tir)**dias_ts24 -
                                    ts25*(1+tir)**dias_ts25 - ts26*(1+tir)**dias_ts26 - ts27*(1+tir)**dias_ts27 -
                                    ts28*(1+tir)**dias_ts28 - ts29*(1+tir)**dias_ts29 - ts30*(1+tir)**dias_ts30 -
                                    ts31*(1+tir)**dias_ts31 - ts32*(1+tir)**dias_ts32 - ts33*(1+tir)**dias_ts33 -
                                    ts34*(1+tir)**dias_ts34 - ts35*(1+tir)**dias_ts35 - ts36*(1+tir)**dias_ts36 -
                                    ts37*(1+tir)**dias_ts37 - ts38*(1+tir)**dias_ts38 - ts39*(1+tir)**dias_ts39 -
                                    ts40*(1+tir)**dias_ts40 - ts41*(1+tir)**dias_ts41 - ts42*(1+tir)**dias_ts42 -
                                    ts43*(1+tir)**dias_ts43 - ts44*(1+tir)**dias_ts44 - ts45*(1+tir)**dias_ts45 -
                                    ts46*(1+tir)**dias_ts46 - ts47*(1+tir)**dias_ts47 - ts48*(1+tir)**dias_ts48 -
                                    ts49*(1+tir)**dias_ts49 - ts50*(1+tir)**dias_ts50 
                                    
                                   
                                    )
                
                lista_tir_n.append(tir)
                lista_error_n.append(error)
            
            listado_n=pd.DataFrame()
            listado_n['error']=lista_error_n
            listado_n['tir']=lista_tir_n
            listado_n['error_abs']=listado_n['error'].abs()
            listado_n.sort_values(by='error_abs',inplace=True)
            listado_n.drop(axis=1,columns='error_abs',inplace=True)
            
            
            # Ahora corregimos este listado para evitar problemas del tipo "controversia del
            # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
            # cobran honorarios. El asunto se resuelve en tres pasos:
            # PRIMERO. Slicing 10 primeros con errores mas pequeños
            listado_n=listado_n.iloc[:10,:]
            
            
            # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
            listado_n.sort_values(by='tir',inplace=True)
            listado_n=listado_n.iloc[:5,:]
            
            
            # TERCERO. Ordenamos de menor a mayor por error absoluto
            listado_n['error_abs']=listado_n['error'].abs()
            listado_n.sort_values(by='error_abs',inplace=True)
            listado_n.drop(axis=1,columns='error_abs',inplace=True)
            
            
            
            
            # ----------------------------- DECIMA PARTE ----------------------------------
            # Se crea un diccionario que contiene el resultado
            # -----------------------------------------------------------------------------
            # Resultado
            rendimientos={'Rend período':[(1+listado_b.iloc[0,1])**dias-1, (1+listado_n.iloc[0,1])**dias-1],
                          'Fecha inicial':[f'{fecha_inicial}','-'],
                          'Fecha final':[f'{fecha_cierre}','-'],
                          'Valor inicial':[f'{valor_inicial}','-'],
                          'Valor final':[f'{valor_cierre}','-'],
                          'Honorarios':[f'{honorario_cierre}','-']}
            
            rendimiento=pd.DataFrame(rendimientos).T
            rendimiento=rendimiento.rename(columns={0:'Rendimiento bruto',1:'Rendimiento neto'})
                    
        else:
            rendimiento = datos_cliente
        
    except:
        rendimiento = 'Introduzca un usuario válido: 1, 2, 3, 4, o 5 (intente con cualquiera)'


    return rendimiento





# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def composicion_cartera_bal(fecha_cierre, numero_interno = 0, nombre_cliente = '',
                            alyc = '', dni = 0, usuario = 1):
    """
    ¿Qué hace el código? Permite que se conozca la composición de la cartera de
    un cliente a cierta fecha.

    Parameters
    ----------
    fecha_cierre : string
        DESCRIPTION.
        Con esta se indica el momento de interes. 
        El formato debe ser yyyy-mm-dd, por ejemplo: 2023-11-17.
        
    numero_interno : integer, por defecto es 0.
        DESCRIPTION.
        Es el numero interno que la empresa asigno al cliente.
        
    nombre_cliente : string, por defecto es ''.
        DESCRIPTION. 
        Es el nombre del cliente tal cual aparece en su cuenta comitente. 
        
    alyc : string, por defecto es ''.
        DESCRIPTION. 
        Es el nombre de la alyc donde esta la cuenta comitente. Puede ser Bull,
        Ieb, o Balanz. Este dato es importante, por de este modo el codigo puede
        reconocer al cliente.
        
    dni : integer, por defecto es 0.
        DESCRIPTION. 
        Es el numero de documento del cliente.
        
    tipo_calculo : string, por defecto es 'rendimiento'.
        DESCRIPTION. 
        Puede tomar dos valores, "rendimiento" o "tenencia". El primero calcula
        la cartera desde una perspectiva de operacion concertada, mientras que 
        el segundo lo hace desde una perspectiva de operacion liquidada. 

    Returns
    -------
    cartera : Dataframe
        DESCRIPTION.
        Es la composicion de la cartera, con los tickets, sus cantidades y precios,
        y la liquidez en pesos y en dolares (junto con el dolar mep del momento)

    """
    try:
        # usuario = 2 # 1, 2, o 3
        
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        
        import pandas as pd
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        from unidecode import unidecode
        
      
        # Se identifica al cliente
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente,
                                   dni = dni, numero_interno = numero_interno,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
        
        
        # Sub parametros
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de Balanz\{nombre_cliente} ({numero_cliente})'
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        tenencia_inicial=f'Tenencia 31-12-22 {nombre_cliente}'
        transferencia_alyc='Transferencias entre alycs y div en especie'
        
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            #                       IMPORTACION DE ARCHIVOS EXCEL
            # -----------------------------------------------------------------------------
            # Se importan los archivos con los movimientos de la cuenta. Sobre cada uno se
            # toma la máscara que contiene movimientos en fechas previas o iguales a la fecha
            # de cierre. Y se ordenan cronológicamente las operaciones.
            # -----------------------------------------------------------------------------
            # Se transforma la fecha de cierre al tipo datetime
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Importamos la tenencia inicial, eliminamos la columna de precios, y tomamos
            # solo los tickets, la liquidez no (pues queda sujeta al saldo, quien cambia
            # automaticamente). En simultaneo, usamos 'try - except' por si el archivo de 
            # tenencia inicial no existe.
            try:
                cartera_inicial_1=pd.read_excel(f'{directorio_origen}\{tenencia_inicial}.xlsx'
                                              ).set_index('Especie')
                cartera_inicial_1.drop(cartera_inicial_1.columns[-1],axis=1,inplace=True)
                cartera_inicial=cartera_inicial_1.iloc[:-4].copy()
            
            except:
                cartera_inicial=0
            
            
            # Importamos el archivo. El 'Try - except' es para contemplar la situacion donde
            # # este archivo no existe. 
            try:   
                archivo = fc.concatenacion_movimientos_bal(alyc = alyc, dni = dni, 
                                                           usuario = usuario,
                                                           nombre_cliente = nombre_cliente, 
                                                           numero_interno = numero_interno) 
                
                # Se toma la mascara de acuerdo a la fecha de cierre y las 'operaciones locas'
                # que implican cambios en la liquidez y cantidad de papales.
                operaciones_locas = archivo.loc[(archivo.Concertacion<=fecha_cierre) &
                                                (archivo.index>fecha_cierre)].copy()
                
                if len(operaciones_locas)>0:
                    operaciones_locas_pesos = operaciones_locas.loc[operaciones_locas.Moneda=='Pesos'].copy()
                    operaciones_locas_usd = operaciones_locas.loc[operaciones_locas.Moneda=='Dolares C.V. 7000'].copy()
                
                else:
                    operaciones_locas_pesos = pd.DataFrame()
                    operaciones_locas_usd = pd.DataFrame()
                
                archivo = archivo.loc[archivo.index<=fecha_cierre].copy()
            
            except:
                archivo = pd.DataFrame()
                operaciones_locas = pd.DataFrame()
                operaciones_locas_pesos = pd.DataFrame()
                operaciones_locas_usd = pd.DataFrame()
            
            
            # Se captura el archivo en pesos. El 'Try - except' es para contemplar la 
            # mascara no existe.
            try:
                archivo_pesos = archivo.loc[archivo.Moneda=='Pesos'].copy()
                
            except:
                archivo_pesos = pd.DataFrame()
            
            
            # Se captura el archivo en usd. El 'Try - except' es para contemplar la 
            # mascara no existe.
            try:
                archivo_usd = archivo.loc[archivo.Moneda=='Dolares C.V. 7000'].copy()
                
            except:
                archivo_usd = pd.DataFrame()
            
            
            # Traemos el archivo que contiene las transferencias entre alycs.
            try:
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')
                archivo_transf_alyc.set_index("Liquida", inplace=True)   
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.index<=fecha_cierre].copy()
                
            except:
                archivo_transf_alyc = pd.DataFrame()
            
            
            
            
            # ----------------------------- SEGUNDA PARTE ---------------------------------
            #     COMPOSICIONES PARCIALES DE CARTERA - MOVIMIENTOS EN PESOS Y DOLARES 
            # -----------------------------------------------------------------------------
            # Armamos los dataframes agrupando de acuerdo a los tickets, compras/ventas, y 
            # calculando las cantidades mantenidas hasta la fecha de cierre (inclusive). 
            # Esto se hace con los tres archivos, movimientos en pesos, en usd, y en ccl.  
            # -----------------------------------------------------------------------------
            # Movimientos en pesos, y liquidez en pesos y en usd.
            if archivo_pesos.empty:
                cartera_pesos=pd.DataFrame()
                cambio_liq_usd = 0
                tenencia_loca = pd.DataFrame()
                
                if type(cartera_inicial)==type(0):
                    liquidez_pesos = 0
                    liquidez_usd = 0
                else:
                    liquidez_pesos = cartera_inicial_1.loc['liquidez_pesos','Cantidad']   
                    tenencia_inicial_usdtotal = cartera_inicial_1.loc['liquidez_usd','Cantidad']
                
            else:
                cartera_pesos=archivo_pesos.groupby('Ticker').Cantidad.sum()
                cartera_pesos=pd.DataFrame(cartera_pesos)
               
                if len(operaciones_locas_pesos)>0:
                    cambio_liq_pesos = operaciones_locas_pesos.Importe.sum()
                    tenencia_loca = operaciones_locas_pesos.groupby('Ticker').Cantidad.sum()
                    tenencia_loca = pd.DataFrame(tenencia_loca)
                    
                else:
                    cambio_liq_pesos = 0
                    tenencia_loca = pd.DataFrame()
                
                cambio_liq_usd = 0    
                if len(operaciones_locas_usd)>0:
                    cambio_liq_usd = operaciones_locas_usd.Importe.sum()
                    
                liquidez_pesos = archivo_pesos.Importe.sum() + cambio_liq_pesos
            
            if archivo_usd.empty:
                liquidez_usd = cambio_liq_usd
                
            else: 
                liquidez_usd = cambio_liq_usd + archivo_usd.Importe.sum()
                
            
            # Cartera por tenencia
            if archivo_transf_alyc.empty:
                cartera_trans_alyc = pd.DataFrame()
            
            else:
                cartera_trans_alyc = archivo_transf_alyc.groupby('Ticker').Cantidad.sum()
                cartera_trans_alyc = pd.DataFrame(cartera_trans_alyc)
            
            
            
            
            
            # ----------------------------- TERCERA PARTE ---------------------------------
            #       COMPOSICIONES PARCIALES DE CARTERA - INTEGRANDO LOS MOVIMIENTOS 
            # -----------------------------------------------------------------------------
            # Fusionamos las carteras en un nuevo vector llamado 'cartera' 
            if (type(cartera_inicial)==type(0)) & (cartera_pesos.empty==True):
                cartera = pd.DataFrame()
                
            elif (type(cartera_inicial)==type(0)) & (cartera_pesos.empty==False):
                cartera = cartera_pesos
            
            elif (type(cartera_inicial)!=type(0)) & (cartera_pesos.empty==True):
                cartera = cartera_inicial
                
            else:
                cartera = pd.concat([cartera_pesos,cartera_inicial],ignore_index=False)
                cartera = cartera.groupby(cartera.index).Cantidad.sum()
                cartera = pd.DataFrame(cartera)
            
            
            # Ahora fusionamos la cartera con las 'operaciones locas' halladas en la primera parte.
            if tenencia_loca.empty:
                cartera = cartera
            
            else:
                cartera = pd.concat([cartera,tenencia_loca],ignore_index=False)
                cartera = cartera.groupby(cartera.index).Cantidad.sum()
                cartera = pd.DataFrame(cartera)
            
            
            # Se fusiona la 'cartera' con 'cartera_trans_alyc'
            if cartera_trans_alyc.empty:
                cartera = cartera
                
            else:
                cartera = pd.concat([cartera,cartera_trans_alyc],ignore_index=False)
                cartera=cartera.groupby(cartera.index).Cantidad.sum()
                cartera=pd.DataFrame(cartera)
                     
                
            # # Tomamos los papeles con cantidades positivas. 
            if len(cartera)==0:
                cartera=pd.DataFrame()
            else:
                cartera=cartera.loc[cartera.Cantidad>0].copy() 
            
            
            # Incorporamos los saldos liquidos en pesos y en dolares al vector "cartera". 
            cartera.loc['liquidez_usd']=float(0)
            cartera.loc['liquidez_usd','Cantidad']=liquidez_usd
            
            cartera.loc['liquidez_pesos']=float(1)
            cartera.loc['liquidez_pesos','Cantidad']=liquidez_pesos
            cartera[fecha_cierre] = float(0)
            cartera.loc['liquidez_pesos',fecha_cierre] = 1 
            
            
            
            
            # ---------------------------- CUARTA PARTE -----------------------------------
            #            SE COLOCAN LOS PRECIOS A CADA UNO DE LOS PAPELES
            # -----------------------------------------------------------------------------
            # Creamos una cartera donde solo esten los tickets de las acciones
            cartera_aux = cartera.iloc[:-2,:].copy()
            
            
            # Importamos el archivo en pesos
            archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                          ,sheet_name='Hoja 2').set_index('fecha')
            
            
            # Resolvemos la fecha de cierre por si no existen precios en dicho momento
            fecha_cierre2 = fecha_cierre
            for i in range(60):
                
                if len(archivo_precios.loc[archivo_precios.index==(fecha_cierre-timedelta(days=i))])==0:
                    fecha_cierre2=fecha_cierre-timedelta(days=i)
                    
                else:
                    fecha_cierre2=fecha_cierre-timedelta(days=i)
                
                if len(archivo_precios.loc[archivo_precios.index==fecha_cierre2])==1:
                    break
            
            
            # Colocamos los precios de las acciones y dolar mep, si el papel no esta en la
            # serie excel de precios, entonces como precio colocamos el valor 0 (cero)
            for i in cartera_aux.index:
                try:
                    precio = archivo_precios.loc[fecha_cierre2,i]
                    cartera.loc[i,fecha_cierre]=precio
                
                except:
                    cartera.loc[i,fecha_cierre]=0    
            
            try:
                cartera.loc['liquidez_usd',fecha_cierre] = archivo_precios.loc[fecha_cierre2,'dolar_mep']
            
            except:
                cartera.loc['liquidez_usd',fecha_cierre] = 0
            
            
            
        else:
            cartera = datos_cliente
        
    except:
        cartera = 'Introduzca un usuario válido: 1, 2, 3, 4, o 5 (intente con cualquiera)'
    
    return cartera






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def honorario_bal(fecha_cierre,alyc='',nombre_cliente='',numero_interno=0,dni=0,
                  usuario = 1):
   
    """ 
    ---------------------------------------------------------------------------
                               ¿PARA QUE SIRVE?
    Es util para obtener los honorarios de la cartera. 
    ---------------------------------------------------------------------------
                               ¿COMO FUNCIONA? 
    Utiliza la función 'composicion_carteraF', con la cual se obtiene la carte-
    ra del cliente con cuenta en bullmarket en la fecha de cierre indicada.  
    A parte de esta se calcula su valor y se aplican la alicuota que corresponde.
    ---------------------------------------------------------------------------
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene cuenta. Puede ser Bull, Ieb, o Balanz. 
        No importa si el nombre de la alyc se escribe con mayusculas o acentos.  
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, el que figura en la cuenta comitente. Puede 
        escribirse con mayusculas y acentos. 
        Ejemplo: 'Marco Aurelio'.
    
    dni : tipo integer.
    
        DESCRIPCION.
        Es el dni del cliente. No debe escribirse con separadores, puntos o comas.
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa le asigno al cliente.  
        Valor por defecto: 0.
        
    Resultado
    -------
    honorario : tipo DataFrame.
       
       DESCRIPCION.
       Es una tabla con el valor de cartera, los honorarios totales, y la fecha
       correspondiente.
    
    """
   

    if usuario == 1: 
        sub_directorio = 'Y'
        auxiliar = '--'
    elif usuario == 2:
        sub_directorio = 'YY'
        auxiliar = '--'
    elif usuario == 3:
        sub_directorio = 'YYY'
        auxiliar = ''
    elif usuario == 4:
        sub_directorio = 'Y_Y'
        auxiliar = ''
    elif usuario == 5:
        sub_directorio = 'YY_YY'
        auxiliar = ''
    elif usuario == 6:
        sub_directorio = 'YYY_YYY'
        auxiliar = ''
        
    try: 
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        # ----------------------------------------------------------------------------
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        import pandas as pd
        from datetime import datetime as dt   
        
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
            
        
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de Balanz\{nombre_cliente} ({numero_cliente})'
        movimiento_pesos = 'Movimientos'
        
        directorio_clasificador=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        nombre_clasificador='- Categorias de papeles para calculo de honorarios'
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # -----------------------------------------------------------------------------
            #         SE OBTIENE LA CARTERA, SE OBTIENE SU VALOR, Y SE CLASIFICA
            # -----------------------------------------------------------------------------
            # Se importa la cartera con tickets, cantidades, precios, mep, y saldo liquido
            # que corresponde a la fecha de cierre.
            try:
                cartera=fc.composicion_cartera_bal(fecha_cierre = fecha_cierre, alyc = alyc,
                                                   nombre_cliente = nombre_cliente, dni = dni,
                                                   numero_interno = numero_interno,
                                                   usuario = usuario)
            
                cartera['monto']=cartera.Cantidad*cartera.iloc[:,1]
                
                # Se clasifican los papeles de la cartera
                clasificador=pd.read_excel(
                    f'{directorio_clasificador}/{nombre_clasificador}.xlsx').set_index('papel')
            
                cartera['categoria']=str(0)
            
                for i in cartera.index:
                    cartera.loc[i,'categoria']=clasificador.loc[i,'clasificacion']
                
                # Agrupamos el monto de la cartera de acuerdo a esta categorizacion y calculamos
                # su participacion
                cartera2=cartera.groupby('categoria').sum()
                cartera2['porcentaje']=cartera2.monto/cartera2.monto.sum()
            
            except:
                cartera=pd.DataFrame()
                
                cartera2=pd.DataFrame()
                
            
            
            
            # -----------------------------------------------------------------------------
            #              SE CALCULA EL VALOR BRUTO Y NETO DE LA CARTERA
            # -----------------------------------------------------------------------------
            # Identificamos los depositos hechos durante el ultimo mes. Para esto debemos 
            # definir el periodo de tiempo entre la fecha de cierre y el ultimo cobro de honorarios.
            
            # El punto de partida es la fecha de cierre, momento donde queremos cobrar los
            # honorarios. Utilizandola junto con el 'dia de corte' del dataframe 'datos_cliente'
            # definimos la fecha del ultimo cobro de honorarios.
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            
            
            # Objetivo: definir puntas del periodo: 1) fecha de cierre es punta final, 2) 
            # fecha ultimo cobro es punta inicial. Esta ultima debe definirse e implica iden-
            # tificar si dada la fecha de cierre hay o no cambio de mes. Si el dia de la 
            # fecha de cierre es menor o igual al dia de fecha de cobro entonces hay cambio 
            # de mes, si es mayor entonces no lo hay. 
            # Con el siguiente condicional identificamos si cambiamos o no de mes
            if fecha_cierre.day <= datos_cliente.iloc[3,0]:
                # Cambiamos el mes del siguiente modo
                try:    
                    # Controlando los dias por febrero 
                    if (datos_cliente.iloc[3,0] > 28) & (fecha_cierre.month == 3):
                        fecha_ultimo_cobro = fecha_cierre.replace(month = 2, day = 28)
                    
                    # Controlando los dias por meses con 31 dias
                    elif datos_cliente.iloc[3,0] == 31:
                        fecha_ultimo_cobro = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                                  day = 30)
                        
                    # Sin necesidad de controles sobre los dias
                    else:
                        fecha_ultimo_cobro = fecha_cierre.replace(month = fecha_cierre.month-1, 
                                                                  day = datos_cliente.iloc[3,0])
                    
                except ValueError:
                    # Cambio de año por tener fecha de cierre en enero y de ultimo cobro en diciembre
                    fecha_ultimo_cobro = fecha_cierre.replace(year = fecha_cierre.year-1, month = 12,
                                                              day = datos_cliente.iloc[3,0])
                    
            else:
                # Al no cambiar de mes solo hay que modificar el dia
                fecha_ultimo_cobro = fecha_cierre.replace(day = datos_cliente.iloc[3,0])
            
            
            # Ahora se procede a identificar los depositos realizados entre el ultimo cobro
            # de honorarios y la fecha de cierre
            # Depositos en pesos
            dias_transcurridos = (fecha_cierre - fecha_ultimo_cobro).days
            
            
            if cartera.empty:
                archivo_pesos=pd.DataFrame()
                
                depositos=pd.DataFrame()
            
                valor_depositos=0
                
            else:
                try:   
                    
                    # Se lo importa y se lo ordena.    
                    archivo_pesos = fc.concatenacion_movimientos_bal(alyc = alyc, dni = dni, 
                                                                      usuario = usuario,
                                                                      nombre_cliente = nombre_cliente, 
                                                                      numero_interno = numero_interno)
                    
                    archivo_pesos = archivo_pesos.loc[(archivo_pesos.index<=fecha_cierre) &
                                                    (archivo_pesos.index>=fecha_ultimo_cobro)].copy()
                    
                    # Se toma la mascara con los depositos        
                    depositos = archivo_pesos.loc[(archivo_pesos.Tipo=='Tesoreria')].copy()
                    
                    if depositos.empty:
                        valor_depositos=0
                    else:
                        depositos = depositos[['Concertacion','Importe']]
                        depositos.reset_index(inplace=True)
                        depositos.set_index('Concertacion',inplace=True)
                        depositos.drop('Liquidacion',axis=1,inplace=True)
                        
                        depositos['dias_corridos'] = int(0)
                        for i in depositos.index:
                            depositos.loc[i,'dias_corridos']=(fecha_cierre-i).days
                            
                        depositos['Importe_ajus']= -1 * (depositos.dias_corridos - dias_transcurridos
                                                      ) * depositos.Importe / dias_transcurridos
                        
                        valor_depositos=depositos.Importe_ajus.sum()
                       
                except:
                    archivo_pesos=pd.DataFrame()
                    
                    depositos=pd.DataFrame()
                
                    valor_depositos=0
            
             
            # Obtenemos el valor neto y bruto de cartera
            if cartera2.empty:
                valor_bruto=float(0)
                
            else:    
                valor_bruto=cartera2.monto.sum()
                
                for i in cartera2.index:
                    cartera2.loc[i,'monto']=cartera2.loc[i,'monto'] - cartera2.loc[i,'porcentaje']*valor_depositos
                
            
            
            
            # -----------------------------------------------------------------------------
            #                       SE CALCULA EL HONORARIO
            # -----------------------------------------------------------------------------
            # Se calculan los honorarios
            honorario=0
            
            alicuota1=0.005
            
            alicuota2=0.0025
            
            sumafija=1_500
            
            if cartera.empty:
                mep = 1
            
            else:
                mep=cartera.iloc[-2,1]
            
            if valor_bruto/mep>=10_000:
                honorario = (valor_bruto - valor_depositos) * alicuota2 * 1.21
             
            elif (valor_bruto/mep>=1_000) & (valor_bruto/mep<10_000):
                if len(cartera2.loc[cartera2.index=='liquidez'])>0:
                    if cartera2.loc['liquidez','porcentaje']>=0.25:
                        honorario_liq = cartera2.loc['liquidez','monto']*alicuota2
                        valor_liquidez = round(cartera2.loc['liquidez','monto'],2)
                        
                    else:
                        honorario_liq = cartera2.loc['liquidez','monto']*alicuota1
                        valor_liquidez = round(cartera2.loc['liquidez','monto'],2)
                        
                else: 
                    honorario_liq = 0
                    valor_liquidez = 0
                
                if len(cartera2.loc[cartera2.index=='renta fija'])>0:
                    if cartera2.loc['renta fija','porcentaje']>=0.1:
                        honorario_rf = cartera2.loc['renta fija','monto']*alicuota2
                        valor_rentaf = round(cartera2.loc['renta fija','monto'],2)
                        
                    else:
                        honorario_rf = cartera2.loc['renta fija','monto']*alicuota1
                        valor_rentaf = round(cartera2.loc['renta fija','monto'],2)
                
                else:
                    honorario_rf = 0
                    valor_rentaf = 0
                
                if len(cartera2.loc[cartera2.index=='renta variable'])>0:
                    honorario_rv = cartera2.loc['renta variable','monto']*alicuota1
                    valor_rentav = round(cartera2.loc['renta variable','monto'],2)
                    
                else:
                    honorario_rv = 0
                    valor_rentav = 0
            
                honorario = (honorario_rv + honorario_rf + honorario_liq + sumafija) * 1.21
                
            else:
                honorario=0
                
            
            # Para calcular los honorarios proporcionales debemos definir una fecha de cierre
            # ideal que represente el momento donde se cumple exactamente un mes desde el 
            # ultimo cobro. 
            # Controlando el mes por cambio de año  
            if fecha_ultimo_cobro.month == 12:
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = 1, 
                                                                year = fecha_ultimo_cobro.year + 1)
            
            # Controlando los dias por meses con 31 dias
            elif (fecha_ultimo_cobro.day == 31) & (fecha_ultimo_cobro.month != 1):
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = fecha_ultimo_cobro.month + 1, 
                                                                day = 30)
                
            # Controlando por mes de febrero
            elif (fecha_ultimo_cobro.month == 1) & (fecha_ultimo_cobro.day > 28):
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = 2, day = 28)
                
            else:
                fecha_cierre_ideal = fecha_ultimo_cobro.replace(month = fecha_ultimo_cobro.month + 1)
                    
            periodo_ideal = (fecha_cierre_ideal - fecha_ultimo_cobro).days
            periodo_transcurrido = (fecha_cierre - fecha_ultimo_cobro).days
            
            
            # Si corresponde, aplicamos proporcionalidad sobre los honorarios
            if fecha_cierre.day != fecha_ultimo_cobro.day:
                honorario = honorario * (periodo_transcurrido)/ periodo_ideal
                
                
            # Se crea un DataFrame que contiene el honorario y el valor de cartera
            if valor_bruto/mep>=10_000:
                portafolio2={'Cartera cuyo valor supera los 10 mil usd':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Valor imponible':[f'$ {round(valor_bruto - valor_depositos,2)}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
            elif (valor_bruto/mep>=1_000) & (valor_bruto/mep<10_000):
                portafolio2={'Cartera cuyo valor se encuentra entre los mil y 10 mil usd':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Valor imponible liquidez':[f'$ {valor_liquidez}'],
                            'Valor imponible renta fija':[f'$ {valor_rentaf}'],
                            'Valor imponible renta variable':[f'$ {valor_rentav}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}'],
                            'Honorario liquidez':[f'$ {round(honorario_liq,2)}'],
                            'Honorarios renta fija':[f'$ {round(honorario_rf,2)}'],
                            'Honorarios renta variable':[f'$ {round(honorario_rv,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
            else:
                portafolio2={'Cartera cuyo valor es inferior a los mil usd':[''],
                              'Cliente':[nombre_cliente],'Fecha':[fecha_cierre],
                            'Valor cartera':[f'$ {round(valor_bruto,2)}'],
                            'Honorarios totales':[f'$ {round(honorario,2)}']}
                
                portafolio2=pd.DataFrame(portafolio2).T
                portafolio2=portafolio2.rename(columns={0:''})
            
          

        else:
            portafolio2 = datos_cliente
        
    except:
        portafolio2 = 'Introduzca un usuario válido: entre 1 y 6'
   

    return portafolio2







# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def rendimientos_bruto_neto_bal(fecha_cierre, alyc = '', nombre_cliente = '',
                            numero_interno = 0, dni = 0, puntos_basicos = 0.1, 
                            dias = 30, usuario = 1):
    """
    ---------------------------------------------------------------------------
                              ¿PARA QUE SIRVE ESTE CODIGO?
    Para hallar la TIR bruta y neta de honorarios de la cartera. Asimismo, se 
    indica la fecha inicial y final del periodo analizado, pues de este modo 
    el resultado de la funcion puede utilizarse junto a otras funciones. 
    ---------------------------------------------------------------------------
                               ¿COMO FUNCIONA EL CODIGO? 
    Se calcula el valor inicial y final de la cartera, junto con los honorarios
    (si corresponden). Tambien, se obtienen los retiros y depositos en pesos y 
    dolares (aqui se incluyen las operaciones por dolar mep).
    A partir de esta informacion, se obtiene el rendimiento como la TIR de un
    polinomio donde se minimiza el error de calculo. Este se se define como la 
    diferencia entre el valor final e inicial de la cartera, ajustando la dife-
    rencia por los retiros y depositos. Algebraicamente:
                      error = SF - (VF[depositos]-VF[retiros]) 
    ---------------------------------------------------------------------------
                               ACLARACIONES ADICIONALES
    Este codigo es utilizado para situaciones donde el cliente realiza, durante
    el mes, menos de 50 depositos y menos de 50 retiros. De exceder estas canti-
    dades, el codigo se 'rompera' (dejara de funcionar).
    ---------------------------------------------------------------------------
    Paramentros
    ----------
    fecha_cierre : tipo string.
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
        DESCRIPCION.
        Es la alyc donde el cliente tiene su cuenta: Bull, Ieb, o Balanz. 
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    dni : tipo integer.
        DESCRIPCION.
        Es el dni del cliente.   
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
        DESCRIPCION.
        Es el numero interno asignado por la empresa al cliente.  
        Valor por defecto: 0.
        
    puntos_basicos : TYPE float
        DESCRIPCION. 
        Valor por defecto: 0.5.
        Define el incremental del iterador utilizado para hallar la TIR. En otras
        palabras, la TIR crece en 0.5 puntos basicos en el siguiente calculo.
        
    dias : tipo integer
        DESCRIPCION. 
        Valor por defecto: 30.
        Define la cantidad de dias del plazo de analisis. En otras palabras, 
        son la cantidad de dias que se restan a la fecha de cierre.              
        
        
    Resultado
    -------
    rendimiento : tipo DataFrame
        DESCRIPCION.
        Es una tabla con el rendimiento bruto y neto mensual de la cartera ana-
        lizada, junto con la fecha inicial y final del periodo correspondiente.

    """ 
    try: 
       
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        import numpy as np
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        from unidecode import unidecode
        
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
            dia_corte = datos_cliente.loc['Dia de corte','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
        
        
        
        # -----------------------------------------------------------------------------
        # Sub Parametros
        # Estos son parametros, pero no es necesario modificarlos.                  
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de Balanz\{nombre_cliente} ({numero_cliente})'

        # -----------------------------------------------------------------------------
        movimiento_pesos='Movimientos'
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            # Se calcula el 'vector_portafolio', que contiene el valor de la cartera en
            # cada momento, los honorarios, y las fechas de dichos momentos.
            # -----------------------------------------------------------------------------
            # Obtenemos los momentos clave
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial=fecha_cierre-timedelta(days=dias)
            
            
            # Transformamos las fechas a formato string
            fecha_cierre=dt.strftime(fecha_cierre, '%Y-%m-%d')
            fecha_inicial=dt.strftime(fecha_inicial, '%Y-%m-%d')
            
            
            # Obtenemos la composicion de las carteras a inicio y final del periodo 
            # de analisis. De esto nos quedamos con la liquidez en pesos solo si es
            # negativa. Lo hacemos asi para ajustar el valor de cartera que obtenemos
            # con la funcion honorarios.
            saldo_liq_pesos_inicio = fc.composicion_cartera_bal(fecha_cierre = fecha_inicial,
                                                                 alyc = alyc, dni = dni,
                                                                 nombre_cliente = nombre_cliente,
                                                                 numero_interno = numero_interno,
                                                                 usuario = usuario)
            
            if saldo_liq_pesos_inicio.empty == False:
                saldo_liq_pesos_inicio = saldo_liq_pesos_inicio.loc['liquidez_pesos','Cantidad']
                
            else:
                saldo_liq_pesos_inicio = 0
            
            saldo_liq_pesos_final = fc.composicion_cartera_bal(fecha_cierre = fecha_cierre,
                                                                  alyc = alyc, dni = dni,
                                                                  nombre_cliente = nombre_cliente,
                                                                  numero_interno = numero_interno,
                                                                  usuario = usuario)
            if saldo_liq_pesos_final.empty == False:
                saldo_liq_pesos_final = saldo_liq_pesos_final.loc['liquidez_pesos','Cantidad']
                
            else:
                saldo_liq_pesos_final = 0
        
                    
            # Calculamos los valores iniciales y finales
            portafolio_cierre=fc.honorario_bal(fecha_cierre = fecha_cierre, dni = dni, 
                                                alyc = alyc, nombre_cliente = nombre_cliente,
                                                numero_interno = numero_interno,
                                                usuario = usuario)
            
            portafolio_inicial=fc.honorario_bal(fecha_cierre = fecha_inicial, dni = dni, 
                                                alyc = alyc, nombre_cliente = nombre_cliente,
                                                numero_interno = numero_interno,
                                                usuario = usuario)
            
            valor_cierre=float(portafolio_cierre.iloc[3,0][2:])
            valor_inicial=float(portafolio_inicial.iloc[3,0][2:])
            
            if saldo_liq_pesos_inicio < 0:
                valor_inicial = valor_inicial + saldo_liq_pesos_inicio
                
            if saldo_liq_pesos_final < 0:
                valor_cierre = valor_cierre + saldo_liq_pesos_final
                
            
            # Se obtienen los plazos
            plazo_cierre=(portafolio_cierre.iloc[2,0]-portafolio_cierre.iloc[2,0]).days
            
            plazo_inicial=(portafolio_cierre.iloc[2,0]-portafolio_inicial.iloc[2,0]).days
            
            
            # Calculamos los honorarios. Recuerde que los mismos se calculan en diferentes
            # fechas dependiendo el cliente. En otras palabras, no se calculan a finales de 
            # cada mes (no necesariamente). Cuando al cliente no se le cobran honorarios
            # porque ya no es cliente (pero tal vez queremos estudiar los rendimientos que
            # tuvo cuando sí lo fue, entonces "dia_corte" va a ser igual a cero, en estos
            # casos tomamos como fecha de corte la fecha de cierre)  
            if dia_corte == 0:
                fecha_corte = fecha_cierre
            
            else:
                fecha_corte = f'{fecha_cierre[:7]}-{dia_corte}'
                
                # Controlamos para fechas de febrero que no existen:
                # Si el try funciona entonces usamos la fecha de corte señalada arriba.
                # Si el try no funciona se utiliza el resultado del except.
                try:
                    fecha_corte_prueba = dt.strptime(fecha_corte,'%Y-%m-%d')
                    
                except:
                    fecha_corte = f'{fecha_cierre[:7]}-28'
            
            portafolio_fecha_corte = fc.honorario_bal(fecha_cierre=fecha_corte, alyc=alyc, 
                                                      nombre_cliente=nombre_cliente,
                                                      numero_interno=numero_interno,
                                                      dni=dni,usuario = usuario)
            if len(portafolio_fecha_corte) == 11:
                honorario_cierre = float(portafolio_fecha_corte.iloc[7,0][2:])
                
            elif len(portafolio_fecha_corte) == 6:
                honorario_cierre = float(portafolio_fecha_corte.iloc[5,0][2:])
            
            elif len(portafolio_fecha_corte) == 5:
                honorario_cierre = float(portafolio_fecha_corte.iloc[4,0][2:])
            
        
            
        
            # ----------------------------- TERCERA PARTE ---------------------------------
            #          SE IDENTIFICAN LOS DEPOSITOS Y RETIROS EN PESOS Y EN USD
            # -----------------------------------------------------------------------------
            # Se transforma la fecha de cierre al tipo datetime
            fecha_cierre=dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial=dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            
            # Importamos los movimientos en pesos 
            try:   
                # Se lo importa y se lo limpia.    
                archivo = fc.concatenacion_movimientos_bal(alyc = alyc, dni = dni, 
                                                           usuario = usuario,
                                                           nombre_cliente = nombre_cliente, 
                                                           numero_interno = numero_interno) 
            
                archivo = archivo.loc[(archivo.index <= fecha_cierre) & (
                                                    archivo.index >= fecha_inicial)].copy()
            
                pesos_depositos = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                              (archivo.Importe > 0) & 
                                              (archivo.Moneda == 'Pesos') | 
                                              (archivo.Tipo == 'Tesorería') &
                                              (archivo.Importe > 0) & 
                                              (archivo.Moneda == 'Pesos')].copy()
                
                pesos_retiros = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                            (archivo.Importe < 0) & 
                                            (archivo.Moneda == 'Pesos') | 
                                            (archivo.Tipo == 'Tesorería') &
                                            (archivo.Importe < 0) & 
                                            (archivo.Moneda == 'Pesos')].copy()
                
                usd_depositos = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                            (archivo.Importe > 0) & 
                                            (archivo.Moneda == 'Dolares C.V. 7000') | 
                                            (archivo.Tipo == 'Tesorería') &
                                            (archivo.Importe > 0) & 
                                            (archivo.Moneda == 'Dolares C.V. 7000')].copy()
                
                usd_retiros = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                          (archivo.Importe < 0) & 
                                          (archivo.Moneda == 'Dolares C.V. 7000') | 
                                          (archivo.Tipo == 'Tesorería') &
                                          (archivo.Importe < 0) & 
                                          (archivo.Moneda == 'Dolares C.V. 7000')].copy()
            
            except:
                archivo = pd.DataFrame()
                
                pesos_depositos = pd.DataFrame()
            
                pesos_retiros = pd.DataFrame()
                
                usd_depositos = pd.DataFrame()
            
                usd_retiros = pd.DataFrame()
            
            
            
            
            # ------------------------------ CUARTA PARTE ---------------------------------
            #               SE ARMAN LOS VECTORES DE DEPOSITOS Y RETIROS
            # -----------------------------------------------------------------------------
            # Vectores de depositos y retiros en pesos
            depositos_pesos=pd.DataFrame()
            depositos_pesos['monto']=float(0)
            depositos_pesos['plazo']=int(0)
            depositos_pesos['depositos_pesos']=int(0)
            
            for i in range(50):
                depositos_pesos.loc[i]=float(0)  
                depositos_pesos.loc[i,'depositos_pesos']=i
            
            depositos_pesos.set_index('depositos_pesos',inplace=True)
            
            for i in range(len(pesos_depositos)):
                depositos_pesos.iloc[i,0]=pesos_depositos.loc[:,'Importe'].iloc[i]
                depositos_pesos.iloc[i,1]=(fecha_cierre-pesos_depositos.index[i]).days
                
                if (depositos_pesos.iloc[i,1] == dias):
                    depositos_pesos.iloc[i,0] = 0
            
            retiros_pesos=pd.DataFrame()
            retiros_pesos['monto']=float(0)
            retiros_pesos['plazo']=int(0)
            retiros_pesos['retiros_pesos']=int(0)
            
            for i in range(50):
                retiros_pesos.loc[i]=float(0)  
                retiros_pesos.loc[i,'retiros_pesos']=i    
            
            retiros_pesos.set_index('retiros_pesos',inplace=True)
            
            for i in range(len(pesos_retiros)):
                retiros_pesos.iloc[i,0]=pesos_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_pesos.iloc[i,1]=(fecha_cierre-pesos_retiros.index[i]).days
                
                if (retiros_pesos.iloc[i,1] == dias):
                    retiros_pesos.iloc[i,0] = 0
              
            
            # Vectores de depositos y retiros en usd
            depositos_usd=pd.DataFrame()
            depositos_usd['monto']=float(0)
            depositos_usd['plazo']=int(0)
            depositos_usd['depositos_usd']=int(0)
            
            for i in range(50):
                depositos_usd.loc[i]=float(0)  
                depositos_usd.loc[i,'depositos_usd']=i
            
            depositos_usd.set_index('depositos_usd',inplace=True)
            
            for i in range(len(usd_depositos)):
                depositos_usd.iloc[i,0]=usd_depositos.loc[:,'Importe'].iloc[i]
                depositos_usd.iloc[i,1]=(fecha_cierre-usd_depositos.index[i]).days
                
                if (depositos_usd.iloc[i,1] == dias):
                    depositos_usd.iloc[i,0] = 0
            
            retiros_usd=pd.DataFrame()
            retiros_usd['monto']=float(0)
            retiros_usd['plazo']=int(0)
            retiros_usd['retiros_usd']=int(0)
            
            for i in range(50):
                retiros_usd.loc[i]=float(0)  
                retiros_usd.loc[i,'retiros_usd']=i    
            
            retiros_usd.set_index('retiros_usd',inplace=True)
            
            for i in range(len(usd_retiros)):
                retiros_usd.iloc[i,0]=usd_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_usd.iloc[i,1]=(fecha_cierre-usd_retiros.index[i]).days 
                
                if (retiros_usd.iloc[i,1] == dias):
                    retiros_usd.iloc[i,0] = 0
                
            
            
            
            # ------------------------------ QUINTA PARTE ---------------------------------
            #             DEPOSITOS Y RETIROS EN DOLARES SE TRADUCEN A PESOS MEP
            # -----------------------------------------------------------------------------
            # Importamos el archivo de precios
            if (len(depositos_usd.loc[depositos_usd.monto>0])>0) or (
                                        len(retiros_usd.loc[retiros_usd.monto>0])>0):
                archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                            ,sheet_name='Hoja 2').set_index('fecha')
            else:
                archivo_precios = pd.DataFrame()
                
            
            # Depositos y retiros en usd a pesos
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in usd_depositos.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                for i in range(len(usd_depositos)):
                    depositos_usd.iloc[i,0]=precio_dolar[i]*depositos_usd.iloc[i,0]
                
                for i in range(len(usd_retiros)):
                    retiros_usd.iloc[i,0]=precio_dolar[i]*retiros_usd.iloc[i,0]
            
            
            
            
            # ----------------------------- SEPTIMA PARTE ----------------------------------
            # Los calculos obtenidos se vuelcan en nuevas variables que los contendran. Estas
            # variables son parte de los terminos de la formula para calcular el rendimiento
            # de la cartera.
            # -----------------------------------------------------------------------------
            # Depositos en pesos (d)
            d1=depositos_pesos.iloc[0,0] ; dias_d1=depositos_pesos.iloc[0,1]
            d2=depositos_pesos.iloc[1,0] ; dias_d2=depositos_pesos.iloc[1,1]
            d3=depositos_pesos.iloc[2,0] ; dias_d3=depositos_pesos.iloc[2,1]
            d4=depositos_pesos.iloc[3,0] ; dias_d4=depositos_pesos.iloc[3,1]
            d5=depositos_pesos.iloc[4,0] ; dias_d5=depositos_pesos.iloc[4,1]
            d6=depositos_pesos.iloc[5,0] ; dias_d6=depositos_pesos.iloc[5,1]
            d7=depositos_pesos.iloc[6,0] ; dias_d7=depositos_pesos.iloc[6,1]
            d8=depositos_pesos.iloc[7,0] ; dias_d8=depositos_pesos.iloc[7,1]
            d9=depositos_pesos.iloc[8,0] ; dias_d9=depositos_pesos.iloc[8,1]
            d10=depositos_pesos.iloc[9,0] ; dias_d10=depositos_pesos.iloc[9,1]
            d11=depositos_pesos.iloc[10,0] ; dias_d11=depositos_pesos.iloc[10,1]
            d12=depositos_pesos.iloc[11,0] ; dias_d12=depositos_pesos.iloc[11,1]
            d13=depositos_pesos.iloc[12,0] ; dias_d13=depositos_pesos.iloc[12,1]
            d14=depositos_pesos.iloc[13,0] ; dias_d14=depositos_pesos.iloc[13,1]
            d15=depositos_pesos.iloc[14,0] ; dias_d15=depositos_pesos.iloc[14,1]
            d16=depositos_pesos.iloc[15,0] ; dias_d16=depositos_pesos.iloc[15,1]
            d17=depositos_pesos.iloc[16,0] ; dias_d17=depositos_pesos.iloc[16,1]
            d18=depositos_pesos.iloc[17,0] ; dias_d18=depositos_pesos.iloc[17,1]
            d19=depositos_pesos.iloc[18,0] ; dias_d19=depositos_pesos.iloc[18,1]
            d20=depositos_pesos.iloc[19,0] ; dias_d20=depositos_pesos.iloc[19,1]
            d21=depositos_pesos.iloc[20,0] ; dias_d21=depositos_pesos.iloc[20,1]
            d22=depositos_pesos.iloc[21,0] ; dias_d22=depositos_pesos.iloc[21,1]
            d23=depositos_pesos.iloc[22,0] ; dias_d23=depositos_pesos.iloc[22,1]
            d24=depositos_pesos.iloc[23,0] ; dias_d24=depositos_pesos.iloc[23,1]
            d25=depositos_pesos.iloc[24,0] ; dias_d25=depositos_pesos.iloc[24,1]
            d26=depositos_pesos.iloc[25,0] ; dias_d26=depositos_pesos.iloc[25,1]
            d27=depositos_pesos.iloc[26,0] ; dias_d27=depositos_pesos.iloc[26,1]
            d28=depositos_pesos.iloc[27,0] ; dias_d28=depositos_pesos.iloc[27,1]
            d29=depositos_pesos.iloc[28,0] ; dias_d29=depositos_pesos.iloc[28,1]
            d30=depositos_pesos.iloc[29,0] ; dias_d30=depositos_pesos.iloc[29,1]
            d31=depositos_pesos.iloc[30,0] ; dias_d31=depositos_pesos.iloc[30,1]
            d32=depositos_pesos.iloc[31,0] ; dias_d32=depositos_pesos.iloc[31,1]
            d33=depositos_pesos.iloc[32,0] ; dias_d33=depositos_pesos.iloc[32,1]
            d34=depositos_pesos.iloc[33,0] ; dias_d34=depositos_pesos.iloc[33,1]
            d35=depositos_pesos.iloc[34,0] ; dias_d35=depositos_pesos.iloc[34,1]
            d36=depositos_pesos.iloc[35,0] ; dias_d36=depositos_pesos.iloc[35,1]
            d37=depositos_pesos.iloc[36,0] ; dias_d37=depositos_pesos.iloc[36,1]
            d38=depositos_pesos.iloc[37,0] ; dias_d38=depositos_pesos.iloc[37,1]
            d39=depositos_pesos.iloc[38,0] ; dias_d39=depositos_pesos.iloc[38,1]
            d40=depositos_pesos.iloc[39,0] ; dias_d40=depositos_pesos.iloc[39,1]
            d41=depositos_pesos.iloc[40,0] ; dias_d41=depositos_pesos.iloc[40,1]
            d42=depositos_pesos.iloc[41,0] ; dias_d42=depositos_pesos.iloc[41,1]
            d43=depositos_pesos.iloc[42,0] ; dias_d43=depositos_pesos.iloc[42,1]
            d44=depositos_pesos.iloc[43,0] ; dias_d44=depositos_pesos.iloc[43,1]
            d45=depositos_pesos.iloc[44,0] ; dias_d45=depositos_pesos.iloc[44,1]
            d46=depositos_pesos.iloc[45,0] ; dias_d46=depositos_pesos.iloc[45,1]
            d47=depositos_pesos.iloc[46,0] ; dias_d47=depositos_pesos.iloc[46,1]
            d48=depositos_pesos.iloc[47,0] ; dias_d48=depositos_pesos.iloc[47,1]
            d49=depositos_pesos.iloc[48,0] ; dias_d49=depositos_pesos.iloc[48,1]
            d50=depositos_pesos.iloc[49,0] ; dias_d50=depositos_pesos.iloc[49,1]
            
            
            # Depositos en dolares (d_usd)
            d_usd1=depositos_usd.iloc[0,0] ; dias_d_usd1=depositos_usd.iloc[0,1]
            d_usd2=depositos_usd.iloc[1,0] ; dias_d_usd2=depositos_usd.iloc[1,1]
            d_usd3=depositos_usd.iloc[2,0] ; dias_d_usd3=depositos_usd.iloc[2,1]
            d_usd4=depositos_usd.iloc[3,0] ; dias_d_usd4=depositos_usd.iloc[3,1]
            d_usd5=depositos_usd.iloc[4,0] ; dias_d_usd5=depositos_usd.iloc[4,1]
            d_usd6=depositos_usd.iloc[5,0] ; dias_d_usd6=depositos_usd.iloc[5,1]
            d_usd7=depositos_usd.iloc[6,0] ; dias_d_usd7=depositos_usd.iloc[6,1]
            d_usd8=depositos_usd.iloc[7,0] ; dias_d_usd8=depositos_usd.iloc[7,1]
            d_usd9=depositos_usd.iloc[8,0] ; dias_d_usd9=depositos_usd.iloc[8,1]
            d_usd10=depositos_usd.iloc[9,0] ; dias_d_usd10=depositos_usd.iloc[9,1]
            d_usd11=depositos_usd.iloc[10,0] ; dias_d_usd11=depositos_usd.iloc[10,1]
            d_usd12=depositos_usd.iloc[11,0] ; dias_d_usd12=depositos_usd.iloc[11,1]
            d_usd13=depositos_usd.iloc[12,0] ; dias_d_usd13=depositos_usd.iloc[12,1]
            d_usd14=depositos_usd.iloc[13,0] ; dias_d_usd14=depositos_usd.iloc[13,1]
            d_usd15=depositos_usd.iloc[14,0] ; dias_d_usd15=depositos_usd.iloc[14,1]
            d_usd16=depositos_usd.iloc[15,0] ; dias_d_usd16=depositos_usd.iloc[15,1]
            d_usd17=depositos_usd.iloc[16,0] ; dias_d_usd17=depositos_usd.iloc[16,1]
            d_usd18=depositos_usd.iloc[17,0] ; dias_d_usd18=depositos_usd.iloc[17,1]
            d_usd19=depositos_usd.iloc[18,0] ; dias_d_usd19=depositos_usd.iloc[18,1]
            d_usd20=depositos_usd.iloc[19,0] ; dias_d_usd20=depositos_usd.iloc[19,1]
            d_usd21=depositos_usd.iloc[20,0] ; dias_d_usd21=depositos_usd.iloc[20,1]
            d_usd22=depositos_usd.iloc[21,0] ; dias_d_usd22=depositos_usd.iloc[21,1]
            d_usd23=depositos_usd.iloc[22,0] ; dias_d_usd23=depositos_usd.iloc[22,1]
            d_usd24=depositos_usd.iloc[23,0] ; dias_d_usd24=depositos_usd.iloc[23,1]
            d_usd25=depositos_usd.iloc[24,0] ; dias_d_usd25=depositos_usd.iloc[24,1]
            d_usd26=depositos_usd.iloc[25,0] ; dias_d_usd26=depositos_usd.iloc[25,1]
            d_usd27=depositos_usd.iloc[26,0] ; dias_d_usd27=depositos_usd.iloc[26,1]
            d_usd28=depositos_usd.iloc[27,0] ; dias_d_usd28=depositos_usd.iloc[27,1]
            d_usd29=depositos_usd.iloc[28,0] ; dias_d_usd29=depositos_usd.iloc[28,1]
            d_usd30=depositos_usd.iloc[29,0] ; dias_d_usd30=depositos_usd.iloc[29,1]
            d_usd31=depositos_usd.iloc[30,0] ; dias_d_usd31=depositos_usd.iloc[30,1]
            d_usd32=depositos_usd.iloc[31,0] ; dias_d_usd32=depositos_usd.iloc[31,1]
            d_usd33=depositos_usd.iloc[32,0] ; dias_d_usd33=depositos_usd.iloc[32,1]
            d_usd34=depositos_usd.iloc[33,0] ; dias_d_usd34=depositos_usd.iloc[33,1]
            d_usd35=depositos_usd.iloc[34,0] ; dias_d_usd35=depositos_usd.iloc[34,1]
            d_usd36=depositos_usd.iloc[35,0] ; dias_d_usd36=depositos_usd.iloc[35,1]
            d_usd37=depositos_usd.iloc[36,0] ; dias_d_usd37=depositos_usd.iloc[36,1]
            d_usd38=depositos_usd.iloc[37,0] ; dias_d_usd38=depositos_usd.iloc[37,1]
            d_usd39=depositos_usd.iloc[38,0] ; dias_d_usd39=depositos_usd.iloc[38,1]
            d_usd40=depositos_usd.iloc[39,0] ; dias_d_usd40=depositos_usd.iloc[39,1]
            d_usd41=depositos_usd.iloc[40,0] ; dias_d_usd41=depositos_usd.iloc[40,1]
            d_usd42=depositos_usd.iloc[41,0] ; dias_d_usd42=depositos_usd.iloc[41,1]
            d_usd43=depositos_usd.iloc[42,0] ; dias_d_usd43=depositos_usd.iloc[42,1]
            d_usd44=depositos_usd.iloc[43,0] ; dias_d_usd44=depositos_usd.iloc[43,1]
            d_usd45=depositos_usd.iloc[44,0] ; dias_d_usd45=depositos_usd.iloc[44,1]
            d_usd46=depositos_usd.iloc[45,0] ; dias_d_usd46=depositos_usd.iloc[45,1]
            d_usd47=depositos_usd.iloc[46,0] ; dias_d_usd47=depositos_usd.iloc[46,1]
            d_usd48=depositos_usd.iloc[47,0] ; dias_d_usd48=depositos_usd.iloc[47,1]
            d_usd49=depositos_usd.iloc[48,0] ; dias_d_usd49=depositos_usd.iloc[48,1]
            d_usd50=depositos_usd.iloc[49,0] ; dias_d_usd50=depositos_usd.iloc[49,1]
            
            
            # Retiros en pesos (r)
            r1=retiros_pesos.iloc[0,0] ; dias_r1=retiros_pesos.iloc[0,1]
            r2=retiros_pesos.iloc[1,0] ; dias_r2=retiros_pesos.iloc[1,1]
            r3=retiros_pesos.iloc[2,0] ; dias_r3=retiros_pesos.iloc[2,1]
            r4=retiros_pesos.iloc[3,0] ; dias_r4=retiros_pesos.iloc[3,1]
            r5=retiros_pesos.iloc[4,0] ; dias_r5=retiros_pesos.iloc[4,1]
            r6=retiros_pesos.iloc[5,0] ; dias_r6=retiros_pesos.iloc[5,1]
            r7=retiros_pesos.iloc[6,0] ; dias_r7=retiros_pesos.iloc[6,1]
            r8=retiros_pesos.iloc[7,0] ; dias_r8=retiros_pesos.iloc[7,1]
            r9=retiros_pesos.iloc[8,0] ; dias_r9=retiros_pesos.iloc[8,1]
            r10=retiros_pesos.iloc[9,0] ; dias_r10=retiros_pesos.iloc[9,1]
            r11=retiros_pesos.iloc[10,0] ; dias_r11=retiros_pesos.iloc[10,1]
            r12=retiros_pesos.iloc[11,0] ; dias_r12=retiros_pesos.iloc[11,1]
            r13=retiros_pesos.iloc[12,0] ; dias_r13=retiros_pesos.iloc[12,1]
            r14=retiros_pesos.iloc[13,0] ; dias_r14=retiros_pesos.iloc[13,1]
            r15=retiros_pesos.iloc[14,0] ; dias_r15=retiros_pesos.iloc[14,1]
            r16=retiros_pesos.iloc[15,0] ; dias_r16=retiros_pesos.iloc[15,1]
            r17=retiros_pesos.iloc[16,0] ; dias_r17=retiros_pesos.iloc[16,1]
            r18=retiros_pesos.iloc[17,0] ; dias_r18=retiros_pesos.iloc[17,1]
            r19=retiros_pesos.iloc[18,0] ; dias_r19=retiros_pesos.iloc[18,1]
            r20=retiros_pesos.iloc[19,0] ; dias_r20=retiros_pesos.iloc[19,1]
            r21=retiros_pesos.iloc[20,0] ; dias_r21=retiros_pesos.iloc[20,1]
            r22=retiros_pesos.iloc[21,0] ; dias_r22=retiros_pesos.iloc[21,1]
            r23=retiros_pesos.iloc[22,0] ; dias_r23=retiros_pesos.iloc[22,1]
            r24=retiros_pesos.iloc[23,0] ; dias_r24=retiros_pesos.iloc[23,1]
            r25=retiros_pesos.iloc[24,0] ; dias_r25=retiros_pesos.iloc[24,1]
            r26=retiros_pesos.iloc[25,0] ; dias_r26=retiros_pesos.iloc[25,1]
            r27=retiros_pesos.iloc[26,0] ; dias_r27=retiros_pesos.iloc[26,1]
            r28=retiros_pesos.iloc[27,0] ; dias_r28=retiros_pesos.iloc[27,1]
            r29=retiros_pesos.iloc[28,0] ; dias_r29=retiros_pesos.iloc[28,1]
            r30=retiros_pesos.iloc[29,0] ; dias_r30=retiros_pesos.iloc[29,1]
            r31=retiros_pesos.iloc[30,0] ; dias_r31=retiros_pesos.iloc[30,1]
            r32=retiros_pesos.iloc[31,0] ; dias_r32=retiros_pesos.iloc[31,1]
            r33=retiros_pesos.iloc[32,0] ; dias_r33=retiros_pesos.iloc[32,1]
            r34=retiros_pesos.iloc[33,0] ; dias_r34=retiros_pesos.iloc[33,1]
            r35=retiros_pesos.iloc[34,0] ; dias_r35=retiros_pesos.iloc[34,1]
            r36=retiros_pesos.iloc[35,0] ; dias_r36=retiros_pesos.iloc[35,1]
            r37=retiros_pesos.iloc[36,0] ; dias_r37=retiros_pesos.iloc[36,1]
            r38=retiros_pesos.iloc[37,0] ; dias_r38=retiros_pesos.iloc[37,1]
            r39=retiros_pesos.iloc[38,0] ; dias_r39=retiros_pesos.iloc[38,1]
            r40=retiros_pesos.iloc[39,0] ; dias_r40=retiros_pesos.iloc[39,1]
            r41=retiros_pesos.iloc[40,0] ; dias_r41=retiros_pesos.iloc[40,1]
            r42=retiros_pesos.iloc[41,0] ; dias_r42=retiros_pesos.iloc[41,1]
            r43=retiros_pesos.iloc[42,0] ; dias_r43=retiros_pesos.iloc[42,1]
            r44=retiros_pesos.iloc[43,0] ; dias_r44=retiros_pesos.iloc[43,1]
            r45=retiros_pesos.iloc[44,0] ; dias_r45=retiros_pesos.iloc[44,1]
            r46=retiros_pesos.iloc[45,0] ; dias_r46=retiros_pesos.iloc[45,1]
            r47=retiros_pesos.iloc[46,0] ; dias_r47=retiros_pesos.iloc[46,1]
            r48=retiros_pesos.iloc[47,0] ; dias_r48=retiros_pesos.iloc[47,1]
            r49=retiros_pesos.iloc[48,0] ; dias_r49=retiros_pesos.iloc[48,1]
            r50=retiros_pesos.iloc[49,0] ; dias_r50=retiros_pesos.iloc[49,1]
            
            
            # Retiros por dolar mep (dm)
            dm1=retiros_usd.iloc[0,0] ; dias_dm1=retiros_usd.iloc[0,1]
            dm2=retiros_usd.iloc[1,0] ; dias_dm2=retiros_usd.iloc[1,1]
            dm3=retiros_usd.iloc[2,0] ; dias_dm3=retiros_usd.iloc[2,1]
            dm4=retiros_usd.iloc[3,0] ; dias_dm4=retiros_usd.iloc[3,1]
            dm5=retiros_usd.iloc[4,0] ; dias_dm5=retiros_usd.iloc[4,1]
            dm6=retiros_usd.iloc[5,0] ; dias_dm6=retiros_usd.iloc[5,1]
            dm7=retiros_usd.iloc[6,0] ; dias_dm7=retiros_usd.iloc[6,1]
            dm8=retiros_usd.iloc[7,0] ; dias_dm8=retiros_usd.iloc[7,1]
            dm9=retiros_usd.iloc[8,0] ; dias_dm9=retiros_usd.iloc[8,1]
            dm10=retiros_usd.iloc[9,0] ; dias_dm10=retiros_usd.iloc[9,1]
            dm11=retiros_usd.iloc[10,0] ; dias_dm11=retiros_usd.iloc[10,1]
            dm12=retiros_usd.iloc[11,0] ; dias_dm12=retiros_usd.iloc[11,1]
            dm13=retiros_usd.iloc[12,0] ; dias_dm13=retiros_usd.iloc[12,1]
            dm14=retiros_usd.iloc[13,0] ; dias_dm14=retiros_usd.iloc[13,1]
            dm15=retiros_usd.iloc[14,0] ; dias_dm15=retiros_usd.iloc[14,1]
            dm16=retiros_usd.iloc[15,0] ; dias_dm16=retiros_usd.iloc[15,1]
            dm17=retiros_usd.iloc[16,0] ; dias_dm17=retiros_usd.iloc[16,1]
            dm18=retiros_usd.iloc[17,0] ; dias_dm18=retiros_usd.iloc[17,1]
            dm19=retiros_usd.iloc[18,0] ; dias_dm19=retiros_usd.iloc[18,1]
            dm20=retiros_usd.iloc[19,0] ; dias_dm20=retiros_usd.iloc[19,1]
            dm21=retiros_usd.iloc[20,0] ; dias_dm21=retiros_usd.iloc[20,1]
            dm22=retiros_usd.iloc[21,0] ; dias_dm22=retiros_usd.iloc[21,1]
            dm23=retiros_usd.iloc[22,0] ; dias_dm23=retiros_usd.iloc[22,1]
            dm24=retiros_usd.iloc[23,0] ; dias_dm24=retiros_usd.iloc[23,1]
            dm25=retiros_usd.iloc[24,0] ; dias_dm25=retiros_usd.iloc[24,1]
            dm26=retiros_usd.iloc[25,0] ; dias_dm26=retiros_usd.iloc[25,1]
            dm27=retiros_usd.iloc[26,0] ; dias_dm27=retiros_usd.iloc[26,1]
            dm28=retiros_usd.iloc[27,0] ; dias_dm28=retiros_usd.iloc[27,1]
            dm29=retiros_usd.iloc[28,0] ; dias_dm29=retiros_usd.iloc[28,1]
            dm30=retiros_usd.iloc[29,0] ; dias_dm30=retiros_usd.iloc[29,1]
            dm31=retiros_usd.iloc[30,0] ; dias_dm31=retiros_usd.iloc[30,1]
            dm32=retiros_usd.iloc[31,0] ; dias_dm32=retiros_usd.iloc[31,1]
            dm33=retiros_usd.iloc[32,0] ; dias_dm33=retiros_usd.iloc[32,1]
            dm34=retiros_usd.iloc[33,0] ; dias_dm34=retiros_usd.iloc[33,1]
            dm35=retiros_usd.iloc[34,0] ; dias_dm35=retiros_usd.iloc[34,1]
            dm36=retiros_usd.iloc[35,0] ; dias_dm36=retiros_usd.iloc[35,1]
            dm37=retiros_usd.iloc[36,0] ; dias_dm37=retiros_usd.iloc[36,1]
            dm38=retiros_usd.iloc[37,0] ; dias_dm38=retiros_usd.iloc[37,1]
            dm39=retiros_usd.iloc[38,0] ; dias_dm39=retiros_usd.iloc[38,1]
            dm40=retiros_usd.iloc[39,0] ; dias_dm40=retiros_usd.iloc[39,1]
            dm41=retiros_usd.iloc[40,0] ; dias_dm41=retiros_usd.iloc[40,1]
            dm42=retiros_usd.iloc[41,0] ; dias_dm42=retiros_usd.iloc[41,1]
            dm43=retiros_usd.iloc[42,0] ; dias_dm43=retiros_usd.iloc[42,1]
            dm44=retiros_usd.iloc[43,0] ; dias_dm44=retiros_usd.iloc[43,1]
            dm45=retiros_usd.iloc[44,0] ; dias_dm45=retiros_usd.iloc[44,1]
            dm46=retiros_usd.iloc[45,0] ; dias_dm46=retiros_usd.iloc[45,1]
            dm47=retiros_usd.iloc[46,0] ; dias_dm47=retiros_usd.iloc[46,1]
            dm48=retiros_usd.iloc[47,0] ; dias_dm48=retiros_usd.iloc[47,1]
            dm49=retiros_usd.iloc[48,0] ; dias_dm49=retiros_usd.iloc[48,1]
            dm50=retiros_usd.iloc[49,0] ; dias_dm50=retiros_usd.iloc[49,1]
            
            
            
            
            # ---------------------------- OCTAVA PARTE -----------------------------------
            # Se calcula la TIR BRUTA de la cartera para el trimestre
            # -----------------------------------------------------------------------------
            lista_error_b=[]
            lista_tir_b=[] # Esta en porcentaje
            
            for tir in np.arange(-1,1,puntos_basicos/10000):
                
                                # FLUJO DE FONDOS PARA LA OBTENCION DEL RENDIMIENTO BRUTO
                error = valor_cierre - (
                                
                                  # SALDO AL INICIO DEL TRIMESTRE
                                  valor_inicial*(1+tir)**plazo_inicial +
                                 
                                  # DEPOSITOS DE PESOS DEL CLIENTE
                                  d1*(1+tir)**dias_d1 + d2*(1+tir)**dias_d2 + d3*(1+tir)**dias_d3 +
                                  d4*(1+tir)**dias_d4 + d5*(1+tir)**dias_d5 + d6*(1+tir)**dias_d6 +
                                  d7*(1+tir)**dias_d7 + d8*(1+tir)**dias_d8 + d9*(1+tir)**dias_d9 +
                                  d10*(1+tir)**dias_d10 + d11*(1+tir)**dias_d11 + d12*(1+tir)**dias_d12 +
                                  d13*(1+tir)**dias_d13 + d14*(1+tir)**dias_d14 + d15*(1+tir)**dias_d15 +
                                  d16*(1+tir)**dias_d16 + d17*(1+tir)**dias_d17 + d18*(1+tir)**dias_d18 +
                                  d19*(1+tir)**dias_d19 + d20*(1+tir)**dias_d20 + d21*(1+tir)**dias_d21 +
                                  d22*(1+tir)**dias_d22 + d23*(1+tir)**dias_d23 + d24*(1+tir)**dias_d24 +
                                  d25*(1+tir)**dias_d25 + d26*(1+tir)**dias_d26 + d27*(1+tir)**dias_d27 +
                                  d28*(1+tir)**dias_d28 + d29*(1+tir)**dias_d29 + d30*(1+tir)**dias_d30 +
                                  d31*(1+tir)**dias_d31 + d32*(1+tir)**dias_d32 + d33*(1+tir)**dias_d33 +
                                  d34*(1+tir)**dias_d34 + d35*(1+tir)**dias_d35 + d36*(1+tir)**dias_d36 +
                                  d37*(1+tir)**dias_d37 + d38*(1+tir)**dias_d38 + d39*(1+tir)**dias_d39 +
                                  d40*(1+tir)**dias_d40 + d41*(1+tir)**dias_d41 + d42*(1+tir)**dias_d42 +
                                  d43*(1+tir)**dias_d43 + d44*(1+tir)**dias_d44 + d45*(1+tir)**dias_d45 +
                                  d46*(1+tir)**dias_d46 + d47*(1+tir)**dias_d47 + d48*(1+tir)**dias_d48 +
                                  d49*(1+tir)**dias_d49 + d50*(1+tir)**dias_d50 +  
                               
                                  # DEPOSITOS DE DOLARES DEL CLIENTE
                                  d_usd1*(1+tir)**dias_d_usd1 + d_usd2*(1+tir)**dias_d_usd2 + d_usd3*(1+tir)**dias_d_usd3 +
                                  d_usd4*(1+tir)**dias_d_usd4 + d_usd5*(1+tir)**dias_d_usd5 + d_usd6*(1+tir)**dias_d_usd6 +
                                  d_usd7*(1+tir)**dias_d_usd7 + d_usd8*(1+tir)**dias_d_usd8 + d_usd9*(1+tir)**dias_d_usd9 +
                                  d_usd10*(1+tir)**dias_d_usd10 + d_usd11*(1+tir)**dias_d_usd11 + d_usd12*(1+tir)**dias_d_usd12 +
                                  d_usd13*(1+tir)**dias_d_usd13 + d_usd14*(1+tir)**dias_d_usd14 + d_usd15*(1+tir)**dias_d_usd15 +
                                  d_usd16*(1+tir)**dias_d_usd16 + d_usd17*(1+tir)**dias_d_usd17 + d_usd18*(1+tir)**dias_d_usd18 +
                                  d_usd19*(1+tir)**dias_d_usd19 + d_usd20*(1+tir)**dias_d_usd20 + d_usd21*(1+tir)**dias_d_usd21 +
                                  d_usd22*(1+tir)**dias_d_usd22 + d_usd23*(1+tir)**dias_d_usd23 + d_usd24*(1+tir)**dias_d_usd24 +
                                  d_usd25*(1+tir)**dias_d_usd25 + d_usd26*(1+tir)**dias_d_usd26 + d_usd27*(1+tir)**dias_d_usd27 +
                                  d_usd28*(1+tir)**dias_d_usd28 + d_usd29*(1+tir)**dias_d_usd29 + d_usd30*(1+tir)**dias_d_usd30 +
                                  d_usd31*(1+tir)**dias_d_usd31 + d_usd32*(1+tir)**dias_d_usd32 + d_usd33*(1+tir)**dias_d_usd33 +
                                  d_usd34*(1+tir)**dias_d_usd34 + d_usd35*(1+tir)**dias_d_usd35 + d_usd36*(1+tir)**dias_d_usd36 +
                                  d_usd37*(1+tir)**dias_d_usd37 + d_usd38*(1+tir)**dias_d_usd38 + d_usd39*(1+tir)**dias_d_usd39 +
                                  d_usd40*(1+tir)**dias_d_usd40 + d_usd41*(1+tir)**dias_d_usd41 + d_usd42*(1+tir)**dias_d_usd42 +
                                  d_usd43*(1+tir)**dias_d_usd43 + d_usd44*(1+tir)**dias_d_usd44 + d_usd45*(1+tir)**dias_d_usd45 +
                                  d_usd46*(1+tir)**dias_d_usd46 + d_usd47*(1+tir)**dias_d_usd47 + d_usd48*(1+tir)**dias_d_usd48 +
                                  d_usd49*(1+tir)**dias_d_usd49 + d_usd50*(1+tir)**dias_d_usd50  -                                        
                                 
                                  # RETIROS DE PESOS DEL CLIENTE
                                  r1*(1+tir)**dias_r1 - r2*(1+tir)**dias_r2 - r3*(1+tir)**dias_r3 -
                                  r4*(1+tir)**dias_r4 - r5*(1+tir)**dias_r5 - r6*(1+tir)**dias_r6 -
                                  r7*(1+tir)**dias_r7 - r8*(1+tir)**dias_r8 - r9*(1+tir)**dias_r9 -
                                  r10*(1+tir)**dias_r10 - r11*(1+tir)**dias_r11 - r12*(1+tir)**dias_r12 -
                                  r13*(1+tir)**dias_r13 - r14*(1+tir)**dias_r14 - r15*(1+tir)**dias_r15 -
                                  r16*(1+tir)**dias_r16 - r17*(1+tir)**dias_r17 - r18*(1+tir)**dias_r18 -
                                  r19*(1+tir)**dias_r19 - r20*(1+tir)**dias_r20 - r21*(1+tir)**dias_r21 -
                                  r22*(1+tir)**dias_r22 - r23*(1+tir)**dias_r23 - r24*(1+tir)**dias_r24 -
                                  r25*(1+tir)**dias_r25 - r26*(1+tir)**dias_r26 - r27*(1+tir)**dias_r27 -
                                  r28*(1+tir)**dias_r28 - r29*(1+tir)**dias_r29 - r30*(1+tir)**dias_r30 -
                                  r31*(1+tir)**dias_r31 - r32*(1+tir)**dias_r32 - r33*(1+tir)**dias_r33 -
                                  r34*(1+tir)**dias_r34 - r35*(1+tir)**dias_r35 - r36*(1+tir)**dias_r36 -
                                  r37*(1+tir)**dias_r37 - r38*(1+tir)**dias_r38 - r39*(1+tir)**dias_r39 -
                                  r40*(1+tir)**dias_r40 - r41*(1+tir)**dias_r41 - r42*(1+tir)**dias_r42 -
                                  r43*(1+tir)**dias_r43 - r44*(1+tir)**dias_r44 - r45*(1+tir)**dias_r45 -
                                  r46*(1+tir)**dias_r46 - r47*(1+tir)**dias_r47 - r48*(1+tir)**dias_r48 -
                                  r49*(1+tir)**dias_r49 - r50*(1+tir)**dias_r50 -
                                  
                                  # RETIROS DE DOLARES (POR DOLAR MEP)
                                  dm1*(1+tir)**dias_dm1 - dm2*(1+tir)**dias_dm2 - dm3*(1+tir)**dias_dm3 -
                                  dm4*(1+tir)**dias_dm4 - dm5*(1+tir)**dias_dm5 - dm6*(1+tir)**dias_dm6 -
                                  dm7*(1+tir)**dias_dm7 - dm8*(1+tir)**dias_dm8 - dm9*(1+tir)**dias_dm9 -
                                  dm10*(1+tir)**dias_dm10 - dm11*(1+tir)**dias_dm11 - dm12*(1+tir)**dias_dm12 -
                                  dm13*(1+tir)**dias_dm13 - dm14*(1+tir)**dias_dm14 - dm15*(1+tir)**dias_dm15 -
                                  dm16*(1+tir)**dias_dm16 - dm17*(1+tir)**dias_dm17 - dm18*(1+tir)**dias_dm18 -
                                  dm19*(1+tir)**dias_dm19 - dm20*(1+tir)**dias_dm20 - dm21*(1+tir)**dias_dm21 -
                                  dm22*(1+tir)**dias_dm22 - dm23*(1+tir)**dias_dm23 - dm24*(1+tir)**dias_dm24 -
                                  dm25*(1+tir)**dias_dm25 - dm26*(1+tir)**dias_dm26 - dm27*(1+tir)**dias_dm27 -
                                  dm28*(1+tir)**dias_dm28 - dm29*(1+tir)**dias_dm29 - dm30*(1+tir)**dias_dm30 -
                                  dm31*(1+tir)**dias_dm31 - dm32*(1+tir)**dias_dm32 - dm33*(1+tir)**dias_dm33 -
                                  dm34*(1+tir)**dias_dm34 - dm35*(1+tir)**dias_dm35 - dm36*(1+tir)**dias_dm36 -
                                  dm37*(1+tir)**dias_dm37 - dm38*(1+tir)**dias_dm38 - dm39*(1+tir)**dias_dm39 -
                                  dm40*(1+tir)**dias_dm40 - dm41*(1+tir)**dias_dm41 - dm42*(1+tir)**dias_dm42 -
                                  dm43*(1+tir)**dias_dm43 - dm44*(1+tir)**dias_dm44 - dm45*(1+tir)**dias_dm45 -
                                  dm46*(1+tir)**dias_dm46 - dm47*(1+tir)**dias_dm47 - dm48*(1+tir)**dias_dm48 -
                                  dm49*(1+tir)**dias_dm49 - dm50*(1+tir)**dias_dm50 
                                                      
                                  )
                
                lista_tir_b.append(tir)
                lista_error_b.append(error)
                
            listado_b=pd.DataFrame()
            listado_b['error']=lista_error_b
            listado_b['tir']=lista_tir_b
            listado_b['error_abs']=listado_b['error'].abs()
            listado_b.sort_values(by='error_abs',inplace=True)
            listado_b.drop(axis=1,columns='error_abs',inplace=True)
            
            
            # Ahora corregimos este listado para evitar problemas del tipo "controversia del
            # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
            # cobran honorarios. El asunto se resuelve en tres pasos:
            # PRIMERO. Slicing 10 primeros con errores mas pequeños
            listado_b=listado_b.iloc[:10,:]
            
            
            # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
            listado_b.sort_values(by='tir',inplace=True)
            listado_b=listado_b.iloc[:5,:]
            
            
            # TERCERO. Ordenamos de menor a mayor por error absoluto
            listado_b['error_abs']=listado_b['error'].abs()
            listado_b.sort_values(by='error_abs',inplace=True)
            listado_b.drop(axis=1,columns='error_abs',inplace=True)
            
            
            
            
            # ----------------------------- NOVENA PARTE ----------------------------------
            # Se calcula la TIR neta de la cartera para el trimestre
            # -----------------------------------------------------------------------------
            lista_error_n=[]
            lista_tir_n=[] # Esta en porcentaje
            
            for tir in np.arange(-1,1,puntos_basicos/10000):
                
                                # FLUJO DE FONDOS PARA LA OBTENCION DEL RENDIMIENTO NETO
                error = ( valor_cierre - honorario_cierre ) - (
                                
                                    # SALDO AL INICIO DEL TRIMESTRE
                                    valor_inicial*(1+tir)**plazo_inicial +
                                  
                                    # DEPOSITOS DE PESOS DEL CLIENTE
                                    d1*(1+tir)**dias_d1 + d2*(1+tir)**dias_d2 + d3*(1+tir)**dias_d3 +
                                    d4*(1+tir)**dias_d4 + d5*(1+tir)**dias_d5 + d6*(1+tir)**dias_d6 +
                                    d7*(1+tir)**dias_d7 + d8*(1+tir)**dias_d8 + d9*(1+tir)**dias_d9 +
                                    d10*(1+tir)**dias_d10 + d11*(1+tir)**dias_d11 + d12*(1+tir)**dias_d12 +
                                    d13*(1+tir)**dias_d13 + d14*(1+tir)**dias_d14 + d15*(1+tir)**dias_d15 +
                                    d16*(1+tir)**dias_d16 + d17*(1+tir)**dias_d17 + d18*(1+tir)**dias_d18 +
                                    d19*(1+tir)**dias_d19 + d20*(1+tir)**dias_d20 + d21*(1+tir)**dias_d21 +
                                    d22*(1+tir)**dias_d22 + d23*(1+tir)**dias_d23 + d24*(1+tir)**dias_d24 +
                                    d25*(1+tir)**dias_d25 + d26*(1+tir)**dias_d26 + d27*(1+tir)**dias_d27 +
                                    d28*(1+tir)**dias_d28 + d29*(1+tir)**dias_d29 + d30*(1+tir)**dias_d30 +
                                    d31*(1+tir)**dias_d31 + d32*(1+tir)**dias_d32 + d33*(1+tir)**dias_d33 +
                                    d34*(1+tir)**dias_d34 + d35*(1+tir)**dias_d35 + d36*(1+tir)**dias_d36 +
                                    d37*(1+tir)**dias_d37 + d38*(1+tir)**dias_d38 + d39*(1+tir)**dias_d39 +
                                    d40*(1+tir)**dias_d40 + d41*(1+tir)**dias_d41 + d42*(1+tir)**dias_d42 +
                                    d43*(1+tir)**dias_d43 + d44*(1+tir)**dias_d44 + d45*(1+tir)**dias_d45 +
                                    d46*(1+tir)**dias_d46 + d47*(1+tir)**dias_d47 + d48*(1+tir)**dias_d48 +
                                    d49*(1+tir)**dias_d49 + d50*(1+tir)**dias_d50 +  
                                
                                    # DEPOSITOS DE DOLARES DEL CLIENTE
                                    d_usd1*(1+tir)**dias_d_usd1 + d_usd2*(1+tir)**dias_d_usd2 + d_usd3*(1+tir)**dias_d_usd3 +
                                    d_usd4*(1+tir)**dias_d_usd4 + d_usd5*(1+tir)**dias_d_usd5 + d_usd6*(1+tir)**dias_d_usd6 +
                                    d_usd7*(1+tir)**dias_d_usd7 + d_usd8*(1+tir)**dias_d_usd8 + d_usd9*(1+tir)**dias_d_usd9 +
                                    d_usd10*(1+tir)**dias_d_usd10 + d_usd11*(1+tir)**dias_d_usd11 + d_usd12*(1+tir)**dias_d_usd12 +
                                    d_usd13*(1+tir)**dias_d_usd13 + d_usd14*(1+tir)**dias_d_usd14 + d_usd15*(1+tir)**dias_d_usd15 +
                                    d_usd16*(1+tir)**dias_d_usd16 + d_usd17*(1+tir)**dias_d_usd17 + d_usd18*(1+tir)**dias_d_usd18 +
                                    d_usd19*(1+tir)**dias_d_usd19 + d_usd20*(1+tir)**dias_d_usd20 + d_usd21*(1+tir)**dias_d_usd21 +
                                    d_usd22*(1+tir)**dias_d_usd22 + d_usd23*(1+tir)**dias_d_usd23 + d_usd24*(1+tir)**dias_d_usd24 +
                                    d_usd25*(1+tir)**dias_d_usd25 + d_usd26*(1+tir)**dias_d_usd26 + d_usd27*(1+tir)**dias_d_usd27 +
                                    d_usd28*(1+tir)**dias_d_usd28 + d_usd29*(1+tir)**dias_d_usd29 + d_usd30*(1+tir)**dias_d_usd30 +
                                    d_usd31*(1+tir)**dias_d_usd31 + d_usd32*(1+tir)**dias_d_usd32 + d_usd33*(1+tir)**dias_d_usd33 +
                                    d_usd34*(1+tir)**dias_d_usd34 + d_usd35*(1+tir)**dias_d_usd35 + d_usd36*(1+tir)**dias_d_usd36 +
                                    d_usd37*(1+tir)**dias_d_usd37 + d_usd38*(1+tir)**dias_d_usd38 + d_usd39*(1+tir)**dias_d_usd39 +
                                    d_usd40*(1+tir)**dias_d_usd40 + d_usd41*(1+tir)**dias_d_usd41 + d_usd42*(1+tir)**dias_d_usd42 +
                                    d_usd43*(1+tir)**dias_d_usd43 + d_usd44*(1+tir)**dias_d_usd44 + d_usd45*(1+tir)**dias_d_usd45 +
                                    d_usd46*(1+tir)**dias_d_usd46 + d_usd47*(1+tir)**dias_d_usd47 + d_usd48*(1+tir)**dias_d_usd48 +
                                    d_usd49*(1+tir)**dias_d_usd49 + d_usd50*(1+tir)**dias_d_usd50 -  
                                  
                                    # RETIROS DE PESOS DEL CLIENTE
                                    r1*(1+tir)**dias_r1 - r2*(1+tir)**dias_r2 - r3*(1+tir)**dias_r3 -
                                    r4*(1+tir)**dias_r4 - r5*(1+tir)**dias_r5 - r6*(1+tir)**dias_r6 -
                                    r7*(1+tir)**dias_r7 - r8*(1+tir)**dias_r8 - r9*(1+tir)**dias_r9 -
                                    r10*(1+tir)**dias_r10 - r11*(1+tir)**dias_r11 - r12*(1+tir)**dias_r12 -
                                    r13*(1+tir)**dias_r13 - r14*(1+tir)**dias_r14 - r15*(1+tir)**dias_r15 -
                                    r16*(1+tir)**dias_r16 - r17*(1+tir)**dias_r17 - r18*(1+tir)**dias_r18 -
                                    r19*(1+tir)**dias_r19 - r20*(1+tir)**dias_r20 - r21*(1+tir)**dias_r21 -
                                    r22*(1+tir)**dias_r22 - r23*(1+tir)**dias_r23 - r24*(1+tir)**dias_r24 -
                                    r25*(1+tir)**dias_r25 - r26*(1+tir)**dias_r26 - r27*(1+tir)**dias_r27 -
                                    r28*(1+tir)**dias_r28 - r29*(1+tir)**dias_r29 - r30*(1+tir)**dias_r30 -
                                    r31*(1+tir)**dias_r31 - r32*(1+tir)**dias_r32 - r33*(1+tir)**dias_r33 -
                                    r34*(1+tir)**dias_r34 - r35*(1+tir)**dias_r35 - r36*(1+tir)**dias_r36 -
                                    r37*(1+tir)**dias_r37 - r38*(1+tir)**dias_r38 - r39*(1+tir)**dias_r39 -
                                    r40*(1+tir)**dias_r40 - r41*(1+tir)**dias_r41 - r42*(1+tir)**dias_r42 -
                                    r43*(1+tir)**dias_r43 - r44*(1+tir)**dias_r44 - r45*(1+tir)**dias_r45 -
                                    r46*(1+tir)**dias_r46 - r47*(1+tir)**dias_r47 - r48*(1+tir)**dias_r48 -
                                    r49*(1+tir)**dias_r49 - r50*(1+tir)**dias_r50 -
                                   
                                    # RETIROS DE DOLARES (POR DOLAR MEP)
                                    dm1*(1+tir)**dias_dm1 - dm2*(1+tir)**dias_dm2 - dm3*(1+tir)**dias_dm3 -
                                    dm4*(1+tir)**dias_dm4 - dm5*(1+tir)**dias_dm5 - dm6*(1+tir)**dias_dm6 -
                                    dm7*(1+tir)**dias_dm7 - dm8*(1+tir)**dias_dm8 - dm9*(1+tir)**dias_dm9 -
                                    dm10*(1+tir)**dias_dm10 - dm11*(1+tir)**dias_dm11 - dm12*(1+tir)**dias_dm12 -
                                    dm13*(1+tir)**dias_dm13 - dm14*(1+tir)**dias_dm14 - dm15*(1+tir)**dias_dm15 -
                                    dm16*(1+tir)**dias_dm16 - dm17*(1+tir)**dias_dm17 - dm18*(1+tir)**dias_dm18 -
                                    dm19*(1+tir)**dias_dm19 - dm20*(1+tir)**dias_dm20 - dm21*(1+tir)**dias_dm21 -
                                    dm22*(1+tir)**dias_dm22 - dm23*(1+tir)**dias_dm23 - dm24*(1+tir)**dias_dm24 -
                                    dm25*(1+tir)**dias_dm25 - dm26*(1+tir)**dias_dm26 - dm27*(1+tir)**dias_dm27 -
                                    dm28*(1+tir)**dias_dm28 - dm29*(1+tir)**dias_dm29 - dm30*(1+tir)**dias_dm30 -
                                    dm31*(1+tir)**dias_dm31 - dm32*(1+tir)**dias_dm32 - dm33*(1+tir)**dias_dm33 -
                                    dm34*(1+tir)**dias_dm34 - dm35*(1+tir)**dias_dm35 - dm36*(1+tir)**dias_dm36 -
                                    dm37*(1+tir)**dias_dm37 - dm38*(1+tir)**dias_dm38 - dm39*(1+tir)**dias_dm39 -
                                    dm40*(1+tir)**dias_dm40 - dm41*(1+tir)**dias_dm41 - dm42*(1+tir)**dias_dm42 -
                                    dm43*(1+tir)**dias_dm43 - dm44*(1+tir)**dias_dm44 - dm45*(1+tir)**dias_dm45 -
                                    dm46*(1+tir)**dias_dm46 - dm47*(1+tir)**dias_dm47 - dm48*(1+tir)**dias_dm48 -
                                    dm49*(1+tir)**dias_dm49 - dm50*(1+tir)**dias_dm50 
                                                          
                                    )
                
                lista_tir_n.append(tir)
                lista_error_n.append(error)
            
            listado_n=pd.DataFrame()
            listado_n['error']=lista_error_n
            listado_n['tir']=lista_tir_n
            listado_n['error_abs']=listado_n['error'].abs()
            listado_n.sort_values(by='error_abs',inplace=True)
            listado_n.drop(axis=1,columns='error_abs',inplace=True)
            
            
            # Ahora corregimos este listado para evitar problemas del tipo "controversia del
            # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
            # cobran honorarios. El asunto se resuelve en tres pasos:
            # PRIMERO. Slicing 10 primeros con errores mas pequeños
            listado_n=listado_n.iloc[:10,:]
            
            
            # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
            listado_n.sort_values(by='tir',inplace=True)
            listado_n=listado_n.iloc[:5,:]
            
            
            # TERCERO. Ordenamos de menor a mayor por error absoluto
            listado_n['error_abs']=listado_n['error'].abs()
            listado_n.sort_values(by='error_abs',inplace=True)
            listado_n.drop(axis=1,columns='error_abs',inplace=True)
            
            
            
            
            # ----------------------------- DECIMA PARTE ----------------------------------
            # Se crea un diccionario que contiene el resultado
            # -----------------------------------------------------------------------------
            # Resultado
            rendimientos={'Rend período':[(1+listado_b.iloc[0,1])**dias-1, (1+listado_n.iloc[0,1])**dias-1],
                          'Fecha inicial':[f'{fecha_inicial}','-'],
                          'Fecha final':[f'{fecha_cierre}','-'],
                          'Valor inicial':[f'{valor_inicial}','-'],
                          'Valor final':[f'{valor_cierre}','-'],
                          'Honorarios':[f'{honorario_cierre}','-']}
            
            rendimiento=pd.DataFrame(rendimientos).T
            rendimiento=rendimiento.rename(columns={0:'Rendimiento bruto',1:'Rendimiento neto'})
        
        else:
            rendimiento = datos_cliente

    except:
        rendimiento = 'Introduzca un usuario válido: 1, 2, 3, 4, o 5 (intente con cualquiera)'


    return rendimiento






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def concatenacion_movimientos_bull(moneda, alyc = '', dni = 0, nombre_cliente = '', 
                                   numero_interno = 0, usuario = 1):
    """  
    ¿Qué hace la funcion? 
    -----------
    La funcion concatena los movimientos de un periodo (actual) con los movimientos 
    de otro periodo (viejo) para formar un unico dataframe de movimientos. Esta
    concatenacion puede darse entre muchos archivos de movimientos.     
    
    Parametros
    ----------     
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    dni : tipo integer.
    
        DESCRIPCION
        Es el dni del cliente.
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    moneda : tipo integer
    
        DESCRIPCION
        Indica el tipo de moneda utilizada para realizar las operaciones: i) Pesos,
        ii) Dolares, o iii) Dolares cable. No importa si estas opciones se escriben o 
        no con mayusculas. 
        
    Resultado
    -------
    archivo : tipo DataFrame.
       
        DESCRIPCION.
        Se obtienen los movimientos/operaciones realizadas en la comitente del 
        cliente en cuestion, y para un periodo determinado de tiempo.

    """
   
    # moneda = 'PESOS' # Para BULLMARKET: Pueden ser PESOS, DOLARES, y DOLARES CABLE
    moneda = moneda.upper()

     
    # ----------------------------------------------------------------------------
    if usuario == 1: 
        sub_directorio = 'Y'
        auxiliar = '--'
    elif usuario == 2:
        sub_directorio = 'YY'
        auxiliar = '--'
    elif usuario == 3:
        sub_directorio = 'YYY'
        auxiliar = ''
    elif usuario == 4:
        sub_directorio = 'Y_Y'
        auxiliar = ''
    elif usuario == 5:
        sub_directorio = 'YY_YY'
        auxiliar = ''
    elif usuario == 6:
        sub_directorio = 'YYY_YYY'
        auxiliar = ''

    directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 

    import pandas as pd
    import sys
    sys.path.append(f'{directorio_funciones}')
    import dp_funciones_c as fc
    import os

    # -----------------------------------------------------------------------------           
    # Sub Parametros
    datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                numero_interno = numero_interno, dni = dni,
                                usuario = usuario)

    try:
        nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
        numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
        fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']

    except:
        nombre_cliente = ''
        numero_cliente = 0
        fecha_movimientos = ''
        

    # Se definen los parametros para entrar en las cuentas donde estan los movimientos
    directorio_origen = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})'
    directorio_origen2 = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})\Movimientos antiguos'

    movimiento = f'Cuenta Corriente {moneda} {fecha_movimientos}' 


    # Se importan los archivos actuales e historicos de movimiento en pesos
    # -----------------------------------------------------------------------------
    # Importamos el archivo en pesos actual.
    try:   
        archivo_actual = pd.read_excel(f'{directorio_origen}\{movimiento}.xlsx')
        archivo_actual.set_index("Liquida", inplace=True)   

    except:
        archivo_actual = pd.DataFrame()

    # ----------------------------------------------------------------------------
    # Importamos los archivos de pesos historicos. Recorre todos los archivos y 
    # directorios dentro del directorio.
    try:
        nombre_archivos = []
        
        for nombre_archivo in os.listdir(directorio_origen2):
            ruta_archivo = os.path.join(directorio_origen2, nombre_archivo)
            
            # Verifica si es un archivo (y no un directorio)
            if os.path.isfile(ruta_archivo):
                nombre_archivos.append(nombre_archivo)
                
        # Nos quedamos solo con el nombre de los archivos .xlsx
        nombre_archivos2 = []
        for i in nombre_archivos:
            if i[17:-14] == moneda:
                nombre_archivos2.append(i[:-5])
                    
    except:
        nombre_archivos2 = []
        

    # Se importan estos archivos
    archivo_viejo = pd.DataFrame()
    archivo_antiguo = pd.DataFrame()

    for i in nombre_archivos2:
        try:   
            # Se importa el archivo antiguo
            archivo_antiguo = pd.read_excel(f'{directorio_origen2}\{i}.xlsx')
            archivo_antiguo.set_index("Liquida", inplace=True)   
            
            # Se concatenan el archivo antiguo con sus los otros archivos antiguos
            archivo_viejo = pd.concat([archivo_viejo,archivo_antiguo],ignore_index=False)
            
        except:
            archivo_viejo = pd.DataFrame()
           
    # ----------------------------------------------------------------------------
    # Se concatenan los movimientos viejos y actuales. 
    archivo = pd.DataFrame()

    archivo = pd.concat([archivo_viejo,archivo_actual],ignore_index=False)
    
    
    return archivo






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def concatenacion_movimientos_ieb(moneda, alyc = '', dni = 0, nombre_cliente = '', 
                                  numero_interno = 0, usuario = 1):
    """  
    ¿Qué hace la funcion? 
    -----------
    La funcion concatena los movimientos de un periodo (actual) con los movimientos 
    de otro periodo (viejo) para formar un unico dataframe de movimientos. Esta
    concatenacion puede darse entre muchos archivos de movimientos.     
    
    Parametros
    ----------     
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    dni : tipo integer.
    
        DESCRIPCION
        Es el dni del cliente.
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    moneda : tipo integer
    
        DESCRIPCION
        Indica el tipo de moneda utilizada para realizar las operaciones: i) Pesos,
        ii) Dolares, o iii) Dolares cable. No importa si estas opciones se escriben o 
        no con mayusculas. 
        
    Resultado
    -------
    archivo : tipo DataFrame.
       
        DESCRIPCION.
        Se obtienen los movimientos/operaciones realizadas en la comitente del 
        cliente en cuestion, y para un periodo determinado de tiempo.

    """
    

    # moneda = 3 # Para IEB: Puede ser 1 (PESOS), 2 (DOLARES), y 3 (DOLARES CABLE)

     
    # ----------------------------------------------------------------------------
    if usuario == 1: 
        sub_directorio = 'Y'
        auxiliar = '--'
    elif usuario == 2:
        sub_directorio = 'YY'
        auxiliar = '--'
    elif usuario == 3:
        sub_directorio = 'YYY'
        auxiliar = ''
    elif usuario == 4:
        sub_directorio = 'Y_Y'
        auxiliar = ''
    elif usuario == 5:
        sub_directorio = 'YY_YY'
        auxiliar = ''
    elif usuario == 6:
        sub_directorio = 'YYY_YYY'
        auxiliar = ''
        
    directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 

    import pandas as pd
    import sys
    sys.path.append(f'{directorio_funciones}')
    import dp_funciones_c as fc
    import os
    from datetime import datetime as dt

    # -----------------------------------------------------------------------------           
    # Sub Parametros
    datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                numero_interno = numero_interno, dni = dni,
                                usuario = usuario)

    try:
        nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
        numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
        fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']

    except:
        nombre_cliente = ''
        numero_cliente = 0
        fecha_movimientos = ''
        

    # Se definen los parametros para entrar en las cuentas donde estan los movimientos
    directorio_origen = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})'
    directorio_origen2 = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})\Movimientos antiguos'

    if moneda == 1:
        movimiento = 'Movimientos de Pesos' 
        
    elif moneda == 2: 
        movimiento = 'Movimientos de Moneda Extranjera'
        
    elif moneda == 3:
        movimiento = 'Movimientos Dividendos y Rentas Cobradas'
        
    fecha_control = '2023-12-31'
    fecha_control = dt.strptime(fecha_control,'%Y-%m-%d')


    if (moneda == 1) or (moneda == 2):
        # Se importan los archivos actuales e historicos de movimiento en pesos
        # -----------------------------------------------------------------------------
        # Importamos el archivo en pesos actual.
        try:   
            # Se lo importa y se lo limpia.    
            archivo_actual = pd.read_excel(f'{directorio_origen}\{movimiento}.xlsx',skiprows=7)
            columnas = archivo_actual.columns[1:]
            archivo_actual = pd.read_excel(f'{directorio_origen}\{movimiento}.xlsx',skiprows=7,
                                        usecols=columnas)
            archivo_actual.set_index("Liquida", inplace=True)  
            
            for i in archivo_actual.index:
                if type(i)==type('A'):
                    archivo_actual.drop(index=i,inplace=True)
            
            archivo_actual['columnita']=0
            for i in archivo_actual.index:
                if type(i)==type(fecha_control):
                    archivo_actual.loc[i,'columnita']=1
                else:
                    archivo_actual.loc[i,'columnita']=2
                    
            archivo_actual.reset_index(inplace=True)
            archivo_actual.set_index('columnita',inplace=True)
            archivo_actual = archivo_actual.loc[archivo_actual.index==1].copy()
            archivo_actual.reset_index(inplace=True)
            archivo_actual.set_index("Liquida", inplace=True) 
            archivo_actual.drop('columnita',axis=1,inplace=True)
        
        except:
            archivo_actual = pd.DataFrame()
            
            
        # ----------------------------------------------------------------------------
        # Importamos los archivos historicos. Recorre todos los archivos y 
        # directorios dentro del directorio.
        try:
            nombre_archivos = []
            
            for nombre_archivo in os.listdir(directorio_origen2):
                ruta_archivo = os.path.join(directorio_origen2, nombre_archivo)
                
                # Verifica si es un archivo (y no un directorio)
                if os.path.isfile(ruta_archivo):
                    nombre_archivos.append(nombre_archivo)
                    
            # Nos quedamos solo con el nombre de los archivos .xlsx
            nombre_archivos2 = []
            for i in nombre_archivos:
                if i[:-14] == movimiento:
                    nombre_archivos2.append(i[:-5])
                        
        except:
            nombre_archivos2 = []
          
        
        # Se importan estos archivos
        archivo_viejo = pd.DataFrame()
        archivo_antiguo = pd.DataFrame()
        
        for i in nombre_archivos2:
            try:   
                # Se lo importa y se lo limpia.    
                archivo_antiguo = pd.read_excel(f'{directorio_origen2}\{i}.xlsx',skiprows=7)
                columnas = archivo_antiguo.columns[1:]
                archivo_antiguo = pd.read_excel(f'{directorio_origen2}\{i}.xlsx',skiprows=7,
                                            usecols=columnas)
                archivo_antiguo.set_index("Liquida", inplace=True)  
                
                for i in archivo_antiguo.index:
                    if type(i)==type('A'):
                        archivo_antiguo.drop(index=i,inplace=True)
                
                archivo_antiguo['columnita']=0
                for i in archivo_antiguo.index:
                    if type(i)==type(fecha_control):
                        archivo_antiguo.loc[i,'columnita']=1
                    else:
                        archivo_antiguo.loc[i,'columnita']=2
                        
                archivo_antiguo.reset_index(inplace=True)
                archivo_antiguo.set_index('columnita',inplace=True)
                archivo_antiguo = archivo_antiguo.loc[archivo_antiguo.index==1].copy()
                archivo_antiguo.reset_index(inplace=True)
                archivo_antiguo.set_index("Liquida", inplace=True) 
                archivo_antiguo.drop('columnita',axis=1,inplace=True)
                
                # Se concatenan el archivo antiguo con sus los otros archivos antiguos
                archivo_viejo = pd.concat([archivo_antiguo,archivo_viejo],ignore_index=False)
                
            except:
                archivo_viejo = pd.DataFrame()
        
        
        # ----------------------------------------------------------------------------
        # Se concatenan los movimientos viejos y actuales. 
        archivo = pd.DataFrame()
        
        archivo = pd.concat([archivo_actual,archivo_viejo],ignore_index=False)


    elif moneda == 3:
        # Importamos el archivo en dolares cable. El 'Try - except' es para contemplar
        # la situacion donde este archivo no existe. 
        columnas2=['Fecha','Cpbt','Número','Especie','Moneda','Portafolio','Divi/renta','Gastos']

        try:
            archivo_actual = pd.read_excel(f'{directorio_origen}\{movimiento}.xlsx',
                                            skiprows=7,usecols=columnas2)
            archivo_actual.set_index("Fecha", inplace=True)    
            
            # Se toma la mascara de acuerdo a la moneda 'DOLARUSA'
            archivo_actual = archivo_actual.loc[archivo_actual.Moneda=='DOLARUSA'].copy()
            
        except:
            archivo_actual = pd.DataFrame()
            
        
        # ----------------------------------------------------------------------------
        # Importamos los archivos historicos. Recorre todos los archivos y 
        # directorios dentro del directorio.
        try:
            nombre_archivos = []
            
            for nombre_archivo in os.listdir(directorio_origen2):
                ruta_archivo = os.path.join(directorio_origen2, nombre_archivo)
                
                # Verifica si es un archivo (y no un directorio)
                if os.path.isfile(ruta_archivo):
                    nombre_archivos.append(nombre_archivo)
                    
            # Nos quedamos solo con el nombre de los archivos .xlsx
            nombre_archivos2 = []
            for i in nombre_archivos:
                if i[:-14] == movimiento:
                    nombre_archivos2.append(i[:-5])
                        
        except:
            nombre_archivos2 = []
               
        # Se importan estos archivos
        archivo_viejo = pd.DataFrame()
        archivo_antiguo = pd.DataFrame()
        
        for i in nombre_archivos2:
            try:   
                archivo_antiguo = pd.read_excel(f'{directorio_origen2}\{i}.xlsx',
                                                skiprows=7,usecols=columnas2)
                archivo_antiguo.set_index("Fecha", inplace=True)    
                
                # Se toma la mascara de acuerdo a la moneda 'DOLARUSA'
                archivo_antiguo = archivo_antiguo.loc[archivo_antiguo.Moneda=='DOLARUSA'].copy()
                           
                # Se concatenan el archivo antiguo con sus los otros archivos antiguos
                archivo_viejo = pd.concat([archivo_viejo,archivo_antiguo],ignore_index=False)
                
            except:
                archivo_viejo = pd.DataFrame()

        # ----------------------------------------------------------------------------
        # Se concatenan los movimientos viejos y actuales. 
        archivo = pd.DataFrame()
        
        archivo = pd.concat([archivo_viejo,archivo_actual],ignore_index=False)



    else: 
        archivo = 'No se especifica correctamente el parametro -moneda (1, 2, o 3)-'
    
    
    
    return archivo






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def concatenacion_movimientos_bal(alyc = '', dni = 0, nombre_cliente = '', 
                                  numero_interno = 0, usuario = 1):
    """  
    ¿Qué hace la funcion? 
    -----------
    La funcion concatena los movimientos de un periodo (actual) con los movimientos 
    de otro periodo (viejo) para formar un unico dataframe de movimientos. Esta
    concatenacion puede darse entre muchos archivos de movimientos.     
    
    Parametros
    ----------     
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    dni : tipo integer.
    
        DESCRIPCION
        Es el dni del cliente.
        Valor por defecto: 0.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    Resultado
    -------
    archivo : tipo DataFrame.
       
        DESCRIPCION.
        Se obtienen los movimientos/operaciones realizadas en la comitente del 
        cliente en cuestion, y para un periodo determinado de tiempo.

    """


    # ----------------------------------------------------------------------------
    if usuario == 1: 
        sub_directorio = 'Y'
        auxiliar = '--'
    elif usuario == 2:
        sub_directorio = 'YY'
        auxiliar = '--'
    elif usuario == 3:
        sub_directorio = 'YYY'
        auxiliar = ''
    elif usuario == 4:
        sub_directorio = 'Y_Y'
        auxiliar = ''
    elif usuario == 5:
        sub_directorio = 'YY_YY'
        auxiliar = ''
    elif usuario == 6:
        sub_directorio = 'YYY_YYY'
        auxiliar = ''

    directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 

    import pandas as pd
    import sys
    sys.path.append(f'{directorio_funciones}')
    import dp_funciones_c as fc
    import os
    from datetime import datetime as dt
    from unidecode import unidecode
    # -----------------------------------------------------------------------------           
    # Sub Parametros
    datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                numero_interno = numero_interno, dni = dni,
                                usuario = usuario)

    try:
        nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
        numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
        fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']

    except:
        nombre_cliente = ''
        numero_cliente = 0
        fecha_movimientos = ''
        

    # Se definen los parametros para entrar en las cuentas donde estan los movimientos
    directorio_origen = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de Balanz\{nombre_cliente} ({numero_cliente})'
    directorio_origen2 = f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de Balanz\{nombre_cliente} ({numero_cliente})\Movimientos antiguos'


    # Se importan los archivos actuales e historicos de movimiento
    # -----------------------------------------------------------------------------
    try:   
        # Se lo importa y se lo limpia.    
        archivo_actual = pd.read_excel(f'{directorio_origen}\Movimientos.xlsx')
        
        # Convertimos las fechas del formato string en formato datetime, y se elimina
        # el acento de la columna 'Moneda'.
        lista = list(archivo_actual.columns)
        for i in range(len(archivo_actual.index)):
            fecha_liq = archivo_actual.loc[i,'Liquidacion']
            archivo_actual.loc[i,'Liquidacion'] = dt.strptime(fecha_liq,'%Y-%m-%d')
            
            fecha_conc = archivo_actual.loc[i,'Concertacion']
            if type(fecha_conc) != type('0'):
                fecha_conc = str(archivo_actual.loc[i,'Concertacion'])[:-9]
                archivo_actual.loc[i,'Concertacion'] = dt.strptime(fecha_conc,'%Y-%m-%d')
                
            elif type(fecha_conc) == type('0'):
                archivo_actual.loc[i,'Concertacion'] = dt.strptime(fecha_conc,'%Y-%m-%d')
                
            for j in range(len(archivo_actual)):
                if (archivo_actual.iloc[j,7] != 'Dólares C.V. 7000') and (
                    archivo_actual.iloc[j,7] != 'Pesos') and (
                    archivo_actual.iloc[j,7] != 'Dolares C.V. 7000'):
                    archivo_actual.iloc[j,7] = 'Pesos'
                    
                else:
                    archivo_actual.iloc[i,lista.index('Moneda')] = unidecode(
                                                    archivo_actual.iloc[i,lista.index('Moneda')])
            
        archivo_actual.set_index("Liquidacion", inplace=True)   
        
    except:
        archivo_actual = pd.DataFrame()
            

    # ----------------------------------------------------------------------------
    # Importamos los archivos historicos. Recorre todos los archivos y 
    # directorios dentro del directorio.
    try:
        nombre_archivos = []
        for nombre_archivo in os.listdir(directorio_origen2):
            ruta_archivo = os.path.join(directorio_origen2, nombre_archivo)
            
            # Verifica si es un archivo (y no un directorio)
            if os.path.isfile(ruta_archivo):
                nombre_archivos.append(nombre_archivo)
                
        # Nos quedamos solo con el nombre de los archivos .xlsx
        nombre_archivos2 = []
        for i in nombre_archivos:
            nombre_archivos2.append(i[:-5])
                    
    except:
        nombre_archivos2 = []

        
    # Se importan estos archivos
    archivo_viejo = pd.DataFrame()
    archivo_antiguo = pd.DataFrame()
       
    for i in nombre_archivos2:
        try:   
            # Se lo importa y se lo limpia.    
            archivo_antiguo = pd.read_excel(f'{directorio_origen2}\{i}.xlsx')
            
            # Convertimos las fechas del formato string en formato datetime, y se elimina
            # el acento de la columna 'Moneda'.
            lista = list(archivo_antiguo.columns)
            for i in range(len(archivo_antiguo.index)):
                fecha_liq = archivo_antiguo.loc[i,'Liquidacion']
                archivo_antiguo.loc[i,'Liquidacion'] = dt.strptime(fecha_liq,'%Y-%m-%d')
                
                fecha_conc = archivo_antiguo.loc[i,'Concertacion']
                if type(fecha_conc) != type('0'):
                    fecha_conc = str(archivo_antiguo.loc[i,'Concertacion'])[:-9]
                    archivo_antiguo.loc[i,'Concertacion'] = dt.strptime(fecha_conc,'%Y-%m-%d')
                    
                elif type(fecha_conc) == type('0'):
                    archivo_antiguo.loc[i,'Concertacion'] = dt.strptime(fecha_conc,'%Y-%m-%d')
                    
                archivo_antiguo.iloc[i,lista.index('Moneda')] = unidecode(
                                                        archivo_antiguo.iloc[i,lista.index('Moneda')])
                
            archivo_antiguo.set_index("Liquidacion", inplace=True)   
            
            # Se concatenan el archivo antiguo con sus los otros archivos antiguos
            archivo_viejo = pd.concat([archivo_antiguo,archivo_viejo],ignore_index=False)
            
        except:
            archivo_viejo = pd.DataFrame()


    # ----------------------------------------------------------------------------
    # Se concatenan los movimientos viejos y actuales. 
    archivo = pd.DataFrame()

    archivo = pd.concat([archivo_actual,archivo_viejo],ignore_index=False)
    
    
    return archivo






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def participacion(fecha_cierre, numero_interno = 0, nombre_cliente = '',
                  alyc = '', dni = 0, usuario = 1):
    """
    ¿Qué hace el código? Permite que se conozca la composición de la cartera de
    un cliente a cierta fecha.

    Parameters
    ----------
    fecha_cierre : string
        DESCRIPTION.
        Con esta se indica el momento de interes. 
        El formato debe ser yyyy-mm-dd, por ejemplo: 2023-11-17.
        
    numero_interno : integer, por defecto es 0.
        DESCRIPTION.
        Es el numero interno que la empresa asigno al cliente.
        
    nombre_cliente : string, por defecto es ''.
        DESCRIPTION. 
        Es el nombre del cliente tal cual aparece en su cuenta comitente. 
        
    alyc : string, por defecto es ''.
        DESCRIPTION. 
        Es el nombre de la alyc donde esta la cuenta comitente. Puede ser Bull,
        Ieb, o Balanz. Este dato es importante, por de este modo el codigo puede
        reconocer al cliente.
        
    dni : integer, por defecto es 0.
        DESCRIPTION. 
        Es el numero de documento del cliente.
        
    tipo_calculo : string, por defecto es 'rendimiento'.
        DESCRIPTION. 
        Puede tomar dos valores, "rendimiento" o "tenencia". El primero calcula
        la cartera desde una perspectiva de operacion concertada, mientras que 
        el segundo lo hace desde una perspectiva de operacion liquidada. 

    Returns
    -------
    cartera : Dataframe
        DESCRIPTION.
        Es la participacion de la cartera, con los tickets, sus cantidades y precios,
        y la liquidez en pesos y en dolares (junto con el dolar mep del momento)

    """
    
    if usuario == 1: 
        sub_directorio = 'Y'
        auxiliar = '--'
    elif usuario == 2:
        sub_directorio = 'YY'
        auxiliar = '--'
    elif usuario == 3:
        sub_directorio = 'YYY'
        auxiliar = ''
    elif usuario == 4:
        sub_directorio = 'Y_Y'
        auxiliar = ''
    elif usuario == 5:
        sub_directorio = 'YY_YY'
        auxiliar = ''
    elif usuario == 6:
        sub_directorio = 'YYY_YYY'
        auxiliar = ''
    
    directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
    
    # -----------------------------------------------------------------------------
    import pandas as pd
    import sys
    sys.path.append(f'{directorio_funciones}')
    import dp_funciones_c as fc
    
    
    alyc = alyc.upper()
    if alyc == 'BULL':
        df = fc.composicion_cartera_bull(fecha_cierre = fecha_cierre, alyc = alyc, 
                                        numero_interno = numero_interno, 
                                        usuario = usuario)
     
        
    elif alyc == 'IEB':
        df = fc.composicion_cartera_ieb(fecha_cierre = fecha_cierre, alyc = alyc, 
                                       numero_interno = numero_interno, 
                                       usuario = usuario)
        
    elif alyc == 'BALANZ':
        df = fc.composicion_cartera_bal(fecha_cierre = fecha_cierre, alyc = alyc, 
                                       numero_interno = numero_interno, 
                                       usuario = usuario)
    
    else: 
        df = 'Introducir nuevamente la ALYC (Bull, Ieb, o Balanz)'
        
    
    
    if type(df) != str(0):
        df[f'Precio al {fecha_cierre}'] = df.iloc[:,1]
        df['monto'] = float(0)
        df['monto'] = df['Cantidad'] * df.iloc[:,1]
        
        for i in range(len(df)):
            if df.index[i] == 'MEP':
                df.drop('MEP', inplace = True)
                break
          
        total = df.monto.sum()
        df['Participación1'] = float(0)
        df['Participación1'] = round(df.monto / total * 100,4)
        
        df['Participación'] = str(0) 
        for j in range(len(df)):
            df.iloc[j,-1] = str(df.iloc[j,-2]) + ' %'   
        
        cantidad = df.iloc[:,:1].copy()    
        precio = df.iloc[:,:4].copy()
        precio = precio.iloc[:,-1:].copy()
        participacion = df.iloc[:,-1:].copy()
        
        cartera = pd.concat([cantidad,precio,participacion], axis = 1)
        


    return cartera






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def depositos_retiros_ieb(fecha_cierre, fecha_inicial, alyc = 'Ieb', usuario = 1, 
                           numero_interno = 0):
    """  
    Aclaraciones
    -----------
                             ¿PARA QUE SIRVE ESTE CODIGO?
    
    Para construir un dataframe con los retiros, depositos y transferencias que 
    han hecho los clientes durante un periodo determinado. 
    
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento final del periodo de interes
        Ejemplo: '2024-10-31'. 
        
    fecha_inicial : tipo string.
    
        DESCRIPCION.
        Indica el momento inicial del periodo de interes
        Ejemplo: '2024-08-31'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    usuario : tipo integer.
    
        DESCRIPCION.
        Es el numero de computadora con el que se accede al dropbox. Al 26 de 
        noviembre del 2024 hay seis computadoras, del 1 al 6 han sido asignados
        sus numeros.
        Valor por defecto: 1.
        
        
    Resultado
    -------
    movimientos : tipo DataFrame.
       
       DESCRIPCION.
       Se obtiene un dataframe con los movimientos de los clientes, esto es, 
       los retiros, los depositos, y las transferencias hacia y desde otras alycs.
       Todo esto exclusivamente para los clientes que tenemos en IEB.

    """
    # -------------------------------------------------------------------------
    try:
        # usuario = 4 
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        # import numpy as np
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        
        
        dni=0
        nombre_cliente='rescovich Elizabeth Romina' 
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            
        
        except:
            nombre_cliente = ''
            numero_cliente = 0

           
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # Sub Parametros
        # Estos son parametros, pero no es necesario modificarlos.                  
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de IEB\{nombre_cliente} ({numero_cliente})'
        # -----------------------------------------------------------------------------
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        transferencia_alyc='Transferencias entre alycs y div en especie'
        
        
        # -----------------------------------------------------------------------------
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            # Se obtienen las fechas donde se ha realizado dolar mep, y los momentos 
            # inicial y final o de cierre, utiles para fijar el periodo de interes 
            # (asi nos ahorramos el tener que estar constantemente convirtiendo la fecha 
            # de un string a un float y viceversa)
            # -----------------------------------------------------------------------------
            # Obtenemos los momentos clave. Convertimos las fechas string en datetime
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial = dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            dias = (fecha_cierre - fecha_inicial).days
        
            
            # Transformamos las fechas a formato string
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            fecha_inicial = dt.strftime(fecha_inicial, '%Y-%m-%d')
            
        
            # ------------------------- SEGUNDA PARTE -----------------------------
            #       SE IDENTIFICAN LOS DEPOSITOS Y RETIROS EN PESOS Y EN USD
            # ---------------------------------------------------------------------
            # Se transforma la fecha de cierre al tipo datetime
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial = dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            
            # Importamos los movimientos en pesos 
            try:   
                # Se lo importa y se lo limpia.    
                archivo_pesos = fc.concatenacion_movimientos_ieb(moneda = 1, alyc = alyc,                                
                                                                 numero_interno = numero_interno,
                                                                 usuario = usuario)
            
                archivo_pesos = archivo_pesos.loc[(archivo_pesos.index<=fecha_cierre) & (
                                                    archivo_pesos.index>=fecha_inicial)].copy()
            
                pesos_depositos = archivo_pesos.loc[(archivo_pesos[archivo_pesos.columns[1]]=='COBW') |
                                                  (archivo_pesos[archivo_pesos.columns[1]]=='COBR')].copy()
                
                pesos_retiros = archivo_pesos.loc[archivo_pesos[archivo_pesos.columns[1]]=='PAGW'].copy()
            
            except:
                archivo_pesos = pd.DataFrame()
                
                pesos_depositos = pd.DataFrame()
            
                pesos_retiros = pd.DataFrame()
                
            
            # Importamos las transferencias y nos quedamos con las correspondientes mascaras
            try: 
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')    
                archivo_transf_alyc.set_index('Liquida', inplace =True)
                
                archivo_transf_alyc = archivo_transf_alyc.loc[
                                    (archivo_transf_alyc[archivo_transf_alyc.columns[1]] == 'TRANSFERENCIA') &
                                    (archivo_transf_alyc.index <= fecha_cierre) &
                                    (archivo_transf_alyc.index >= fecha_inicial)].copy()
                
                # Identificamos las transferencias desde y hacia la alyc.
                trans_desde_alycs = archivo_transf_alyc.loc[archivo_transf_alyc.Importe > 0].copy()
                
                trans_hacia_alycs = archivo_transf_alyc.loc[archivo_transf_alyc.Importe < 0].copy() 
                
            except:
                trans_desde_alycs = pd.DataFrame()
                trans_hacia_alycs = pd.DataFrame()
               
            
            # Importamos los movimientos en pesos dólares
            try:   
                # Se lo importa y se lo limpia.    
                archivo_usd = fc.concatenacion_movimientos_ieb(moneda = 2, alyc = alyc, 
                                                               numero_interno = numero_interno,
                                                               usuario = usuario)
            
                archivo_usd = archivo_usd.loc[(archivo_usd.index<=fecha_cierre)].copy()
                archivo_usd = archivo_usd.loc[(archivo_usd.index>=fecha_inicial)].copy()
            
                usd_depositos = archivo_usd.loc[(archivo_usd[archivo_usd.columns[2]]=='COUW') |
                                              (archivo_usd[archivo_usd.columns[2]]=='COME')].copy()
                
                usd_retiros = archivo_usd.loc[(archivo_usd[archivo_usd.columns[2]]=='PAUW') |
                                              (archivo_usd[archivo_usd.columns[2]]=='PAME')].copy()
            
            except:
                archivo_usd = pd.DataFrame()
                
                usd_depositos = pd.DataFrame()
            
                usd_retiros = pd.DataFrame()
            
            
            
            
            # -------------------------- TERCERA PARTE ---------------------------------
            #     SE ARMAN LOS VECTORES DE DEPOSITOS, RETIROS, Y TRANSFERENCIAS
            # --------------------------------------------------------------------------
            # Vectores de depositos y retiros en pesos
            depositos_pesos = pd.DataFrame()
            depositos_pesos['monto'] = float(0)
            depositos_pesos['fecha'] = pd.to_datetime(0)
            depositos_pesos['depositos_pesos'] = int(0)
            
            for i in range(50):
                depositos_pesos.loc[i] = float(0)  
                depositos_pesos.loc[i,'depositos_pesos'] = i
            
            depositos_pesos.set_index('depositos_pesos',inplace=True)
            
            
            depositos_pesos['fecha'] = pd.to_datetime(0)
            for i in range(len(pesos_depositos)):
                depositos_pesos.iloc[i,0] = pesos_depositos.loc[:,'Importe'].iloc[i]
                depositos_pesos.iloc[i,1] = pesos_depositos.index[i]
                
                if (depositos_pesos.iloc[i,1] == dias):
                    depositos_pesos.iloc[i,0] = 0
            
            
            retiros_pesos = pd.DataFrame()
            retiros_pesos['monto'] = float(0)
            retiros_pesos['fecha'] = pd.to_datetime(0)
            retiros_pesos['retiros_pesos'] = int(0)
            
            for i in range(50):
                retiros_pesos.loc[i] = float(0)  
                retiros_pesos.loc[i,'retiros_pesos'] = i    
            
            retiros_pesos.set_index('retiros_pesos',inplace=True)
            
            
            retiros_pesos['fecha'] = pd.to_datetime(0)
            for i in range(len(pesos_retiros)):
                retiros_pesos.iloc[i,0] = pesos_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_pesos.iloc[i,1] = pesos_retiros.index[i]
                
                if (retiros_pesos.iloc[i,1] == dias):
                    retiros_pesos.iloc[i,0] = 0
              
            
            # Vector de transferencia desde otras ALYCS
            alycs_trans_desde = pd.DataFrame()
            alycs_trans_desde['monto'] = float(0)
            alycs_trans_desde['fecha'] = pd.to_datetime(0)
            alycs_trans_desde['alycs_trans_desde'] = int(0)
            
            for i in range(50):
                alycs_trans_desde.loc[i] = float(0) 
                alycs_trans_desde.loc[i,'alycs_trans_desde'] = i
            
            alycs_trans_desde.set_index('alycs_trans_desde',inplace=True)
            
            
            alycs_trans_desde['fecha'] = pd.to_datetime(0)
            for i in range(len(trans_desde_alycs)):
                alycs_trans_desde.iloc[i,0] = trans_desde_alycs.loc[:,'Importe'].iloc[i]
                alycs_trans_desde.iloc[i,1] = trans_desde_alycs.index[i] 
                
                if (alycs_trans_desde.iloc[i,1] == dias):
                    alycs_trans_desde.iloc[i,0] = 0
                 
            
            # Vector de transferencia hacia otras ALYCS
            alycs_trans_hacia = pd.DataFrame()
            alycs_trans_hacia['monto'] = float(0)
            alycs_trans_hacia['fecha'] = pd.to_datetime(0)
            alycs_trans_hacia['alycs_trans_hacia'] = int(0)
            
            for i in range(50):
                alycs_trans_hacia.loc[i] = float(0) 
                alycs_trans_hacia.loc[i,'alycs_trans_hacia'] = i
            
            alycs_trans_hacia.set_index('alycs_trans_hacia',inplace=True)
            
            
            alycs_trans_hacia['fecha'] = pd.to_datetime(0)
            for i in range(len(trans_hacia_alycs)):
                alycs_trans_hacia.iloc[i,0] = trans_hacia_alycs.loc[:,'Importe'].iloc[i]*-1
                alycs_trans_hacia.iloc[i,1] = trans_hacia_alycs.index[i]
                 
                if (alycs_trans_hacia.iloc[i,1] == dias):
                    alycs_trans_hacia.iloc[i,0] = 0
            
            
            # Vectores de depositos y retiros en usd
            depositos_usd=pd.DataFrame()
            depositos_usd['monto'] = float(0)
            depositos_usd['fecha'] = pd.to_datetime(0)
            depositos_usd['depositos_usd'] = int(0)
            
            for i in range(50):
                depositos_usd.loc[i] = float(0)  
                depositos_usd.loc[i,'depositos_usd'] = i
            
            depositos_usd.set_index('depositos_usd',inplace=True)
            
            
            depositos_usd['fecha'] = pd.to_datetime(0)
            for i in range(len(usd_depositos)):
                depositos_usd.iloc[i,0] = usd_depositos.loc[:,'Importe'].iloc[i]
                depositos_usd.iloc[i,1] = usd_depositos.index[i]
                
                if (depositos_usd.iloc[i,1] == dias):
                    depositos_usd.iloc[i,0] = 0
            
            
            retiros_usd = pd.DataFrame()
            retiros_usd['monto'] = float(0)
            retiros_usd['fecha'] = pd.to_datetime(0)
            retiros_usd['retiros_usd'] = int(0)
            
            for i in range(50):
                retiros_usd.loc[i] = float(0)  
                retiros_usd.loc[i,'retiros_usd'] = i    
            
            retiros_usd.set_index('retiros_usd',inplace=True)
            
            
            retiros_usd['fecha'] = pd.to_datetime(0)
            for i in range(len(usd_retiros)):
                retiros_usd.iloc[i,0] = usd_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_usd.iloc[i,1] = usd_retiros.index[i] 
                
                if (retiros_usd.iloc[i,1] == dias):
                    retiros_usd.iloc[i,0] = 0
                
            
            
            
            # ------------------------------ CUARTA PARTE ---------------------------------
            #             DEPOSITOS Y RETIROS EN DOLARES SE TRADUCEN A PESOS MEP
            # -----------------------------------------------------------------------------
            # Importamos el archivo de precios
            if (len(depositos_usd.loc[depositos_usd.monto>0])>0) or (
                                        len(retiros_usd.loc[retiros_usd.monto>0])>0):
                archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                            ,sheet_name='Hoja 2').set_index('fecha')
            else:
                archivo_precios = pd.DataFrame()
                
            
            # Depositos en usd a pesos
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in usd_depositos.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                for i in range(len(usd_depositos)):
                    depositos_usd.iloc[i,0]=precio_dolar[i]*depositos_usd.iloc[i,0]
            
            
            # Retiros en usd a pesos
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in usd_retiros.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                for i in range(len(usd_retiros)):
                    retiros_usd.iloc[i,0]=precio_dolar[i]*retiros_usd.iloc[i,0]
            
            
            
            # -------------------------- QUINTA PARTE ---------------------------------
            # Se crea un dataframe que contiene retiros, depositos, y transferencias.
            # -------------------------------------------------------------------------
            # Se generan los dataframes que contendran depositos y retiros
            # Depositos
            movimientos_d = pd.DataFrame()
            movimientos_d['depositos'] = float(0)
            movimientos_d['retiros'] = float(0)
            movimientos_d['fecha'] = pd.to_datetime(0)
            
            for i in range(100):
                movimientos_d.loc[i] = float(0) 
            
            movimientos_d['fecha'] = pd.to_datetime(0)
            
            # Retiros
            movimientos_r = pd.DataFrame()
            movimientos_r['depositos'] = float(0)
            movimientos_r['retiros'] = float(0)
            movimientos_r['fecha'] = pd.to_datetime(0)
            
            for i in range(100):
                movimientos_r.loc[i] = float(0) 
            
            movimientos_r['fecha'] = pd.to_datetime(0)
                
            
            # Agrupamos los retiros por un lado y los depositos por el otro antes de
            # incorporarlos en el dataframe 'movimientos'  
            depositos = pd.concat([depositos_pesos, depositos_usd, alycs_trans_desde], 
                                  ignore_index = True)
            
            depositos = depositos.loc[depositos.monto != 0].copy()
            
            depositos = pd.DataFrame(depositos.groupby('fecha').monto.sum())
            
            depositos.reset_index(inplace = True)
            
            
            retiros = pd.concat([retiros_pesos, retiros_usd, alycs_trans_hacia], 
                                  ignore_index = True)
            
            retiros = retiros.loc[retiros.monto != 0].copy()
            
            retiros = pd.DataFrame(retiros.groupby('fecha').monto.sum())
            
            retiros.reset_index(inplace = True)
            
            
            # Se incorporan los datos de 'depositos' y 'retiros' en diferentes data- 
            # frames.
            for i in range(len(depositos)):
                movimientos_d.iloc[i,0] = depositos.iloc[i,1]
                movimientos_d.iloc[i,2] = depositos.iloc[i,0]
                
            movimientos_d = movimientos_d.loc[movimientos_d.fecha != pd.to_datetime(0)].copy()
            
            for i in range(len(retiros)):
                movimientos_r.iloc[i,1] = retiros.iloc[i,1]
                movimientos_r.iloc[i,2] = retiros.iloc[i,0]
            
            movimientos_r = movimientos_r.loc[movimientos_r.fecha != pd.to_datetime(0)].copy()
            
            
            # Concatenamos
            movimientos = pd.concat([movimientos_d, movimientos_r], ignore_index = True)
            
            # Agrupar por la columna de fechas y sumar los montos
            movimientos = movimientos.groupby('fecha').agg({'depositos': 'sum',
                                                            'retiros': 'sum'
                                                            }).reset_index()

            # Sirve para que los float se muestren en decimales y no en notacion
            # cientifica
            pd.set_option('display.float_format', '{:.2f}'.format)  
            
            
        else:
            movimientos = datos_cliente
        
    
    except:
        movimientos = 'Introduzca un usuario válido: entero entre 1 y 6'



    return movimientos





# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def depositos_retiros_bull(fecha_cierre, fecha_inicial, ctte_adm = '', alyc = 'Bull', 
                           usuario = 1, numero_interno = 0):
    """  
    Aclaraciones
    -----------
                             ¿PARA QUE SIRVE ESTE CODIGO?
    
    Para construir un dataframe con los retiros, depositos y transferencias que 
    han hecho los clientes durante un periodo determinado. 
    
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento final del periodo de interes
        Ejemplo: '2024-10-31'. 
        
    fecha_inicial : tipo string.
    
        DESCRIPCION.
        Indica el momento inicial del periodo de interes
        Ejemplo: '2024-08-31'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    usuario : tipo integer.
    
        DESCRIPCION.
        Es el numero de computadora con el que se accede al dropbox. Al 26 de 
        noviembre del 2024 hay seis computadoras, del 1 al 6 han sido asignados
        sus numeros.
        Valor por defecto: 1.
        
    ctte_adm : tipo string.
    
        DESCRIPCION.
        Permite obtener los retiros y depositos considerando las transferencias 
        de papeles en determinadas circunstancias. Admite uno de tres valores: 
        1) 'si', en este caso se consideran solo las transferencias entre cttes
        administradas por catalaxia; 2) 'no', en este caso se considera todo lo 
        no sea una transferencia hecha entre cttes administradas por catalaxia; 
        y 3) '', en este caso si considera todo tipo de transferencia. 
        Valor por defecto: ''.
        
        
    Resultado
    -------
    movimientos : tipo DataFrame.
       
       DESCRIPCION.
       Se obtiene un dataframe con los movimientos de los clientes, esto es, 
       los retiros, los depositos, y las transferencias hacia y desde otras alycs.
       Todo esto exclusivamente para los clientes que tenemos en bullmarket.

    """
    # -------------------------------------------------------------------------
    try:
        # usuario = 4 
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        
        
       
        dni=0
        nombre_cliente='rescovich Elizabeth Romina' 
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
            dia_corte = datos_cliente.loc['Dia de corte','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
            
            
        # -----------------------------------------------------------------------------
        # Sub Parametros
        # Estos son parametros, pero no es necesario modificarlos.                  
        directorio_origen=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\Cuentas de BullMarket\{nombre_cliente} ({numero_cliente})'
        
        movimiento_pesos=f'Cuenta Corriente PESOS {fecha_movimientos}' 
        movimiento_usd=f'Cuenta Corriente DOLARES {fecha_movimientos}' 
        
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        
        transferencia_alyc='Transferencias entre alycs y div en especie'
        
        directorio_clientes=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS'
        nombre_archivo_clientes='Base de Datos de Clientes'
        
        
        # -----------------------------------------------------------------------------
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            # Se obtienen las fechas donde se ha realizado dolar mep, y los momentos 
            # inicial y final o de cierre, utiles para fijar el periodo de interes 
            # (asi nos ahorramos el tener que estar constantemente convirtiendo la fecha 
            # de un string a un float y viceversa)
            # -----------------------------------------------------------------------------
            # Obtenemos los momentos clave. Convertimos las fechas string en datetime
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial = dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            dias = (fecha_cierre - fecha_inicial).days
            
            
            # Transformamos las fechas a formato string para uso de funciones
            fecha_cierre = dt.strftime(fecha_cierre, '%Y-%m-%d')
            fecha_inicial = dt.strftime(fecha_inicial, '%Y-%m-%d')
            
            
            # Transformamos las fechas a formato datetime para tomar mascaras
            fecha_cierre_masc = dt.strptime(fecha_cierre, '%Y-%m-%d')
            fecha_inicial_masc = dt.strptime(fecha_inicial, '%Y-%m-%d')
            
            
            
            
            # ------------------------- SEGUNDA PARTE ---------------------------------
            # Se calculan las extracciones por operaciones dolar MEP (retiros en usd)
            # -----------------------------------------------------------------------------
            # Creamos el 'retiros_usd' que contiene los retiros por dolar MEP y el plazo de 
            # la operacion.
            retiros_usd=pd.DataFrame()
            retiros_usd['monto']=float(0)
            retiros_usd['fecha']=pd.to_datetime(0)
            
            for i in range(50):
                retiros_usd.loc[i]=float(0)
            
            fecha_inicial=dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            
            # Bucamos los valores de los retiros en USD (dolar MEP)
            cartera_cierre=fc.composicion_cartera_bull(fecha_cierre=fecha_cierre, 
                                                        alyc=alyc, dni=dni, 
                                                        numero_interno=numero_interno, 
                                                        nombre_cliente=nombre_cliente,
                                                        usuario = usuario)
            
            mascara_mep=cartera_cierre.loc[cartera_cierre.index=='MEP'].copy()
            
            mascara_mep=mascara_mep.loc[mascara_mep['fecha mep']>=fecha_inicial].copy()
            
            
            # Rellenamos el 'retiros_usd' con los valores, siempre que existan.
            retiros_usd['fecha']=pd.to_datetime(0)
            
            if len(mascara_mep)>0:
                mascara_mep['monto'] = mascara_mep.Cantidad*mascara_mep.iloc[:,1]*-1
                
                for i in range(len(mascara_mep)):
                    retiros_usd.iloc[i,0] = mascara_mep.iloc[i,3]
                    retiros_usd.iloc[i,1] = mascara_mep.iloc[i,2]
                    
                    if (retiros_usd.iloc[i,1] == dias):
                        retiros_usd.iloc[i,0] = 0
            
            
            
            
            # ------------------------ TERCERA PARTE ----------------------------------
            # Se calculan los retiros y depositos en pesos, y tambien, los depositos en usd
            # -----------------------------------------------------------------------------
            # Se construyen los vectores de depositos en pesos, retiros en pesos, y depositos
            # en dolares. Se controlan estos montos para que no se contabilicen dos veces 
            # (una en el monto final o inicial, y otra como entrada o salida de dinero)
            # Depositos en pesos
            depositos_pesos=pd.DataFrame()
            depositos_pesos['monto']=float(0)
            depositos_pesos['fecha']=pd.to_datetime(0)
            
            for i in range(50):
                depositos_pesos.loc[i]=float(0) 
                
            
            # Retiros en pesos
            retiros_pesos=pd.DataFrame()
            retiros_pesos['monto']=float(0)
            retiros_pesos['fecha']=pd.to_datetime(0)
            
            for i in range(50):
                retiros_pesos.loc[i]=float(0) 
                
            
            # Depositos en dolares
            depositos_usd=pd.DataFrame()
            depositos_usd['monto']=float(0)
            depositos_usd['fecha']=pd.to_datetime(0)
            
            for i in range(50):
                depositos_usd.loc[i]=float(0) 
            
            
            # Se importan los archivos de movimiento en pesos y dolares y se toman sus 
            # mascaras
            try:
                archivo_pesos = fc.concatenacion_movimientos_bull(moneda = 'Pesos', alyc = alyc, 
                                                                  dni = dni,
                                                                  nombre_cliente = nombre_cliente, 
                                                                  numero_interno = numero_interno, 
                                                                  usuario = usuario)
                
                archivo_pesos=archivo_pesos.loc[(archivo_pesos.index>=fecha_inicial_masc
                                                  ) & (
                                                archivo_pesos.index<=fecha_cierre_masc)]
            
            except:
                archivo_pesos=[]
                archivo_pesos=pd.DataFrame()
            
            try:    
                archivo_usd = fc.concatenacion_movimientos_bull(moneda = 'Dolares', alyc = alyc, 
                                                                  dni = dni,
                                                                  nombre_cliente = nombre_cliente, 
                                                                  numero_interno = numero_interno, 
                                                                  usuario = usuario)
                
                archivo_usd=archivo_usd.loc[(archivo_usd.index>=fecha_inicial_masc
                                                  ) & (
                                                archivo_usd.index<=fecha_cierre_masc)]
            
            except:
                archivo_usd=[]
                archivo_usd=pd.DataFrame()
            
              
            # Se rellena el vector de depositos en pesos
            try:
                mascara_depositos_pesos=archivo_pesos.loc[(archivo_pesos.Referencia=='CREDITO CTA. CTE.') |
                                                          (archivo_pesos.Referencia=='COTITULAR')].copy()
                mascara_depositos_pesos.reset_index(inplace=True)
                
            except:
                mascara_depositos_pesos=pd.DataFrame()
            
            
            depositos_pesos['fecha']=pd.to_datetime(0)
            if len(mascara_depositos_pesos)>0:
                for i in range(len(mascara_depositos_pesos)):
                    depositos_pesos.iloc[i,0]=mascara_depositos_pesos.Importe[i]
                    depositos_pesos.iloc[i,1] = mascara_depositos_pesos.iloc[i,0]
                    
                    if (depositos_pesos.iloc[i,1] == dias):
                        depositos_pesos.iloc[i,0] = 0
            
            
            # Se rellena el vector de retiros en pesos
            try:
                mascara_retiros_pesos=archivo_pesos.loc[archivo_pesos.Referencia=='TRANSFERENCIA VIA MEP'].copy() 
                mascara_retiros_pesos.reset_index(inplace=True)
            
            except:
                mascara_retiros_pesos=pd.DataFrame()
            
            
            retiros_pesos['fecha']=pd.to_datetime(0)
            if len(mascara_retiros_pesos)>0:
                for i in range(len(mascara_retiros_pesos)):
                    retiros_pesos.iloc[i,0] = mascara_retiros_pesos.Importe[i]*-1
                    retiros_pesos.iloc[i,1] = mascara_retiros_pesos.iloc[i,0]
                    
                    if (retiros_pesos.iloc[i,1] == dias):
                        retiros_pesos.iloc[i,0] = 0
                    
            
            # Se rellena el vector de depositos en dolares
            try:
                mascara_depositos_usd=archivo_usd.loc[archivo_usd.Referencia=='CREDITO CTA. CTE.'].copy()
                mascara_depositos_usd.reset_index(inplace=True)
            
            except:
                mascara_depositos_usd=pd.DataFrame()
                
                
            depositos_usd['fecha']=pd.to_datetime(0)    
            if len(mascara_depositos_usd)>0:
                for i in range(len(mascara_depositos_usd)):
                    depositos_usd.iloc[i,0]=mascara_depositos_usd.Importe[i]
                    depositos_usd.iloc[i,1] = mascara_depositos_usd.iloc[i,0]
                    
                    if (depositos_usd.iloc[i,1] == dias):
                        depositos_usd.iloc[i,0] = 0
            
            
            # Transformamos los depositos en dolares en depositos en pesos
            # Importamos el archivo de precios
            if len(depositos_usd.loc[depositos_usd.monto>0])>0:
                archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                            ,sheet_name='Hoja 2').set_index('fecha')
                
                mascara_depositos_usd.set_index('Liquida',inplace=True)
                
            else:
                archivo_precios = pd.DataFrame()
            
            
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in mascara_depositos_usd.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                
                for i in range(len(mascara_depositos_usd)):
                    depositos_usd.iloc[i,0]=precio_dolar[i]*depositos_usd.iloc[i,0]
            
            
            
            
            # -------------------------- CUARTA PARTE ---------------------------------
            # Se crea un vector con las transferencia de papeles desde otras ALYCS. Este
            # tipo de operaciones se tratan como un deposito cuando llegan los papeles, y 
            # como un retiro cuando salen
            # -----------------------------------------------------------------------------
            # Traemos el archivo que contiene las transferencias entre alycs.
            try:
                archivo_transf_alyc = pd.read_excel(f'{directorio_origen}\{transferencia_alyc}.xlsx')
                archivo_transf_alyc.set_index("Liquida", inplace=True)   
                
                # Se toma la mascara de acuerdo a la fecha de cierre
                archivo_transf_alyc = archivo_transf_alyc.loc[
                                (archivo_transf_alyc.index <= fecha_cierre_masc) &
                                (archivo_transf_alyc.index >= fecha_inicial_masc)].copy()
                
                # Tomamos la mascara del archivo transferencia segun la variable 'ctte_adm'
                if ctte_adm == 'si': # nos quedamos solo con las transferencias entre ctte administradas por catalaxia
                    archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.ctte_adm == 'si'].copy()
                    
                elif ctte_adm == 'no': # nos quedamos solo con las transferencias desde y hacia ctte no administradas por catalaxia
                    archivo_transf_alyc = archivo_transf_alyc.loc[archivo_transf_alyc.ctte_adm != 'si'].copy()
                    
                elif ctte_adm == '': # se consideran todas las transferencias de papeles
                    archivo_transf_alyc = archivo_transf_alyc.copy()
                
                # Se consiguen las mascaras de entrada y salida por transferencias
                transferencia_entrada = archivo_transf_alyc.loc[(archivo_transf_alyc.Importe>0) & 
                                                (archivo_transf_alyc.Comprobante == 'TRANSFERENCIA')].copy()
                
                transferencia_salida = archivo_transf_alyc.loc[(archivo_transf_alyc.Importe<0) & 
                                                (archivo_transf_alyc.Comprobante == 'TRANSFERENCIA')].copy()
                
            except:
                transferencia_entrada = pd.DataFrame()
                transferencia_salida = pd.DataFrame()
            
            
            # Se arman y "rellenan" los vectores correspondientes.
            # Entrada de papeles procedentes de otras alycs (depositos)
            transferencia_entreda2=pd.DataFrame()
            transferencia_entreda2['monto']=float(0)
            transferencia_entreda2['fecha']=pd.to_datetime(0)
            
            for i in range(50):
                transferencia_entreda2.loc[i]=float(0) 
            
            transferencia_entreda2['fecha']=pd.to_datetime(0)
            if len(transferencia_entrada)>0:
                for i in range(len(transferencia_entrada)):
                    transferencia_entreda2.iloc[i,0] = transferencia_entrada.loc[:,'Importe'].iloc[i]
                    transferencia_entreda2.iloc[i,1] = transferencia_entrada.index[i]   
                    
                    if (transferencia_entreda2.iloc[i,1] == dias):
                        transferencia_entreda2.iloc[i,0] = 0
                
                
            # Salida de papeles desde la alyc actual (retiros)
            transferencia_salida2=pd.DataFrame()
            transferencia_salida2['monto']=float(0)
            transferencia_salida2['fecha']=pd.to_datetime(0)
            
            for i in range(50):
                transferencia_salida2.loc[i]=float(0) 
            
            transferencia_salida2['fecha']=pd.to_datetime(0)
            if len(transferencia_salida)>0:
                for i in range(len(transferencia_salida)):
                    transferencia_salida2.iloc[i,0] = transferencia_salida.loc[:,'Importe'].iloc[i]*-1
                    transferencia_salida2.iloc[i,1] = transferencia_salida.index[i]
                    
                    if (transferencia_salida2.iloc[i,1] == dias):
                        transferencia_salida2.iloc[i,0] = 0
            
            
            
            
            # -------------------------- QUINTA PARTE ---------------------------------
            # Se crea un dataframe que contiene retiros, depositos, y transferencias.
            # -------------------------------------------------------------------------
            # Se generan los dataframes que contendran depositos y retiros
            # Depositos
            movimientos_d = pd.DataFrame()
            movimientos_d['depositos'] = float(0)
            movimientos_d['retiros'] = float(0)
            movimientos_d['fecha'] = pd.to_datetime(0)
            
            for i in range(100):
                movimientos_d.loc[i] = float(0) 
            
            movimientos_d['fecha'] = pd.to_datetime(0)
            
            # Retiros
            movimientos_r = pd.DataFrame()
            movimientos_r['depositos'] = float(0)
            movimientos_r['retiros'] = float(0)
            movimientos_r['fecha'] = pd.to_datetime(0)
            
            for i in range(100):
                movimientos_r.loc[i] = float(0) 
            
            movimientos_r['fecha'] = pd.to_datetime(0)
            
               
            # Agrupamos los retiros por un lado y los depositos por el otro antes de
            # incorporarlos en el dataframe 'movimientos'  
            depositos = pd.concat([depositos_pesos,depositos_usd,transferencia_entreda2], 
                                  ignore_index = True)
            
            depositos = depositos.loc[depositos.monto != 0].copy()
            
            depositos = pd.DataFrame(depositos.groupby('fecha').monto.sum())
            
            depositos.reset_index(inplace = True)
            
            
            retiros = pd.concat([retiros_pesos,retiros_usd,transferencia_salida2], 
                                  ignore_index = True)
            
            retiros = retiros.loc[retiros.monto != 0].copy()
               
            retiros = pd.DataFrame(retiros.groupby('fecha').monto.sum())
            
            retiros.reset_index(inplace = True)
            
            
            # Se incorporan los datos de 'depositos' y 'retiros' en diferentes data- 
            # frames.
            for i in range(len(depositos)):
                movimientos_d.iloc[i,0] = depositos.iloc[i,1]
                movimientos_d.iloc[i,2] = depositos.iloc[i,0]
                
            movimientos_d = movimientos_d.loc[movimientos_d.fecha != pd.to_datetime(0)].copy()
            
            for i in range(len(retiros)):
                movimientos_r.iloc[i,1] = retiros.iloc[i,1]
                movimientos_r.iloc[i,2] = retiros.iloc[i,0]
            
            movimientos_r = movimientos_r.loc[movimientos_r.fecha != pd.to_datetime(0)].copy()
            
            
            # Concatenamos
            movimientos = pd.concat([movimientos_d, movimientos_r], ignore_index = True)
            
            # Agrupar por la columna de fechas y sumar los montos
            movimientos = movimientos.groupby('fecha').agg({'depositos': 'sum',
                                                            'retiros': 'sum'
                                                            }).reset_index()
            
            # Sirve para que los float se muestren en decimales y no en notacion
            # cientifica
            pd.set_option('display.float_format', '{:.2f}'.format)  
                
            # Tomamos la mascara de 'movimientos' entre las fechas de cierre e inicial
            # de este modo evitamos tomar montos que luego se contabilizan en otras 
            # funciones como valor final o inicial (respectivamente)
            movimientos = movimientos.loc[(movimientos.fecha <= fecha_cierre_masc) & 
                                          (movimientos.fecha > fecha_inicial_masc)].copy()
        
        else:
            movimientos = datos_cliente


    except:
        movimientos = 'Introduzca un usuario válido: entero entre 1 y 6'



    return movimientos





# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def depositos_retiros_balanz(fecha_cierre, fecha_inicial, alyc = 'Balanz', usuario = 1, 
                             numero_interno = 0):
    """  
    Aclaraciones
    -----------
                             ¿PARA QUE SIRVE ESTE CODIGO?
    
    Para construir un dataframe con los retiros, depositos y transferencias que 
    han hecho los clientes durante un periodo determinado. 
    
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento final del periodo de interes
        Ejemplo: '2024-10-31'. 
        
    fecha_inicial : tipo string.
    
        DESCRIPCION.
        Indica el momento inicial del periodo de interes
        Ejemplo: '2024-08-31'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es la alyc donde el cliente tiene la cuenta, sea Bull, Ieb, o Balanz. 
        Valor por defecto: ''. Este dato es importante, por de este modo el codigo 
        puede reconocer al cliente.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero que la empresa asigna al cliente.  
        Valor por defecto: 0.
        
    usuario : tipo integer.
    
        DESCRIPCION.
        Es el numero de computadora con el que se accede al dropbox. Al 26 de 
        noviembre del 2024 hay seis computadoras, del 1 al 6 han sido asignados
        sus numeros.
        Valor por defecto: 1.
        
        
    Resultado
    -------
    movimientos : tipo DataFrame.
       
       DESCRIPCION.
       Se obtiene un dataframe con los movimientos de los clientes, esto es, 
       los retiros, los depositos, y las transferencias hacia y desde otras alycs.
       Todo esto exclusivamente para los clientes que tenemos en balanz.

    """
    # -------------------------------------------------------------------------
    try:
        # usuario = 4 
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        from datetime import datetime as dt
        from datetime import timedelta
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        
  
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc,
                                   numero_interno = numero_interno, 
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  

        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            
           
     
        serie_precio='- Serie precios Argy y Cedears'
        directorio_precio=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'

        
        
        # -----------------------------------------------------------------------------
        controlador = type(datos_cliente)==str
        if controlador == False:
            # ----------------------------- PRIMERA PARTE ---------------------------------
            # Se obtienen las fechas donde se ha realizado dolar mep, y los momentos 
            # inicial y final o de cierre, utiles para fijar el periodo de interes 
            # (asi nos ahorramos el tener que estar constantemente convirtiendo la fecha 
            # de un string a un float y viceversa)
            # -----------------------------------------------------------------------------
            # Obtenemos los momentos clave. Convertimos las fechas string en datetime
            fecha_cierre = dt.strptime(fecha_cierre,'%Y-%m-%d')
            fecha_inicial = dt.strptime(fecha_inicial,'%Y-%m-%d')
            
            dias = (fecha_cierre - fecha_inicial).days
        
          
            
            
            # ------------------------ SEGUNDA PARTE ------------------------------
            #          SE IDENTIFICAN LOS DEPOSITOS Y RETIROS EN PESOS Y EN USD
            # ---------------------------------------------------------------------
            # Importamos los movimientos en pesos 
            try:   
                # Se lo importa y se lo limpia.    
                archivo = fc.concatenacion_movimientos_bal(alyc = alyc, 
                                                            usuario = usuario,                                                           
                                                            numero_interno = numero_interno) 

                archivo = archivo.loc[(archivo.index <= fecha_cierre) & (
                                                    archivo.index >= fecha_inicial)].copy()

                pesos_depositos = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                              (archivo.Importe > 0) & 
                                              (archivo.Moneda == 'Pesos') | 
                                              (archivo.Tipo == 'Tesorería') &
                                              (archivo.Importe > 0) & 
                                              (archivo.Moneda == 'Pesos')].copy()
                
                pesos_retiros = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                            (archivo.Importe < 0) & 
                                            (archivo.Moneda == 'Pesos') | 
                                            (archivo.Tipo == 'Tesorería') &
                                            (archivo.Importe < 0) & 
                                            (archivo.Moneda == 'Pesos')].copy()
                
                usd_depositos = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                            (archivo.Importe > 0) & 
                                            (archivo.Moneda == 'Dolares C.V. 7000') | 
                                            (archivo.Tipo == 'Tesorería') &
                                            (archivo.Importe > 0) & 
                                            (archivo.Moneda == 'Dolares C.V. 7000')].copy()
                
                usd_retiros = archivo.loc[(archivo.Tipo == 'Tesorería ') &
                                          (archivo.Importe < 0) & 
                                          (archivo.Moneda == 'Dolares C.V. 7000') | 
                                          (archivo.Tipo == 'Tesorería') &
                                          (archivo.Importe < 0) & 
                                          (archivo.Moneda == 'Dolares C.V. 7000')].copy()

            except:
                archivo = pd.DataFrame()
                
                pesos_depositos = pd.DataFrame()

                pesos_retiros = pd.DataFrame()
                
                usd_depositos = pd.DataFrame()

                usd_retiros = pd.DataFrame()

            
            

            # ------------------------------ CUARTA PARTE ---------------------------------
            #               SE ARMAN LOS VECTORES DE DEPOSITOS Y RETIROS
            # -----------------------------------------------------------------------------
            # Vectores de depositos y retiros en pesos
            depositos_pesos=pd.DataFrame()
            depositos_pesos['monto']=float(0)
            depositos_pesos['fecha']=pd.to_datetime(0)
            depositos_pesos['depositos_pesos']=int(0)

            for i in range(50):
                depositos_pesos.loc[i]=float(0)  
                depositos_pesos.loc[i,'depositos_pesos']=i

            depositos_pesos.set_index('depositos_pesos',inplace=True)
            
            depositos_pesos['fecha']=pd.to_datetime(0)
            for i in range(len(pesos_depositos)):
                depositos_pesos.iloc[i,0]=pesos_depositos.loc[:,'Importe'].iloc[i]
                depositos_pesos.iloc[i,1]=pesos_depositos.index[i]
                
                if (depositos_pesos.iloc[i,1] == dias):
                    depositos_pesos.iloc[i,0] = 0

            retiros_pesos=pd.DataFrame()
            retiros_pesos['monto']=float(0)
            retiros_pesos['fecha']=pd.to_datetime(0)
            retiros_pesos['retiros_pesos']=int(0)

            for i in range(50):
                retiros_pesos.loc[i]=float(0)  
                retiros_pesos.loc[i,'retiros_pesos']=i    

            retiros_pesos.set_index('retiros_pesos',inplace=True)
            
            retiros_pesos['fecha']=pd.to_datetime(0)
            for i in range(len(pesos_retiros)):
                retiros_pesos.iloc[i,0]=pesos_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_pesos.iloc[i,1]=pesos_retiros.index[i]
                
                if (retiros_pesos.iloc[i,1] == dias):
                    retiros_pesos.iloc[i,0] = 0
              

            # Vectores de depositos y retiros en usd
            depositos_usd=pd.DataFrame()
            depositos_usd['monto']=float(0)
            depositos_usd['fecha']=pd.to_datetime(0)
            depositos_usd['depositos_usd']=int(0)

            for i in range(50):
                depositos_usd.loc[i]=float(0)  
                depositos_usd.loc[i,'depositos_usd']=i

            depositos_usd.set_index('depositos_usd',inplace=True)
            
            depositos_usd['fecha']=pd.to_datetime(0)
            for i in range(len(usd_depositos)):
                depositos_usd.iloc[i,0]=usd_depositos.loc[:,'Importe'].iloc[i]
                depositos_usd.iloc[i,1]=usd_depositos.index[i]
                
                if (depositos_usd.iloc[i,1] == dias):
                    depositos_usd.iloc[i,0] = 0

            retiros_usd=pd.DataFrame()
            retiros_usd['monto']=float(0)
            retiros_usd['fecha']=pd.to_datetime(0)
            retiros_usd['retiros_usd']=int(0)

            for i in range(50):
                retiros_usd.loc[i]=float(0)  
                retiros_usd.loc[i,'retiros_usd']=i    

            retiros_usd.set_index('retiros_usd',inplace=True)
            
            retiros_usd['fecha']=pd.to_datetime(0)
            for i in range(len(usd_retiros)):
                retiros_usd.iloc[i,0]=usd_retiros.loc[:,'Importe'].iloc[i]*-1
                retiros_usd.iloc[i,1]=usd_retiros.index[i]
                
                if (retiros_usd.iloc[i,1] == dias):
                    retiros_usd.iloc[i,0] = 0
                



            # ------------------------------ QUINTA PARTE ---------------------------------
            #             DEPOSITOS Y RETIROS EN DOLARES SE TRADUCEN A PESOS MEP
            # -----------------------------------------------------------------------------
            # Importamos el archivo de precios
            if (len(depositos_usd.loc[depositos_usd.monto>0])>0) or (
                                        len(retiros_usd.loc[retiros_usd.monto>0])>0):
                archivo_precios=pd.read_excel(f'{directorio_precio}\{serie_precio}.xlsx'
                                            ,sheet_name='Hoja 2').set_index('fecha')
            else:
                archivo_precios = pd.DataFrame()
                

            # Depositos y retiros en usd a pesos
            if archivo_precios.empty == False:
                precio_dolar=[]
                for j in usd_depositos.index:
                    fecha_precio=j
                    fecha_precio2=fecha_precio
                    
                    for i in range(60):
                        
                        if len(archivo_precios.loc[archivo_precios.index==(fecha_precio-timedelta(days=i))])==0:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                            
                        else:
                            fecha_precio2=fecha_precio-timedelta(days=i)
                        
                        if len(archivo_precios.loc[archivo_precios.index==fecha_precio2])==1:
                            break
                        
                    precio_dolar.append(archivo_precios.loc[fecha_precio2,'dolar_mep'])
                
                for i in range(len(usd_depositos)):
                    depositos_usd.iloc[i,0]=precio_dolar[i]*depositos_usd.iloc[i,0]
                
                for i in range(len(usd_retiros)):
                    retiros_usd.iloc[i,0]=precio_dolar[i]*retiros_usd.iloc[i,0]



            
            
            
            # -------------------------- QUINTA PARTE ---------------------------------
            # Se crea un dataframe que contiene retiros, depositos, y transferencias.
            # -------------------------------------------------------------------------
            # Se generan los dataframes que contendran depositos y retiros
            # Depositos
            movimientos_d = pd.DataFrame()
            movimientos_d['depositos'] = float(0)
            movimientos_d['retiros'] = float(0)
            movimientos_d['fecha'] = pd.to_datetime(0)
            
            for i in range(100):
                movimientos_d.loc[i] = float(0) 
            
            movimientos_d['fecha'] = pd.to_datetime(0)
            
            # Retiros
            movimientos_r = pd.DataFrame()
            movimientos_r['depositos'] = float(0)
            movimientos_r['retiros'] = float(0)
            movimientos_r['fecha'] = pd.to_datetime(0)
            
            for i in range(100):
                movimientos_r.loc[i] = float(0) 
            
            movimientos_r['fecha'] = pd.to_datetime(0)
                
            
            # Agrupamos los retiros por un lado y los depositos por el otro antes de
            # incorporarlos en el dataframe 'movimientos'  
            depositos = pd.concat([depositos_pesos, depositos_usd], ignore_index = True)
            
            depositos = depositos.loc[depositos.monto != 0].copy()
            
            depositos = pd.DataFrame(depositos.groupby('fecha').monto.sum())
            
            depositos.reset_index(inplace = True)
            
            
            retiros = pd.concat([retiros_pesos, retiros_usd], ignore_index = True)
            
            retiros = retiros.loc[retiros.monto != 0].copy()
            
            retiros = pd.DataFrame(retiros.groupby('fecha').monto.sum())
            
            retiros.reset_index(inplace = True)
            
            
            # Se incorporan los datos de 'depositos' y 'retiros' en diferentes data- 
            # frames.
            for i in range(len(depositos)):
                movimientos_d.iloc[i,0] = depositos.iloc[i,1]
                movimientos_d.iloc[i,2] = depositos.iloc[i,0]
                
            movimientos_d = movimientos_d.loc[movimientos_d.fecha != pd.to_datetime(0)].copy()
            
            for i in range(len(retiros)):
                movimientos_r.iloc[i,1] = retiros.iloc[i,1]
                movimientos_r.iloc[i,2] = retiros.iloc[i,0]
            
            movimientos_r = movimientos_r.loc[movimientos_r.fecha != pd.to_datetime(0)].copy()
            
            
            # Concatenamos
            movimientos = pd.concat([movimientos_d, movimientos_r], ignore_index = True)
            
            # Agrupar por la columna de fechas y sumar los montos
            movimientos = movimientos.groupby('fecha').agg({'depositos': 'sum',
                                                            'retiros': 'sum'
                                                            }).reset_index()

            # Sirve para que los float se muestren en decimales y no en notacion
            # cientifica
            pd.set_option('display.float_format', '{:.2f}'.format)  
            
        else:
            movimientos = datos_cliente
        

    except:
        movimientos = 'Introduzca un usuario válido: entero entre 1 y 6'
              
    
    return movimientos






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def grafica_composicion_ieb(fecha_cierre, alyc = '', dni = 0, numero_interno = 0,
                            nombre_cliente = '', usuario = 1):
    """
    ---------------------------------------------------------------------------
                                  ¿QUE HACE EL CODIGO?
    Redefine la cartera en terminos sectoriales, calculando la participacion
    correspondiente y, finalmente, graficando el resultado.
    ---------------------------------------------------------------------------
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es el nombre de la alyc donde esta la cuenta del cliente: Bull, Ieb, o
        Balanz. Se puede escribi con mayuscula y acentos.  
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero interno que la empresa asigna al cliente.  
        Valor por defecto: 0.

    dni : tipo integer
    
        DESCRIPCION
        Es el dni del cliente. No debe escribirse separando con puntos o comas.
        Valor por defecto: 0.
        
        
    Resultado
    -------
    Elabora tres graficas de donas. Una para la cartera, otra para desomponer la
    liquidez entre pesos y divisas, y otra para desagregar la tenencia mas peque-
    ña entre los papeles correspondientes.
    
    """
    
    try:

        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''

        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'

        # -----------------------------------------------------------------------------
        import pandas as pd
        import matplotlib.pyplot as plt 
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc


        # -----------------------------------------------------------------------------
        directorio_composicion=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        archivo_composicion_merval='Clasificacion del MERVAL por rama de actividad'
        archivo_composicion_spy='Clasificacion de algunos papeles del SPX por rama de actividad'


        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)

        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
       

        except:
            nombre_cliente = ''
           
            
        controlador = type(datos_cliente)==str
        if controlador == False:
            #------------------------------- PRIMERA PARTE --------------------------------
            #           Calculando participaciones y colocando etiquetas sectoriales
            #------------------------------------------------------------------------------
            # Buscamos los clasificadores del merval y spy
            composicion_merval=pd.read_excel(f'{directorio_composicion}/{archivo_composicion_merval}.xlsx')
            composicion_merval.set_index('Ticket',inplace=True)
            
            composicion_spy=pd.read_excel(f'{directorio_composicion}/{archivo_composicion_spy}.xlsx')
            composicion_spy.set_index('Ticket',inplace=True)
            
            
            # Traemos la cartera a fecha de cierre y calculamos la participacion de cada 'Especie'
            cartera=fc.composicion_cartera_ieb(fecha_cierre = fecha_cierre, alyc = alyc,
                                                dni = dni, nombre_cliente = nombre_cliente,
                                                numero_interno = numero_interno,
                                                usuario = usuario)
            
            
            # Corregimos la cartera por si existe liquidez en pesos negativa. Esto lo hacemos
            # por que de lo contrario, el codigo no podra graficar el numero negativo.
            if cartera.loc['liquidez_pesos','Cantidad']<0:
                cartera.loc['liquidez_pesos','Cantidad']=0
            
            cartera['participacion']=cartera.Cantidad*cartera.iloc[:,1]
            cartera['participacion']=cartera['participacion']/cartera.participacion.sum()
            
            cartera['sector']=str(0)
            
            
            # Se coloca la etiqueta a cada 'Especie'
            for i in cartera.index:
                try:
                    cartera.loc[i,'sector']=composicion_merval.loc[i,'Sector']
                except:
                    try:
                        cartera.loc[i,'sector']=composicion_spy.loc[i,'Sector']
                    except:
                        if i=='liquidez_usd':
                            cartera.loc[i,'sector']='Liquidez en divisas'
                        elif i=='liquidez_pesos':
                            cartera.loc[i,'sector']='Liquidez en pesos'
                        else:
                            cartera.loc[i,'sector']='Otro'
            
            
            
            
            #------------------------------- SEGUNDA PARTE --------------------------------
            #                   Construyendo las carteras a graficar
            #------------------------------------------------------------------------------
            # Obtenemos la participacion para cada sector.
            cartera_sector=cartera.groupby('sector').participacion.sum()
            cartera_sector=pd.DataFrame(cartera_sector)
            cartera_sector.sort_values(by='participacion',ascending=False,inplace=True)
            
            liquidez_pesos=cartera_sector.loc[(cartera_sector.index=='Liquidez en pesos')].copy()
            liquidez_divisas=cartera_sector.loc[(cartera_sector.index=='Liquidez en divisas')].copy()
            
            cartera_sector.drop(['Liquidez en pesos','Liquidez en divisas'],axis=0,inplace=True)
            
            cartera_sector=pd.concat([cartera_sector,liquidez_pesos,liquidez_divisas])
            
            
            # Formamos las principales secciones de clasficacion: Liquidez, Principales, y Resto
            cartera_papeles=cartera_sector.drop(['Liquidez en pesos','Liquidez en divisas'],
                                                                            axis=0).copy()
            cartera_liquidez=pd.DataFrame()
            cartera_liquidez['participacion']=0
            cartera_liquidez['sector']=0
            cartera_liquidez.set_index('sector',inplace=True)
            cartera_liquidez.loc['Liquidez']=liquidez_pesos.iloc[0,0]+liquidez_divisas.iloc[0,0]
            
            if len(cartera_papeles)>=5:
                cartera_principales=cartera_papeles.iloc[:5,:].copy()
            
                cartera_resto2=cartera_papeles.iloc[5:,:].copy()
                
                cartera_resto=pd.DataFrame()
                cartera_resto['participacion']=0
                cartera_resto['sector']=0
                cartera_resto.set_index('sector',inplace=True)
                cartera_resto.loc['Resto']=cartera_resto2.participacion.sum()
            
                cartera_central=pd.concat([cartera_principales,cartera_resto,cartera_liquidez])  
                
            else:
                cartera_central=pd.concat([cartera_papeles,cartera_liquidez])  
                cartera_resto=pd.DataFrame()
                cartera_resto2=pd.DataFrame()
            
            
            # Desagregamos las carteras Resto y liquidez, recalculando su participacion 
            liquidez_cartera=cartera.iloc[-2:,:].participacion.copy()
            liquidez_cartera=pd.DataFrame(liquidez_cartera)
            liquidez_cartera.loc['Pesos']=liquidez_cartera.loc['liquidez_pesos','participacion']
            liquidez_cartera.loc['Divisas']=liquidez_cartera.loc['liquidez_usd','participacion']
            liquidez_cartera.drop(['liquidez_pesos','liquidez_usd'],axis=0,inplace=True)
            
            if cartera_liquidez.iloc[0,0]!=0:
                liquidez_cartera.participacion=liquidez_cartera.participacion/cartera_liquidez.iloc[0,0]
            
            else:
                liquidez_cartera.participacion=0
                
            if len(cartera_papeles)>=5:
                cartera_resto2.participacion=cartera_resto2.participacion/cartera_resto.iloc[0,0]
                
            else:
                cartera_resto2.participacion=0
                
            
                
            
            #------------------------------- TERCERA PARTE --------------------------------
            #               Graficando la composicion de la cartera central
            #------------------------------------------------------------------------------
            # Se crea la grafica de dona de la cartera central
            colors = [ '#FF8A80', '#FFCC80', '#FFFF8D', '#CCFF90', '#A7FFEB',
                '#80D8FF', '#82B1FF', '#B388FF', '#FF8A65', '#FFD180',
                '#FFE57F', '#C5E1A5', '#B2FF59', '#69F0AE', '#84FFFF',
                '#80D8FF', '#82B1FF', '#B388FF', '#FF80AB', '#FF9E80']
            
            
            # # Grafica de dona
            if cartera_central.iloc[0,0]!=0:
                fig, ax = plt.subplots(figsize=(15,15))
                ax.pie(cartera_central.participacion, labels=cartera_central.index
                        , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
                        ,textprops={'fontsize': 23},colors=colors)
                ax.axis('equal')
                
                # Ajustar el tamaño de la fuente del título
                ax.set_title(f'Composición sectorial de la cartera', fontsize=40)
            
            
            
            
            # # ------------------------------- CUARTA PARTE ---------------------------------
            # #       Graficando la composicion de las sub-carteras: Resto y liquidez
            # #------------------------------------------------------------------------------
            # # Se crea la grafica de dona de la cartera liquidez
            # colors = [ '#FF8A80', '#FFCC80', '#FFFF8D', '#CCFF90', '#A7FFEB',
            #     '#80D8FF', '#82B1FF', '#B388FF', '#FF8A65', '#FFD180',
            #     '#FFE57F', '#C5E1A5', '#B2FF59', '#69F0AE', '#84FFFF',
            #     '#80D8FF', '#82B1FF', '#B388FF', '#FF80AB', '#FF9E80']
            
            # if cartera_liquidez.iloc[0,0]!=0:
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(liquidez_cartera.participacion, labels=liquidez_cartera.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de la liquidez', fontsize=40)
            
            
            # # Se crea la grafica de dona de la cartera resto
            # if cartera_resto2.empty==False:
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(cartera_resto2.participacion, labels=cartera_resto2.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de la categoría "Resto"', fontsize=40)
            
            
            # # Se construye la grafica que desagrega la categoria otro, si corresponde.
            # if len(cartera.loc[cartera.sector=='Otro'])>0:
            #     cartera_otro=cartera.loc[cartera.sector=='Otro'].copy()
            #     cartera_otro.participacion = cartera_otro.participacion / cartera_otro.participacion.sum()
            
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(cartera_otro.participacion, labels=cartera_otro.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de Otro', fontsize=40)
                
            else:
                cartera_central = pd.DataFrame()

        else:
            cartera_central = datos_cliente    

    except:
        cartera_central = 'Introduzca un usuario válido: entero entre 1 y 6'






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def grafica_composicion_bull(fecha_cierre, alyc = '', dni = 0, numero_interno = 0,
                        nombre_cliente = '', usuario = 1):
    """
    ---------------------------------------------------------------------------
                                  ¿QUE HACE EL CODIGO?
    Redefine la cartera en terminos sectoriales, calculando la participacion
    correspondiente y, finalmente, graficando el resultado.
    ---------------------------------------------------------------------------
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es el nombre de la alyc donde esta la cuenta del cliente: Bull, Ieb, o
        Balanz. Se puede escribi con mayuscula y acentos.  
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero interno que la empresa asigna al cliente.  
        Valor por defecto: 0.

    dni : tipo integer
    
        DESCRIPCION
        Es el dni del cliente. No debe escribirse separando con puntos o comas.
        Valor por defecto: 0.
        
        
    Resultado
    -------
    Elabora tres graficas de donas. Una para la cartera, otra para desomponer la
    liquidez entre pesos y divisas, y otra para desagregar la tenencia mas peque-
    ña entre los papeles correspondientes.
    
    """
    
    try:

        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        import matplotlib.pyplot as plt 
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
        from datetime import datetime
        
       
        
        # -----------------------------------------------------------------------------
        directorio_composicion=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        archivo_composicion_merval='Clasificacion del MERVAL por rama de actividad'
        archivo_composicion_spy='Clasificacion de algunos papeles del SPX por rama de actividad'
        
        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)
        
        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
            numero_cliente = datos_cliente.loc['numero cliente','Datos del cliente']  
            fecha_movimientos = datos_cliente.loc['fecha movimientos','Datos del cliente']
        
        except:
            nombre_cliente = ''
            numero_cliente = 0
            fecha_movimientos = ''
        
        
        
        
        controlador = type(datos_cliente)==str
        if controlador == False:
            #------------------------------- PRIMERA PARTE --------------------------------
            #           Calculando participaciones y colocando etiquetas sectoriales
            #------------------------------------------------------------------------------
            # Buscamos los clasificadores del merval y spy
            composicion_merval=pd.read_excel(f'{directorio_composicion}/{archivo_composicion_merval}.xlsx')
            composicion_merval.set_index('Ticket',inplace=True)
            
            composicion_spy=pd.read_excel(f'{directorio_composicion}/{archivo_composicion_spy}.xlsx')
            composicion_spy.set_index('Ticket',inplace=True)
            
            
            # Traemos la cartera a fecha de cierre y calculamos la participacion de cada 'Especie'
            cartera=fc.composicion_cartera_bull(fecha_cierre=fecha_cierre, alyc=alyc,
                                                dni=dni, numero_interno=numero_interno,
                                                nombre_cliente=nombre_cliente,
                                                usuario = usuario)
            
            # Identificamos los contratos de futuros para posteriormente colocarles el precio
            # simbolico de $ 1.
            lista_futuros = []

            for i in cartera.index:
                if i[:3] == "DLR":
                    lista_futuros.append(i)
                    
            fecha_cierre = datetime.strptime(fecha_cierre, "%Y-%m-%d")
                   
            for i in lista_futuros:
                cartera.loc[i,fecha_cierre] = float(1)
                
                
            # Corregimos la cartera por si existe liquidez en pesos negativa. Esto lo hacemos
            # por que de lo contrario, el codigo no podra graficar el numero negativo.
            if cartera.loc['liquidez_pesos','Cantidad']<0:
                cartera.loc['liquidez_pesos','Cantidad']=0
            
            
            # Se continua con el calculo de proporciones
            if len(cartera.loc[cartera.index=='MEP'])>0:
                cartera.drop('MEP',axis=0,inplace=True) 
            
            cartera.drop('fecha mep',axis=1,inplace=True)
            cartera.drop('PRECIO MEP',axis=0,inplace=True)
                
            cartera['participacion']=cartera.Cantidad*cartera.iloc[:,1]
            cartera['participacion']=cartera['participacion']/cartera.participacion.sum()
            
            cartera['sector']=str(0)
            
            
            # Se coloca la etiqueta a cada 'Especie'
            for i in cartera.index:
                try:
                    cartera.loc[i,'sector']=composicion_merval.loc[i,'Sector']
                except:
                    try:
                        cartera.loc[i,'sector']=composicion_spy.loc[i,'Sector']
                    except:
                        if i=='liquidez_usd':
                            cartera.loc[i,'sector']='Liquidez en divisas'
                        elif i=='liquidez_pesos':
                            cartera.loc[i,'sector']='Liquidez en pesos'
                        else:
                            cartera.loc[i,'sector']='Otro'
            
            
            
            
            #------------------------------- SEGUNDA PARTE --------------------------------
            #                   Construyendo las carteras a graficar
            #------------------------------------------------------------------------------
            # Obtenemos la participacion para cada sector.
            cartera_sector=cartera.groupby('sector').participacion.sum()
            cartera_sector=pd.DataFrame(cartera_sector)
            cartera_sector.sort_values(by='participacion',ascending=False,inplace=True)
            
            liquidez_pesos=cartera_sector.loc[(cartera_sector.index=='Liquidez en pesos')].copy()
            liquidez_divisas=cartera_sector.loc[(cartera_sector.index=='Liquidez en divisas')].copy()
            
            cartera_sector.drop(['Liquidez en pesos','Liquidez en divisas'],axis=0,inplace=True)
            
            cartera_sector=pd.concat([cartera_sector,liquidez_pesos,liquidez_divisas])
            
            
            # Formamos las principales secciones de clasficacion: Liquidez, Principales, y Resto
            cartera_papeles=cartera_sector.drop(['Liquidez en pesos','Liquidez en divisas'],
                                                                            axis=0).copy()
            cartera_liquidez=pd.DataFrame()
            cartera_liquidez['participacion']=0
            cartera_liquidez['sector']=0
            cartera_liquidez.set_index('sector',inplace=True)
            cartera_liquidez.loc['Liquidez']=liquidez_pesos.iloc[0,0]+liquidez_divisas.iloc[0,0]
            
            if len(cartera_papeles)>=5:
                cartera_principales=cartera_papeles.iloc[:5,:].copy()
            
                cartera_resto2=cartera_papeles.iloc[5:,:].copy()
                
                cartera_resto=pd.DataFrame()
                cartera_resto['participacion']=0
                cartera_resto['sector']=0
                cartera_resto.set_index('sector',inplace=True)
                cartera_resto.loc['Resto']=cartera_resto2.participacion.sum()
            
                cartera_central=pd.concat([cartera_principales,cartera_resto,cartera_liquidez])  
                
            else:
                cartera_central=pd.concat([cartera_papeles,cartera_liquidez])  
                cartera_resto=pd.DataFrame()
                cartera_resto2=pd.DataFrame()
            
            
            # Desagregamos las carteras Resto y liquidez, recalculando su participacion 
            liquidez_cartera=cartera.iloc[-2:,:].participacion.copy()
            liquidez_cartera=pd.DataFrame(liquidez_cartera)
            liquidez_cartera.loc['Pesos']=liquidez_cartera.loc['liquidez_pesos','participacion']
            liquidez_cartera.loc['Divisas']=liquidez_cartera.loc['liquidez_usd','participacion']
            liquidez_cartera.drop(['liquidez_pesos','liquidez_usd'],axis=0,inplace=True)
            
            if cartera_liquidez.iloc[0,0]!=0:
                liquidez_cartera.participacion=liquidez_cartera.participacion/cartera_liquidez.iloc[0,0]
            
            else:
                liquidez_cartera.participacion=0
                
            if len(cartera_papeles)>=5:
                cartera_resto2.participacion=cartera_resto2.participacion/cartera_resto.iloc[0,0]
                
            else:
                cartera_resto2.participacion=0
                
            
                
            
            #------------------------------- TERCERA PARTE --------------------------------
            #               Graficando la composicion de la cartera central
            #------------------------------------------------------------------------------
            # Se crea la grafica de dona de la cartera central
            colors = [ '#FF8A80', '#FFCC80', '#FFFF8D', '#CCFF90', '#A7FFEB',
                '#80D8FF', '#82B1FF', '#B388FF', '#FF8A65', '#FFD180',
                '#FFE57F', '#C5E1A5', '#B2FF59', '#69F0AE', '#84FFFF',
                '#80D8FF', '#82B1FF', '#B388FF', '#FF80AB', '#FF9E80']
            
            
            # # Grafica de dona
            if cartera_central.iloc[0,0]!=0:
                fig, ax = plt.subplots(figsize=(15,15))
                ax.pie(cartera_central.participacion, labels=cartera_central.index
                        , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
                        ,textprops={'fontsize': 23},colors=colors)
                ax.axis('equal')
                
                # Ajustar el tamaño de la fuente del título
                ax.set_title(f'Composición sectorial de la cartera', fontsize=40)
                
            
            
            
            # # ------------------------------- CUARTA PARTE ---------------------------------
            # #       Graficando la composicion de las sub-carteras: Resto y liquidez
            # #------------------------------------------------------------------------------
            # # Se crea la grafica de dona de la cartera liquidez
            # colors = [ '#FF8A80', '#FFCC80', '#FFFF8D', '#CCFF90', '#A7FFEB',
            #     '#80D8FF', '#82B1FF', '#B388FF', '#FF8A65', '#FFD180',
            #     '#FFE57F', '#C5E1A5', '#B2FF59', '#69F0AE', '#84FFFF',
            #     '#80D8FF', '#82B1FF', '#B388FF', '#FF80AB', '#FF9E80']
            
            # if cartera_liquidez.iloc[0,0]!=0:
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(liquidez_cartera.participacion, labels=liquidez_cartera.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de la liquidez', fontsize=40)
            
            
            # # Se crea la grafica de dona de la cartera resto
            # if cartera_resto2.empty==False:
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(cartera_resto2.participacion, labels=cartera_resto2.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de la categoría "Resto"', fontsize=40)
            
            
            # # Se construye la grafica que desagrega la categoria otro, si corresponde.
            # if len(cartera.loc[cartera.sector=='Otro'])>0:
            #     cartera_otro=cartera.loc[cartera.sector=='Otro'].copy()
            #     cartera_otro.participacion = cartera_otro.participacion / cartera_otro.participacion.sum()
            
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(cartera_otro.participacion, labels=cartera_otro.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de Otro', fontsize=40)
                
            else:
                cartera_central = pd.DataFrame()

        else:
            cartera_central = datos_cliente

    except:
        cartera_central = 'Introduzca un usuario válido: entero entre 1 y 6'






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def grafica_composicion_balanz(fecha_cierre, alyc = '', dni = 0, numero_interno = 0,
                               nombre_cliente = '', usuario = 1):
    """
    ---------------------------------------------------------------------------
                                  ¿QUE HACE EL CODIGO?
    Redefine la cartera en terminos sectoriales, calculando la participacion
    correspondiente y, finalmente, graficando el resultado.
    ---------------------------------------------------------------------------
    
    Parametros
    ----------
    fecha_cierre : tipo string.
    
        DESCRIPCION.
        Indica el momento donde deseamos conocer la composicion de la cartera
        Ejemplo: '2023-02-24'. 
        
    alyc : tipo string.
    
        DESCRIPCION.
        Es el nombre de la alyc donde esta la cuenta del cliente: Bull, Ieb, o
        Balanz. Se puede escribi con mayuscula y acentos.  
        Valor por defecto: ''.
        
    nombre_cliente : tipo string.
    
        DESCRIPCION.
        Es el nombre del cliente, debe escribirse tal cual esta en el archivo 
        de donde se obtienen los movimientos y la tenencia.
        Ejemplo: 'Marco Aurelio'.
        
    numero_interno : tipo integer.
    
        DESCRIPCION.
        Es el numero interno que la empresa asigna al cliente.  
        Valor por defecto: 0.

    dni : tipo integer
    
        DESCRIPCION
        Es el dni del cliente. No debe escribirse separando con puntos o comas.
        Valor por defecto: 0.
        
        
    Resultado
    -------
    Elabora tres graficas de donas. Una para la cartera, otra para desomponer la
    liquidez entre pesos y divisas, y otra para desagregar la tenencia mas peque-
    ña entre los papeles correspondientes.
    
    """
    
    try:
  
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''

        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c'

        # -----------------------------------------------------------------------------
        import pandas as pd
        import matplotlib.pyplot as plt 
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc


        # -----------------------------------------------------------------------------
        directorio_composicion=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes'
        archivo_composicion_merval='Clasificacion del MERVAL por rama de actividad'
        archivo_composicion_spy='Clasificacion de algunos papeles del SPX por rama de actividad'

        # -----------------------------------------------------------------------------           
        # Sub Parametros
        datos_cliente = fc.cliente(alyc = alyc, nombre_cliente = nombre_cliente, 
                                   numero_interno = numero_interno, dni = dni,
                                   usuario = usuario)

        try:
            nombre_cliente = datos_cliente.loc['nombre cliente','Datos del cliente']
          
        except:
            nombre_cliente = ''
       


        controlador = type(datos_cliente)==str
        if controlador == False:
            #------------------------------- PRIMERA PARTE --------------------------------
            #           Calculando participaciones y colocando etiquetas sectoriales
            #------------------------------------------------------------------------------
            # Buscamos los clasificadores del merval y spy
            composicion_merval=pd.read_excel(f'{directorio_composicion}/{archivo_composicion_merval}.xlsx')
            composicion_merval.set_index('Ticket',inplace=True)
            
            composicion_spy=pd.read_excel(f'{directorio_composicion}/{archivo_composicion_spy}.xlsx')
            composicion_spy.set_index('Ticket',inplace=True)
            
            
            # Traemos la cartera a fecha de cierre y calculamos la participacion de cada 'Especie'
            cartera=fc.composicion_cartera_bal(fecha_cierre=fecha_cierre, alyc=alyc,
                                                dni=dni, numero_interno=numero_interno,
                                                nombre_cliente=nombre_cliente,
                                                usuario = usuario)
            
            
            # Corregimos la cartera por si existe liquidez en pesos negativa. Esto lo hacemos
            # por que de lo contrario, el codigo no podra graficar el numero negativo.
            if cartera.loc['liquidez_pesos','Cantidad']<0:
                cartera.loc['liquidez_pesos','Cantidad']=0
                
            cartera['participacion']=cartera.Cantidad*cartera.iloc[:,1]
            cartera['participacion']=cartera['participacion']/cartera.participacion.sum()
            
            cartera['sector']=str(0)
            
            
            # Se coloca la etiqueta a cada 'Especie'
            for i in cartera.index:
                try:
                    cartera.loc[i,'sector']=composicion_merval.loc[i,'Sector']
                except:
                    try:
                        cartera.loc[i,'sector']=composicion_spy.loc[i,'Sector']
                    except:
                        if i=='liquidez_usd':
                            cartera.loc[i,'sector']='Liquidez en divisas'
                        elif i=='liquidez_pesos':
                            cartera.loc[i,'sector']='Liquidez en pesos'
                        else:
                            cartera.loc[i,'sector']='Otro'
            
            
            
            
            #------------------------------- SEGUNDA PARTE --------------------------------
            #                   Construyendo las carteras a graficar
            #------------------------------------------------------------------------------
            # Obtenemos la participacion para cada sector.
            cartera_sector=cartera.groupby('sector').participacion.sum()
            cartera_sector=pd.DataFrame(cartera_sector)
            cartera_sector.sort_values(by='participacion',ascending=False,inplace=True)
            
            
            # Lo siguiente se hace para que la liquidez en pesos y en usd queden al final
            # de la lista, incluso cuando tienen mucha participacion
            liquidez_pesos=cartera_sector.loc[(cartera_sector.index=='Liquidez en pesos')].copy()
            liquidez_divisas=cartera_sector.loc[(cartera_sector.index=='Liquidez en divisas')].copy()
            
            cartera_sector.drop(['Liquidez en pesos','Liquidez en divisas'],axis=0,inplace=True)
            
            cartera_sector=pd.concat([cartera_sector,liquidez_pesos,liquidez_divisas])
            
            
            # Formamos las principales secciones de clasficacion: Liquidez, Principales, y Resto
            cartera_papeles=cartera_sector.drop(['Liquidez en pesos','Liquidez en divisas'],
                                                                            axis=0).copy()
            cartera_liquidez=pd.DataFrame()
            cartera_liquidez['participacion']=0
            cartera_liquidez['sector']=0
            cartera_liquidez.set_index('sector',inplace=True)
            cartera_liquidez.loc['Liquidez']=liquidez_pesos.iloc[0,0]+liquidez_divisas.iloc[0,0]
            
            if len(cartera_papeles)>=5:
                cartera_principales=cartera_papeles.iloc[:5,:].copy()
            
                cartera_resto2=cartera_papeles.iloc[5:,:].copy()
                
                cartera_resto=pd.DataFrame()
                cartera_resto['participacion']=0
                cartera_resto['sector']=0
                cartera_resto.set_index('sector',inplace=True)
                cartera_resto.loc['Resto']=cartera_resto2.participacion.sum()
            
                cartera_central=pd.concat([cartera_principales,cartera_resto,cartera_liquidez])  
                
            else:
                cartera_central=pd.concat([cartera_papeles,cartera_liquidez])  
                cartera_resto=pd.DataFrame()
                cartera_resto2=pd.DataFrame()
            
            
            # Desagregamos las carteras Resto y liquidez, recalculando su participacion 
            liquidez_cartera=cartera.iloc[-2:,:].participacion.copy()
            liquidez_cartera=pd.DataFrame(liquidez_cartera)
            liquidez_cartera.loc['Pesos']=liquidez_cartera.loc['liquidez_pesos','participacion']
            liquidez_cartera.loc['Divisas']=liquidez_cartera.loc['liquidez_usd','participacion']
            liquidez_cartera.drop(['liquidez_pesos','liquidez_usd'],axis=0,inplace=True)
            
            if cartera_liquidez.iloc[0,0]!=0:
                liquidez_cartera.participacion=liquidez_cartera.participacion/cartera_liquidez.iloc[0,0]
            
            else:
                liquidez_cartera.participacion=0
                
            if len(cartera_papeles)>=5:
                cartera_resto2.participacion=cartera_resto2.participacion/cartera_resto.iloc[0,0]
                
            else:
                cartera_resto2.participacion=0
                
            
                
            
            #------------------------------- TERCERA PARTE --------------------------------
            #               Graficando la composicion de la cartera central
            #------------------------------------------------------------------------------
            # Se crea la grafica de dona de la cartera central
            colors = [ '#FF8A80', '#FFCC80', '#FFFF8D', '#CCFF90', '#A7FFEB',
                '#80D8FF', '#82B1FF', '#B388FF', '#FF8A65', '#FFD180',
                '#FFE57F', '#C5E1A5', '#B2FF59', '#69F0AE', '#84FFFF',
                '#80D8FF', '#82B1FF', '#B388FF', '#FF80AB', '#FF9E80']
            
            
            # # Grafica de dona
            if cartera_central.iloc[0,0]!=0:
                fig, ax = plt.subplots(figsize=(15,15))
                ax.pie(cartera_central.participacion, labels=cartera_central.index
                        , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
                        ,textprops={'fontsize': 23},colors=colors)
                ax.axis('equal')
                
                # Ajustar el tamaño de la fuente del título
                ax.set_title(f'Composición sectorial de la cartera', fontsize=40)
            
            
            
            
            # # ------------------------------- CUARTA PARTE ---------------------------------
            # #       Graficando la composicion de las sub-carteras: Resto y liquidez
            # #------------------------------------------------------------------------------
            # # Se crea la grafica de dona de la cartera liquidez
            # colors = [ '#FF8A80', '#FFCC80', '#FFFF8D', '#CCFF90', '#A7FFEB',
            #     '#80D8FF', '#82B1FF', '#B388FF', '#FF8A65', '#FFD180',
            #     '#FFE57F', '#C5E1A5', '#B2FF59', '#69F0AE', '#84FFFF',
            #     '#80D8FF', '#82B1FF', '#B388FF', '#FF80AB', '#FF9E80']
            
            # if cartera_liquidez.iloc[0,0]!=0:
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(liquidez_cartera.participacion, labels=liquidez_cartera.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de la liquidez', fontsize=40)
            
            
            # # Se crea la grafica de dona de la cartera resto
            # if cartera_resto2.empty==False:
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(cartera_resto2.participacion, labels=cartera_resto2.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de la categoría "Resto"', fontsize=40)
            
            
            # # Se construye la grafica que desagrega la categoria otro, si corresponde.
            # if len(cartera.loc[cartera.sector=='Otro'])>0:
            #     cartera_otro=cartera.loc[cartera.sector=='Otro'].copy()
            #     cartera_otro.participacion = cartera_otro.participacion / cartera_otro.participacion.sum()
            
            #     # Grafica de dona
            #     fig, ax = plt.subplots(figsize=(15,15))
            #     ax.pie(cartera_otro.participacion, labels=cartera_otro.index
            #             , autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05, wedgeprops={'width': 0.3}
            #             ,textprops={'fontsize': 23},colors=colors)
            #     ax.axis('equal')
                
            #     # Ajustar el tamaño de la fuente del título
            #     ax.set_title(f'Composición de Otro', fontsize=40)
                
            else:
                cartera_central = pd.DataFrame()

        else:
            cartera_central = datos_cliente

    except:
        cartera_central = 'Introduzca un usuario válido: entero entre 1 y 6'






# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def rendimiento_neto(usuario, numero_interno,     # Datos de indentificacion
                          
                     fecha_cierre, fecha_inicial, # Fechas
                          
                     dias, alyc,                 # plazo y alyc
                          
                     valor_final, valor_inicial,  # valor de cartera 
                     
                     lista_honorarios, lista_plazo_honorarios, # Monto de honorarios y sus plazos
                     
                     puntos_basicos = 0.1, nombre_cliente = '', dni = 0): # parametros fijos

    """
    Esta funcion permite obtener el rendimiento neto del trimestre.
    
    Como se observa en sus argumetos, muchos valores deben obtenerse por otra via.
    
    La funcion se penso para ser utilizada exclusivamente en el script de Reportes trimestrales.
    """
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    try:
        # usuario = 4 
          
        if usuario == 1: 
            sub_directorio = 'Y'
            auxiliar = '--'
        elif usuario == 2:
            sub_directorio = 'YY'
            auxiliar = '--'
        elif usuario == 3:
            sub_directorio = 'YYY'
            auxiliar = ''
        elif usuario == 4:
            sub_directorio = 'Y_Y'
            auxiliar = ''
        elif usuario == 5:
            sub_directorio = 'YY_YY'
            auxiliar = ''
        elif usuario == 6:
            sub_directorio = 'YYY_YYY'
            auxiliar = ''
        
        directorio_funciones=f'C:/Users\{sub_directorio}\Dropbox{auxiliar}\HONORARIOS\Clientes\libreria_py_c' 
        
        # -----------------------------------------------------------------------------
        import pandas as pd
        import numpy as np
        from datetime import datetime as dt
        import sys
        sys.path.append(f'{directorio_funciones}')
        import dp_funciones_c as fc
     
        
        # -----------------------------------------------------------------------------           
        # controlador = type(datos_cliente)==str
        # if controlador == False:        
        # ----------------------------- PRIMERA PARTE ---------------------------------
        # Se obtienen los movimientos (retiros y depositos)
        # -----------------------------------------------------------------------------
        # Movimientos
        # Obtenemos la tabla de movimientos del trimestre
        fecha_cierre2 = dt.strptime(fecha_cierre, '%Y-%m-%d')
        fecha_inicial2 = dt.strptime(fecha_inicial, '%Y-%m-%d') 
        
        if alyc == 'Bull':
            movimientos = fc.depositos_retiros_bull(fecha_cierre = fecha_cierre,
                                                    fecha_inicial = fecha_inicial,
                                                    usuario = usuario,
                                                    numero_interno = numero_interno,
                                                    ctte_adm = '')  
            
            movimientos = movimientos.loc[movimientos.fecha <= fecha_cierre2].copy()
            movimientos = movimientos.loc[movimientos.fecha >= fecha_inicial2].copy()
        
        elif alyc == 'Balanz':
            movimientos = fc.depositos_retiros_balanz(fecha_cierre = fecha_cierre,
                                                      fecha_inicial = fecha_inicial,
                                                      usuario = usuario,
                                                      numero_interno = numero_interno,
                                                      ctte_adm = '')
            
            movimientos = movimientos.loc[movimientos.fecha <= fecha_cierre2].copy()
            movimientos = movimientos.loc[movimientos.fecha >= fecha_inicial2].copy()
        
        elif alyc == 'Ieb':
            movimientos = fc.depositos_retiros_ieb(fecha_cierre = fecha_cierre,
                                                    fecha_inicial = fecha_inicial,
                                                    usuario = usuario,
                                                    numero_interno = numero_interno,
                                                    ctte_adm = '')
            
            movimientos = movimientos.loc[movimientos.fecha <= fecha_cierre2].copy()
            movimientos = movimientos.loc[movimientos.fecha >= fecha_inicial2].copy()
        
        # Aplicamos mayusculas a los nombres de las columnas
        movimientos.columns = movimientos.columns.str.capitalize()
        
        # Calculamos los dias entre la fecha de cierre y cada movimiento
        movimientos['Plazo'] = int(0)
        fecha_cierre = dt.strptime(fecha_cierre, '%Y-%m-%d')
        
        for i in movimientos.index:
            movimientos.loc[i,'Plazo'] = (fecha_cierre - movimientos.loc[i,'Fecha']).days
            
        
          
        # # ----------------------------- SEGUNDA PARTE ---------------------------------
        # # Se construyen las tablas de honorarios
        # # -----------------------------------------------------------------------------
        # Creamos el dataframe de honorarios
        tabla_honorarios = pd.DataFrame()
        tabla_honorarios['monto'] = float(0)
        tabla_honorarios['plazo'] = float(0)
        
        for i in range(50):
            tabla_honorarios.loc[i] = float(0)
        
        for i in range(len(lista_honorarios)):
            tabla_honorarios.loc[i,'monto'] = lista_honorarios[i]
            
        for i in range(len(lista_plazo_honorarios)):
            tabla_honorarios.loc[i,'plazo'] = lista_plazo_honorarios[i]
        
        
        
        # -----------------------------------------------------------------------------
        # ----------------------------- CUARTA PARTE ----------------------------------
        # Se calcula la TIR neta de la cartera 
        # -----------------------------------------------------------------------------
        lista_n_error = []
        listado_n_tir = []
        
        for tir in np.arange(-1,1,puntos_basicos/10000):
            
            termino_dep = 0 # elemento que acumula la suma de todos los depositos capitalizados 
            termino_ret = 0 # elemento que acumula la suma de todos los retiros capitalizados   
            termino_hon = 0 # elemento que acumula la suma de todos los honorarios capitalizados
            
            valor_inicial_bis = valor_inicial
            
            for i in range(len(movimientos)):                
                # Obteniendo depositos, retiros, y plazos
                monto_dep = movimientos.Depositos[i]
                monto_ret = movimientos.Retiros[i]
                plazo = movimientos.Plazo[i]
           
                # Acumulacion de los depositos y retiros capitalizados
                termino_dep = termino_dep + monto_dep * (1 + tir) ** plazo  
                termino_ret = termino_ret + monto_ret * (1 + tir) ** plazo 
                
            for i in range(len(tabla_honorarios)):
                monto_hon = tabla_honorarios.monto[i]
                plazo_hon = tabla_honorarios.plazo[i]
                
                # Acumulacion de honorarios
                termino_hon = termino_hon + monto_hon * (1 + tir) ** plazo_hon
                
            # Capitalizacion del valor inicial y de los honorarios
            valor_inicial_bis = valor_inicial_bis * (1+tir) ** dias
            
            # Calculo del error
            error = valor_final + termino_ret - (valor_inicial_bis + termino_dep) - termino_hon
        
            lista_n_error.append(error)
            listado_n_tir.append(tir)
            
        lista_n = pd.DataFrame()    
        lista_n['tir_diaria'] = listado_n_tir
        lista_n['error'] = lista_n_error
        lista_n['error_abs']=lista_n['error'].abs()
        lista_n.sort_values(by='error_abs',inplace=True)
        lista_n.drop(axis=1,columns='error_abs',inplace=True)
        
        # Ahora corregimos este listado para evitar problemas del tipo "controversia del
        # capital", es decir, que al cobrar honorarios la tir sea mayor que cuando no se
        # cobran honorarios. El asunto se resuelve en tres pasos:
        # PRIMERO. Slicing 10 primeros con errores mas pequeños
        lista_n = lista_n.iloc[:10,:]
        
        # SEGUNDO. Ordenar de menor a mayor por TIR y 5 primeros TIR
        lista_n.sort_values(by='tir_diaria',inplace=True)
        lista_n = lista_n.iloc[:5,:]
        
        # TERCERO. Ordenamos de menor a mayor por error absoluto
        lista_n['error_abs'] = lista_n['error'].abs()
        lista_n.sort_values(by='error_abs',inplace=True)
        lista_n.drop(axis=1,columns='error_abs',inplace=True)
        
        
         
        # ----------------------------- QUINTA PARTE ----------------------------------
        # Se crea un diccionario que contiene el resultado
        # -----------------------------------------------------------------------------
        # Resultado
        tir_d_neta = lista_n.iloc[0,0]
           
        tir_a_neta = np.exp(dias * np.log(1 + tir_d_neta)) - 1
        
        rendimiento_neto = tir_a_neta
        
    except:
        rendimiento_neto = 'Introduzca un usuario vÃ¡lido: entero entre 1 y 6'
    
    
    return rendimiento_neto  




