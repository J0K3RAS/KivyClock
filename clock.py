from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from datetime import datetime
from threading import Thread
import time

kv = '''
FloatLayout:
    id: main_widget
    Image:
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        id: clock
        source: 'clock.png'
    Image:
        id: bhand
        source: 'big_hand.png'
        canvas.before:
            PushMatrix
            Rotate:
                angle: app.bangle
                axis: 0, 0, 1
                origin: root.center
        canvas.after:
            PopMatrix 
    Image:
        id: shand
        source: 'small_hand.png'
        canvas.before:
            PushMatrix
            Rotate:
                angle: app.sangle
                axis: 0, 0, 1
                origin: root.center
        canvas.after:
            PopMatrix 
'''

class AnalogClock(App):
    sangle = NumericProperty(-45)
    bangle = NumericProperty(90)
    
    def build(self):
        self.layout = Builder.load_string(kv)
        Thread(target = self.clock).start()
        return self.layout
    
    def clock(self):
        while True:
            t = str(datetime.now().time())
            hours = int(t[0:2])
            if  hours > 12: hours -= 12
            minutes =  int(t[3:5])
            self.bangle = -6*minutes
            #self.layout.ids.shand.reload()
            self.sangle = -30*hours
            #self.layout.ids.bhand.reload()
            time.sleep(5)

        

if __name__ == '__main__':
    AnalogClock().run()
