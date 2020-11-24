from kivy.app import App
from kivy.lang import Builder
# we need builder to load kv string
from kivy.properties import NumericProperty
# NumericProperty helps us define the angle (in degrees) of each hand
from datetime import datetime
# Get system time
from threading import Thread
# Run the program without the ui freezing
import time
# We will pause the program for 5 sec between each iteration

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
    sangle = NumericProperty(-45) # Initialize the small hand angle
    bangle = NumericProperty(90) # Initialize the big hand angle
    
    def build(self):
        '''
        Loads layout from kv string and starts the main loop
        '''
        self.layout = Builder.load_string(kv)
        Thread(target = self.clock).start()
        return self.layout
    
    def clock(self):
        '''
        Main program loop. Calculate angle from system time 
        '''
        while True:
            t = str(datetime.now().time())              # get current time
            hours = int(t[0:2])                         # from t get hour
            if  hours > 12: hours -= 12                 # convert 24h to 12h
            minutes =  int(t[3:5])                      # from t get minutes
            self.bangle = -6*minutes                    # 1 minute equals to 6 degrees of rotation
            self.sangle = -30*hours - 0.5*minutes       # 1 hour equals to 30 degrees of rotation + 0.5*degrees per minute
            time.sleep(5)                               # It is not necessary to do many loops per second, so we decide to wait 5 sec.

        

if __name__ == '__main__':
    AnalogClock().run()
