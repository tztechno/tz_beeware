!pip install toga

################################
import toga
def build(app):
    box = toga.Box()
    label = toga.Label('Hello, BeeWare!', style=css)
    box.add(label)
    return box

if __name__ == '__main__':
    app = toga.App('Hello', 'org.pybee.hello', startup=build)
    app.main_loop()
#################################

!python hello.py
