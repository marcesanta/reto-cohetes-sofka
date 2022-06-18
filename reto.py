class Cohete():
    def __init__(self, para_que_sirve, tipo_de_combustible, pais_o_fabricante, nombre_de_la_lanzadera, 
                    peso_de_la_lanzadera, empuje_de_la_lanzadera, capacidad_de_carga, fecha_de_fabricacion, 
                    fecha_de_salida, altura, potencia, satelite=None, sonda=None, tripulada=None):
        
        self.tipo_de_combustible = tipo_de_combustible
        self.pais_o_fabricante = pais_o_fabricante
        self.nombre_de_la_lanzadera = nombre_de_la_lanzadera
        self.peso_de_la_lanzadera = peso_de_la_lanzadera
        self.empuje_de_la_lanzadera = empuje_de_la_lanzadera
        self.capacidad_de_carga = capacidad_de_carga
        self.fecha_de_fabricacion = fecha_de_fabricacion
        self.fecha_de_salida = fecha_de_salida
        self.altura = altura
        self.potencia = potencia
        self.para_que_sirve = para_que_sirve
        self.satelite = satelite
        self.sonda = sonda
        self.tripulada = tripulada


saturno_v = Cohete(
    para_que_sirve="Principal carga: los Apolo", 
    tipo_de_combustible="Combustible líquido", 
    pais_o_fabricante="EEUU", 
    nombre_de_la_lanzadera="Saturno V", 
    peso_de_la_lanzadera="3500 toneladas", 
    empuje_de_la_lanzadera= "2900 toneladas",
    capacidad_de_carga= "118 toneladas",
    fecha_de_fabricacion="1967", 
    fecha_de_salida="1973",
    altura="100 metros",
    potencia= "32000x5",
    tripulada = "Apolo 6"
)

transbordador_espacial = Cohete(
    para_que_sirve="Colocar en orbita al Mercury", 
    tipo_de_combustible="LOX y RP-1", 
    pais_o_fabricante="EEUU", 
    nombre_de_la_lanzadera="Atlas", 
    peso_de_la_lanzadera="116000 kg", 
    empuje_de_la_lanzadera= "1590 kN",
    capacidad_de_carga= "No especifica",
    fecha_de_fabricacion="La primera prueba fue en 1957", 
    fecha_de_salida="No especifica",
    altura="22,9 metros",
    potencia= "No especifica",
    tripulada = "Mercury"
)