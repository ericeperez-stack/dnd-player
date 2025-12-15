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

# --- KITS DE EQUIPO (Pág 202 Manual) ---
DATA_KITS = {
    "Kit de Ladrón": "Mochila, 1000 balines de metal, 10 pies de hilo, campana, 5 velas, palanca, martillo, 10 pitones, linterna sorda, 2 frascos de aceite, 5 días de raciones, caja de yesca y odre. Incluye 50 pies de cuerda atada al costado.",
    "Kit de Diplomático": "Cofre, 2 estuches para mapas/pergaminos, ropa fina, botella de tinta, pluma, lámpara de aceite, 2 frascos de aceite, 5 hojas de papel, vial de perfume, lacre y jabón.",
    "Kit de Dungeon": "Mochila, palanca, martillo, 10 pitones, 10 antorchas, caja de yesca, 10 días de raciones y odre. Incluye 50 pies de cuerda atada al costado.",
    "Kit de Artista": "Mochila, saco de dormir, 2 disfraces, 5 velas, 5 días de raciones, odre y un kit de disfraz.",
    "Kit de Explorador": "Mochila, saco de dormir, kit de comedor, caja de yesca, 10 antorchas, 10 días de raciones y odre. Incluye 50 pies de cuerda atada al costado.",
    "Kit de Sacerdote": "Mochila, manta, 10 velas, caja de yesca, caja de limosnas, 2 bloques de incienso, incensario, vestimentas, 2 días de raciones y odre.",
    "Kit de Erudito": "Mochila, libro de conocimientos, botella de tinta, pluma, 10 hojas de pergamino, bolsa pequeña de arena y cuchillo pequeño."
}

# --- HERRAMIENTAS Y SUMINISTROS (Descripciones de Componentes - Pág 222+) ---
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

# --- LISTA COMPLETA DE DOTES (FEATS) ---
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
    "Entrenamiento armas marciales": "+1 Fue/Des. Competencia con 4 armas.",
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
    "Maestro armaduras medias": "+1 CA en media (Max Dex +3). Sin desventaja Sigilo.",
    "Maestro armaduras pesadas": "+1 Fue. Reduces daño no mágico en 3.",
    "Maestro armas de asta": "Ataque extra 1d4. Oportunidad al entrar en alcance.",
    "Maestro armas pesadas": "Ataque extra al crítico/matar. -5 ataque / +10 daño.",
    "Maestro de escudos": "Empujar como bonus. Bono escudo a salvación Des. Evasión con reacción.",
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
    page.title = "D&D Player App v8 Final"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page.window_height = 850
    page.padding = 10

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
            "dotes_list": [], # Lista de dicts {n: nombre, d: descripcion}
            "spells_config": {f"lvl{i}": 0 for i in range(1, 10)},
            "spells_used": {f"lvl{i}": [] for i in range(1, 10)},
            "inv_armas": [], "inv_armaduras": [], "inv_pociones": [], "inv_comida": [], "inv_varios": [],
            "kits_tools": []
        }

    all_chars = page.client_storage.get("dnd_chars_v8") or {"Default": get_empty_char()}
    
    # Migración
    for d in all_chars.values():
        if "dotes_list" not in d: d["dotes_list"] = [] 

    char_data = all_chars[current_char_name]

    def guardar():
        all_chars[current_char_name] = char_data
        page.client_storage.set("dnd_chars_v8", all_chars)

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
                page.client_storage.set("dnd_chars_v8", all_chars)
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

    header = ft.Row([ft.Icon("person"), dd_personajes, ft.IconButton("add", on_click=nuevo_pj)], alignment="center")

    # --- PESTAÑA 1: GENERAL ---
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

    # --- DOTES (FILTRO + SCROLL + DELETE FIXED) ---
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
    ], padding=10)

    # --- PESTAÑA 2: COMBATE ---
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
    ], padding=10)

    # --- PESTAÑA 3: MAGIA ---
    col_spells = ft.Column(scroll="auto")
    def crear_fila_spell(nivel):
        key = f"lvl{nivel}"
        max_val = char_data["spells_config"].get(key, 0)
        txt_max = ft.TextField(value=str(max_val), label=f"Nv {nivel}", width=60, height=40, text_size=12, keyboard_type="NUMBER")
        row_checks = ft.Row(wrap=True, expand=True)

        def refresh_checks():
            row_checks.controls.clear()
            try: limit = int(txt_max.value)
            except: limit = 0
            used_list = char_data["spells_used"][key]
            for i in range(limit):
                is_checked = (i in used_list)
                chk = ft.Checkbox(value=is_checked)
                def on_click(e, idx=i):
                    if e.control.value:
                        if idx not in char_data["spells_used"][key]: char_data["spells_used"][key].append(idx)
                    else:
                        if idx in char_data["spells_used"][key]: char_data["spells_used"][key].remove(idx)
                    guardar()
                chk.on_change = on_click
                row_checks.controls.append(chk)
            page.update()

        def on_change_max(e):
            val_str = e.control.value
            val = int(val_str) if val_str and val_str.isdigit() else 0
            char_data["spells_config"][key] = val
            guardar()
            refresh_checks()
        txt_max.on_change = on_change_max
        refresh_checks()
        return ft.Container(bgcolor="grey900", padding=5, margin=2, border_radius=5, content=ft.Row([txt_max, row_checks]))

    def render_spells():
        col_spells.controls.clear()
        for n in range(1, 10):
            col_spells.controls.append(crear_fila_spell(n))
        page.update()

    tab_magia = ft.Container(padding=10, content=ft.Column([ft.Text("Slots de Conjuro", weight="bold"), col_spells], scroll="auto"))

    # --- PESTAÑA 4: MOCHILA ---
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
        col_items = ft.Column(spacing=5)
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
        return ft.Tab(text=titulo, content=ft.Container(padding=10, content=ft.Column([
            ft.Column([txt_item, txt_desc, ft.ElevatedButton("Añadir a Mochila", on_click=add_item_click)]),
            ft.Divider(),
            ft.Column([col_items], scroll="auto", expand=True) 
        ], expand=True)))

    # --- KITS Y HERRAMIENTAS SEPARADOS (SCROLL FIXED) ---
    col_kits = ft.ListView(expand=True, spacing=5)
    def build_kits_and_tools():
        col_kits.controls.clear()
        
        # 1. KITS
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

        # 2. HERRAMIENTAS
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
            ft.Tab(text="Kits/Herramientas", content=ft.Container(padding=10, content=col_kits)) 
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
        build_kits_and_tools()
        container_mochila.content = ft.Column([ui_gold, ft.Divider(), get_inv_tabs()], expand=True)
        page.update()

    main_tabs = ft.Tabs(selected_index=0, tabs=[
        ft.Tab(text="General", icon="person", content=tab_general),
        ft.Tab(text="Combate", icon="flash_on", content=tab_combate),
        ft.Tab(text="Magia", icon="auto_fix_high", content=tab_magia),
        ft.Tab(text="Mochila", icon="backpack", content=container_mochila),
    ], expand=True)

    page.add(header, ft.Divider(height=1), main_tabs)
    recargar_interfaz()

ft.app(target=main)