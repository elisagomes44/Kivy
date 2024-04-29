from kivy.app import App 
from kivy.uix.button import Button 

def botao_pressionado(instance):
    print("Botão pressionado!")

class MinhaApp(App):
    def build(self):
        bnt = Button(text='Clique Aqui', size_hint=(0.5,0.2))
        bnt.bind (on_press= botao_pressionado)
        return bnt 
    
if __name__ == '__main__': 
     MinhaApp().run()
