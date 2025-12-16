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
**Dado de Golpe:** 1d12 por nivel.
**Competencias:** Armaduras ligeras, medias, escudos. Armas sencillas, marciales.
**Salvaciones:** Fuerza, Constitución.

## RASGOS
**NIVEL 1: FURIA**
Ventaja en pruebas de FUE. Resistencia daño contundente/perforante/cortante. +2 Daño. (No conjuros).

**NIVEL 1: DEFENSA SIN ARMADURA**
CA = 10 + Des + Con (si no llevas armadura).

**NIVEL 2: ATAQUE TEMERARIO**
Ventaja en tu ataque de FUE, pero enemigos tienen ventaja contra ti.

**NIVEL 2: SENTIR EL PELIGRO**
Ventaja en salvaciones de DES contra lo que veas.

**NIVEL 3: SUBCLASE (SENDA)**
Eliges tu camino (Berserker, Totémico, etc).

**NIVEL 5: ATAQUE EXTRA**
Atacas dos veces por acción.

**NIVEL 5: MOVIMIENTO RÁPIDO**
+3m velocidad (sin armadura pesada).
""",
    "Bardo": """# BARDO
**Dado de Golpe:** 1d8.
**Competencias:** Ligera. Armas sencillas, ballesta mano, espada larga/corta, estoque. 3 instrumentos.
**Salvaciones:** Destreza, Carisma.

## RASGOS
**NIVEL 1: INSPIRACIÓN**
Acción bonus: Dar d6 a aliado (60 min uso).

**NIVEL 1: CONJUROS**
Carisma. Rituales permitidos.

**NIVEL 2: APRENDIZ DE MUCHO**
Sumas mitad de competencia a pruebas sin competencia.

**NIVEL 2: CANCIÓN DE DESCANSO**
Aliados recuperan +1d6 en descanso corto.

**NIVEL 3: COLEGIO (SUBCLASE)**
Eliges tu especialidad.

**NIVEL 3: PERICIA**
Doble competencia en 2 habilidades.

**NIVEL 5: FUENTE DE INSPIRACIÓN**
Recuperas inspiración en descanso corto. Dado sube a d8.
""",
    "Clérigo": """# CLÉRIGO
**Dado de Golpe:** 1d8.
**Competencias:** Ligera, Media, Escudos. Sencillas.
**Salvaciones:** Sabiduría, Carisma.

## RASGOS
**NIVEL 1: DOMINIO (SUBCLASE)**
Eliges Vida, Guerra, Luz, etc. Otorga rasgos.

**NIVEL 1: CONJUROS**
Sabiduría. Preparas lista diaria.

**NIVEL 2: CANALIZAR DIVINIDAD**
Expulsar Muertos Vivientes (huyen si fallan SAB). Efecto de Dominio.

**NIVEL 5: DESTRUIR MUERTOS VIVIENTES**
Si fallan expulsión, reciben daño radiante.
""",
    "Druida": """# DRUIDA
**Dado de Golpe:** 1d8.
**Competencias:** Ligera, Media, Escudos (No metal). Armas druídicas. Herboristería.
**Salvaciones:** Inteligencia, Sabiduría.

## RASGOS
**NIVEL 1: DRUÍDICO**
Idioma secreto.

**NIVEL 1: CONJUROS**
Sabiduría. Preparas lista diaria.

**NIVEL 2: FORMA SALVAJE**
Transformarse en bestia (VD 1/4 al inicio). Mantienes mente, usas físico bestia.

**NIVEL 2: CÍRCULO (SUBCLASE)**
Eliges Tierra, Luna, etc.
""",
    "Guerrero": """# GUERRERO
**Dado de Golpe:** 1d10.
**Competencias:** Todas armaduras, Escudos. Todas armas.
**Salvaciones:** Fuerza, Constitución.

## RASGOS
**NIVEL 1: ESTILO COMBATE**
Defensa, Arqueria, Duelo, etc.

**NIVEL 1: SEGUNDO ALIENTO**
Bonus: Curas 1d10 + Nivel (1/descanso).

**NIVEL 2: ACTION SURGE**
Haces una acción extra en tu turno (1/descanso).

**NIVEL 3: ARQUETIPO (SUBCLASE)**
Campeón, Maestro Batalla, etc.

**NIVEL 5: ATAQUE EXTRA**
Dos ataques por acción.
""",
    "Monje": """# MONJE
**Dado de Golpe:** 1d8.
**Competencias:** Sencillas, Espadas cortas.
**Salvaciones:** Fuerza, Destreza.

## RASGOS
**NIVEL 1: DEFENSA SIN ARMADURA**
CA = 10 + Des + Sab.

**NIVEL 1: ARTES MARCIALES**
Usas DES para ataque/daño. Dado daño d4 (sube). Ataque extra desarmado como bonus.

**NIVEL 2: KI**
Puntos = Nivel.
* Ráfaga: 2 ataques bonus (1 ki).
* Paciente: Esquivar bonus (1 ki).
* Paso Viento: Destrabar/Correr bonus (1 ki).

**NIVEL 3: DESVIAR FLECHAS**
Reacción para reducir daño proyectil.

**NIVEL 3: TRADICIÓN (SUBCLASE)**
Mano Abierta, Sombra, etc.

**NIVEL 5: GOLPE ATURDIDOR**
Gastar 1 ki para aturdir (CON save).
""",
    "Paladín": """# PALADÍN
**Dado de Golpe:** 1d10.
**Competencias:** Todas armaduras, Escudos. Todas armas.
**Salvaciones:** Sabiduría, Carisma.

## RASGOS
**NIVEL 1: SENTIDO DIVINO**
Detectas celestiales/infernales/no-muertos.

**NIVEL 1: IMPONER MANOS**
Puntos curación = Nivel x 5.

**NIVEL 2: ESTILO COMBATE**
Defensa, Duelo, etc.

**NIVEL 2: CONJUROS**
Carisma. Preparas lista (Nivel/2 + Car).

**NIVEL 2: DIVINE SMITE**
Gasta slot para +2d8 radiante en golpe.

**NIVEL 3: JURAMENTO (SUBCLASE)**
Devoción, Venganza, Antiguos.
""",
    "Explorador (Ranger)": """# EXPLORADOR
**Dado de Golpe:** 1d10.
**Competencias:** Ligera, Media, Escudos. Todas armas.
**Salvaciones:** Fuerza, Destreza.

## RASGOS
**NIVEL 1: ENEMIGO PREDILECTO**
Ventajas contra un tipo de enemigo.

**NIVEL 1: EXPLORADOR NATO**
Ventajas en terreno elegido.

**NIVEL 2: ESTILO COMBATE**
Arqueria, Dos armas, etc.

**NIVEL 2: CONJUROS**
Sabiduría.

**NIVEL 3: ARQUETIPO (SUBCLASE)**
Cazador, Bestias, etc.
""",
    "Pícaro": """# PÍCARO
**Dado de Golpe:** 1d8.
**Competencias:** Ligera. Sencillas, ballesta mano, espadas, arco corto. Herramientas ladrón.
**Salvaciones:** Destreza, Inteligencia.

## RASGOS
**NIVEL 1: PERICIA**
Doble competencia en 2 habilidades.

**NIVEL 1: ATAQUE FURTIVO**
+1d6 daño si tienes ventaja o aliado cerca (arma sutil/rango). Sube con nivel.

**NIVEL 1: JERGA DE LADRONES**
Idioma secreto.

**NIVEL 2: ACCIÓN ASTUTA**
Bonus: Correr, Destrabarse, Esconderse.

**NIVEL 3: ARQUETIPO (SUBCLASE)**
Ladrón, Asesino, Arcane Trickster.

**NIVEL 5: ESQUIVA ASOMBROSA**
Reacción: Mitad daño de un ataque.
""",
    "Hechicero": """# HECHICERO
**Dado de Golpe:** 1d6.
**Competencias:** Ninguna armadura. Sencillas.
**Salvaciones:** Constitución, Carisma.

## RASGOS
**NIVEL 1: ORIGEN (SUBCLASE)**
Dracónico, Salvaje, etc.

**NIVEL 1: CONJUROS**
Carisma. Conocidos (no preparados).

**NIVEL 2: FUENTE DE MAGIA**
Puntos de Hechicería. Crear slots con puntos y viceversa.

**NIVEL 3: METAMAGIA**
Modificar conjuros (Sutil, Gemelo, Rápido).
""",
    "Brujo (Warlock)": """# BRUJO
**Dado de Golpe:** 1d8.
**Competencias:** Ligera. Sencillas.
**Salvaciones:** Sabiduría, Carisma.

## RASGOS
**NIVEL 1: PATRÓN (SUBCLASE)**
Archifey, Demonio, Primigenio.

**NIVEL 1: MAGIA DE PACTO**
Slots siempre nivel máximo. Recargan en descanso CORTO.

**NIVEL 2: INVOCACIONES**
Poderes pasivos/activos a elección.

**NIVEL 3: PACTO**
Hoja (arma), Cadena (familiar), Libro (trucos).
""",
    "Mago": """# MAGO
**Dado de Golpe:** 1d6.
**Competencias:** Ninguna armadura. Sencillas.
**Salvaciones:** Inteligencia, Sabiduría.

## RASGOS
**NIVEL 1: CONJUROS**
Libro de conjuros. Inteligencia. Rituales desde libro.

**NIVEL 1: RECUPERACIÓN ARCANA**
Recuperar slots en descanso corto (1 vez/día).

**NIVEL 2: TRADICIÓN (SUBCLASE)**
Evocación, Nigromancia, etc.
""",
    "OTRA (Manual)": "Consulta tu manual."
}

# --- KITS Y HERRAMIENTAS ---
DATA_KITS = {
    "Kit de Ladrón": "Mochila, 1000 balines, hilo, campana, velas, palanca, martillo, pitones, linterna, aceite, raciones, yesca, odre, cuerda.",
    "Kit de Diplomático": "Cofre, estuches, ropa fina, tinta, pluma, lámpara, aceite, papel, perfume, lacre, jabón.",
    "Kit de Dungeon": "Mochila, palanca, martillo, pitones, antorchas, yesca, raciones, odre, cuerda.",
    "Kit de Artista": "Mochila, saco, disfraces, velas, raciones, odre, kit disfraz.",
    "Kit de Explorador": "Mochila, saco, comedor, yesca, antorchas, raciones, odre, cuerda.",
    "Kit de Sacerdote": "Mochila, manta, velas, yesca, limosnas, incienso, vestimentas, raciones, odre.",
    "Kit de Erudito": "Mochila, libro, tinta, pluma, pergamino, arena, cuchillo."
}

DATA_HERRAMIENTAS_FULL = {
    "Herramientas de Ladrón": "Componentes: Lima, ganzúas, espejo, tijeras, alicates.",
    "Herramientas de Navegante": "Componentes: Sextante, compás, regla, pergamino, tinta, pluma.",
    "Kit de Disfraz": "Componentes: Cosméticos, tinte, prendas, accesorios.",
    "Kit de Falsificación": "Componentes: Tintas, papeles, sellos, cera, herramientas escultura.",
    "Kit de Herboristería": "Componentes: Bolsas, tijeras podar, guantes, mortero, frascos.",
    "Kit de Envenenador": "Componentes: Viales, mortero, químicos, varilla.",
    "Juego de Dados": "Componentes: Dados o cartas.",
    "Suministros de Alquimista": "Componentes: Vasos, marco, varilla, mortero, ingredientes comunes.",
    "Suministros de Cervecero": "Componentes: Jarra, lúpulo, sifón, tubos.",
    "Suministros de Caligrafía": "Componentes: Tinta, pergaminos, plumas.",
    "Suministros de Pintor": "Componentes: Caballete, lienzos, pinturas, pinceles.",
    "Utensilios de Cocinero": "Componentes: Olla, cuchillos, cubiertos, rallador, especias.",
    "Herramientas de Artesano (Gral)": "Martillo, cincel, sierra, etc según el oficio (Carpintero, Herrero, etc)."
}

# --- DOTES ---
DATA_DOTES_FULL = {
    "Acechador": "Esconderse luz tenue. No revelas posición al fallar.",
    "Actor": "+1 CAR. Ventaja Engaño/Actuación. Imitar voces.",
    "Afortunado": "3 puntos suerte. Reroll d20.",
    "Alerta": "+5 Iniciativa. No sorprendido.",
    "Atleta": "+1 FUE/DES. Levantarse fácil. Escalar.",
    "Cargador": "Ataque bonus o empujón tras correr.",
    "Curandero": "Kit estabiliza a 1 HP. Cura 1d6+4+Nv.",
    "Defensor": "Reacción atacar si atacan aliado.",
    "Dureza": "+2 HP por nivel.",
    "Francotirador": "-5 ataque / +10 daño distancia. Ignora cobertura.",
    "Gran Maestro de Armas": "-5 ataque / +10 daño pesada. Ataque extra crítico.",
    "Lider Inspirador": "HP Temp a aliados = Nivel + CAR.",
    "Maestro de Armaduras Medias": "Max DES +3. Sin desventaja sigilo.",
    "Maestro de Armaduras Pesadas": "-3 daño recibido.",
    "Maestro de Escudos": "Empujar bonus. Evasión.",
    "Mente Aguda": "Saber norte, hora, memoria perfecta.",
    "Movil": "+3m vel. No oportunidad si atacas.",
    "Observador": "+5 Pasivas. Leer labios.",
    "Resiliente": "+1 Stat. Competencia salvación.",
    "Ritualista": "Libro rituales.",
    "Robusto": "Min curación dados golpe = 2xCON.",
    "Sentinela": "Oportunidad para a 0 vel. Ignora destrabarse.",
    "War Caster": "Ventaja concentración. Conjuro como oportunidad."
}

def main(page: ft.Page):
    page.title = "D&D Player App v16 Fix"
    page.theme_mode = ft.ThemeMode.DARK
    # padding 0 para que el SafeArea controle los bordes
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

    all_chars = page.client_storage.get("dnd_chars_v16") or {"Default": get_empty_char()}
    
    # Migración simple
    for d in all_chars.values():
        if "dotes_list" not in d: d["dotes_list"] = [] 
        if "kits_tools" not in d: d["kits_tools"] = []
        if "extras" not in d: d["extras"] = [{"n": "Recurso 1", "m": "0", "used": []}, {"n": "Recurso 2", "m": "0", "used": []}, {"n": "Recurso 3", "m": "0", "used": []}]

    char_data = all_chars[current_char_name]

    def guardar():
        all_chars[current_char_name] = char_data
        page.client_storage.set("dnd_chars_v16", all_chars)

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
                page.client_storage.set("dnd_chars_v16", all_chars)
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

    # --- PESTAÑA 1: GENERAL (LISTVIEW PARA EVITAR PANTALLA NEGRA) ---
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

    # CORRECCIÓN PANTALLA NEGRA: Usamos ListView en lugar de Contenedores anidados complejos
    tab_general = ft.ListView([
        ft.Text("Datos", weight="bold"), 
        ft.Row([dd_raza, dd_clase]), 
        ft.Row([txt_nivel, ft.Text("Dado de Golpe:", color="grey"), txt_hit_dice]), 
        ft.Row([txt_raza_c, txt_clase_c]),
        ft.Divider(), ft.Text("Stats", weight="bold"), col_stats,
        ft.Divider(), 
        ft.Text("Dotes (Feats)", weight="bold"), 
        ft.Row([dd_dotes_select, ft.IconButton("add_circle", icon_color="green", on_click=add_dote_click)]),
        col_dotes_active
    ], padding=10, expand=True)

    # --- PESTAÑA: INFO DE CLASE ---
    dd_info_clase = ft.Dropdown(options=[ft.dropdown.Option(c) for c in LISTA_CLASES if c != "OTRA (Manual)"], label="Ver Info Clase", expand=True)
    md_clase_info = ft.Markdown(value="Selecciona arriba.", selectable=True)
    
    def change_info_clase(e):
        if dd_info_clase.value in DATA_CLASES_INFO: md_clase_info.value = DATA_CLASES_INFO[dd_info_clase.value]
        page.update()
    dd_info_clase.on_change = change_info_clase

    # CORRECCIÓN: Column con scroll=auto dentro del Tab
    tab_clase_info = ft.Container(padding=10, content=ft.Column([
        dd_info_clase, ft.Divider(),
        ft.Container(content=ft.Column([md_clase_info], scroll="auto", expand=True), expand=True)
    ], expand=True))

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

    tab_combate = ft.ListView([
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

    # CORRECCIÓN: ListView para scroll
    tab_magia = ft.ListView([
        ft.Text("Recursos de Clase / Extras", weight="bold", color="cyan"), col_extras,
        ft.Divider(), ft.Text("Slots de Conjuro", weight="bold"), col_spells
    ], padding=10, expand=True)

    # --- PESTAÑA 5: MOCHILA ---
    txt_gold = ft.Text("0", size=30, weight="bold", color="yellow")
    def mod_gold(d):
        char_data["gold"] = max(0, int(txt_gold.value) + d); txt_gold.value = str(char_data["gold"]); guardar(); page.update()
    
    ui_gold = ft.Container(bgcolor="black", padding=10, border=ft.border.all(1, "yellow"), border_radius=10, content=ft.Column([
        ft.Text("Oro (GP)", color="yellow", size=12),
        ft.Row([ft.IconButton("remove", on_click=lambda e: mod_gold(-10), icon_color="yellow"), ft.IconButton("remove", on_click=lambda e: mod_gold(-1), icon_size=15), txt_gold, ft.IconButton("add", on_click=lambda e: mod_gold(1), icon_size=15), ft.IconButton("add", on_click=lambda e: mod_gold(10), icon_color="yellow")], alignment="center")
    ], alignment="center"))

    def crear_tab_inv_manual(key_db, titulo):
        col_items = ft.ListView(expand=True, spacing=5) # LISTVIEW CLAVE
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
        # Estructura corregida: Inputs fijos + Lista expandible
        return ft.Tab(text=titulo, content=ft.Container(padding=10, content=ft.Column([
            ft.Column([txt_item, txt_desc, ft.ElevatedButton("Añadir", on_click=add_item)]),
            ft.Divider(), col_items
        ], expand=True)))

    col_kits = ft.ListView(expand=True, spacing=5) # LISTVIEW CLAVE
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

    # --- ESTRUCTURA PRINCIPAL SIN SAFE AREA WRAPPER COMPLEJO (SOLUCIÓN PANTALLA NEGRA) ---
    # Añadimos SafeArea solo al contenedor principal
    page.add(ft.SafeArea(ft.Column([header, ft.Divider(height=1), main_tabs], expand=True), expand=True))
    recargar_interfaz()

ft.app(target=main)
