from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
Sky()
player = FirstPersonController()

boxes = []
for n in range(8):
    for k in range(8):
        box = Button(
            parent=scene,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.green,
            highlight_color=color.white,
            position=(k,0,n)
        )
        boxes.append(box)
    def input(key):
        for box in boxes:
            if box.hovered:
                if key=='right mouse down':
                    newBox = Button(
                        parent=scene,
                        model='cube',
                        origin_y=0.5,
                        texture='white_cube',
                        color=color.green,
                        highlight_color=color.white,
                        position=box.position + mouse.normal
                    )
                    boxes.append(newBox)
                if key=='left mouse down':
                    boxes.remove(box)
                    destroy(box)
app.run()