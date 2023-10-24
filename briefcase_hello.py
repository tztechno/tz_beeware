
pip install briefcase

briefcase new

###########################
import toga
def build(app):
    box = toga.Box()
    label = toga.Label('Hello, BeeWare!')
    box.add(label)
    return box
if __name__ == '__main__':
    app = toga.App('Hello', 'org.pybee.hello', startup=build)
    app.main_loop()
###########################

briefcase dev

cd dist/osx
./Hello
