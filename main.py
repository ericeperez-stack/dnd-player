import flet as ft
import math

# --- DATOS DE REFERENCIA ---
LISTA_CLASES = ["Bárbaro", "Bardo", "Clérigo", "Druida", "Guerrero", "Monje", "Paladín", "Explorador (Ranger)", "Pícaro", "Hechicero", "Brujo (Warlock)", "Mago", "OTRA (Manual)"]
LISTA_RAZAS = ["Humano", "Elfo", "Enano", "Halfling", "Dracónido", "Gnomo", "Orco", "Tiefling", "Goliath", "Aasimar", "OTRA (Manual)"]

DADOS_GOLPE = {
    "Hechicero": "d6", "Mago": "d6", "Bardo": "d8", "Clérigo": "d8", "Druida": "d8", "Monje": "d8", 
    "Pícaro": "d8", "Brujo (Warlock)": "d8", "Guerrero": "d10", "Paladín": "d10", 
    "Explorador (Ranger)": "d10", "Bárbaro": "d12", "OTRA (Manual)": "?"
}

# --- INFORMACIÓN TEXTUAL DE CLASES ---
DATA_CLASES_INFO = {
    "Bárbaro": """# BÁRBARO
**Dado de Golpe:** 1d12 por nivel de bárbaro.
**Competencias:** Armaduras ligeras, medias y escudos. Armas sencillas y marciales.
**Salvaciones:** Fuerza, Constitución.
**Habilidades:** Elige dos: Atletismo, Intimidación, Naturaleza, Percepción, Supervivencia o Trato con animales.

## RASGOS DE CLASE
**NIVEL 1: DEFENSA SIN ARMADURA**
Mientras no lleves armadura alguna, tu clase de armadura base será igual a 10 más tus modificadores por Destreza y Constitución. Obtienes este beneficio aunque lleves un escudo.

**NIVEL 1: FURIA**
Puedes imbuirte de un poder primigenio llamado furia. Puedes dejarte llevar por ella como acción adicional si no llevas puesta una armadura pesada.
* **Resistencia al daño:** Tienes resistencia al daño contundente, cortante y perforante.
* **Daño por furia:** Cuando llevas a cabo un ataque que use la Fuerza, obtienes un bonificador al daño (+2 a nivel 1).
* **Ventaja en Fuerza:** Tienes ventaja en las pruebas de Fuerza y en las tiradas de salvación de Fuerza.
* **Sin concentración ni conjuros:** No puedes mantener la concentración ni lanzar conjuros.

**NIVEL 1: MAESTRÍA CON ARMAS**
Tu entrenamiento con armas te permite utilizar las propiedades de maestría con dos tipos de armas cuerpo a cuerpo sencillas o marciales de tu elección.

**NIVEL 2: ATAQUE TEMERARIO**
Puedes dejar de lado toda preocupación por tu defensa para atacar con una desesperación feroz. Cuando haces tu primera tirada de ataque en tu turno, puedes decidir atacar temerariamente. Tienes ventaja en las tiradas de ataque de armas cuerpo a cuerpo que usen Fuerza durante este turno, pero las tiradas de ataque contra ti tienen ventaja hasta el inicio de tu siguiente turno.

**NIVEL 2: SENTIR EL PELIGRO**
Tienes una asombrosa sensación de cuándo las cosas no van como deberían, lo que te otorga ventaja en las tiradas de salvación de Destreza, a menos que tengas el estado de cegado o ensordecido.

**NIVEL 3: CONOCIMIENTO PRIMIGENIO**
Ganas competencia en otra habilidad de la lista de habilidades de bárbaro. Además, mientras estés en furia, puedes usar tu Fuerza en lugar de cualquier otra característica para las pruebas de Acrobacias, Intimidación, Percepción, Sigilo o Supervivencia.

**NIVEL 3: SUBCLASE DE BÁRBARO**
Consigues una subclase de bárbaro de tu elección (Senda del Árbol del Mundo, Berserker, Corazón Salvaje, Fanático).

**NIVEL 5: ATAQUE ADICIONAL**
Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Atacar en tu turno.

**NIVEL 5: MOVIMIENTO RÁPIDO**
Tu velocidad aumenta en 3 m mientras no lleves armadura pesada.

**NIVEL 7: INSTINTO SALVAJE**
Tu instinto es tan agudo que tienes ventaja en las tiradas de iniciativa. Además, si te sorprenden al comienzo del combate y no tienes el estado de incapacitado, puedes actuar normalmente en tu primer turno, pero solo si entras en furia antes de hacer cualquier otra cosa.

**NIVEL 9: GOLPE BRUTAL**
Puedes prescindir de la ventaja de tu Ataque temerario para golpear con más fuerza. Si usas Ataque temerario, puedes renunciar a la ventaja en una tirada de ataque para infligir 1d10 de daño adicional si aciertas.

**NIVEL 11: FURIA IMPLACABLE**
Tu furia puede mantenerte luchando a pesar de las heridas graves. Si tus puntos de golpe se reducen a 0 mientras estás en furia y no mueres al instante, puedes hacer una tirada de salvación de Constitución CD 10. Si tienes éxito, te quedas con 1 punto de golpe.

**NIVEL 15: FURIA PERSISTENTE**
Tu furia es tan intensa que solo termina antes de tiempo si caes inconsciente o si tú decides finalizarla.
""",

    "Bardo": """# BARDO
**Dado de Golpe:** 1d8 por nivel de bardo.
**Competencias:** Armaduras ligeras. Armas sencillas.
**Herramientas:** Tres instrumentos musicales.
**Salvaciones:** Destreza, Carisma.
**Habilidades:** Elige tres cualesquiera.

## RASGOS DE CLASE
**NIVEL 1: INSPIRACIÓN BÁRDICA**
Como acción adicional, puedes inspirar a otra criatura que esté a 18 m o menos de ti. Esa criatura obtiene un dado de Inspiración bárdica (d6). Una vez en los siguientes 60 minutos, la criatura puede tirar el dado y sumar el resultado a una prueba de característica, tirada de ataque o tirada de salvación.

**NIVEL 1: LANZAMIENTO DE CONJUROS**
Lanzas conjuros usando tu Carisma. Puedes lanzar cualquier conjuro de bardo que conozcas como un ritual si tiene la etiqueta de ritual.

**NIVEL 2: APRENDIZ DE MUCHO**
Puedes sumar la mitad de tu bonificador por competencia (redondeando hacia abajo) a cualquier prueba de característica que hagas que no use ya tu bonificador por competencia.

**NIVEL 2: PERICIA**
Elige dos de tus competencias en habilidades. Tu bonificador por competencia se duplica para cualquier prueba de característica que hagas usándolas.

**NIVEL 3: SUBCLASE DE BARDO**
Eliges un Colegio de Bardo (Danza, Conocimiento, Glamour, Valor).

**NIVEL 5: FUENTE DE INSPIRACIÓN**
Recuperas todos tus usos de Inspiración bárdica cuando terminas un descanso corto o largo. Además, tu dado de Inspiración bárdica se convierte en un d8.

**NIVEL 6: CONTRAENCANTAMIENTO**
Como reacción cuando tú o una criatura a 9 m falláis una salvación contra un efecto que hechiza o asusta, puedes permitir que la criatura repita la salvación con ventaja.

**NIVEL 10: SECRETOS MÁGICOS**
Has aprendido conocimientos mágicos de un amplio espectro de disciplinas. Elige dos conjuros de cualquier clase (Bardo, Clérigo, Druida, Mago, etc.).

**NIVEL 20: PALABRAS DE CREACIÓN**
Siempre tienes preparados los conjuros Palabra de poder: sanar y Palabra de poder: matar. Puedes lanzar uno de ellos sin gastar un espacio de conjuro una vez por descanso largo.
""",

    "Clérigo": """# CLÉRIGO
**Dado de Golpe:** 1d8 por nivel de clérigo.
**Competencias:** Armaduras ligeras, medias y escudos. Armas sencillas.
**Salvaciones:** Sabiduría, Carisma.
**Habilidades:** Elige dos: Historia, Medicina, Perspicacia, Persuasión o Religión.

## RASGOS DE CLASE
**NIVEL 1: LANZAMIENTO DE CONJUROS**
Preparas conjuros divinos diariamente. Sabiduría es tu aptitud mágica. Puedes lanzar rituales.

**NIVEL 1: ORDEN DIVINA**
Elige una:
* **Protector:** Competencia con armas marciales y armaduras pesadas.
* **Taumaturgo:** Un truco extra y sumas tu Sabiduría a pruebas de Religión o Arcanos.

**NIVEL 2: CANALIZAR DIVINIDAD**
Ganas la capacidad de canalizar energía divina, empezando con dos efectos:
* **Chispa Divina:** Acción mágica. Curas o dañas (radiante/necrótico) 1d8 + Sab a una criatura.
* **Expulsar Muertos Vivientes:** Acción mágica. Cada muerto viviente a 9 m debe superar salvación de Sabiduría o huir.

**NIVEL 3: SUBCLASE DE CLÉRIGO**
Eliges un Dominio Divino (Guerra, Luz, Vida, Engaño).

**NIVEL 5: DESTRUIR MUERTOS VIVIENTES**
Cuando un muerto viviente falla su salvación contra tu Expulsar muertos vivientes, la criatura recibe daño radiante instantáneo.

**NIVEL 7: GOLPES BENDITOS**
Elige uno:
* **Golpe Divino:** 1d8 daño radiante/necrótico extra con armas (1/turno).
* **Lanzamiento de Conjuros Potente:** Sumas Sabiduría al daño de tus trucos.

**NIVEL 10: INTERVENCIÓN DIVINA**
Puedes invocar a tu deidad para que intervenga. Como acción, describe la asistencia que buscas y tira dados de porcentaje. Si sacas un número igual o menor a tu nivel de clérigo, tu deidad interviene.
""",

    "Druida": """# DRUIDA
**Dado de Golpe:** 1d8 por nivel de druida.
**Competencias:** Armaduras ligeras, medias y escudos (no de metal). Armas de druida (bastón, cimitarra, hoz, etc). Útiles de herborista.
**Salvaciones:** Inteligencia, Sabiduría.
**Habilidades:** Elige dos: Arcanos, Medicina, Naturaleza, Percepción, Perspicacia, Religión, Supervivencia o Trato con animales.

## RASGOS DE CLASE
**NIVEL 1: DRUÍDICO**
Conoces el idioma secreto Druídico.

**NIVEL 1: ORDEN PRIMIGENIA**
Elige una:
* **Guardián:** Competencia armadura media y armas marciales.
* **Naturalista:** Truco extra. Sumas Sabiduría a Naturaleza.

**NIVEL 2: COMPAÑERO SALVAJE**
Puedes gastar un uso de Forma Salvaje para lanzar *Encontrar Familiar* sin componentes materiales. El familiar es un espíritu feérico.

**NIVEL 2: FORMA SALVAJE**
Como acción adicional, puedes transformarte mágicamente en una bestia que hayas visto antes. Puedes mantener la forma un número de horas igual a la mitad de tu nivel de druida.

**NIVEL 3: SUBCLASE DE DRUIDA**
Eliges un Círculo Druídico (Luna, Tierra, Estrellas, Mar).

**NIVEL 5: RESURGIMIENTO SALVAJE**
Puedes usar un uso de Forma Salvaje para recuperar un espacio de conjuro de nivel 1 (acción adicional).

**NIVEL 18: CONJURAR COMO BESTIA**
Puedes lanzar muchos de tus conjuros de druida en cualquier forma que adoptes con Forma Salvaje.
""",

    "Guerrero": """# GUERRERO (FIGHTER)
**Dado de Golpe:** 1d10 por nivel de guerrero.
**Competencias:** Todas las armaduras y escudos. Armas sencillas y marciales.
**Salvaciones:** Fuerza, Constitución.
**Habilidades:** Elige dos: Acrobacias, Atletismo, Historia, Intimidación, Percepción, Perspicacia, Supervivencia o Trato con animales.

## RASGOS DE CLASE
**NIVEL 1: ESTILO DE COMBATE**
Adoptas un estilo de combate particular como especialidad (Arququería, Defensa, Duelo, Arma a dos manos, Protección, Combate con dos armas).

**NIVEL 1: MAESTRÍA CON ARMAS**
Dominas las propiedades de maestría de 3 armas a tu elección.

**NIVEL 1: TOMAR ALIENTO (SECOND WIND)**
Tienes una reserva de resistencia. En tu turno, puedes usar una acción adicional para recuperar puntos de golpe iguales a 1d10 + tu nivel de guerrero.

**NIVEL 2: ACCIÓN SÚBITA (ACTION SURGE)**
Puedes forzarte para superar tus límites normales momentáneamente. En tu turno, puedes realizar una acción adicional aparte de tu acción normal y tu posible acción extra.

**NIVEL 2: MENTE TÁCTICA**
Cuando fallas una prueba de característica, puedes gastar un uso de Tomar Aliento para sumar 1d10 a la tirada.

**NIVEL 3: SUBCLASE DE GUERRERO**
Eliges un Arquetipo Marcial (Campeón, Caballero Arcano, Maestro de Batalla, Guerrero Psiónico).

**NIVEL 5: ATAQUE ADICIONAL**
Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Atacar en tu turno.

**NIVEL 9: INDÓMITO**
Puedes volver a tirar una tirada de salvación que falles. Debes usar el nuevo resultado.
""",

    "Monje": """# MONJE
**Dado de Golpe:** 1d8 por nivel de monje.
**Competencias:** Armas sencillas y espadas cortas.
**Salvaciones:** Fuerza, Destreza.
**Habilidades:** Elige dos: Acrobacias, Atletismo, Historia, Percepción, Religión o Sigilo.

## RASGOS DE CLASE
**NIVEL 1: DEFENSA SIN ARMADURA**
Mientras no lleves armadura ni escudo, tu CA es 10 + Destreza + Sabiduría.

**NIVEL 1: ARTES MARCIALES**
* Puedes usar Destreza en lugar de Fuerza para ataques y daño desarmado/armas de monje.
* Puedes tirar un d6 en lugar del daño normal de tu ataque sin armas.
* Cuando usas la acción de Atacar con un ataque sin armas o arma de monje, puedes realizar un ataque sin armas como acción adicional.

**NIVEL 2: CONCENTRACIÓN (KI)**
Tienes puntos de concentración igual a tu nivel.
* **Ráfaga de Golpes:** Gasta 1 punto para hacer dos ataques sin armas como acción adicional.
* **Defensa Paciente:** Gasta 1 punto para realizar la acción de Esquivar y Destrabarse como acción adicional.
* **Paso del Viento:** Gasta 1 punto para realizar la acción de Destrabarse y Correr como acción adicional, y tu salto se duplica.

**NIVEL 2: METABOLISMO ASOMBROSO**
Una vez por día, al tirar iniciativa, recuperas todos tus puntos de concentración y sanas tu nivel de monje en HP.

**NIVEL 3: DESVIAR ATAQUES**
Puedes usar tu reacción para desviar o atrapar el proyectil cuando te golpea un ataque de arma a distancia. El daño se reduce en 1d10 + Destreza + Nivel de monje.

**NIVEL 5: GOLPE ATURDIDOR**
Cuando golpeas a otra criatura con un ataque de arma cuerpo a cuerpo, puedes gastar 1 punto de concentración para intentar un golpe aturdidor.
""",

    "Paladín": """# PALADÍN
**Dado de Golpe:** 1d10 por nivel de paladín.
**Competencias:** Todas las armaduras y escudos. Armas sencillas y marciales.
**Salvaciones:** Sabiduría, Carisma.
**Habilidades:** Elige dos: Atletismo, Intimidación, Medicina, Perspicacia, Persuasión o Religión.

## RASGOS DE CLASE
**NIVEL 1: IMPONER LAS MANOS**
Tienes una reserva de curación igual a tu nivel de paladín x 5. Como acción, puedes tocar a una criatura y sanarla gastando puntos de la reserva. También puedes gastar 5 puntos para curar una enfermedad o neutralizar un veneno.

**NIVEL 1: SENTIDO DIVINO**
Como acción adicional, puedes abrir tu conciencia para detectar fuerzas del bien y del mal. Conoces la ubicación de cualquier celestial, infernal o muerto viviente a 18 m de ti.

**NIVEL 2: ESTILO DE COMBATE**
Eliges un estilo de combate (Defensa, Duelo, Arma a dos manos, Protección).

**NIVEL 2: LANZAMIENTO DE CONJUROS**
Preparas conjuros divinos. Carisma es tu aptitud mágica.

**NIVEL 2: CASTIGO DIVINO (SMITE)**
Cuando golpeas a una criatura con un ataque de arma cuerpo a cuerpo, puedes gastar un espacio de conjuro para infligir daño radiante adicional al objetivo (2d8 por un espacio de nivel 1, +1d8 por cada nivel superior).

**NIVEL 3: CANALIZAR DIVINIDAD**
Obtienes opciones de canalizar energía divina según tu Juramento Sagrado.

**NIVEL 3: SUBCLASE DE PALADÍN**
Eliges un Juramento Sagrado (Devoción, Gloria, Antiguos, Venganza).

**NIVEL 6: AURA DE PROTECCIÓN**
Siempre que tú o una criatura amistosa a 3 m de ti debáis realizar una tirada de salvación, la criatura gana un bonificador a la tirada igual a tu modificador por Carisma.
""",

    "Explorador (Ranger)": """# EXPLORADOR (RANGER)
**Dado de Golpe:** 1d10 por nivel de explorador.
**Competencias:** Armaduras ligeras, medias y escudos. Armas sencillas y marciales.
**Salvaciones:** Fuerza, Destreza.
**Habilidades:** Elige tres: Atletismo, Investigación, Naturaleza, Percepción, Perspicacia, Sigilo, Supervivencia o Trato con animales.

## RASGOS DE CLASE
**NIVEL 1: ENEMIGO PREDILECTO**
Siempre tienes preparado el conjuro *Marca del Cazador*. Puedes lanzarlo sin gastar espacio de conjuro una cantidad de veces igual a tu modificador de Sabiduría.

**NIVEL 1: EXPLORADOR HÁBIL (DEFT EXPLORER)**
* Ganas pericia en una de tus habilidades.
* Aprendes dos idiomas adicionales.

**NIVEL 1: LANZAMIENTO DE CONJUROS**
Preparas conjuros de la naturaleza. Sabiduría es tu aptitud mágica.

**NIVEL 2: ESTILO DE COMBATE**
Eliges un estilo de combate (Arququería, Defensa, Duelo, Combate con dos armas).

**NIVEL 3: SUBCLASE DE EXPLORADOR**
Eliges un Conclave de Explorador (Cazador, Bestias, Acechador en la Penumbra, Errante Feérico).

**NIVEL 5: ATAQUE ADICIONAL**
Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Atacar en tu turno.

**NIVEL 6: ERRANTE (ROVING)**
Tu velocidad caminando aumenta en 3 m. Ganas velocidad de escalada y natación igual a tu velocidad caminando.
""",

    "Pícaro": """# PÍCARO (ROGUE)
**Dado de Golpe:** 1d8 por nivel de pícaro.
**Competencias:** Armaduras ligeras. Armas sencillas, ballesta de mano, espada larga, estoque, espada corta. Herramientas de ladrón.
**Salvaciones:** Destreza, Inteligencia.
**Habilidades:** Elige cuatro: Acrobacias, Atletismo, Engaño, Intimidación, Investigación, Juego de manos, Percepción, Perspicacia, Persuasión, Sigilo.

## RASGOS DE CLASE
**NIVEL 1: PERICIA**
Elige dos de tus competencias en habilidades, o una habilidad y herramientas de ladrón. Tu bonificador por competencia se duplica para ellas.

**NIVEL 1: ATAQUE FURTIVO**
Una vez por turno, puedes infligir 1d6 de daño adicional a una criatura a la que golpees con un ataque si tienes ventaja en la tirada de ataque. El ataque debe usar un arma sutil o a distancia. No necesitas ventaja si otro enemigo del objetivo está a 1.5 m de él.

**NIVEL 1: JERGA DE LADRONES**
Durante tu entrenamiento aprendiste la jerga de ladrones, una mezcla de dialecto, argot y código secreto.

**NIVEL 2: ACCIÓN ASTUTA**
Tu rapidez mental y agilidad te permiten moverte y actuar rápidamente. Puedes realizar una acción adicional en cada uno de tus turnos de combate. Esta acción solo puede usarse para: Correr, Destrabarse o Esconderse.

**NIVEL 3: SUBCLASE DE PÍCARO**
Eliges un Arquetipo de Pícaro (Ladrón, Asesino, Embaucador Arcano, Soulknife).

**NIVEL 5: ESQUIVA ASOMBROSA**
Cuando un atacante que puedes ver te golpea con un ataque, puedes usar tu reacción para reducir a la mitad el daño del ataque contra ti.

**NIVEL 7: EVASIÓN**
Cuando estás sometido a un efecto que te permite hacer una tirada de salvación de Destreza para recibir solo la mitad de daño, no recibes daño si tienes éxito y solo la mitad si fallas.
""",

    "Hechicero": """# HECHICERO (SORCERER)
**Dado de Golpe:** 1d6 por nivel de hechicero.
**Competencias:** Ninguna armadura. Armas sencillas.
**Salvaciones:** Constitución, Carisma.
**Habilidades:** Elige dos: Arcanos, Engaño, Intimidación, Perspicacia, Persuasión o Religión.

## RASGOS DE CLASE
**NIVEL 1: LANZAMIENTO DE CONJUROS**
La magia innata fluye a través de ti. Conoces conjuros y los lanzas usando Carisma.

**NIVEL 1: HECHICERÍA INNATA**
Como acción adicional, puedes entrar en un estado de poder durante 1 minuto. La CD de tus conjuros aumenta en 1 y tienes ventaja en tiradas de ataque de conjuro.

**NIVEL 2: FUENTE DE MAGIA**
Tienes una reserva de Puntos de Hechicería igual a tu nivel. Puedes usarlos para crear espacios de conjuro o convertir espacios en puntos.

**NIVEL 2: METAMAGIA**
Obtienes la capacidad de alterar tus conjuros. Eliges 2 opciones de Metamagia (ej: Conjuro Cuidadoso, Conjuro Sutil, Conjuro Gemelo).

**NIVEL 3: SUBCLASE DE HECHICERO**
Eliges un Origen Hechicero (Dracónico, Magia Salvaje, Aberrante, Mecánico).

**NIVEL 5: RESPUESTA HECHICERA**
Cuando fallas una tirada de salvación, puedes gastar puntos de hechicería para volver a tirar.
""",

    "Brujo (Warlock)": """# BRUJO (WARLOCK)
**Dado de Golpe:** 1d8 por nivel de brujo.
**Competencias:** Armaduras ligeras. Armas sencillas.
**Salvaciones:** Sabiduría, Carisma.
**Habilidades:** Elige dos: Arcanos, Engaño, Historia, Intimidación, Investigación, Naturaleza o Religión.

## RASGOS DE CLASE
**NIVEL 1: MAGIA DEL PACTO**
Tus investigaciones arcanas te han otorgado facilidad con los conjuros.
* **Espacios de Conjuro:** Tus espacios son siempre del máximo nivel posible.
* **Recuperación:** Recuperas todos tus espacios gastados al finalizar un descanso corto o largo.

**NIVEL 1: INVOCACIONES ELDRITCH**
En tus estudios, has descubierto invocaciones eldrítch, fragmentos de conocimiento prohibido que te imbuyen de una capacidad mágica permanente. (Eliges 1 a nivel 1, más a niveles superiores).

**NIVEL 2: ASTUCIA MÁGICA**
Puedes recuperar la mitad de tus espacios de pacto gastados realizando un ritual de 1 minuto (1 vez/día).

**NIVEL 3: SUBCLASE DE BRUJO**
Eliges un Patrón de Otro Mundo (Archifey, Celestial, Infernal, Gran Antiguo).

**NIVEL 3: PACTO DEL BOON**
Eliges un don de tu patrón (Pacto de la Hoja, Pacto de la Cadena, Pacto del Tomo).
""",

    "Mago": """# MAGO (WIZARD)
**Dado de Golpe:** 1d6 por nivel de mago.
**Competencias:** Ninguna armadura. Armas sencillas.
**Salvaciones:** Inteligencia, Sabiduría.
**Habilidades:** Elige dos: Arcanos, Historia, Investigación, Medicina, Naturaleza o Religión.

## RASGOS DE CLASE
**NIVEL 1: LANZAMIENTO DE CONJUROS**
Tienes un libro de conjuros que contiene tus hechizos. Preparas una lista de conjuros diariamente. Puedes lanzar rituales directamente desde tu libro. Inteligencia es tu aptitud mágica.

**NIVEL 1: RECUPERACIÓN ARCANA**
Una vez al día, cuando terminas un descanso corto, puedes elegir espacios de conjuro gastados para recuperarlos. Los espacios pueden tener un nivel combinado igual o inferior a la mitad de tu nivel de mago (redondeado hacia arriba).

**NIVEL 1: ADEPTO EN RITUALES**
Puedes copiar cualquier conjuro de ritual que encuentres en tu libro de conjuros y lanzarlo como ritual.

**NIVEL 2: ERUDITO**
Ganas pericia en una de tus habilidades académicas (Arcanos, Historia, Naturaleza, Religión).

**NIVEL 3: SUBCLASE DE MAGO**
Eliges una Tradición Arcana (Abjuración, Adivinación, Evocación, Ilusión).

**NIVEL 5: MEMORIZAR CONJURO**
Puedes cambiar un conjuro preparado por otro de tu libro tras 1 minuto de estudio.
""",

    "OTRA (Manual)": """# CLASE PERSONALIZADA
Esta sección está reservada para clases que no aparecen en el Manual del Jugador 2024 o contenido de terceros.
Por favor, consulta la fuente original de tu clase para ver los rasgos y anótalos manualmente en las notas de tu personaje.
"""
}

# --- KITS Y HERRAMIENTAS ---
DATA_KITS = {
    "Kit de Ladrón": "Mochila, 1000 balines de metal, 10 pies de hilo, campana, 5 velas, palanca, martillo, 10 pitones, linterna sorda, 2 frascos de aceite, 5 días de raciones, caja de yesca y odre. Incluye 50 pies de cuerda atada al costado.",
    "Kit de Diplomático": "Cofre, 2 estuches para mapas/pergaminos, ropa fina, botella de tinta, pluma, lámpara de aceite, 2 frascos de aceite, 5 hojas de papel, vial de perfume, lacre y jabón.",
    "Kit de Dungeon": "Mochila, palanca, martillo, 10 pitones, 10 antorchas, caja de yesca, 10 días de raciones y odre. Incluye 50 pies de cuerda atada al costado.",
    "Kit de Artista": "Mochila, saco de dormir, 2 disfraces, 5 velas, 5 días de raciones, odre y un kit de disfraz.",
    "Kit de Explorador": "Mochila, saco de dormir, kit de comedor, caja de yesca, 10 antorchas, 10 días de raciones y odre. Incluye 50 pies de cuerda atada al costado.",
    "Kit de Sacerdote": "Mochila, manta, 10 velas, caja de yesca, caja de limosnas, 2 bloques de incienso, incensario, vestimentas, 2 días de raciones y odre.",
    "Kit de Erudito": "Mochila, libro de conocimientos, botella de tinta, pluma, 10 hojas de pergamino, bolsa pequeña de arena y cuchillo pequeño."
}

DATA_HERRAMIENTAS_FULL = {
    "Herramientas de Ladrón": "Componentes: Una pequeña lima, un juego de ganzúas, un pequeño espejo montado en un mango de metal, un juego de tijeras de hoja estrecha y un par de alicates.",
    "Herramientas de Navegante": "Componentes: Un sextante, un compás, calibradores, una regla, pergamino, tinta y una pluma.",
    "Kit de Disfraz": "Componentes: Cosméticos, tinte de pelo, prendas pequeñas y accesorios.",
    "Kit de Falsificación": "Componentes: Varios tipos de tintas, pergaminos, papeles, plumas, sellos y cera, hoja de oro y plata, y pequeñas herramientas para esculpir sellos de cera derretida.",
    "Kit de Herboristería": "Componentes: Bolsas para almacenar hierbas, tijeras de podar, guantes de cuero, mortero y mano, y varios frascos de vidrio.",
    "Kit de Envenenador": "Componentes: Viales de vidrio, un mortero y mano, productos químicos y una varilla de vidrio para agitar.",
    "Juego de Dados": "Componentes: Un set de dados de hueso o madera, o una baraja de cartas.",
    "Suministros de Alquimista": "Componentes: Dos vasos de precipitados de vidrio, un marco de metal, una varilla de vidrio para agitar, un pequeño mortero y mano, y una bolsa de ingredientes alquímicos comunes (sal, hierro en polvo, agua purificada).",
    "Suministros de Cervecero": "Componentes: Una gran jarra de vidrio, una cantidad de lúpulo, un sifón y varios metros de tubo.",
    "Suministros de Caligrafía": "Componentes: Tinta de varios colores, pergaminos de alta calidad y varias plumas de distintos grosores.",
    "Suministros de Pintor": "Componentes: Un caballete, lienzos, pinturas, pinceles, carbón vegetal y una paleta.",
    "Utensilios de Cocinero": "Componentes: Una olla de metal, cuchillos, tenedores, cucharas, cucharón, un rallador, una tabla de cortar y especias.",
    "Herramientas de Albañil": "Componentes: Una paleta, un martillo, un cincel, cepillos y una escuadra.",
    "Herramientas de Alfarero": "Componentes: Agujas de alfarero, costillas, raspadores, un cuchillo y alambre.",
    "Herramientas de Carpintero": "Componentes: Una sierra, un martillo, clavos, un hacha de mano, una escuadra, una regla, una azuela, un cepillo y un cincel.",
    "Herramientas de Cartógrafo": "Componentes: Una regla, compases, calibradores, tinta, plumas, pergamino y un estuche para mapas.",
    "Herramientas de Curtidor": "Componentes: Un cuchillo, un mazo, un cortador de bordes, un punzón, hilo y retales de cuero.",
    "Herramientas de Herrero": "Componentes: Martillos, tenazas, carbón, trapos, piedras de afilar, pegamento y aceite.",
    "Herramientas de Hojalatero": "Componentes: Herramientas manuales variadas, hilo, agujas, piedra de afilar, retales de tela y cuero, y un pequeño pote de pegamento.",
    "Herramientas de Joyero": "Componentes: Una pequeña sierra, un martillo, limas, alicates y pinzas.",
    "Herramientas de Soplador de Vidrio": "Componentes: Una caña de soplar, unas tenazas pequeñas, unas tijeras y una marver (superficie plana).",
    "Herramientas de Tallador de Madera": "Componentes: Un cuchillo, una gubia y una sierra pequeña.",
    "Herramientas de Tejedor": "Componentes: Hilo, agujas y retales de tela.",
    "Herramientas de Zapatero": "Componentes: Un martillo, un punzón, un cuchillo, hilo encerado, agujas, hormas de zapatos y retales de cuero."
}

# --- DOTES ---
DATA_DOTES_FULL = {
    "Acechador": "Puedes esconderte con luz tenue. No revelas posición al fallar ataque a distancia. Luz tenue no da desventaja a Percepción.",
    "Actor": "+1 Carisma. Ventaja en Engaño/Actuación. Puedes imitar voces de otras personas o criaturas.",
    "Afortunado": "3 puntos de suerte/día. Gasta 1 para tirar un d20 extra en ataques/pruebas/salvaciones. Puedes hacer que un enemigo tire de nuevo su ataque.",
    "Alerta": "+5 Iniciativa. No puedes ser sorprendido. Enemigos ocultos no tienen ventaja al atacarte.",
    "Apresador": "Ventaja en ataques contra quien tengas apresado. Puedes inmovilizar a quien tengas apresado.",
    "Atacante a la carga": "Si mueves 10 pies y golpeas, puedes hacer un ataque extra como acción adicional.",
    "Atacante salvaje": "Rerollea daño de arma cuerpo a cuerpo una vez por turno y usa el mejor.",
    "Atleta": "+1 Fue/Des. Levantarse cuesta 5 pies. Escalar no cuesta extra. Salto con carrera de 5 pies.",
    "Azote de magos": "Reacción para atacar si lanzan conjuro a 5 pies. Desventaja en mantener concentración si los dañas. Ventaja en salvación contra conjuros a 5 pies.",
    "Centinela": "Oportunidad reduce velocidad a 0. Oportunidad aunque usen Destrabarse. Reacción para atacar si atacan a aliado.",
    "Chef": "+1 Con/Sab. Preparas comida en descanso corto (cura 1d8 extra).",
    "Combate con armas a dos manos": "Rerollea 1s y 2s en daño.",
    "Combate con armas arrojadizas": "+2 daño con armas arrojadizas. Sacar arma es gratis.",
    "Combate con dos armas": "Añades mod de característica al daño de la segunda mano.",
    "Combate sin armas": "Daño 1d6 + Fue (o 1d8). 1d4 daño a apresados al inicio de turno.",
    "Combatiente con dos armas": "+1 CA con dos armas. Puedes usar armas no ligeras.",
    "Combatiente montado": "Ventaja contra criaturas más pequeñas que tu montura. Rediriges ataques a montura hacia ti. Evasión para montura.",
    "Defensa": "+1 a la Clase de Armadura con armadura.",
    "Don de la fortaleza": "+1 Constitución.",
    "Don de la habilidad": "Competencia en una habilidad (o pericia).",
    "Don de la pericia en combate": "Aprendes 1 maniobra y 1 dado de superioridad d6.",
    "Don de la recuperación": "Acción para gastar dado de golpe y curarte.",
    "Don de la resistencia a energías": "Resistencia a un tipo de daño (ácido, fuego, frío, etc).",
    "Don de la velocidad": "+10 pies de velocidad.",
    "Don de la visión verdadera": "Visión en oscuridad 60 pies.",
    "Don del ataque imparable": "Ignoras resistencia a daño no mágico.",
    "Don del destino": "Sumas competencia a una tirada fallada (1/descanso).",
    "Don del espíritu de la noche": "Invisibilidad en luz tenue/oscuridad hasta atacar.",
    "Don del recuerdo de conjuros": "Aprendes 1 truco y 1 conjuro de nivel 1.",
    "Don del viaje dimensional": "Paso Brumoso 1 vez/día.",
    "Duelista defensivo": "Reacción para sumar competencia a CA contra un ataque.",
    "Duelo": "+2 daño con arma a una mano.",
    "Duro": "+2 HP por nivel.",
    "Entrenamiento con armas marciales": "+1 Fue/Des. Competencia con 4 armas marciales.",
    "Envenenador": "Ignoras resistencia veneno. Aplicar veneno es acción adicional.",
    "Experto en ballestas": "Ignoras carga. No desventaja a 5 pies. Ataque extra con ballesta de mano.",
    "Experto en habilidades": "+1 característica. 1 competencia. 1 pericia.",
    "Fabricante": "Competencia herramientas. Trabajas doble rápido.",
    "Habilidoso": "3 competencias a elección.",
    "Influencia feérica": "+1 Car. Ventaja contra encantar/dormir.",
    "Influencia sombría": "Visión en oscuridad mágica 120 pies. Ventaja Sigilo.",
    "Iniciado en la magia": "2 trucos y 1 conjuro nivel 1.",
    "Intercepción": "Reacción para reducir daño a aliado en 1d10+Comp.",
    "Lanzador en combate": "Ventaja concentración. Conjurar con manos ocupadas. Conjuro como oportunidad.",
    "Lanzador preciso": "Ignoras cobertura parcial con trucos.",
    "Lanzador ritual": "Libro de rituales con 2 conjuros.",
    "Líder inspirador": "HP Temp a 6 aliados = Nivel + Car.",
    "Ligeramente acorazado": "+1 Fue/Des. Armadura ligera.",
    "Lucha a ciegas": "Visión ciega 10 pies.",
    "Maestro de armas": "+1 Fue/Des. 3 maniobras, 1 dado d6.",
    "Maestro en armaduras medias": "+1 CA en media (Max Dex +3). Sin desventaja Sigilo.",
    "Maestro en armaduras pesadas": "+1 Fue. Reduces daño no mágico en 3.",
    "Maestro en armas de asta": "Ataque extra 1d4. Oportunidad al entrar en alcance.",
    "Maestro en armas pesadas": "Ataque extra al crítico/matar. -5 ataque / +10 daño.",
    "Maestro en escudos": "Empujar como bonus. Bono escudo a salvación Des. Evasión con reacción.",
    "Matón de taberna": "+1 Fue/Con. Desarmado 1d4. Apresar como bonus.",
    "Mejora de característica": "+2 a una o +1 a dos.",
    "Mente aguda": "+1 Int. Sabes norte, hora, recuerdas todo.",
    "Moderadamente acorazado": "+1 Fue/Des. Armadura media y escudo.",
    "Músico": "+1 Car. Inspiración a aliados tras descanso.",
    "Muy acorazado": "+1 Fue. Armadura pesada.",
    "Observador": "+1 Int/Sab. +5 Pasivas. Lees labios.",
    "Perforador": "+1 Fue/Des. Reroll daño perforante. Crítico añade dado.",
    "Protección": "Reacción para dar desventaja a ataque contra aliado.",
    "Rebanador": "+1 Fue/Des. Daño cortante reduce velocidad. Crítico da desventaja.",
    "Resiliente": "+1 Característica y competencia en su salvación.",
    "Resistente": "+1 Con. Curación mínima con dados es 2xCon.",
    "Sanador": "Estabilizar cura 1 HP. Kit cura 1d6+4+Nivel.",
    "Telepático": "+1 Int/Sab/Car. Telepatía 60 pies. Detectar pensamientos.",
    "Telequinético": "+1 Int/Sab/Car. Mano mago invisible. Empujar 5 pies bonus.",
    "Tirador de primera": "Ignoras cobertura. Sin desventaja larga distancia. -5 ataque / +10 daño.",
    "Tiro con arco": "+2 ataque armas distancia.",
    "Triturador": "+1 Fue/Con. Daño contundente empuja 5 pies. Crítico da ventaja a aliados.",
    "Veloz": "+10 pies. Ignoras terreno difícil al correr.",
    "Versado en un elemento": "Reroll 1s en daño elemental. Ignoras resistencia."
}

def main(page: ft.Page):
    page.title = "D&D Player App v15 Final"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0 

    # --- ESTADO Y DATOS ---
    current_char_name = "Default"
    
    def get_empty_char():
        return {
            "raza": "", "clase": "", "nivel": "1",
            "custom_raza": "", "custom_clase": "",
            "hp_max": 20, "hp_current": 20, 
            "hp_temp": 0, "hp_temp_max": 10,
            "gold": 0, "ac": 10,
            "stats": {"Fuerza": 10, "Destreza": 10, "Constitución": 10, "Inteligencia": 10, "Sabiduría": 10, "Carisma": 10},
            "armas": [], 
            "dotes_list": [], 
            "extras": [
                {"n": "Recurso Clase 1", "m": "0", "used": []},
                {"n": "Recurso Clase 2", "m": "0", "used": []},
                {"n": "Recurso Clase 3", "m": "0", "used": []}
            ],
            "spells_config": {f"lvl{i}": 0 for i in range(1, 10)},
            "spells_used": {f"lvl{i}": [] for i in range(1, 10)},
            "inv_armas": [], "inv_armaduras": [], "inv_pociones": [], "inv_comida": [], "inv_varios": [],
            "kits_tools": []
        }

    all_chars = page.client_storage.get("dnd_chars_v15") or {"Default": get_empty_char()}
    
    for d in all_chars.values():
        if "dotes_list" not in d: d["dotes_list"] = [] 
        if "kits_tools" not in d: d["kits_tools"] = []
        if "extras" not in d: 
            d["extras"] = [{"n": "Recurso 1", "m": "0", "used": []}, {"n": "Recurso 2", "m": "0", "used": []}, {"n": "Recurso 3", "m": "0", "used": []}]
        else:
            for ex in d["extras"]:
                if "used" not in ex: ex["used"] = []

    char_data = all_chars[current_char_name]

    def guardar():
        all_chars[current_char_name] = char_data
        page.client_storage.set("dnd_chars_v15", all_chars)

    # --- HEADER ---
    dd_personajes = ft.Dropdown(options=[ft.dropdown.Option(k) for k in all_chars.keys()], value=current_char_name, expand=True)

    def cambiar_pj(e):
        nonlocal current_char_name, char_data
        current_char_name = dd_personajes.value
        char_data = all_chars[current_char_name]
        recargar_interfaz()

    def nuevo_pj(e):
        def crear(e):
            if txt_new.value and txt_new.value not in all_chars:
                all_chars[txt_new.value] = get_empty_char()
                page.client_storage.set("dnd_chars_v15", all_chars)
                nonlocal current_char_name, char_data
                current_char_name = txt_new.value
                char_data = all_chars[current_char_name]
                dd_personajes.options.append(ft.dropdown.Option(txt_new.value))
                dd_personajes.value = txt_new.value
                recargar_interfaz()
                page.close(dlg)
        txt_new = ft.TextField(label="Nombre")
        dlg = ft.AlertDialog(title=ft.Text("Crear Personaje"), content=txt_new, actions=[ft.TextButton("Crear", on_click=crear)])
        page.open(dlg)

    header = ft.Container(
        padding=10,
        content=ft.Row([ft.Icon("person"), dd_personajes, ft.IconButton("add", on_click=nuevo_pj)], alignment="center")
    )

    # --- PESTAÑA 1: GENERAL (Column Scrollable) ---
    dd_raza = ft.Dropdown(label="Raza", options=[ft.dropdown.Option(x) for x in LISTA_RAZAS], expand=True, on_change=lambda e: update_gen("raza", e.control.value))
    txt_raza_c = ft.TextField(label="Otra Raza", visible=False, expand=True, on_change=lambda e: update_gen("custom_raza", e.control.value))
    dd_clase = ft.Dropdown(label="Clase", options=[ft.dropdown.Option(x) for x in LISTA_CLASES], expand=True, on_change=lambda e: update_gen("clase", e.control.value))
    txt_clase_c = ft.TextField(label="Otra Clase", visible=False, expand=True, on_change=lambda e: update_gen("custom_clase", e.control.value))
    txt_nivel = ft.TextField(label="Nivel", width=60, on_change=lambda e: update_gen("nivel", e.control.value))
    
    txt_hit_dice = ft.Text("?", size=20, weight="bold", color="yellow")

    def update_hit_dice_display():
        clase = char_data["clase"]
        dado = DADOS_GOLPE.get(clase, "?")
        txt_hit_dice.value = f"{dado}" 

    def update_gen(key, val):
        char_data[key] = val
        if key in ["raza", "clase", "nivel"]:
            txt_raza_c.visible = (char_data["raza"] == "OTRA (Manual)")
            txt_clase_c.visible = (char_data["clase"] == "OTRA (Manual)")
            update_hit_dice_display() 
            page.update()
        guardar()

    col_stats = ft.Column()
    def build_stats():
        col_stats.controls.clear()
        for s, v in char_data["stats"].items():
            mod = math.floor((int(v)-10)/2)
            col_stats.controls.append(ft.Container(bgcolor="grey900", padding=5, border_radius=5, content=ft.Row([
                ft.Text(s, width=90, weight="bold"),
                ft.TextField(value=str(v), width=50, text_align="center", keyboard_type="NUMBER", on_change=lambda e, s=s: update_stat(e, s)),
                ft.Text("MOD:", size=10, color="grey"),
                ft.Text(f"{mod:+d}", size=18, weight="bold", color="cyan")
            ], alignment="spaceBetween")))
    
    def update_stat(e, stat):
        try:
            val = int(e.control.value)
            char_data["stats"][stat] = val
            mod = math.floor((val-10)/2)
            e.control.parent.controls[3].value = f"{mod:+d}"
            guardar()
            page.update()
        except: pass

    # --- DOTES ---
    col_dotes_active = ft.Column()
    lista_opciones_dotes = sorted(list(DATA_DOTES_FULL.keys()))
    
    dd_dotes_select = ft.Dropdown(
        label="Escriba para buscar Dote...",
        options=[ft.dropdown.Option(text=k, key=k) for k in lista_opciones_dotes],
        expand=True,
        enable_filter=True, 
        enable_feedback=True
    )

    def add_dote_click(e):
        selected_key = dd_dotes_select.value
        if selected_key:
            desc = DATA_DOTES_FULL[selected_key]
            exists = any(d['n'] == selected_key for d in char_data["dotes_list"])
            if not exists:
                char_data["dotes_list"].append({"n": selected_key, "d": desc})
                guardar()
                render_dotes_active()
                dd_dotes_select.value = None
                page.update()

    def delete_dote_click(e):
        dote_nombre = e.control.data 
        char_data["dotes_list"] = [d for d in char_data["dotes_list"] if d['n'] != dote_nombre]
        guardar()
        render_dotes_active()

    def render_dotes_active():
        col_dotes_active.controls.clear()
        for dote in char_data["dotes_list"]:
            col_dotes_active.controls.append(
                ft.Container(
                    bgcolor="grey900", border_radius=5, margin=2,
                    content=ft.Column([
                        ft.Row([
                            ft.Text(dote['n'], color="yellow", weight="bold", expand=True),
                            ft.IconButton("delete", icon_color="red", data=dote['n'], on_click=delete_dote_click)
                        ]),
                        ft.ExpansionTile(
                            title=ft.Text("Ver descripción", size=12, italic=True),
                            controls=[ft.Container(padding=10, content=ft.Text(dote['d'], size=13))],
                            text_color="white", collapsed_text_color="grey",
                            maintain_state=True
                        )
                    ], spacing=0)
                )
            )
        page.update()

    # CAMBIO IMPORTANTE: ft.Column(scroll="auto") en lugar de ListView
    tab_general = ft.Container(
        padding=10,
        expand=True,
        content=ft.Column([
            ft.Text("Datos", weight="bold"), 
            ft.Row([dd_raza, dd_clase]), 
            ft.Row([txt_nivel, ft.Text("Dado de Golpe:", color="grey"), txt_hit_dice]), 
            ft.Row([txt_raza_c, txt_clase_c]),
            ft.Divider(), ft.Text("Stats", weight="bold"), col_stats,
            ft.Divider(), 
            ft.Text("Dotes (Feats)", weight="bold"), 
            ft.Row([dd_dotes_select, ft.IconButton("add_circle", icon_color="green", on_click=add_dote_click)]),
            col_dotes_active
        ], scroll="auto", expand=True)
    )

    # --- PESTAÑA: INFO DE CLASE ---
    dd_info_clase = ft.Dropdown(
        options=[ft.dropdown.Option(c) for c in LISTA_CLASES if c != "OTRA (Manual)"],
        label="Selecciona Clase para ver Info",
        expand=True
    )
    
    md_clase_info = ft.Markdown(
        value="Selecciona una clase arriba para ver su información.",
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB
    )
    
    def change_info_clase(e):
        clase = dd_info_clase.value
        if clase in DATA_CLASES_INFO:
            md_clase_info.value = DATA_CLASES_INFO[clase]
        else:
            md_clase_info.value = "Información no disponible."
        page.update()

    dd_info_clase.on_change = change_info_clase

    tab_clase_info = ft.Container(
        padding=10, 
        content=ft.Column([
            dd_info_clase,
            ft.Divider(),
            ft.Container(
                content=ft.Column([md_clase_info], scroll="auto", expand=True),
                expand=True
            )
        ], expand=True)
    )

    # --- PESTAÑA 3: COMBATE ---
    txt_ac = ft.TextField(value="10", width=40, text_align="center", border="none", text_size=20, text_style=ft.TextStyle(weight="bold"), on_change=lambda e: update_combat("ac", e.control.value))
    
    def update_combat(k, v):
        try: char_data[k] = int(v); guardar()
        except: pass

    ui_ac = ft.Container(
        width=80, height=90, bgcolor="bluegrey900", border=ft.border.all(2, "cyan200"),
        border_radius=ft.border_radius.only(10,10,40,40), alignment=ft.alignment.center,
        content=ft.Column([ft.Text("AC", size=10, weight="bold"), txt_ac], alignment="center", spacing=0)
    )

    txt_hp = ft.Text("20", size=30, weight="bold", color="green")
    txt_hp_max = ft.TextField(label="Max", width=50, text_size=12, on_change=lambda e: update_combat("hp_max", e.control.value))
    txt_hp_temp = ft.Text("0", size=25, weight="bold", color="cyan")
    txt_hp_temp_max = ft.TextField(label="Max", width=50, text_size=12, on_change=lambda e: update_combat("hp_temp_max", e.control.value))

    def mod_hp(d, is_temp=False):
        key = "hp_temp" if is_temp else "hp_current"
        txt_target = txt_hp_temp if is_temp else txt_hp
        curr = int(txt_target.value) + d
        if curr < 0: curr = 0
        char_data[key] = curr
        txt_target.value = str(curr)
        if not is_temp: txt_target.color = "red" if curr <= 0 else "green"
        guardar()
        page.update()

    col_armas = ft.Column()
    txt_w_name = ft.TextField(label="Arma", expand=True, height=40)
    txt_w_cant = ft.TextField(label="Nº", width=40, height=40, value="1")
    dd_w_dice = ft.Dropdown(options=[ft.dropdown.Option(d) for d in ["d4","d6","d8","d10","d12","d20"]], width=70, value="d8")
    
    def add_weapon(e):
        if txt_w_name.value:
            char_data["armas"].append({"n": txt_w_name.value, "c": txt_w_cant.value, "d": dd_w_dice.value})
            txt_w_name.value = ""
            guardar()
            render_armas()
    def render_armas():
        col_armas.controls.clear()
        for w in char_data["armas"]:
            col_armas.controls.append(ft.Container(bgcolor="grey800", padding=10, border_radius=5, content=ft.Row([
                ft.Icon("security", color="red"),
                ft.Column([ft.Text(w['n'], weight="bold"), ft.Text(f"{w['c']}{w['d']}", color="yellow", size=12)], expand=True),
                ft.IconButton("delete", icon_size=15, on_click=lambda e,w=w: del_weapon(w))
            ])))
        page.update()
    def del_weapon(w):
        char_data["armas"].remove(w)
        guardar()
        render_armas()

    tab_combate = ft.ListView([
        ft.Row([ui_ac, ft.Column([
            ft.Text("Puntos de Golpe (HP)"),
            ft.Row([ft.IconButton("remove", on_click=lambda e: mod_hp(-1)), txt_hp, ft.IconButton("add", on_click=lambda e: mod_hp(1))]),
            ft.Row([ft.Text("Max:"), txt_hp_max]),
            ft.Divider(),
            ft.Text("HP Temporal", color="cyan"),
            ft.Row([ft.IconButton("remove", on_click=lambda e: mod_hp(-1, True)), txt_hp_temp, ft.IconButton("add", on_click=lambda e: mod_hp(1, True))]),
            ft.Row([ft.Text("Max:"), txt_hp_temp_max]),
        ])], alignment="spaceEvenly"),
        ft.Divider(),
        ft.Text("Armas", weight="bold"),
        ft.Row([txt_w_name, txt_w_cant, dd_w_dice]),
        ft.ElevatedButton("Agregar Arma", on_click=add_weapon, width=400),
        col_armas
    ], padding=10, expand=True)

    # --- PESTAÑA 4: MAGIA ---
    col_spells = ft.Column()
    col_extras = ft.Column()

    def crear_fila_recurso(label, current_val_str, callback_max_change, list_used_indices, callback_check_click):
        txt_max = ft.TextField(value=str(current_val_str), label=label, width=70, height=40, text_size=12, keyboard_type="NUMBER")
        row_checks = ft.Row(wrap=True, expand=True)

        def refresh_checks():
            row_checks.controls.clear()
            try: limit = int(txt_max.value)
            except: limit = 0
            
            for i in range(limit):
                is_checked = (i in list_used_indices)
                chk = ft.Checkbox(value=is_checked)
                def on_click(e, idx=i):
                    callback_check_click(e.control.value, idx)
                chk.on_change = on_click
                row_checks.controls.append(chk)
            page.update()

        def on_change_max(e):
            callback_max_change(e.control.value)
            refresh_checks()

        txt_max.on_change = on_change_max
        refresh_checks()
        return ft.Container(bgcolor="grey900", padding=5, margin=2, border_radius=5, content=ft.Row([txt_max, row_checks]))

    def render_extras():
        col_extras.controls.clear()
        for i, extra in enumerate(char_data["extras"]):
            txt_name = ft.TextField(value=extra["n"], expand=True, height=40, text_size=12, hint_text="Nombre (ej: Ki)")
            
            def save_name(e, idx=i):
                char_data["extras"][idx]["n"] = e.control.value
                guardar()
            txt_name.on_change = save_name

            def on_max_change(new_val, idx=i):
                char_data["extras"][idx]["m"] = new_val
                guardar()
            
            def on_check_click(is_checked, check_idx, idx=i):
                used_list = char_data["extras"][idx]["used"]
                if is_checked:
                    if check_idx not in used_list: used_list.append(check_idx)
                else:
                    if check_idx in used_list: used_list.remove(check_idx)
                guardar()

            fila_recurso = crear_fila_recurso("Max", extra["m"], on_max_change, extra["used"], on_check_click)
            col_extras.controls.append(ft.Column([txt_name, fila_recurso], spacing=2))

    def render_spells():
        col_spells.controls.clear()
        for n in range(1, 10):
            key = f"lvl{n}"
            def on_max_change(val, k=key):
                val_int = int(val) if val and val.isdigit() else 0
                char_data["spells_config"][k] = val_int
                guardar()
            def on_check_click(is_checked, idx, k=key):
                used_list = char_data["spells_used"][k]
                if is_checked:
                    if idx not in used_list: used_list.append(idx)
                else:
                    if idx in used_list: used_list.remove(idx)
                guardar()
            fila = crear_fila_recurso(f"Nv {n}", char_data["spells_config"].get(key, 0), on_max_change, char_data["spells_used"][key], on_check_click)
            col_spells.controls.append(fila)
        page.update()

    tab_magia = ft.Container(padding=10, content=ft.ListView([
        ft.Text("Recursos de Clase / Extras", weight="bold", color="cyan"),
        col_extras,
        ft.Divider(),
        ft.Text("Slots de Conjuro", weight="bold"), 
        col_spells
    ], expand=True))

    # --- PESTAÑA 5: MOCHILA (Fix UI Scroll) ---
    txt_gold = ft.Text("0", size=30, weight="bold", color="yellow")
    def mod_gold(d):
        curr = int(txt_gold.value) + d
        if curr < 0: curr = 0
        char_data["gold"] = curr
        txt_gold.value = str(curr)
        guardar()
        page.update()
    
    ui_gold = ft.Container(
        bgcolor="black", padding=10, border=ft.border.all(1, "yellow"), border_radius=10,
        content=ft.Column([
            ft.Text("Piezas de Oro (GP)", color="yellow", size=12),
            ft.Row([
                ft.IconButton("remove", on_click=lambda e: mod_gold(-10), icon_color="yellow"),
                ft.IconButton("remove", on_click=lambda e: mod_gold(-1), icon_size=15),
                txt_gold,
                ft.IconButton("add", on_click=lambda e: mod_gold(1), icon_size=15),
                ft.IconButton("add", on_click=lambda e: mod_gold(10), icon_color="yellow")
            ], alignment="center")
        ], alignment="center")
    )

    def crear_tab_inv_manual(key_db, titulo):
        # CAMBIO IMPORTANTE: ListView para scroll
        col_items = ft.ListView(expand=True, spacing=5)
        txt_item = ft.TextField(label="Nombre Item", expand=True, height=40)
        txt_desc = ft.TextField(label="Descripción", expand=True, height=40, text_size=12)
        
        def render_local_items():
            col_items.controls.clear()
            current_list = char_data[key_db]
            for item_dict in current_list:
                col_items.controls.append(ft.Container(
                    bgcolor="grey900", padding=5, border_radius=5,
                    content=ft.Row([
                        ft.Column([
                            ft.Text("• " + item_dict['n'], weight="bold"),
                            ft.Text(item_dict['d'], size=10, italic=True, color="grey")
                        ], expand=True, spacing=0),
                        ft.IconButton("close", icon_size=14, icon_color="red", on_click=lambda e, i=item_dict: borrar_item(i))
                    ])
                ))
            page.update()

        def add_item_click(e):
            if txt_item.value:
                nuevo = {"n": txt_item.value, "d": txt_desc.value}
                char_data[key_db].append(nuevo)
                txt_item.value = ""
                txt_desc.value = ""
                guardar()
                render_local_items()
        
        def borrar_item(item_target):
            if item_target in char_data[key_db]:
                char_data[key_db].remove(item_target)
                guardar()
                render_local_items()
        render_local_items()
        
        # Estructura segura: Inputs fijos, Lista scroll
        return ft.Tab(text=titulo, content=ft.Container(padding=10, content=ft.Column([
            ft.Column([txt_item, txt_desc, ft.ElevatedButton("Añadir a Mochila", on_click=add_item_click)]),
            ft.Divider(),
            col_items 
        ], expand=True)))

    # --- KITS Y HERRAMIENTAS (Scrollable) ---
    col_kits = ft.ListView(expand=True, spacing=5)
    def build_kits_and_tools():
        col_kits.controls.clear()
        
        col_kits.controls.append(ft.Text("Kits de Equipo", weight="bold", size=16, color="cyan"))
        for n, d in DATA_KITS.items():
            active = n in char_data["kits_tools"]
            col_kits.controls.append(ft.ExpansionTile(
                title=ft.Text(n), 
                leading=ft.Checkbox(value=active, on_change=lambda e,x=n: toggle_k(e,x)),
                controls=[ft.Container(padding=10, content=ft.Text(d, color="white70"))],
                text_color="white", collapsed_text_color="grey"
            ))
        
        col_kits.controls.append(ft.Divider())

        col_kits.controls.append(ft.Text("Herramientas y Útiles", weight="bold", size=16, color="orange"))
        for n, d in DATA_HERRAMIENTAS_FULL.items():
            active = n in char_data["kits_tools"]
            col_kits.controls.append(ft.ExpansionTile(
                title=ft.Text(n), 
                leading=ft.Checkbox(value=active, on_change=lambda e,x=n: toggle_k(e,x)),
                controls=[ft.Container(padding=10, content=ft.Text(d, color="white70"))],
                text_color="white", collapsed_text_color="grey"
            ))

    def toggle_k(e, name):
        if e.control.value: 
            if name not in char_data["kits_tools"]: char_data["kits_tools"].append(name)
        else:
            if name in char_data["kits_tools"]: char_data["kits_tools"].remove(name)
        guardar()

    def get_inv_tabs():
        return ft.Tabs(selected_index=0, tabs=[
            crear_tab_inv_manual("inv_armas", "Armas"),
            crear_tab_inv_manual("inv_armaduras", "Armaduras"),
            crear_tab_inv_manual("inv_pociones", "Pociones"),
            crear_tab_inv_manual("inv_comida", "Comida"),
            crear_tab_inv_manual("inv_varios", "Varios"),
            # CAMBIO IMPORTANTE: expand=True en el Container que envuelve la lista
            ft.Tab(text="Kits/Herramientas", content=ft.Container(padding=10, content=col_kits, expand=True)) 
        ], expand=True)

    container_mochila = ft.Container()

    # --- MAIN LOAD ---
    def recargar_interfaz():
        dd_raza.value = char_data["raza"]
        dd_clase.value = char_data["clase"]
        txt_nivel.value = str(char_data["nivel"])
        txt_raza_c.value = char_data["custom_raza"]
        txt_clase_c.value = char_data["custom_clase"]
        txt_raza_c.visible = (char_data["raza"] == "OTRA (Manual)")
        txt_clase_c.visible = (char_data["clase"] == "OTRA (Manual)")
        
        if char_data["clase"] in LISTA_CLASES and char_data["clase"] != "OTRA (Manual)":
             dd_info_clase.value = char_data["clase"]
             if char_data["clase"] in DATA_CLASES_INFO:
                 md_clase_info.value = DATA_CLASES_INFO[char_data["clase"]]

        update_hit_dice_display()
        build_stats()
        render_dotes_active()
        txt_ac.value = str(char_data["ac"])
        txt_hp.value = str(char_data["hp_current"])
        txt_hp_max.value = str(char_data["hp_max"])
        txt_hp.color = "red" if int(txt_hp.value) <= 0 else "green"
        txt_hp_temp.value = str(char_data["hp_temp"])
        txt_hp_temp_max.value = str(char_data["hp_temp_max"])
        txt_gold.value = str(char_data["gold"])
        render_armas()
        render_spells()
        render_extras() 
        build_kits_and_tools()
        container_mochila.content = ft.Column([ui_gold, ft.Divider(), get_inv_tabs()], expand=True)
        page.update()

    main_tabs = ft.Tabs(selected_index=0, tabs=[
        ft.Tab(text="General", icon="person", content=tab_general),
        ft.Tab(text="Clase", icon="menu_book", content=tab_clase_info),
        ft.Tab(text="Combate", icon="flash_on", content=tab_combate),
        ft.Tab(text="Magia", icon="auto_fix_high", content=tab_magia),
        ft.Tab(text="Mochila", icon="backpack", content=container_mochila),
    ], expand=True)

    # --- SAFE AREA WRAPPER ---
    page.add(
        ft.SafeArea(
            ft.Column([
                header, 
                ft.Divider(height=1), 
                main_tabs
            ], expand=True)
        )
    )
    
    recargar_interfaz()

ft.app(target=main)
