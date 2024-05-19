from random import randint

from flet import (
    Text,
    TextButton,
    AlertDialog,
    Row,
    Column,
    Container,
    icons,
    Page,
    app,
    AppBar,
    IconButton,
    PopupMenuButton,
    PopupMenuItem,
    Icon,
    TextField,
    Alignment,
    alignment,
    
)

def main(page: Page):
    page.title = "RNG - Random Number Generator"
    page.window_width = 840
    page.window_height = 450
    page.window_resizable = False
    page.update()
    
    def on_roll(e):
        min_value = int(Box_Lenght_min.value)
        max_value = int(Box_Lenght_max.value)
        
        number_sequence.value = randint(min_value, max_value)
        
        page.update()
    
    def open_settings(e):
        page.dialog = popup_settings
        popup_settings.open = True
        page.update()
    
    def open_about(e):
        page.dialog = popup_about
        popup_about.open = True
        page.update()

    
    
    more_about = PopupMenuButton(
        items=[
            PopupMenuItem(icon=icons.SETTINGS ,text="Settings", on_click=open_settings),
            PopupMenuItem(icon=icons.INFO, text="Info", on_click=open_about)   
        ]
    )
    
    line_info = Row(
        spacing=13,
        controls=[
            Text("RNG", weight="w400", opacity=0.7),
            Text("Random Number Generator", weight="w100", size=14, opacity=0.4)
        ]
    )
    
    Box_Lenght_min = TextField(value=10000 ,hint_text="Defalt is 10000", width=300)
    Box_Lenght_max = TextField(value=1000000 ,hint_text="Defalt is 1000000", width=300)
    
    popup_settings = AlertDialog(
        modal=False,
        open=False,
        title=Row(
            width=500,
            controls=[
                Icon(icons.SETTINGS),
                Text("Settings", weight="w100")
            ]
        ),
        actions=[
            Column(
                horizontal_alignment="center",
                spacing=15,
                controls=[
                    Row(
                        controls=[
                            Text("Length Min", opacity=0.6, weight="w100"),
                            Box_Lenght_min
                        ]
                    ),
                    Row(
                        controls=[
                            Text("Length Max", opacity=0.6, weight="w100"),
                            Box_Lenght_max
                        ]
                    ),
                ],
            )
        ]
    )
    
    popup_about = AlertDialog(
        modal=False,
        open=False,
        title=Row(
            width=300,
            controls=[
                Icon(icons.INFO),
                Text("About", weight="w100")
            ]
        ),
        content=Column(
            height=400,
            horizontal_alignment="center",
            alignment="left",
            spacing=10,
            controls=[
                Text("version: 24un", size=14, weight="w100"),
                Text("Created by Gabriel Xavier", size=16, weight="w200", opacity=0.8),
                Text("in Flet with Python", opacity=0.3)
            ]
        )
    )
    
    
    App_Bar_Main = AppBar(
        title=line_info,
        actions=[
           more_about
        ]
    )
    
    number_sequence = Text("############", weight="w300", size=34)
    btn_roll = TextButton("Roll", on_click=on_roll)
    
    main_actions = Column(
        width=840,
        alignment=alignment.center,
        horizontal_alignment=alignment.center,
        controls=[
            number_sequence,
            btn_roll
        ]
    )
    
    Box_Content = Container(
        width=840,
        alignment=alignment.center,
        content=main_actions,
    )
    
    
    page.add(
        App_Bar_Main,
        Box_Content,
    )



app(target=main)

