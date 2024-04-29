from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build (self):
        return AsyncImage (source='https://th.bing.com/th/id/R.4a82a811169281ecd8e6d7e2baa3b483?rik=Yr%2fZC88kDlawFA&pid=ImgRaw&r=0.png')
    
if __name__ == '__main__':
    MinhaApp().run() 
