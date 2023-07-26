from ... import ElementsType
from .. import Provider as BaseProvider


class Provider(BaseProvider):
    # Source:
    # https://www.ilo.org/public/spanish/bureau/stat/isco/docs/struct08.xls
    jobs: ElementsType[str] = (
        "Abogado",
        "Acarreador de agua",
        "Recolector de leña",
        "Ayudante de cámara",
        "Actor",
        "Administrador de sistemas",
        "Agente de administración tributaria",
        "Agente de aduanas",
        "Inspector de fronteras",
        "Agente de bolsa",
        "Agente de compras",
        "Consignatario",
        "Agente de empleo",
        "Agente de seguros",
        "Agente de servicios de expedición de licencias y permisos",
        "Agente de servicios de seguridad social",
        "Agente inmobiliario",
        "Agricultor",
        "Agrónomo",
        "Albañil",
        "Alfarero",
        "Analista de gestión y organización",
        "Analista de sistemas",
        "Analista financiero",
        "Aparejador",
        "Empalmador de cables",
        "Curtidor",
        "Apicultor",
        "Sericultor",
        "Archivista",
        "Curador de museos",
        "Arquitecto",
        "Paisajista",
        "Artesano",
        "Artista plástico",
        "Asesor financiero y en inversiones",
        "Asesor de inversiones",
        "Asistente de venta",
        "Astrólogo",
        "Adivinador",
        "Deportista",
        "Audiólogo",
        "Escritor",
        "Auxiliar de maestro",
        "Auxiliar de servicio de abordo",
        "Auxiliar laico de las religión",
        "Avicultor",
        "Ayudante de ambulancia",
        "Ayudante de cocina",
        "Bailarín",
        "Coreógrafo",
        "Barnizador",
        "Barrendero",
        "Bibliotecarios",
        "Focumentalista",
        "Biólogo",
        "Botánico",
        "Zoólogo",
        "Zoólogo",
        "Bombero",
        "Buzo",
        "Cajero de banco",
        "Cajero",
        "Tipógrafo",
        "Camarero de barra",
        "Camarero de mesa",
        "Capitán decubierta",
        "Oficial de cubierta",
        "Carnicero",
        "Pescadero",
        "Carpintero",
        "Cartógrafo",
        "Agrimensor",
        "Catador de alimentos y bebidas",
        "Catador de bebidas",
        "Cazador",
        "Tramper",
        "Chapista",
        "Calderero",
        "Chef",
        "Clasificador de desechos",
        "Clasificador de productos",
        "Cobrador",
        "Cocinero",
        "Cocinero de comidas rápidas",
        "Codificador de datos",
        "Corrector de pruebas de imprenta",
        "Comerciante de tiendas",
        "Conductor de autobús",
        "Conductor de tranvía",
        "Conductor de automóviles",
        "Conductor de taxis",
        "Conductor de camiones pesados",
        "Conductor de motocicletas",
        "Conductor de vehículos accionados a pedal o a brazo",
        "Conductor de vehículos y máquinas de tracción animal",
        "Conserje",
        "Constructor de casas",
        "Contable",
        "Controlador de instalaciones de procesamiento de productos químicos",
        "Controlador de procesos",
        "Controlador de tráfico aéreo",
        "Costurero",
        "Bordador",
        "Criador de ganado",
        "Cristalero",
        "Cuidador de animales",
        "Cuidador de niños",
        "Declarante de aduana",
        "Gestor de aduana",
        "Delineante",
        "Dibujante técnico",
        "Demostrador de tiendas",
        "Dentista",
        "Ayudante de odontología",
        "Desarrollador de software",
        "Desarrollador Web y multimedia",
        "Nutricionista",
        "Dinamitero",
        "Director de servicios de bienestar social",
        "Director de cine",
        "Director de teatro",
        "Director de empresas de abastecimiento, distribución y afines",
        "Director de empresas de construcción",
        "Director de explotaciones de minería",
        "Director de industrias manufactureras",
        "Director de investigación y desarrollo",
        "Director de políticas y planificación",
        "Director de producción agropecuaria y silvicultura",
        "Director de producción de piscicultura y pesca",
        "Director de publicidad y relaciones públicas",
        "Director de recursos humanos",
        "Director de servicios de cuidado de las personas de edad",
        "Director de servicios de cuidados infantiles",
        "Director de servicios de educación",
        "Director de servicios de salud",
        "Director de servicios de tecnología de la información y las comunicaciones",
        "Director de ventas y comercialización",
        "Director financiero",
        "Gerente general",
        "Diseñador de productos",
        "Diseñador de prendas",
        "Diseñador gráfico",
        "Diseñador multimedia",
        "Diseñador de bases de datos",
        "Administrador de bases de datos",
        "Diseñador de interior",
        "Decorador de interior",
        "Ebanista",
        "Economista",
        "Ecónomo y mayordomos domésticos",
        "Mayordomo doméstico",
        "Educador para necesidades especiales",
        "Electricista de obras",
        "Electrotécnico",
        "Empacador manual",
        "Empleado de agencia de viajes",
        "Empleado de archivos",
        "Empleado de biblioteca",
        "Empleado de centro de llamadas",
        "Empleado de contabilidad y cálculo de costos",
        "Empleado de control de abastecimientos e inventario",
        "Empleado de servicios de apoyo a la producción",
        "Empleado de servicios de correos",
        "Empleado de servicios de transporte",
        "Empleado de servicios estadísticos, financieros y de seguros",
        "Empleado de ventanillas de informaciones",
        "Empleado del servicio de personal",
        "Empleado encargado de las nóminas",
        "Encuadernador",
        "Ensamblador de equipos eléctricos",
        "Ensamblador de equipos electrónicos",
        "Ensamblador de maquinaria mecánica",
        "Entrenador deportivo",
        "Árbitro deportivo",
        "Entrevistador de encuestas",
        "Entrevistador de investigaciones de mercados",
        "Escribiente público",
        "Especialista en formación del personal",
        "Especialista en métodos pedagógicos",
        "Especialista en políticas de administración",
        "Especialista en políticas y servicios de personal",
        "Especialista en tratamientos de belleza",
        "Expendedor de gasolineras",
        "Fabricante de instrumentos musicales",
        "Afinador de instrumentos musicales",
        "Farmacéutico",
        "Filósofo",
        "Historiador",
        "Especialista en ciencias políticas",
        "Físico",
        "Astrónomos",
        "Fisioterapeuta",
        "Fontanero",
        "Fotógrafo",
        "Fumigador",
        "Controlador de plagas y malas hierbas",
        "Geólogo",
        "Ggeofísico",
        "Gerente de centros deportivos, de esparcimiento y culturales",
        "Gerente de comercios al por mayor y al por menor",
        "Gerente de hoteles o restaurantes",
        "Gerente de sucursales de bancos, de servicios financieros y de seguros",
        "Grabador de datos",
        "Guardafrenos",
        "Guardagujas",
        "Agente de maniobras",
        "Guardián de prisión",
        "Guardia de protección",
        "Guía de turismo",
        "Herramentista",
        "Herrero",
        "Gorjadore",
        "Impresor",
        "Ingeniero civil",
        "Ingeniero de minas",
        "Ingeniero metalúrgico",
        "Ingeniero electricista",
        "Ingeniero electrónico",
        "Ingeniero en telecomunicaciones",
        "Ingeniero industrial",
        "Ingeniero mecánico",
        "Ingeniero medioambiental",
        "Ingeniero químico",
        "Inspector de la salud laboral",
        "Inspector medioambiental y afines",
        "Inspector de policía",
        "Detective",
        "Instalador de material aislante y de insonorización",
        "Instalador y reparador de líneas eléctricas",
        "Instalador y reparador en tecnología de la información y las comunicaciones",
        "Instructor de autoescuela",
        "Instructor de educación física y actividades recreativas",
        "Instructor en tecnologías de la información",
        "Jefe de pequeñas poblaciones",
        "Joyero",
        "Orfebre",
        "Platero",
        "Juez",
        "Lavador de vehículos",
        "Lavador de ventanas",
        "Lavandero",
        "Planchador manuales",
        "Limpiador de fachadas",
        "Deshollinador",
        "Limpiador y asistente de oficinas, hoteles y otros establecimientos",
        "Limpiador y asistente doméstico",
        "Locutor de radio",
        "Locutor de televisión",
        "Maestro de enseñanza primaria",
        "Maestro preescolar",
        "Mampostero",
        "Labrante",
        "Tronzador",
        "Grabador de piedra",
        "Maquinista de locomotoras",
        "Marinero de cubierta",
        "Matemático",
        "Actuario",
        "Estadístico",
        "Mecánico y ajustador electricista",
        "Mecánico y reparador de instrumentos de precisión",
        "Mecánico y reparador de máquinas agrícolas e industriales",
        "Mecánico y reparador de motores de avión",
        "Mecánico y reparador de vehículos de motor",
        "Mecánico y reparador en electrónica",
        "Mecánico-montador de instalaciones de refrigeración y climatización",
        "Médico especialista",
        "Médico general",
        "Mensajero",
        "Mandader",
        "Maleter",
        "Repartidor",
        "Meteorólogo",
        "Minero",
        "Operador de instalaciones mineras",
        "Modelo de moda, arte y publicidad",
        "Moldeador y machero",
        "Montador de estructuras metálicas",
        "Músico",
        "Cantante",
        "Compositor",
        "Oficial de las fuerzas armadas",
        "Oficial de préstamos y créditos",
        "Oficial maquinistas en navegación",
        "Oficinista general",
        "Operador de autoelevadoras",
        "Operador de grúas y aparatos elevadores",
        "Operador de incineradores, instalaciones de tratamiento de agua",
        "Operador de instalaciones de tratamiento de agua",
        "Operador de instalaciones de procesamiento de la madera",
        "Operador de instalaciones de procesamiento de metales",
        "Operador de instalaciones de procesamiento de minerales y rocas",
        "Operador de instalaciones de producción de energía",
        "Operador de instalaciones de refinación de petróleo y gas natural",
        "Operador de instalaciones de vidriería y cerámica",
        "Operador de instalaciones para la preparación de pasta para papel y papel",
        "Operador de maquinaria agrícola y forestal móvil",
        "Operador de máquinas de blanqueamiento, teñido y limpieza de tejidos",
        "Operador de máquinas de coser",
        "Operador de máquinas de embalaje, embotellamiento y etiquetado ",
        "Operador de máquinas de movimiento de tierras",
        "Operador de máquinas de preparación de fibras, hilado y devanado",
        "Operador de máquinas de procesamiento de texto y mecanógrafos",
        "Operador de máquinas de tratamiento de pieles y cueros",
        "Operador de máquinas de vapor y calderas",
        "Operador de máquinas lavarropas",
        "Operador de máquinas para elaborar alimentos y productos afines",
        "Operador de máquinas para fabricar cemento y otros productos minerales",
        "Operador de máquinas para fabricar productos de caucho",
        "Operador de máquinas para fabricar productos de material plástico",
        "Operador de máquinas para fabricar productos de papel",
        "Operador de máquinas para fabricar productos fotográficos",
        "Operador de máquinas para la fabricación de calzado",
        "Operador de máquinas pulidoras, galvanizadoras y recubridoras de metales ",
        "Operador de plantas y máquinas de productos químicos",
        "Operador de telar y otras máquinas tejedoras",
        "Operario de la conservación de frutas, legumbres y verduras",
        "Operario de la elaboración de productos lácteos",
        "Operario del tratamiento de la madera",
        "Operario en cemento armado y enfoscador",
        "Optometrista",
        "Organizador de conferencias y eventos",
        "Personal de limpieza",
        "Miembro de las fuerzas armadas",
        "Profesional de nivel medio en actividades culturales y artísticas",
        "Profesor de artes",
        "Profesor de idiomas",
        "Profesor de música",
        "Panaderos, pasteleros y confiteros",
        "Parquetero y colocador de suelos",
        "Patronista y cortador de tela",
        "Peluqueros",
        "Peón de carga",
        "Peón de explotaciones agrícolas",
        "Peón de explotaciones de cultivos mixtos y ganaderos",
        "Peón de explotaciones ganaderas",
        "Peón de jardinería y horticultura",
        "Peón de la construcción de edificios",
        "Peón de minas y canteras",
        "Peón de obras públicas y mantenimiento",
        "Peón de pesca y acuicultura",
        "Peón forestales",
        "Perforador y sondista de pozos",
        "Periodista",
        "Personal de pompas fúnebres y embalsamador",
        "Personal directivo de la administración pública",
        "Personas que realizan trabajos varios",
        "Pescador, cazador, tramperos y recolector de subsistencia",
        "Pescador de agua dulce y en aguas costeras",
        "Pescador de alta mar",
        "Piloto de aviación",
        "Pintor y empapelador",
        "Policías",
        "Practicante paramédico",
        "Practicante y asistente médico",
        "Preparador y elaborador de tabaco y sus productos",
        "Prestamista",
        "Productor y trabajador calificado de explotaciones agropecuarias mixtas",
        "Profesional de enfermería",
        "Profesional de la protección medioambiental",
        "Profesional de la publicidad y la comercialización",
        "Profesional de la salud y la higiene laboral y ambiental",
        "Profesional de medicina",
        "Profesional de medicina alternativa",
        "Profesional de nivel medio de enfermería",
        "Profesional de nivel medio de medicina tradicional y alternativa",
        "Profesional de nivel medio de medicina alternativa",
        "Profesional de nivel medio de partería",
        "Profesional de nivel medio de servicios estadísticos o matemáticos",
        "Profesional de nivel medio del derecho y servicios legales",
        "Profesional de partería",
        "Profesional de relaciones públicas",
        "Profesional de ventas de tecnología de la información y las comunicaciones",
        "Profesional de ventas técnicas y médicas",
        "Profesional del trabajo social",
        "Profesional en redes de computadores",
        "Profesional religioso",
        "Profesor de enseñanza secundaria",
        "Profesor de formación profesional",
        "Profesor de universidades y de la enseñanza superior",
        "Programador de aplicaciones",
        "Psicólogo",
        "Pulidor de metales y afilador de herramientas",
        "Químico",
        "Recepcionista de hoteles",
        "Recepcionista",
        "Receptor de apuestas",
        "Recolector de basura y material reciclable",
        "Recolector de dinero en aparatos de venta automática y lector de medidores",
        "Redactor de carteles, pintor decorativos y grabador",
        "Regulador y operador de máquinas de labrar madera",
        "Regulador y operador de máquinas y herramientas",
        "Reparador de bicicletas",
        "Reponedor de estanterías",
        "Representante comercial",
        "Revisor y cobrador de los transportes públicos",
        "Revocador",
        "Modisto",
        "Peletero",
        "Sombrerero",
        "Secretario administrativo",
        "Secretario ejecutivo",
        "Secretario (general)",
        "Secretario jurídicos",
        "Secretario médicos",
        "Sociólogo",
        "Antropólogo",
        "Soldador y oxicortador",
        "Soplador de vidrio",
        "Modelador de vidrio",
        "Laminador de vidrio",
        "Cortador de vidrio",
        "Pulidor de vidrio",
        "Suboficial de las fuerzas armadas",
        "Supervisor de industria manufacturera",
        "Supervisor de la construcción",
        "Supervisor de mantenimiento y limpieza en oficinas, hoteles y otros establecimientos",
        "Supervisor de secretaría",
        "Supervisor de tiendas y almacenes",
        "Supervisor en ingeniería de minas",
        "Tapicero",
        "Colchonero",
        "Tasador",
        "Techador",
        "Técnico agropecuario",
        "Técnico de telecomunicaciones",
        "Técnico de la Web",
        "Técnico de laboratorio médico",
        "Técnico de prótesis médicas y dentales",
        "Técnico de radiodifusión y grabación audio visual",
        "Técnico en aparatos de diagnóstico y tratamiento médico",
        "Técnico en asistencia al usuario de tecnología de la información y las comunicaciones",
        "Técnico en ciencias biológicas",
        "Técnico en ciencias físicas y químicas",
        "Técnico en documentación sanitaria",
        "Técnico en electrónica",
        "Técnico en galerías de arte, museos y bibliotecas",
        "Técnico en ingeniería civil",
        "Técnico en ingeniería de minas y metalurgia",
        "Técnico en ingeniería mecánica",
        "Técnico en operaciones de tecnología de la información y las comunicaciones",
        "Técnico en optometría y ópticos",
        "Técnico en química industrial",
        "Técnico en redes y sistemas de computadores",
        "Técnico en seguridad aeronáutica",
        "Técnico forestal",
        "Asistente farmacéutico",
        "Asistente fisioterapeuta",
        "Asistente veterinario",
        "Telefonista",
        "Tenedor de libros",
        "Trabajador agrícola de subsistencia",
        "Trabajador agropecuario de subsistencia",
        "Trabajador ambulante de servicios",
        "Trabajador comunitario de la salud",
        "Trabajador de explotaciones de acuicultura",
        "Trabajador de cuidados personales a domicilio",
        "Trabajador de cuidados personales en instituciones",
        "Trabajador forestal calificado",
        "Trabajador pecuario de subsistencia",
        "Trabajador social de nivel medio",
        "Traductor e intérprete",
        "Lingüista",
        "Urbanistas e ingenieros de tránsito",
        "Vendedor ambulantes de productos comestibles",
        "Vendedor ambulantes (excluyendo de comida)",
        "Vendedor de comidas al mostrador",
        "Vendedor de quioscos y de puestos de mercado",
        "Vendedor por teléfono",
        "Vendedor puerta a puerta",
        "Veterinario",
        "Zapatero",
        "Miembro del poder legislativo",
    )
