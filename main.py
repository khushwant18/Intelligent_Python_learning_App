from kivy.app import App
from kivy.lang import Builder

from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.base import runTouchApp

from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.uix.widget import Widget
from kivy.uix.button import ButtonBehavior
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.checkbox import CheckBox

from book_summarizer import book_sum
from final_web_scrapping import web_scraping
from Assesment import Evaluation
from kivy import app

Window.size = (435, 750)

class HomeScreen(Screen):
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Enter Username and Password[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Login Successful!!![/color]'
                self.manager.current="select_screen"
            else:
                info.text = '[color=#FF0000]Invalid Credentials[/color]'
                
a,b,c,d='','','',''
class TWidget(BoxLayout):
    anstoq = StringProperty()    
    def insert_data1(self,anstoq):
        global a
        a=anstoq
        print(a)
    pass 
    def insert_data2(self,anstoq):
        global b
        b=anstoq
        print(b)
    pass  
    def insert_data3(self,anstoq):
        global c
        c=anstoq
        print(c)
    pass   
    def insert_data4(self,anstoq):
        global a,b,c,d
        d=anstoq
        print(d)
        a=a+b+c+d
        print(a)
    pass


class SelectScreen(Screen):
    pass

class BookScreen(Screen):
    pass

class QuesScreen(Screen):
    def evaluate(self):
        global a
  
        marks=[]
        answers="BCAA"
        for i in range(len(a)):
            if answers[i]==a[i]:
                marks.append(1)
            else:
                marks.append(0)
        print(marks)
        Evaluation().add_Score(marks)
        self.manager.current="ans_screen"
    pass


class AnsScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class SettingsScreen(Screen):
    pass

b=book_sum().book_scrap()
c=web_scraping().get_data()
ques,ans=web_scraping().format_data(c)

class CWidget(ScrollView):
    s=''
    # for j in range(len(b)):
    for i in b[0]:
        s+='\n'+i+'\n'
    bc=StringProperty(s)

    s=''
    for i in b[1]:
        s+='\n'+i+'\n'
    bc1=StringProperty(s)

    s=''
    for i in b[2]:
        s+='\n'+i+'\n'
    bc2=StringProperty(s)

    s=''
    for i in b[3]:
        s+='\n'+i+'\n'
    bc3=StringProperty(s)

    s=''
    for i in b[4]:
        s+='\n'+i+'\n'
    bc4=StringProperty(s)

    s=''
    for i in b[5]:
        s+='\n'+i+'\n'
    bc5=StringProperty(s)

    s=''
    for i in b[6]:
        s+='\n'+i+'\n'
    bc6=StringProperty(s)

    s=''
    for i in b[7]:
        s+='\n'+i+'\n'
    bc7=StringProperty(s)

    s=''
    for i in b[8]:
        s+='\n'+i+'\n'
    bc8=StringProperty(s)

    s=''
    for i in b[9]:
        s+='\n'+i+'\n'
    bc9=StringProperty(s)

    s=''
    for i in b[10]:
        s+='\n'+i+'\n'
    bc10=StringProperty(s)

    s=''
    for i in b[11]:
        s+='\n'+i+'\n'
    bc11=StringProperty(s)

    s=''
    for i in b[12]:
        s+='\n'+i+'\n'
    bc12=StringProperty(s)

    s=''
    for i in b[13]:
        s+='\n'+i+'\n'
    bc13=StringProperty(s)

    s=''
    for i in b[14]:
        s+='\n'+i+'\n'
    bc14=StringProperty(s)

    s=''
    for i in b[15]:
        s+='\n'+i+'\n'
    bc15=StringProperty(s)

    s=''
    for i in b[16]:
        s+='\n'+i+'\n'
    bc16=StringProperty(s)

    s=''
    for i in b[17]:
        s+='\n'+i+'\n'
    bc17=StringProperty(s)

    s=''
    for i in b[18]:
        s+='\n'+i+'\n'
    bc18=StringProperty(s)

    s=''
    for i in b[19]:
        s+='\n'+i+'\n'
    bc19=StringProperty(s)

    s=''
    for i in b[20]:
        s+='\n'+i+'\n'
    bc20=StringProperty(s)

class QWidget(ScrollView):
    k=''
    for i in range(4):
        k+='\n'+ques[i]+'\n'
    qo=StringProperty(k)
    

class AWidget(ScrollView):
    a=''
    for i in range(4):
        a+=ans[i]+'\n'
    an=StringProperty(a)

class TWidget(ScrollView):
    pass

class Chapters():
    def __init__(self,bc):
        self.bc=bc

class Ques():
    def __init__(self,qo):
        self.qo=qo

class Ans():
    def __init__(self,an):
        self.an=an

GUI=Builder.load_file("main.kv")

class MainApp(App):
    theme_cls=ThemeManager()
    title='Python Learning App'
    
    def change_screen(self, screen_name):
        screen_manager=self.root.ids['screen_manager']
        screen_manager.current=screen_name
MainApp().run()