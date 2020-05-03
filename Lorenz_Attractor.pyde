#globals
x = 0.01
y = 0
z = 0
a = 10
b = 28
c = (8/3)

points = []

def setup():
    size(1280,720, P3D)
    colorMode(HSB)


def draw():
    background(0)
    
    #access the globals 
    global x
    global y
    global z
    
    #lorenz attractor ODE's
    dt = 0.01
    dx = (a * (y-x))*dt
    dy = (x*(b-z)-y)*dt
    dz = (x*y-c*z)*dt
    x += dx
    y += dy
    z += dz
    
    #add all the points to a list 
    points.append((x,y,z))
    
    #all the actual drawing stuff 
    translate(width/2,height/2)
    scale(10)
    stroke(255)
    noFill()
    hu = 0
    beginShape()
    for v in points:
        stroke(hu,255,255)
        vertex(v[0],v[1],v[2])
        hu += 0.25
        if hu > 255:
            hu = 0
    endShape()
