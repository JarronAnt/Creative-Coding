theta = PI/8


def setup():
    size(800,800)
    
def draw():
    background(51)
    len = 200
    stroke(255)
    translate(400,height)
    branch(len)

#note push and pop are used to save and remove drawing states(ie translations, rotations etc)
def branch(len):
    line(0,0,0,-len)
    translate(0,-len)
    if len > 6: 
        push()
        rotate(theta)
        branch(len*0.66)
        pop()
        push()
        rotate(-theta)
        branch(len*0.66)
        pop()
