from algfullmap import Mapalgorithm
from pyglet.window import key
import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
# image = pyglet.resource.image('kitten.jpg')
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        print "quit"

platform = pyglet.window.get_platform()
display = platform.get_default_display()
print display.get_default_screen()
@window.event
def on_draw():
    window.clear()
    # image.blit(0,0)
    label.draw()
    # pyglet.graphics.draw(1, GL_POINTS, ('v2i',(10,20)))

pyglet.app.run()
