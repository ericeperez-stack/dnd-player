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

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles de bárbaro 8, 12 y 16.

**NIVEL 5: ATAQUE ADICIONAL**
Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Atacar en tu turno.

**NIVEL 5: MOVIMIENTO RÁPIDO**
Tu velocidad aumenta en 3 m mientras no lleves armadura pesada.

**NIVEL 7: INSTINTO SALVAJE**
Tu instinto es tan agudo que tienes ventaja en las tiradas de iniciativa. Además, si te sorprenden al comienzo del combate y no tienes el estado de incapacitado, puedes actuar normalmente en tu primer turno, pero solo si entras en furia antes de hacer cualquier otra cosa.

**NIVEL 7: SALTO INSTINTIVO**
Como parte de la acción adicional para dejarte llevar por la furia, puedes moverte hasta la mitad de tu velocidad. 

**NIVEL 9: GOLPE BRUTAL**
Puedes prescindir de la ventaja de tu Ataque temerario para golpear con más fuerza. Si usas Ataque temerario, puedes renunciar a la ventaja en una tirada de ataque para infligir 1d10 de daño adicional si aciertas.

**NIVEL 11: FURIA IMPLACABLE**
Tu furia puede mantenerte luchando a pesar de las heridas graves. Si tus puntos de golpe se reducen a 0 mientras estás en furia y no mueres al instante, puedes hacer una tirada de salvación de Constitución CD 10. Si tienes éxito, te quedas con 1 punto de golpe.

**NIVEL 13: GOLPE BRUTAL MEJORADO**
Has perfeccionado tus formas de atacar con fiereza. Entre las opciones de Golpe brutal se encuentran ahora los siguientes efectos:
Golpe abrumador. El objetivo tiene desventaja en la siguiente tirada de salvación que haga y no puede llevar a cabo ataques de oportunidad hasta el principio de tu siguiente turno. 
Golpe desgarrador. Antes del principio de tu siguiente turno, la próxima tirada de ataque realizada por otra criatura contra el objetivo obtiene un bonificador de +5. Una tirada de ataque puede obtener solo un bonificador de un golpe desgarrador. 

**NIVEL 15: FURIA PERSISTENTE**
Tu furia es tan intensa que solo termina antes de tiempo si caes inconsciente o si tú decides finalizarla.

**NIVEL 17: GOLPE BRUTAL MEJORADO**
El daño adicional de tu Golpe brutal aumenta a 2d10. Además, puedes utilizar dos efectos diferentes de Golpe brutal siempre que uses tu rasgo Golpe brutal.

**NIVEL 18: PODERÍO INDÓMITO**
Si tu resultado en una prueba de Fuerza o una tirada de salvación de Fuerza es inferior a tu puntuación de Fuerza, puedes usar esa puntuación en lugar del resultado.

**NIVEL 19: DON ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del ataque imparable.

**NIVEL 20: CAMPEÓN PRIMORDIAL**
Encarnas un poder primigenio. Tus puntuaciones de Fuerza y Constitución aumentan en 4, hasta un máximo de 25. 
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

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles de bardo 8, 12 y 16.

**NIVEL 5: FUENTE DE INSPIRACIÓN**
Recuperas todos tus usos de Inspiración bárdica cuando terminas un descanso corto o largo. Además, tu dado de Inspiración bárdica se convierte en un d8.

**NIVEL 7: CONTRAENCANTAMIENTO**
Como reacción cuando tú o una criatura a 9 m falláis una salvación contra un efecto que hechiza o asusta, puedes permitir que la criatura repita la salvación con ventaja.

**NIVEL 10: SECRETOS MÁGICOS**
Has aprendido conocimientos mágicos de un amplio espectro de disciplinas. Elige dos conjuros de cualquier clase (Bardo, Clérigo, Druida, Mago, etc.).

**NIVEL 18: NSPIRACIÓN SUPERIOR**
Cuando tires iniciativa, recuperarás usos gastados de Inspiración bárdica hasta que tengas dos, si tuvieras menos de esta cifra. 

**NIVEL 19: DON ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del recuerdo de conjuros. 

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

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles de clerigo 8, 12 y 16.

**NIVEL 5: DESTRUIR MUERTOS VIVIENTES**
Cuando un muerto viviente falla su salvación contra tu Expulsar muertos vivientes, la criatura recibe daño radiante instantáneo.

**NIVEL 7: GOLPES BENDITOS**
Elige uno:
* **Golpe Divino:** 1d8 daño radiante/necrótico extra con armas (1/turno).
* **Lanzamiento de Conjuros Potente:** Sumas Sabiduría al daño de tus trucos.

**NIVEL 10: INTERVENCIÓN DIVINA**
Puedes invocar a tu deidad para que intervenga. Como acción, describe la asistencia que buscas y tira dados de porcentaje. Si sacas un número igual o menor a tu nivel de clérigo, tu deidad interviene.

**NIVEL 14: GOLPES BENDITOS MEJORADOS**
La opción elegida para Golpes benditos se vuelve más poderosa.
Golpe divino. El daño adicional de tu Golpe divino aumenta a 2d8.
Lanzamiento potente. Cuando lances un truco de clérigo y causes daño a una criatura con él, podrás transmitir vitalidad a tio a otra criatura que esté a 18 m o menos de ti; se concederá una cantidad de puntos de golpe temporales igual al doble de tu modificador por Sabiduría. 

**NIVEL 19: DON EPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del destino.

**NIVEL 20: INTERCESIÒN DIVINA MAYOR**
Puedes solicitar una intercesión divina todavía más poderosa. Cuando uses tu rasgo Intercesión divina, puedes elegir deseo al seleccionar un conjuro. Si lo haces, no podrás volver a usar Intercesión divina hasta que finalices 2d4 descansos largos.
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

**NIVEL 7: FURIA ELEMENTAL**
El poder de los elementos fluye por ti. Obtienes una de las siguientes opciones, a tu elección. 
Golpe primordial. Una vez en cada uno de tus turnos, cuando aciertes a una criatura con una tirada de ataque usando un arma o un ataque de una bestia en Forma salvaje, podrás hacer que el objetivo sufra 1d8 de daño de frío, fuego, relámpago o trueno adicional (elígelo cuando aciertes). 
Lanzamiento potente. Sumas tu modificador por Sabiduría al daño que causas con cualquier truco de druida. 

**NIVEL 14: FURIA ELEMENTAL MEJORADA**
La opción elegida para Furia elemental se vuelve más poderosa, como se detalla a continuación. 
Golpe primordial. El daño adicional de tu Golpe primordial aumenta a 2d8. 
Lanzamiento potente. Cuando lances un truco de druida con un alcance de 3 m o más, el alcance del conjuro aumentará en 90 m.

**NIVEL 18: CONJURAR COMO BESTIA**
Puedes lanzar muchos de tus conjuros de druida en cualquier forma que adoptes con Forma Salvaje.

**NIVEL 19: DON EPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del viaje dimensional.

**NIVEL 20: ARCHIDRUIDA**
La vitalidad de la naturaleza florece en ti de manera constante, lo que te otorga los siguientes beneficios. Forma salvaje perenne. Cuando tires iniciativa y no te queden usos de Forma salvaje, recuperas uno de los usos gastados. 
Mago de la naturaleza. Puedes convertir los usos de Forma salvaje en un espacio de conjuro (no requiere acción). Elige una cantidad de usos no gastados de Forma salvaje para convertirlos en un único espacio de conjuro. Cada uso aporta 2 niveles de conjuro. Por ejemplo, si conviertes dos usos de Forma salvaje, produces un espacio de conjuro de nivel 4. Cuando uses este beneficio, no podrás volver a hacerlo hasta que finalices un descanso largo. 
Longevidad. La magia primigenia que dominas ralentiza tu envejecimiento. Por cada diez años que pasen, tu cuerpo envejece solo uno.
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

**NIVEL 4: MEJORA DE CARACTERISTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 6, 8,12, 14 y 16 de guerrero. 

**NIVEL 5: ATAQUE ADICIONAL**
Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Atacar en tu turno.

**NIVEL 5: DESPLAZAMIENTO TÀCTICO**
Cuando uses tu rasgo Tomar aliento con una acción adicional, podrás moverte hasta la mitad de tu velocidad sin provocar ataques de oportunidad. 

**NIVEL 9: INDÓMITO**
Puedes volver a tirar una tirada de salvación que falles. Debes usar el nuevo resultado.

**NIVEL 9: MAESTRO TÁCTICO**
Cuando ataques usando un arma con la que puedas utilizar su propiedad de maestría, puedes sustituir la propiedad para ese ataque por la de debilitar, empujar o ralentizar.

**NIVEL 11: DOS ATAQUES ADICIONALES**
Cuando lleves a cabo la acción de atacar en tu turno, podrás hacer tres ataques en lugar de uno.

**NIVEL 13: ATAQUES ESTUDIADOS**
Estudias a tus adversarios y aprendes con cada ataque que realizas. Si haces una tirada de ataque contra una criatura y fallas, tendrás ventaja en tu siguiente tirada de ataque contra esa criatura antes del final de tu siguiente turno.

**NIVEL 19: DON ÈPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don de la pericia en combate. 

**NIVEL 20: TRES ATAQUES ADICIONALES**
Cuando lleves a cabo la acción de atacar en tu turno, podrás hacer cuatro ataques en lugar de uno. 
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

**NIVEL 2: MOVIMIENTO SIN ARMADURA**
Tu velocidad aumenta en 3 m si no llevas armadura ni portas un escudo. Esta bonificación aumenta cuando alcanzas ciertos niveles de monje, como se muestra en la tabla “Rasgos de monje”. 

**NIVEL 3: DESVIAR ATAQUES**
Puedes usar tu reacción para desviar o atrapar el proyectil cuando te golpea un ataque de arma a distancia. El daño se reduce en 1d10 + Destreza + Nivel de monje.

**NIVEL 3: SUBCLASE DE MONJE**
Consigues una subclase de monje de tu elección. 
Las subclases de guerrero de la mano abierta, guerrero de la misericordia, guerrero de la sombra y guerrero de los elementos se detallan tras la descripción de esta clase. Una subclase es una especialización que te proporciona rasgos cuando alcanzas ciertos niveles de monje. De aquí en adelante, obtienes todos los rasgos de tu subclase que sean de tu nivel de monje e inferiores. 

**NIVEL 4: CAIDA LENTA**
Puedes llevar a cabo una reacción cuando caigas para reducir cualquier daño que sufras de la caída en una cantidad igual a cinco veces tu nivel de monje.

**NIVEL 4: MEJORA DE CARACTERÌSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 12 y 16 de monje. 

**NIVEL 5: ATAQUE ADICIONAL**
Cuando lleves a cabo la acción de atacar en tu turno, podrás hacer dos ataques en lugar de uno.

**NIVEL 5: GOLPE ATURDIDOR**
Cuando golpeas a otra criatura con un ataque de arma cuerpo a cuerpo, puedes gastar 1 punto de concentración para intentar un golpe aturdidor.

**NIVEL 6: GOLPES POTENCIADOS**
Siempre que inflijas daño con tu ataque sin armas, puedes elegir entre causar daño de fuerza o su tipo de daño normal.

**NIVEL 7: EVASIÒN**
Cuando sufras un efecto que te permita hacer una tirada de salvación de Destreza para sufrir solo la mitad de daño, no recibes daño alguno si la superas y'solo sufres la mitad si la fallas. 
No te beneficias de este rasgo si tienes el estado de incapacitado. 

**NIVEL 9: MOVIMIENTO ACROBATICO**
Mientras no lleves armadura ni portes un escudo, obtienes la capacidad de moverte por superficies verticales y sobre líquidos sin caerte.

**NIVEL 10: AUTORRESTABLECIMIENTO**
Por pura fuerza de voluntad, puedes eliminar uno de los siguientes estados que te afecten al final de cada uno de tus turnos: asustado, envenenado o hechizado. 
Además, privarte de comida y bebida no te aplica niveles de cansancio. 

**NIVEL 10: CONCENTRACION AGUDIZADA**
Tus rasgos Defensa paciente, Paso del viento y Ráfaga de golpes obtienen los siguientes beneficios: 
Defensa paciente. Cuando gastes un punto de concentración para usar Defensa paciente, obtienes una cantidad de puntos de golpe temporales igual al resultado de dos tiradas de tu dado de Artes marciales. 
Paso del viento. Cuando gastes un punto de concentración para usar Paso del viento, puedes elegir una criatura voluntaria Grande o más pequeña que esté a 1,5 m o menos de ti. Moverás a la criatura contigo hasta el final de tu turno. El movimiento de la criatura no provoca ataques de oportunidad. 
Ráfaga de golpes. Puedes gastar 1 punto de concentración para usar Ráfaga de golpes y hacer tres ataques sin armas en lugar de dos. 

**NIVEL 13: DESVIAR ENERGIA**
Ahora puedes usar tu rasgo Desviar ataques contra ataques que causen cualquier tipo de daño, no solo contundente, cortante o perforante. 

**NiIvEL 14: SUPERVIVIENTE DISCIPLINADO**
Tu disciplina física y mental te otorga competencia en todas las tiradas de salvación. 
Además, cuando hagas una tirada de salvación y falles, puedes gastar 1 punto de concentración para repetirla, pero deberás utilizar el nuevo resultado. 

**NiveL 15: CONCENTRACIÓN PERFECTA**
Cuando tires iniciativa y no utilices Metabolismo asombroso, recuperas los puntos de concentración gastados hasta que tengas 4 si te quedan 3 o menos. 

**NiveL 18: DEFENSA SUPERIOR**
Al principio de tu turno, puedes gastar 3 puntos de concentración para protegerte del daño durante 1 minuto o hasta que tengas el estado de incapacitado. Durante ese tiempo, tendrás resistencia a todo el daño excepto al de fuerza. 

**NiveL 19: Don ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del ataque imparable. 

**NivEL 20: CUERPO Y MENTE**
Has llevado tu cuerpo y mente a otro nivel. Tus puntuaciones de Destreza y Sabiduría aumentan en 4, hasta un máximo de 25. 
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

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 12 y 16 de paladín. 

**NIVEL 5: ATAQUE ADICIONAL**
Cuando lleves a cabo la acción de atacar en tu turno, podrás hacer dos ataques en lugar de uno. 

**NIVEL 5: CORCEL FIEL**
Puedes invocar la ayuda de un corcel sobrenatural. 
Siempre tienes el conjuro hallar corcel preparado. 
También puedes lanzarlo una vez sin gastar un espacio de conjuro y recuperas la capacidad de hacerlo tras finalizar un descanso largo. 

**NIVEL 6: AURA DE PROTECCIÓN**
Siempre que tú o una criatura amistosa a 3 m de ti debáis realizar una tirada de salvación, la criatura gana un bonificador a la tirada igual a tu modificador por Carisma.

NIVEL 9: ABJURAR DE LOS ENEMIGOS 
Como acción de magia, puedes gastar uno de los usos de Canalizar divinidad de esta clase para sobrecoger a tus enemigos. Mientras muestras tu símbolo sagrado o arma, puedes hacer objetivo a una cantidad de criaturas que puedas ver a 18 m o menos de ti igual a tu modificadorpor Carisma (mínimo una criatura). Cada objetivo deberá superar una tirada de salvación de Sabiduría o tendrá el estado de asustado durante 1 minuto o hasta recibir daño. 
Mientras esté asustado de esta forma, un objetivo solo podrá hacer una de estas opciones en sus turnos: moverse, realizar una acción o realizar una acción adicional.

**NIVEL 10: AURA DE CORAJE**
Tus aliados y tú tenéis inmunidad al estado de asustados mientras estéis dentro de tu Aura de protección. Si un aliado asustado entra en el aura, ese estado no tendrá efecto en él mientras esté dentro. 

**NIVEL 11: GOLPES RADIANTES**
Ahora, tus golpes tienen un poder sobrenatural. Cuando aciertes a un objetivo con una tirada de ataque usando un arma cuerpo a cuerpo o un ataque sin armas, el objetivo recibirá 1d8 de daño radiante adicional. 

**NIVEL 14: TOQUE REPARADOR**
Cuando uses Imponer las manos sobre una criatura, también podrás eliminar uno o más de los siguientes estados que la afecten: asustado, aturdido, cegado, ensordecido, hechizado o paralizado. Deberás gastar 5 puntos de golpe de la reserva de curación de Imponer las manos por cada uno de los estados que elimines, pero esos puntos gastados no restaurarán puntos de golpe. 

**NIVEL 18: EXPANSIÓN DE AURA**
Tu Aura de protección ahora es una emanación de 9 m. 

**NIVEL 19: Don ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don de la visión verdadera.
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

**NIVEL 1: MAESTRÍA CON ARMAS**
Tu entrenamiento con armas te permite utilizar las propiedades de maestría con dos tipos de armas de tu elección con las que tengas competencia, como arcos largos y espadas cortas. 
Tras finalizar un descanso largo, puedes cambiar los tipos de armas elegidas. Por ejemplo, podrías pasar a utilizar las propiedades de maestría con cimitarras y espadas largas.

**NIVEL 2: ESTILO DE COMBATE**
Eliges un estilo de combate (Arququería, Defensa, Duelo, Combate con dos armas).

**NIVEL 3: SUBCLASE DE EXPLORADOR**
Eliges un Conclave de Explorador (Cazador, Bestias, Acechador en la Penumbra, Errante Feérico).

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 12 y 16 de explorador.

**NIVEL 5: ATAQUE ADICIONAL**
Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Atacar en tu turno.

**NIVEL 6: ERRANTE (ROVING)**
Tu velocidad caminando aumenta en 3 m. Ganas velocidad de escalada y natación igual a tu velocidad caminando.

**NIVEL 9: PERICIA**
Escoge dos de tus competencias en habilidades con las que no tengas pericia. Ganas pericia en esas habilidades.

**NIVEL 10: INFATIGABLE**
Las fuerzas primigenias te ayudan ahora en tus viajes, lo que te otorga los siguientes beneficios. 
Puntos de golpe temporales. Como acción de magia, puedes concederte una cantidad de puntos de golpe temporales igual a 148 más tu modificador por Sabiduría (mínimo de 1). Puedes usar esta acción una cantidad de veces igual a tu modificador por Sabiduría (mínimo una vez) y recuperas todos los usos tras finalizar un descanso largo. Disminuir cansancio. Tras finalizar un descanso corto, tu nivel de cansancio, si lo tienes, se reduce en 1. 

**NIVEL 13: CAZADOR PERSISTENTE**
Sufrir daño no rompe tu concentración de marca del cazador. 

**NIVEL 14: VELO DE LA NATURALEZA**
Invocas espíritus de la naturaleza para esconderte mágicamente. Como acción adicional, puedes otorgarte el estado de invisible hasta el final de tu siguiente turno. Puedes usar este rasgo una cantidad de veces igual a tu modificador por Sabiduría (mínimo una vez) y recuperas todos los usos tras finalizar un descanso largo. 

**NIVEL 17: CAZADOR PRECISO**
Tienes ventaja en las tiradas de ataque contra la criatura que tenga tu marca del cazador sobre ella. 

**NIVEL 18: SENTIDOS SALVAJES**
Tu conexión con las fuerzas de la naturaleza te otorga visión ciega hasta 9 m. 

**NIVEL 19: Don ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del viaje dimensional. 

**NIVEL 20: AZOTE DE ENEMIGOS**
El dado de daño de tu marca del cazador es un d10 en lugar de un d6. 
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

**NIVEL 1: MAESTRÍA CON ARMAS**
Tu entrenamiento con armas te permite utilizar las propiedades de maestría con dos tipos de armas de tuelección con las que tengas competencia, como dagas y arcos cortos. 
Tras finalizar un descanso largo, puedes cambiar los tipos de armas elegidas. Por ejemplo, podrías pasar a utilizar las propiedades de maestría con cimitarras y espadas cortas. 

**NIVEL 2: ACCIÓN ASTUTA**
Tu rapidez mental y agilidad te permiten moverte y actuar rápidamente. Puedes realizar una acción adicional en cada uno de tus turnos de combate. Esta acción solo puede usarse para: Correr, Destrabarse o Esconderse.

**NIVEL 3: SUBCLASE DE PÍCARO**
Eliges un Arquetipo de Pícaro (Ladrón, Asesino, Embaucador Arcano, Soulknife).

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 10, 12 y 16 de pícaro.

**NIVEL 5: ESQUIVA ASOMBROSA**
Cuando un atacante que puedes ver te golpea con un ataque, puedes usar tu reacción para reducir a la mitad el daño del ataque contra ti.

**NIVEL 5: GOLPE ASTUTO**
Has desarrollado formas astutas de usar tu Ataque furtivo. 
Cuando infliges daño de Ataque furtivo, puedes añadir uno de los siguientes efectos de Golpe astuto. Cada unotiene un coste en dados que es la cantidad de dados de daño de Ataque furtivo a los que debes renunciar para añadir el efecto. Retiras la cantidad de dados antes de tirar y el efecto se produce inmediatamente después de que se cause el daño del ataque. Por ejemplo, si añades el efecto de veneno, quita 1d6 del daño de Ataque furtivo antes de tirar. 
Si un efecto de Golpe astuto requiere una tirada de salvación, la CD es igual a 8 más tu modificador por Destreza y tu bonificador por competencia. 
Retirada (coste: 1d6). Justo después del ataque, te mueves hasta la mitad de tu velocidad sin provocar ataques de oportunidad. 
Tropiezo (coste: 1d6). Si el objetivo es Grande o más pequeño, deberá superar una tirada de salvación de Destreza o tendrá el estado de derribado. 
Veneno (coste: 146). Añades una toxina a tu golpe, lo que obliga al objetivo a hacer una tirada de salvación de Constitución. Si la falla, tendrá el estado de envenenado durante 1 minuto. Al final de cada uno de sus turnos, el objetivo envenenado repetirá la tirada de salvación y, si tiene éxito, se librará del efecto. Para usar este efecto, debes llevar contigo unos útiles de envenenador. 

**NIVEL 7: EVASIÓN**
Cuando estás sometido a un efecto que te permite hacer una tirada de salvación de Destreza para recibir solo la mitad de daño, no recibes daño si tienes éxito y solo la mitad si fallas.

**NIVEL 7: TALENTOS FIABLES**
Cuando hagas una prueba de característica que utilice una de tus competencias en habilidades o con herramientas, puedes sustituir un resultado de 9 o menos en el d20 por un 10.

**NIVEL 11: GOLPE ASTUTO MEJORADO**
Puedes usar hasta dos efectos de Golpe astuto cuando inflijas daño de Ataque furtivo pagando el coste en dados por cada efecto. 

**NIVEL 14: GOLPES TAIMADOS**
Has practicado nuevas formas de usar tu Ataque furtivo de forma artera. Entre las opciones de Golpe astuto se encuentran ahora los siguientes efectos. 
Confundir (coste: 2d6). El objetivo deberá superar una tirada de salvación de Constitución. Si no lo hace, en su próximo turno solo podrá moverse, realizar una acción o realizar una acción adicional. 
Noquear (coste: 6d6). El objetivo deberá superar una tirada de salvación de Constitución o tendrá el estado de inconsciente durante 1 minuto o hasta recibir daño. El objetivo inconsciente repetirá la tirada de salvación al final de cada uno de sus turnos y, si tiene éxito, se librará del efecto. 
Ofuscar (coste: 3d6). El objetivo deberá superar una tirada de salvación de Destreza o tendrá el estado de cegado hasta el final de su siguiente turno. 

**NIVEL 15: MENTE ESCURRIDIZA**
Tu mente astuta es excepcionalmente difícil de controlar. Ganas competencia en las tiradas de salvación de Sabiduría y Carisma. 

**NIVEL 18: ELUSIVO** Eres tan escurridizo que será raro que un atacante pueda golpearte con facilidad. Ninguna tirada de ataque contra ti tendrá ventaja a menos que tengas el estado de incapacitado. 

**NIVEL 19: Don ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del espíritu de la noche. 

**NIVEL 20: GOLPE DE SUERTE**
Has desarrollado una capacidad asombrosa para tener éxito justo cuando lo necesitas. Si fallas una prueba con d20, puedes convertir el resultado de la tirada en un 20. Cuando uses este rasgo, no podrás volver a hacerlo hasta que finalices un descanso corto o largo.
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

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 12 y 16 de hechicero. 

**NIVEL 5: RESPUESTA HECHICERA**
Cuando fallas una tirada de salvación, puedes gastar puntos de hechicería para volver a tirar.


**NIVEL 7: ENCARNACIÓN MÁGICA*
Si no te quedan usos del rasgo Hechicería innata, puedes usarlo si gastas 2 puntos de hechicería cuando empleas la acción adicional para activarlo. 
Además, mientras tengas activo el rasgo Hechicería innata, puedes usar hasta dos de tus opciones de metamagia en cada conjuro que lances. 

**NIVEL 19: DON ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del viaje dimensional. 

**NIVEL 20: APOTEOSIS ARCANA**
Mientras tengas activo el rasgo Hechicería innata, puedes usar una opción de metamagia en cada uno de tus turnos sin gastar puntos de hechicería. 
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

**NIVEL 4: MEJORA DE CARACTERÍSTICA** Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 12 y 16 de brujo. 

**NIVEL 9: CONTACTAR PATRÓN 
Antes solías ponerte en contacto con tu patrón a través de intermediarios. Ahora puedes comunicarte directamente, ya que siempre tienes el conjuro contactar con otro plano preparado. Con este rasgo, puedes lanzar el conjuro sin gastar un espacio de conjuro para contactar con tu patrón y superas automáticamente la tirada de salvación del conjuro. 
Cuando lances el conjuro con este rasgo, no podrás volver a hacerlo de esta forma hasta que finalices un descanso largo. 

**NIVEL 11: ARCANUM MÍSTICO 
Tu patrón te recompensa con un secreto mágico denominado arcanum. Escoge uno de los conjuros de brujo de nivel 6 como este arcanum. 
Puedes lanzar tu conjuro de arcanum una vez sin gastar un espacio de conjuro y debes finalizar un descanso largo antes de poder volver a lanzarlo de este modo. 
Obtendrás más conjuros de brujo de tu elección que podrás lanzar de esta forma cuando alcances los niveles 13 (conjuro de nivel 7), 15 (conjuro de nivel 8) y 17 (conjuro de nivel 9) de brujo, como se muestra en la tabla “Rasgos de brujo”. Recuperas todos los usos de tu Arcanum místico tras finalizar un descanso largo. 
Siempre que subas un nivel de brujo, puedes sustituir uno de tus conjuros de arcanum por otro conjuro de brujo del mismo nivel. 

**NivEL 19: DON ÉPICO 
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del destino. 

**NIVEL 20: MAESTRO SOBRENATURAL 
Cuando empleas tu rasgo Astucia mágica, recuperas todos los espacios de conjuro utilizados de Magia del pacto. 
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

**NIVEL 2: ACADÉMICO**
Mientras estudiabas magia, también te especializaste en otro campo. Elige una de las siguientes habilidades en la que tengas competencia: Conocimiento arcano, Historia, Investigación, Medicina, Naturaleza o Religión. Ganas pericia en la habilidad elegida. 

**NIVEL 3: SUBCLASE DE MAGO**
Eliges una Tradición Arcana (Abjuración, Adivinación, Evocación, Ilusión).

**NIVEL 4: MEJORA DE CARACTERÍSTICA**
Obtienes la dote Mejora de característica (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Vuelves a obtener este rasgo en los niveles 8, 12 y 16 de mago.

**NIVEL 5: MEMORIZAR CONJURO**
Puedes cambiar un conjuro preparado por otro de tu libro tras 1 minuto de estudio.

**NIVEL 18: MAESTRÍA SOBRE CONJUROS**
Has alcanzado tal maestría sobre ciertos conjuros que puedes lanzarlos a voluntad. Elige un conjuro de nivel 1 y otro de nivel 2 de tu libro de conjuros con un tiempo de lanzamiento de una acción. Siempre tienes esos conjuros preparados y puedes lanzarlos a su nivel más bajo sin gastar un espacio de conjuro. Para lanzar cualquiera de ellos a un nivel superior, deberás gastar un espacio de conjuro. Tras finalizar un descanso largo, puedes estudiar tu libro de conjuros y sustituir uno de los conjuros por otro del libro del mismo nivel que cumpla los requisitos.

**NiveL 19: Don ÉPICO**
Obtienes una dote de don épico (consulta el capítulo 5) u otra dote de tu elección para la que cumplas las condiciones. Se recomienda Don del recuerdo de conjuros. 

**NIvEL 20: CONJUROS CARACTERÍSTICOS**
Escoge dos conjuros de nivel 3 que figuren en tu libro de conjuros como conjuros característicos. Siempre tienes esos conjuros preparados y puedes lanzar cada uno de ellos una vez a nivel 3 sin gastar un espacio de conjuro. Una vez que los lances, no podrás volver a hacerlo de este modo hasta que finalices un descanso corto o largo. Para lanzar cualquiera de ellos a un nivel superior, deberás gastar un espacio de conjuro. 
""",

    "OTRA (Manual)": """# CLASE PERSONALIZADA
Esta sección está reservada para clases que no aparecen en el Manual del Jugador 2024 o contenido de terceros.
Por favor, consulta la fuente original de tu clase para ver los rasgos y anótalos manualmente en las notas de tu personaje.
"""
}

# --- PAQUETES DE EQUIPO ---
DATA_KITS = {
    "Paquete de Artista": "(40 po) Campana, cantimplora, 3 disfraces, espejo, 8 frascos de aceite, linterna de ojo de buey, mochila, petate, raciones para 9 días y yesquero.",
    
    "Paquete de Diplomático": "(39 po) Cofre, 2 estuches para mapas o pergaminos, 4 frascos de aceite, 5 hojas de papel, 5 hojas de pergamino, lámpara, perfume, 5 plumas, ropas de calidad, tinta y yesquero.",
    
    "Paquete de Erudito": "(40 po) 10 frascos de aceite, 10 hojas de pergamino, lámpara, libro, mochila, pluma, tinta y yesquero.",
    
    "Paquete de Explorador": "(10 po) 10 antorchas, cantimplora, cuerda, 2 frascos de aceite, mochila, petate, raciones para 10 días y yesquero.",
    
    "Paquete de Explorador de Mazmorras": "(12 po) Abrojos, 10 antorchas, cantimplora, cuerda, 2 frascos de aceite, mochila, palanqueta, raciones para 10 días y yesquero.",
    
    "Paquete de Ladrón": "(16 po) Bolas de metal, campana, cantimplora, cuerda, 7 frascos de aceite, linterna sorda, mochila, palanqueta, raciones para 5 días, 10 velas y yesquero.",
    
    "Paquete de Sacerdote": "(33 po) Agua bendita, lámpara, manta, mochila, raciones para 7 días, túnica y yesquero."
}

# --- HERRAMIENTAS COMPLETAS (TEXTUALES) ---
DATA_HERRAMIENTAS_FULL = {
    "Herramientas de Albañil": """(10 po) - Peso: 4 kg
Característica: Fuerza
Utilizar: Esculpir un símbolo o un agujero en la piedra (CD 10).
Fabricar: Polipasto.""",

    "Herramientas de Alfarero": """(10 po) - Peso: 1.5 kg
Característica: Inteligencia
Utilizar: Distinguir lo que ha contenido un objeto de cerámica durante las últimas 24 horas (CD 15).
Fabricar: Jarro, lámpara.""",

    "Herramientas de Carpintero": """(8 po) - Peso: 3 kg
Característica: Fuerza
Utilizar: Sellar o forzar una puerta o un recipiente (CD 20).
Fabricar: Bastón, garrote, garrote grande, antorcha, ariete portátil, barril, cofre, escalera, vara.""",

    "Herramientas de Cartógrafo": """(15 po) - Peso: 3 kg
Característica: Sabiduría
Utilizar: Dibujar un mapa de una zona pequeña (CD 15).
Fabricar: Mapa.""",

    "Herramientas de Curtidor": """(5 po) - Peso: 2.5 kg
Característica: Destreza
Utilizar: Añadir un diseño a un objeto de cuero (CD 10).
Fabricar: Honda, látigo, armadura de cuero, armadura de cuero tachonado, armadura de pieles, aljaba, bolsa, cantimplora, estuche para mapas/pergaminos/virotes, mochila, pergamino.""",

    "Herramientas de Ebanista": """(1 po) - Peso: 2.5 kg
Característica: Destreza
Utilizar: Tallar un dibujo en madera (CD 10).
Fabricar: Bastón, garrote, garrote grande, armas a distancia (salvo honda/fuego), canalizador arcano/druídico, dardos, flechas, pluma, virotes.""",

    "Herramientas de Herrero": """(20 po) - Peso: 4 kg
Característica: Fuerza
Utilizar: Forzar una puerta o un recipiente (CD 20).
Fabricar: Cualquier arma cuerpo a cuerpo (salvo madera/cuero), armaduras medias (salvo pieles), armaduras pesadas, abrojos, balas, bolas de metal, cadena, cubo, garfio, olla, palanqueta, proyectiles, puntas.""",

    "Herramientas de Joyero": """(25 po) - Peso: 1 kg
Característica: Inteligencia
Utilizar: Discernir el valor de una gema (CD 15).
Fabricar: Canalizador arcano, símbolo sagrado.""",

    "Herramientas de Manitas": """(50 po) - Peso: 5 kg
Característica: Destreza
Utilizar: Montar un objeto Diminuto de chatarra que se desarma en 1 minuto (CD 20).
Fabricar: Mosquete, pistola, campana, cerradura, espejo, esposas, frasco, linterna, pala, silbato, trampa, yesquero.""",

    "Herramientas de Soplador de Vidrio": """(30 po) - Peso: 2.5 kg
Característica: Inteligencia
Utilizar: Distinguir contenido de objeto de vidrio en últimas 24h (CD 15).
Fabricar: Botella de cristal, catalejo, lupa, vial.""",

    "Herramientas de Tejedor": """(1 po) - Peso: 2.5 kg
Característica: Destreza
Utilizar: Remendar roto o coser diseño Diminuto (CD 10).
Fabricar: Armadura acolchada, cesta, cordel, cuerda, manta, petate, red, ropas, saco, tienda, túnica.""",

    "Herramientas de Zapatero": """(5 po) - Peso: 2.5 kg
Característica: Destreza
Utilizar: Modificar calzado para dar ventaja en Acrobacias (CD 10).
Fabricar: Útiles de escalada.""",

    "Suministros de Alquimista": """(50 po) - Peso: 4 kg
Característica: Inteligencia
Utilizar: Identificar sustancia o encender fuego (CD 15).
Fabricar: Aceite, ácido, fuego de alquimista, papel, perfume, saquito de componentes.""",

    "Suministros de Calígrafo": """(10 po) - Peso: 2.5 kg
Característica: Destreza
Utilizar: Escribir texto con florituras infalsificable (CD 15).
Fabricar: Pergamino de conjuro, tinta.""",

    "Suministros de Cervecero": """(20 po) - Peso: 4.5 kg
Característica: Inteligencia
Utilizar: Detectar bebida envenenada (CD 15) o identificar alcohol (CD 10).
Fabricar: Antitoxina.""",

    "Suministros de Pintor": """(10 po) - Peso: 2.5 kg
Característica: Sabiduría
Utilizar: Pintar imagen reconocible de memoria (CD 10).
Fabricar: Canalizador druídico, símbolo sagrado.""",

    "Útiles de Cocinero": """(1 po) - Peso: 4 kg
Característica: Sabiduría
Utilizar: Mejorar sabor (CD 10) o detectar veneno/podrido (CD 15).
Fabricar: Raciones.""",

    "Herramientas de Ladrón": """(25 po) - Peso: 0.5 kg
Característica: Destreza
Utilizar: Forzar cerradura o desarmar trampa (CD 15).""",

    "Herramientas de Navegante": """(25 po) - Peso: 1 kg
Característica: Sabiduría
Utilizar: Trazar rumbo (CD 10) o determinar posición por estrellas (CD 15).""",

    "Instrumento Musical": """(Precio/Peso Variable)
Característica: Carisma
Utilizar: Tocar melodía conocida (CD 10) o improvisar (CD 15).
Variantes: Chirimía, Cuerno, Dulcémele, Flauta, Gaita, Laúd, Lira, Tambor, Viola, etc.""",

    "Juego": """(Precio Variable)
Característica: Sabiduría
Utilizar: Distinguir trampas (CD 10) o ganar partida (CD 20).
Variantes: Ajedrez dragón, Dados, Naipes, Tres dragones.""",

    "Útiles de Envenenador": """(50 po) - Peso: 1 kg
Característica: Inteligencia
Utilizar: Detectar objeto envenenado (CD 10).
Fabricar: Veneno básico.""",

    "Útiles de Herborista": """(5 po) - Peso: 1.5 kg
Característica: Inteligencia
Utilizar: Identificar una planta (CD 10).
Fabricar: Antitoxina, poción de curación, útiles de sanador, vela.""",

    "Útiles para Disfrazarse": """(25 po) - Peso: 1.5 kg
Característica: Carisma
Utilizar: Maquillar (CD 10).
Fabricar: Disfraz.""",

    "Útiles para Falsificar": """(15 po) - Peso: 2.5 kg
Característica: Destreza
Utilizar: Escribir <10 palabras imitando letra (CD 15) o duplicar sello (CD 20)."""
}

# --- DOTES COMPLETOS (TEXTUALES) ---
DATA_DOTES_FULL = {
    # --- DOTES DE ORIGEN ---
    "Afortunado": """Dote de origen
Obtienes los siguientes beneficios:
* Puntos de suerte: Tienes una cantidad de puntos igual a tu bonificador por competencia. Recuperas los gastados tras un descanso largo.
* Ventaja: Cuando tires 1d20 para una prueba, puedes gastar 1 punto para ganar ventaja.
* Desventaja: Cuando una criatura tire 1d20 en un ataque contra ti, puedes gastar 1 punto para imponerle desventaja.""",

    "Alerta": """Dote de origen
Obtienes los siguientes beneficios:
* Competencia en iniciativa: Puedes sumar tu bonificador por competencia a la iniciativa.
* Intercambio de iniciativa: Justo después de tirar iniciativa, puedes cambiar tu resultado con el de un aliado dispuesto en el mismo combate (si ninguno está incapacitado).""",

    "Atacante Salvaje": """Dote de origen
Te has preparado para asestar golpes especialmente dañinos.
Una vez por turno, cuando aciertes a un objetivo con un arma, podrás tirar dos veces los dados de daño del arma y usar el resultado que prefieras.""",

    "Duro": """Dote de origen
Tus puntos de golpe máximos aumentan en una cantidad igual al doble del nivel de tu personaje cuando adquieres esta dote.
A partir de entonces, cada vez que subas un nivel, tus HP máximos aumentan en 2 puntos adicionales.""",

    "Fabricante": """Dote de origen
Obtienes los siguientes beneficios:
* Competencia con herramientas: Ganas competencia con tres herramientas de artesano a tu elección.
* Descuento: 20% de descuento al comprar objetos no mágicos.
* Fabricación rápida: Tras un descanso largo, puedes fabricar un objeto de la tabla de fabricación rápida si tienes las herramientas. Dura hasta el siguiente descanso largo.""",

    "Habilidoso": """Dote de origen
Ganas competencia en cualquier combinación de tres habilidades o herramientas que elijas.
Repetible: Puedes elegir esta dote más de una vez.""",

    "Iniciado en la Magia": """Dote de origen
Obtienes los siguientes beneficios:
* Dos trucos: Aprendes 2 trucos de la lista de Clérigo, Druida o Mago.
* Conjuro de nivel 1: Elige un conjuro de nivel 1 de la misma lista. Siempre lo tienes preparado. Puedes lanzarlo una vez gratis por descanso largo, o usando tus espacios de conjuro.
* Cambiar conjuro: Al subir de nivel, puedes reemplazar uno de estos conjuros.
* Repetible: Puedes elegirla más veces (con listas distintas).""",

    "Matón de Taberna": """Dote de origen
Obtienes los siguientes beneficios:
* Ataque sin armas mejorado: Daño 1d4 + Fuerza.
* Repetir tiradas de daño: Si sacas un 1 en el daño de ataque sin armas, puedes volver a tirar (usas el nuevo).
* Armas improvisadas: Tienes competencia con ellas.
* Empujar: Cuando aciertes con un ataque sin armas al Atacar, puedes empujar al objetivo 1.5m (una vez por turno).""",

    "Músico": """Dote de origen
Obtienes los siguientes beneficios:
* Formación instrumental: Competencia con 3 instrumentos.
* Canción alentadora: Tras un descanso corto/largo, tocas una canción. Das inspiración heroica a aliados igual a tu bonificador de competencia.""",

    "Sanador": """Dote de origen
Obtienes los siguientes beneficios:
* Médico de batalla: Si tienes útiles de sanador, gasta un uso y una acción para que una criatura a 1.5m gaste un dado de golpe y recupere HP igual al resultado + tu competencia.
* Repetir tiradas de curación: Si sacas un 1 al curar con conjuro o esta dote, puedes volver a tirar.""",

    # --- DOTES GENERALES ---
    "Acechador": """Requisito: Nivel 4+, Des 13+
* Mejora de característica: +1 Destreza (max 20).
* Visión ciega: Hasta 3 m.
* Niebla de guerra: Ventaja en Sigilo al esconderse en combate.
* En la sombra: Fallar un ataque escondido no revela tu posición.""",

    "Actor": """Requisito: Nivel 4+, Car 13+
* Mejora de característica: +1 Carisma (max 20).
* Suplantación: Ventaja en Engaño/Interpretación al disfrazarte de otra persona.
* Imitación: Puedes imitar sonidos y voces. Detectarlo requiere superar CD (8 + Car + Comp).""",

    "Apresador": """Requisito: Nivel 4+, Fue/Des 13+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Golpear y agarrar: Al acertar un ataque sin armas, puedes usar opciones de daño y agarre (1/turno).
* Ventaja al atacar: Ventaja en ataques contra quien tengas agarrado.
* Luchador rápido: No te cuesta movimiento extra mover a una criatura agarrada de tu tamaño o menor.""",

    "Atacante a la Carga": """Requisito: Nivel 4+, Fue/Des 13+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Carrera mejorada: Al usar la acción Correr, tu velocidad aumenta 3 m.
* Ataque con carga: Si mueves 3m en línea recta y golpeas cuerpo a cuerpo, elige: +1d8 daño O empujar 3m (1/turno).""",

    "Atleta": """Requisito: Nivel 4+, Fue/Des 13+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Velocidad trepando: Igual a tu velocidad normal.
* Levantarse de un salto: Levantarte solo cuesta 1.5 m.
* Saltar: Saltos con carrera tras moverte solo 1.5 m.""",

    "Azote de Magos": """Requisito: Nivel 4+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Anticoncentración: Si dañas a alguien concentrándose, tiene desventaja en la salvación.
* Mente robusta: Si fallas salvación de Int/Sab/Car, puedes decidir superarla (1/descanso).""",

    "Centinela": """Requisito: Nivel 4+, Fue/Des 13+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Guardián: Si una criatura a 1.5m usa Destrabarse o ataca a otro, puedes hacerle un ataque de oportunidad.
* Detener: Si aciertas oportunidad, su velocidad es 0 el resto del turno.""",

    "Chef": """Requisito: Nivel 4+
* Mejora de característica: +1 Con o Sab (max 20).
* Útiles de cocinero: Ganas competencia.
* Comida reconstituyente: En descanso corto, cocinas. Quienes coman y gasten dados de golpe recuperan +1d8 HP.
* Tentempiés: Preparas bocados (acción bonus comer) que dan HP Temporales = Competencia.""",

    "Combatiente con Dos Armas": """Requisito: Nivel 4+, Fue/Des 13+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Manejo doble mejorado: Al atacar con arma ligera, puedes hacer el ataque extra con cualquier arma que no sea 'a dos manos' (no solo ligeras).
* Desenvainar rápido: Sacas/guardas dos armas a la vez.""",

    "Combatiente Montado": """Requisito: Nivel 4+
* Mejora de característica: +1 Fue, Des o Sab (max 20).
* Golpe montado: Ventaja en ataques contra criaturas a pie más pequeñas que tu montura.
* Esquivar de un salto: Tu montura gana Evasión (si tú estás montado y consciente).
* Girar bruscamente: Puedes redirigir un ataque contra tu montura hacia ti.""",

    "Duelista Defensivo": """Requisito: Nivel 4+, Des 13+
* Mejora de característica: +1 Destreza (max 20).
* Parada: Si empuñas arma sutil y te aciertan cuerpo a cuerpo, usa reacción para sumar Competencia a tu CA (puede hacer que falle). Dura hasta tu turno.""",

    "Entrenamiento con Armas Marciales": """Requisito: Nivel 4+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Competencia: Ganas competencia con armas marciales.""",

    "Envenenador": """Requisito: Nivel 4+
* Mejora de característica: +1 Des o Int (max 20).
* Veneno potente: Tu daño de veneno ignora resistencia.
* Preparar veneno: Competencia kit envenenador. Creas dosis (coste 50po). Aplicar es acción bonus. CD Salvación = 8 + Mod + Comp. Daño 2d8 y estado envenenado.""",

    "Experto en Ballestas": """Requisito: Nivel 4+, Des 13+
* Mejora de característica: +1 Destreza (max 20).
* Ignorar recarga: Ignoras la propiedad de carga.
* Disparar cuerpo a cuerpo: No tienes desventaja al disparar a 1.5m de un enemigo.
* Manejo doble: Si atacas con arma ligera, puedes hacer ataque extra con ballesta ligera.""",

    "Experto en Habilidades": """Requisito: Nivel 4+
* Mejora de característica: +1 a una característica (max 20).
* Competencia: Ganas una habilidad nueva.
* Pericia: Ganas pericia en una habilidad que ya tengas.""",

    "Influencia Feérica": """Requisito: Nivel 4+
* Mejora de característica: +1 Int, Sab o Car (max 20).
* Magia feérica: Aprendes un conjuro nvl 1 (Adivinación/Encantamiento) y Paso Brumoso. Puedes lanzarlos gratis 1 vez/día o con slots.""",

    "Influencia Sombría": """Requisito: Nivel 4+
* Mejora de característica: +1 Int, Sab o Car (max 20).
* Magia de las sombras: Aprendes un conjuro nvl 1 (Ilusión/Nigromancia) e Invisibilidad. Puedes lanzarlos gratis 1 vez/día o con slots.""",

    "Lanzador en Combate": """Requisito: Nivel 4+, puede lanzar conjuros
* Mejora de característica: +1 Int, Sab o Car (max 20).
* Concentración: Ventaja en Constitución para mantener concentración.
* Conjuro reactivo: Puedes lanzar un conjuro (1 acción) como reacción de oportunidad.
* Componentes somáticos: Puedes lanzar con las manos ocupadas (armas/escudo).""",

    "Lanzador Preciso": """Requisito: Nivel 4+, puede lanzar conjuros
* Mejora de característica: +1 Int, Sab o Car (max 20).
* Sortear cobertura: Ignoras cobertura media y tres cuartos.
* Cuerpo a cuerpo: No tienes desventaja al lanzar conjuros de ataque a 1.5m.
* Alcance aumentado: +18m al alcance de conjuros de ataque (si tienen al menos 3m).""",

    "Lanzador Ritual": """Requisito: Nivel 4+, Int/Sab/Car 13+
* Mejora de característica: +1 Int, Sab o Car (max 20).
* Conjuros rituales: Elige rituales de nivel 1 igual a tu competencia. Siempre preparados.
* Ritual rápido: Puedes lanzar un ritual preparado con su tiempo normal (1 acción) en lugar del tiempo largo (1 vez/descanso).""",

    "Líder Inspirador": """Requisito: Nivel 4+, Sab/Car 13+
* Mejora de característica: +1 Sabiduría o Carisma (max 20).
* Interpretación fortalecedora: Tras descanso, das HP Temporales a 6 aliados = Nivel + Mod Característica.""",

    "Ligeramente Acorazado": """Requisito: Nivel 4+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Entrenamiento: Competencia con armaduras ligeras y escudos.""",

    "Maestro de Armas": """Requisito: Nivel 4+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Propiedad de maestría: Puedes usar la propiedad de maestría de un arma a elección.""",

    "Maestro en Armaduras Medias": """Requisito: Nivel 4+, Armadura Media
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Portador diestro: Con armadura media, puedes sumar +3 Des a la CA (en vez de +2) si tienes Des 16+.""",

    "Maestro en Armaduras Pesadas": """Requisito: Nivel 4+, Armadura Pesada
* Mejora de característica: +1 Con o Fue (max 20).
* Reducción de daño: Reduces daño contundente/cortante/perforante en una cantidad igual a tu Competencia.""",

    "Maestro en Armas de Asta": """Requisito: Nivel 4+, Fue/Des 13+
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Golpe con asta: Tras atacar con lanza/bastón/alabarda, acción bonus para golpear con el otro extremo (1d4).
* Golpe reactivo: Reacción de oportunidad cuando entran en tu alcance.""",

    "Maestro en Armas Pesadas": """Requisito: Nivel 4+, Fue 13+
* Mejora de característica: +1 Fuerza (max 20).
* Maestría: Al golpear con arma pesada, +Competencia al daño.
* Avasallar: Si haces crítico o matas, ataque extra como acción bonus.""",

    "Maestro en Escudos": """Requisito: Nivel 4+, Escudos
* Mejora de característica: +1 Fuerza (max 20).
* Golpe con escudo: Si atacas, puedes empujar o derribar con escudo (bonus).
* Interponer escudo: Reacción para no recibir daño en salvaciones de DES exitosas.""",

    "Mejora de Característica": """Requisito: Nivel 4+
Aumenta una característica en +2, o dos en +1 (Max 20).
Repetible.""",

    "Mente Aguda": """Requisito: Nivel 4+, Int 13+
* Mejora de característica: +1 Inteligencia (max 20).
* Sabiduría popular: Pericia en una habilidad de saber (Arcanos, Historia, etc).
* Estudio rápido: Acción Estudiar como bonus.""",

    "Moderadamente Acorazado": """Requisito: Nivel 4+, Armadura Ligera
* Mejora de característica: +1 Fuerza o Destreza (max 20).
* Entrenamiento: Competencia con armaduras medias.""",

    "Muy Acorazado": """Requisito: Nivel 4+, Armadura Media
* Mejora de característica: +1 Con o Fue (max 20).
* Entrenamiento: Competencia con armaduras pesadas.""",

    "Observador": """Requisito: Nivel 4+, Int/Sab 13+
* Mejora de característica: +1 Int o Sab (max 20).
* Observador perspicaz: Pericia en Investigación, Percepción o Perspicacia.
* Búsqueda rápida: Acción Buscar como bonus.""",

    "Perforador": """Requisito: Nivel 4+
* Mejora de característica: +1 Fue o Des (max 20).
* Horadar: Rerollear un dado de daño perforante por turno.
* Crítico potenciado: Críticos perforantes añaden un dado extra de daño.""",

    "Rebanador": """Requisito: Nivel 4+
* Mejora de característica: +1 Fue o Des (max 20).
* Lacerar: Daño cortante reduce velocidad objetivo 3m (1/turno).
* Crítico potenciado: Críticos cortantes imponen desventaja en ataques al objetivo.""",

    "Resiliente": """Requisito: Nivel 4+
* Mejora: +1 a una característica.
* Competencia: Ganas competencia en salvaciones de esa característica.""",

    "Resistente": """Requisito: Nivel 4+
* Mejora de característica: +1 Constitución (max 20).
* Desafiar muerte: Ventaja en salvaciones de muerte.
* Recuperación: Bonus para gastar un dado de golpe y curarte.""",

    "Telepático": """Requisito: Nivel 4+
* Mejora: +1 Int, Sab o Car (max 20).
* Habla telepática: 18m.
* Detectar pensamientos: Puedes lanzarlo gratis 1/día o con slots.""",

    "Telequinético": """Requisito: Nivel 4+
* Mejora: +1 Int, Sab o Car (max 20).
* Telequinesis menor: Aprendes Mano de Mago (invisible, más rango).
* Empellón: Acción bonus para empujar 1.5m (Salvación FUE).""",

    "Tirador de Primera": """Requisito: Nivel 4+, Des 13+
* Mejora: +1 Destreza (max 20).
* Sortear cobertura: Ignoras media y tres cuartos.
* Cuerpo a cuerpo: Sin desventaja a 1.5m.
* Tiros lejanos: Sin desventaja a largo alcance.""",

    "Triturador": """Requisito: Nivel 4+
* Mejora: +1 Fue o Con (max 20).
* Empujar: Daño contundente mueve 1.5m (1/turno).
* Crítico: Tus críticos dan ventaja a los ataques contra el objetivo.""",

    "Veloz": """Requisito: Nivel 4+, Des/Con 13+
* Mejora: +1 Des o Con (max 20).
* Velocidad: +3m.
* Terreno difícil: Ignoras terreno difícil al correr.
* Ágil: Oportunidad contra ti tiene desventaja.""",

    "Versado en un Elemento": """Requisito: Nivel 4+, conjuros
* Mejora: +1 Int, Sab o Car (max 20).
* Dominio: Elige un tipo (fuego, frío, etc). Ignoras resistencia. Los 1s en daño cuentan como 2s.""",

    # --- ESTILOS DE COMBATE ---
    "Estilo: Armas a Dos Manos": "Rerollea 1s y 2s en daño con armas a dos manos/versátiles.",
    "Estilo: Armas Arrojadizas": "+2 daño con armas arrojadizas.",
    "Estilo: Dos Armas": "Sumas modificador de característica al daño del segundo ataque.",
    "Estilo: Sin Armas": "Daño desarmado 1d6 + Fue (o 1d8). 1d4 daño a agarrados.",
    "Estilo: Defensa": "+1 CA con armadura.",
    "Estilo: Duelo": "+2 daño con una sola arma.",
    "Estilo: Intercepción": "Reacción para reducir daño a aliado (1d10+Comp).",
    "Estilo: Lucha a Ciegas": "Visión ciega 3m.",
    "Estilo: Protección": "Reacción con escudo para dar desventaja a ataque contra aliado.",
    "Estilo: Tiro con Arco": "+2 ataque armas distancia.",

    # --- DONES ÉPICOS (Nivel 19+) ---
    "Don de la Fortaleza": "+1 Característica (max 30). +40 HP. Curación extra por turno.",
    "Don de la Habilidad": "+1 Característica (max 30). Competencia en TODAS las habilidades. Pericia en una.",
    "Don de la Pericia": "+1 Característica (max 30). Si fallas ataque, puedes acertar (1/turno).",
    "Don de la Recuperación": "+1 Característica. Evitas caer a 0 HP (1/descanso). Reserva curación 10d10.",
    "Don de Resistencia": "+1 Característica. Resistencia a 2 tipos de daño. Reacción para redirigir daño.",
    "Don de la Velocidad": "+1 Característica. Acción bonus Destrabarse. +9m velocidad.",
    "Don de Visión Verdadera": "+1 Característica. Visión verdadera 18m.",
    "Don de Ataque Imparable": "+1 Fue/Des. Ignoras resistencia física. Críticos añaden daño extra.",
    "Don del Destino": "+1 Característica. Bonus/Penalizador 2d4 a una tirada cercana (1/combate).",
    "Don Espíritu Noche": "+1 Característica. Invisibilidad como bonus en oscuridad. Resistencia daño (salvo rad/psi).",
    "Don Recuerdo Conjuros": "+1 Int/Sab/Car. 25% prob. de no gastar slot (niveles 1-4).",
    "Don Viaje Dimensional": "+1 Característica. Teletransporte 9m tras atacar o lanzar conjuro."
}

def main(page: ft.Page):
    page.title = "D&D Player App v17 Final"
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
            "extras": [{"n": "Recurso 1", "m": "0", "used": []}, {"n": "Recurso 2", "m": "0", "used": []}, {"n": "Recurso 3", "m": "0", "used": []}],
            "spells_config": {f"lvl{i}": 0 for i in range(1, 10)},
            "spells_used": {f"lvl{i}": [] for i in range(1, 10)},
            "inv_armas": [], "inv_armaduras": [], "inv_pociones": [], "inv_comida": [], "inv_varios": [],
            "kits_tools": []
        }

    all_chars = page.client_storage.get("dnd_chars_v17") or {"Default": get_empty_char()}
    
    for d in all_chars.values():
        if "dotes_list" not in d: d["dotes_list"] = [] 
        if "kits_tools" not in d: d["kits_tools"] = []
        if "extras" not in d: d["extras"] = [{"n": "Recurso 1", "m": "0", "used": []}, {"n": "Recurso 2", "m": "0", "used": []}, {"n": "Recurso 3", "m": "0", "used": []}]

    char_data = all_chars[current_char_name]

    def guardar():
        all_chars[current_char_name] = char_data
        page.client_storage.set("dnd_chars_v17", all_chars)

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
                page.client_storage.set("dnd_chars_v17", all_chars)
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

    # --- PESTAÑA 1: GENERAL (MODO SEGURO) ---
    # Eliminamos el height=40 forzado para evitar crashes en móviles con fuentes grandes.
    # Usamos dense=True para mantenerlo compacto de forma natural.
    padding_compact = ft.padding.symmetric(horizontal=10)

    dd_raza = ft.Dropdown(
        label="Raza",
        options=[ft.dropdown.Option(x) for x in LISTA_RAZAS],
        expand=True,
        # height=40,  <-- ELIMINADO PARA SEGURIDAD
        text_size=12,
        content_padding=padding_compact,
        dense=True,
        on_change=lambda e: update_gen("raza", e.control.value)
    )

    txt_raza_c = ft.TextField(
        label="Otra Raza", 
        visible=False, 
        expand=True, 
        # height=40, <-- ELIMINADO PARA SEGURIDAD
        text_size=12, 
        content_padding=padding_compact, 
        dense=True,
        on_change=lambda e: update_gen("custom_raza", e.control.value)
    )

    dd_clase = ft.Dropdown(
        label="Clase",
        options=[ft.dropdown.Option(x) for x in LISTA_CLASES],
        expand=True,
        # height=40, <-- ELIMINADO PARA SEGURIDAD
        text_size=12,
        content_padding=padding_compact,
        dense=True,
        on_change=lambda e: update_gen("clase", e.control.value)
    )
    
    txt_nivel = ft.TextField(
        label="Nivel", 
        width=60, 
        # height=40, <-- ELIMINADO PARA SEGURIDAD
        text_size=12,
        content_padding=padding_compact, 
        dense=True,
        on_change=lambda e: update_gen("nivel", e.control.value)
    )

    txt_clase_c = ft.TextField(label="Otra Clase", visible=False, expand=True, dense=True, content_padding=padding_compact, text_size=12, on_change=lambda e: update_gen("custom_clase", e.control.value))
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

    col_dotes_active = ft.Column()
    dd_dotes_select = ft.Dropdown(
        label="Buscar Dote...",
        options=[ft.dropdown.Option(text=k, key=k) for k in sorted(DATA_DOTES_FULL.keys())],
        expand=True, enable_filter=True
    )

    def add_dote_click(e):
        if dd_dotes_select.value:
            desc = DATA_DOTES_FULL[dd_dotes_select.value]
            if not any(d['n'] == dd_dotes_select.value for d in char_data["dotes_list"]):
                char_data["dotes_list"].append({"n": dd_dotes_select.value, "d": desc})
                guardar()
                render_dotes_active()
                dd_dotes_select.value = None
                page.update()

    def delete_dote_click(e):
        char_data["dotes_list"] = [d for d in char_data["dotes_list"] if d['n'] != e.control.data]
        guardar()
        render_dotes_active()

    def render_dotes_active():
        col_dotes_active.controls.clear()
        for dote in char_data["dotes_list"]:
            col_dotes_active.controls.append(ft.Container(bgcolor="grey900", border_radius=5, margin=2, content=ft.Column([
                ft.Row([ft.Text(dote['n'], color="yellow", weight="bold", expand=True), ft.IconButton("delete", icon_color="red", data=dote['n'], on_click=delete_dote_click)]),
                ft.ExpansionTile(title=ft.Text("Ver descripción", size=12, italic=True), controls=[ft.Container(padding=10, content=ft.Text(dote['d'], size=13))])
            ])))
        page.update()

    tab_general = ft.Container(
        content=ft.ListView([
            ft.Text("Datos", weight="bold"), 
            ft.Row([dd_raza, dd_clase]), 
            ft.Row([txt_nivel, ft.Text("Dado de Golpe:", color="grey"), txt_hit_dice]), 
            ft.Row([txt_raza_c, txt_clase_c]),
            ft.Divider(), ft.Text("Stats", weight="bold"), col_stats,
            ft.Divider(), 
            ft.Text("Dotes (Feats)", weight="bold"), 
            ft.Row([dd_dotes_select, ft.IconButton("add_circle", icon_color="green", on_click=add_dote_click)]),
            col_dotes_active
        ], padding=10, spacing=10),
        expand=True
    )

    # --- PESTAÑA 2: INFO DE CLASE (CORREGIDA) ---
    dd_info_clase = ft.Dropdown(options=[ft.dropdown.Option(c) for c in LISTA_CLASES if c != "OTRA (Manual)"], label="Ver Info Clase", expand=True)
    md_clase_info = ft.Markdown(value="Selecciona arriba.", selectable=True)
    
    def change_info_clase(e):
        if dd_info_clase.value in DATA_CLASES_INFO: md_clase_info.value = DATA_CLASES_INFO[dd_info_clase.value]
        page.update()
    dd_info_clase.on_change = change_info_clase

    tab_clase_info = ft.Container(
        padding=10,
        content=ft.Column([
            dd_info_clase, 
            ft.Divider(),
            ft.Container(
                content=ft.Column([md_clase_info], scroll=ft.ScrollMode.AUTO, expand=True),
                expand=True, 
                border_radius=5,
                padding=5,
                border=ft.border.all(1, "grey900")
            )
        ], expand=True)
    )

    # --- PESTAÑA 3: COMBATE ---
    txt_ac = ft.TextField(value="10", width=40, text_align="center", on_change=lambda e: update_combat("ac", e.control.value))
    def update_combat(k, v):
        try: char_data[k] = int(v); guardar()
        except: pass
    ui_ac = ft.Container(width=80, height=90, bgcolor="bluegrey900", border=ft.border.all(2, "cyan200"), border_radius=ft.border_radius.only(10,10,40,40), alignment=ft.alignment.center, content=ft.Column([ft.Text("AC", size=10, weight="bold"), txt_ac], alignment="center", spacing=0))
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
        guardar()
        page.update()

    col_armas = ft.Column()
    txt_w_name = ft.TextField(label="Arma", expand=True, height=40)
    txt_w_cant = ft.TextField(label="Nº", width=40, height=40, value="1")
    dd_w_dice = ft.Dropdown(options=[ft.dropdown.Option(d) for d in ["d4","d6","d8","d10","d12","d20"]], width=70, value="d8")
    
    def add_weapon(e):
        if txt_w_name.value:
            char_data["armas"].append({"n": txt_w_name.value, "c": txt_w_cant.value, "d": dd_w_dice.value})
            txt_w_name.value = ""; guardar(); render_armas()
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
        char_data["armas"].remove(w); guardar(); render_armas()

    tab_combate = ft.Container(
        content=ft.ListView([
            ft.Row([ui_ac, ft.Column([
                ft.Text("Puntos de Golpe"),
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
        ], padding=10, expand=True),
        expand=True
    )

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
                chk = ft.Checkbox(value=(i in list_used_indices), on_change=lambda e, idx=i: callback_check_click(e.control.value, idx))
                row_checks.controls.append(chk)
            page.update()
        txt_max.on_change = lambda e: [callback_max_change(e.control.value), refresh_checks()]
        refresh_checks()
        return ft.Container(bgcolor="grey900", padding=5, margin=2, border_radius=5, content=ft.Row([txt_max, row_checks]))

    def render_extras():
        col_extras.controls.clear()
        for i, extra in enumerate(char_data["extras"]):
            txt_name = ft.TextField(value=extra["n"], expand=True, height=40, text_size=12, hint_text="Nombre (ej: Ki)")
            txt_name.on_change = lambda e, idx=i: [char_data["extras"][idx].update({"n": e.control.value}), guardar()]
            def on_max(v, idx=i): char_data["extras"][idx]["m"] = v; guardar()
            def on_click(chk, c_idx, idx=i):
                u = char_data["extras"][idx]["used"]
                if chk and c_idx not in u: u.append(c_idx)
                elif not chk and c_idx in u: u.remove(c_idx)
                guardar()
            col_extras.controls.append(ft.Column([txt_name, crear_fila_recurso("Max", extra["m"], on_max, extra["used"], on_click)], spacing=2))

    def render_spells():
        col_spells.controls.clear()
        for n in range(1, 10):
            k = f"lvl{n}"
            def on_max(v, key=k): char_data["spells_config"][key] = int(v) if v.isdigit() else 0; guardar()
            def on_click(chk, idx, key=k):
                u = char_data["spells_used"][key]
                if chk and idx not in u: u.append(idx)
                elif not chk and idx in u: u.remove(idx)
                guardar()
            col_spells.controls.append(crear_fila_recurso(f"Nv {n}", char_data["spells_config"].get(k, 0), on_max, char_data["spells_used"][k], on_click))
        page.update()

    tab_magia = ft.Container(
        content=ft.ListView([
            ft.Text("Recursos de Clase / Extras", weight="bold", color="cyan"), col_extras,
            ft.Divider(), ft.Text("Slots de Conjuro", weight="bold"), col_spells
        ], padding=10, expand=True),
        expand=True
    )

    # --- PESTAÑA 5: MOCHILA ---
    txt_gold = ft.Text("0", size=30, weight="bold", color="yellow")
    def mod_gold(d):
        char_data["gold"] = max(0, int(txt_gold.value) + d); txt_gold.value = str(char_data["gold"]); guardar(); page.update()
    
    ui_gold = ft.Container(bgcolor="black", padding=10, border=ft.border.all(1, "yellow"), border_radius=10, content=ft.Column([
        ft.Text("Oro (GP)", color="yellow", size=12),
        ft.Row([ft.IconButton("remove", on_click=lambda e: mod_gold(-10), icon_color="yellow"), ft.IconButton("remove", on_click=lambda e: mod_gold(-1), icon_size=15), txt_gold, ft.IconButton("add", on_click=lambda e: mod_gold(1), icon_size=15), ft.IconButton("add", on_click=lambda e: mod_gold(10), icon_color="yellow")], alignment="center")
    ], alignment="center"))

    def crear_tab_inv_manual(key_db, titulo):
        col_items = ft.ListView(expand=True, spacing=5)
        txt_item = ft.TextField(label="Nombre", expand=True, height=40)
        txt_desc = ft.TextField(label="Desc", expand=True, height=40)
        
        def render_items():
            col_items.controls.clear()
            for item in char_data[key_db]:
                col_items.controls.append(ft.Container(bgcolor="grey900", padding=5, border_radius=5, content=ft.Row([
                    ft.Column([ft.Text("• " + item['n'], weight="bold"), ft.Text(item['d'], size=10, italic=True)], expand=True, spacing=0),
                    ft.IconButton("close", icon_size=14, icon_color="red", on_click=lambda e, i=item: [char_data[key_db].remove(i), guardar(), render_items()])
                ])))
            page.update()
        
        def add_item(e):
            if txt_item.value:
                char_data[key_db].append({"n": txt_item.value, "d": txt_desc.value}); txt_item.value=""; txt_desc.value=""; guardar(); render_items()
        
        render_items()
        return ft.Tab(text=titulo, content=ft.Container(padding=10, content=ft.Column([
            ft.Column([txt_item, txt_desc, ft.ElevatedButton("Añadir", on_click=add_item)]),
            ft.Divider(), col_items
        ], expand=True)))

    col_kits = ft.ListView(expand=True, spacing=5)
    def build_kits():
        col_kits.controls.clear()
        col_kits.controls.append(ft.Text("Kits", weight="bold", color="cyan"))
        for n, d in DATA_KITS.items():
            col_kits.controls.append(ft.ExpansionTile(title=ft.Text(n), leading=ft.Checkbox(value=(n in char_data["kits_tools"]), on_change=lambda e,x=n: toggle_k(e,x)), controls=[ft.Container(padding=10, content=ft.Text(d, color="white70"))]))
        col_kits.controls.append(ft.Divider())
        col_kits.controls.append(ft.Text("Herramientas", weight="bold", color="orange"))
        for n, d in DATA_HERRAMIENTAS_FULL.items():
            col_kits.controls.append(ft.ExpansionTile(title=ft.Text(n), leading=ft.Checkbox(value=(n in char_data["kits_tools"]), on_change=lambda e,x=n: toggle_k(e,x)), controls=[ft.Container(padding=10, content=ft.Text(d, color="white70"))]))

    def toggle_k(e, name):
        if e.control.value: 
            if name not in char_data["kits_tools"]: char_data["kits_tools"].append(name)
        else: 
            if name in char_data["kits_tools"]: char_data["kits_tools"].remove(name)
        guardar()

    container_mochila = ft.Container()

    # --- MAIN UI ---
    def recargar_interfaz():
        dd_raza.value = char_data["raza"]; dd_clase.value = char_data["clase"]; txt_nivel.value = str(char_data["nivel"])
        txt_raza_c.value = char_data["custom_raza"]; txt_clase_c.value = char_data["custom_clase"]
        txt_raza_c.visible = (char_data["raza"] == "OTRA (Manual)")
        txt_clase_c.visible = (char_data["clase"] == "OTRA (Manual)")
        if char_data["clase"] in LISTA_CLASES and char_data["clase"] != "OTRA (Manual)":
             dd_info_clase.value = char_data["clase"]
             if char_data["clase"] in DATA_CLASES_INFO: md_clase_info.value = DATA_CLASES_INFO[char_data["clase"]]
        update_hit_dice_display(); build_stats(); render_dotes_active()
        txt_ac.value = str(char_data["ac"]); txt_hp.value = str(char_data["hp_current"])
        txt_hp_max.value = str(char_data["hp_max"]); txt_hp.color = "red" if int(txt_hp.value) <= 0 else "green"
        txt_hp_temp.value = str(char_data["hp_temp"]); txt_hp_temp_max.value = str(char_data["hp_temp_max"])
        txt_gold.value = str(char_data["gold"])
        render_armas(); render_spells(); render_extras(); build_kits()
        
        # PESTAÑAS DE MOCHILA
        tabs_mochila = ft.Tabs(selected_index=0, tabs=[
            crear_tab_inv_manual("inv_armas", "Armas"), crear_tab_inv_manual("inv_armaduras", "Armaduras"),
            crear_tab_inv_manual("inv_pociones", "Pociones"), crear_tab_inv_manual("inv_comida", "Comida"),
            crear_tab_inv_manual("inv_varios", "Varios"),
            ft.Tab(text="Kits", content=ft.Container(padding=10, content=col_kits, expand=True))
        ], expand=True)
        container_mochila.content = ft.Column([ui_gold, ft.Divider(), tabs_mochila], expand=True)
        page.update()

    main_tabs = ft.Tabs(selected_index=0, tabs=[
        ft.Tab(text="General", icon="person", content=tab_general),
        ft.Tab(text="Clase", icon="menu_book", content=tab_clase_info),
        ft.Tab(text="Combate", icon="flash_on", content=tab_combate),
        ft.Tab(text="Magia", icon="auto_fix_high", content=tab_magia),
        ft.Tab(text="Mochila", icon="backpack", content=container_mochila),
    ], expand=True)

    # --- ESTRUCTURA PRINCIPAL SEGURA ---
    # Corrección final para evitar pantalla negra en móviles
    layout_principal = ft.Column(
        controls=[
            header, 
            ft.Divider(height=1), 
            main_tabs
        ], 
        expand=True,
        spacing=0
    )

    page.add(ft.SafeArea(layout_principal, expand=True))
    recargar_interfaz()

ft.app(target=main)
