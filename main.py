from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix import screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineListItem, TwoLineListItem, OneLineListItem, ImageLeftWidget
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.window import Window
from create_apk import cursor, conn


Window.size = (480, 853)

class Container(MDScreen):
    pass

class MainApp(MDApp):
           
    def StartSQL():
        # import sqlite3
        from create_apk import conn, cursor
        if conn:
            print('Базу даних Основних засобів підключено')
        else:
            print('Помилка підключення бази даних Основних засобів')

    def Get_work_place():
        MainApp.StartSQL()
        rows=cursor.execute("SELECT * FROM work_place ORDER BY id").fetchall()
        # print(rows)
        return rows

    def Get_osnovni():
        MainApp.StartSQL()
        rows=cursor.execute("SELECT * FROM osnovni ORDER BY field3").fetchall()
        # print(rows)
        return rows

    def build(self):
        self.theme_cls.material_style = "M3"
    # return Builder.load_string(Test)
        return Container()

    def on_press_button(self, instance):
        # current = self.root.ids.on_release
        if instance.text:
            button_text = instance.text
        else:
            button_text = instance.icon
        print('You pressed the button - '+str(button_text))

    def on_start(self):

        rows=MainApp.Get_work_place()
        text=''
        for i in rows:
            if i[2] is not None:
                text=str(i[2])+" - "+str(i[5])+" д.в. "+str(i[4])
            if i[6] is not None:
                text+=" "+str(i[6])+" - "+str(i[8])+" д.в. "+str(i[9])
            print(id)
            self.root.ids.lists.add_widget(
                ThreeLineListItem(on_press=self.on_press_button,
                    # on_release=i[0],
                    text="Робоче місце - "+str(i[1]),
                    secondary_text=text,
                    tertiary_text="Принтер струйний, телефон, лампа"
                )
            )
        rows=MainApp.Get_osnovni()
        text=''
        for i in rows:
            self.root.ids.OZLists.add_widget(
                TwoLineListItem(on_press=self.on_press_button,
                    # on_release=i[0],
                    text="Інвентарний номер - "+str(i[0])+" дата вводу - "+str(i[2]),
                    secondary_text=str(i[1])
                )
            )
            # button.bind(on_press=self.on_press_button)
            # text=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]  {name_tab}"
        self.root.ids.box.add_widget(
            MDFloatingActionButton(
                    on_press=self.on_press_button,
                    md_bg_color="#97ecf8",
                    # theme_icon_color="#eeeaea",
                    # icon_color="#eeeaea",
                    icon="archive-plus",
                    text="edit"
                )
            )
        
        return super().on_start()

# if __name__=='__main__':
MainApp().run()