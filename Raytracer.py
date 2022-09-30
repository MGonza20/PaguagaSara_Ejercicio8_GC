from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales
marble1 = Material( diffuse = (0.8, 0.8, 0.8), texture = Texture("colored-tex.bmp"), spec = 32, matType = REFLECTIVE) 
marble2 = Material( diffuse = (0.8, 0.8, 0.8), texture = Texture("colored-tex-2.bmp"), spec = 32, matType = REFLECTIVE) 
marble3 = Material( diffuse = (0.8, 0.8, 0.8), texture = Texture("colored-tex-3.bmp"), spec = 32, matType = OPAQUE) 
marble4 = Material( diffuse = (1, 1, 1), texture = Texture("colored-tex-6.bmp"), spec = 32, matType = OPAQUE) 
marble5 = Material( diffuse = (171/255, 240/255, 1), texture = Texture("colored-tex-8.bmp"), spec = 32,  ior = 1.5, matType = TRANSPARENT) 
marble6 = Material( diffuse = (247/255, 95/255, 20/255), texture = Texture("colored-tex-8.bmp"), spec = 32,  ior = 2.417, matType = TRANSPARENT) 


rtx = Raytracer(width, height)

rtx.envMap = Texture("sunset.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))

# Row 1
rtx.scene.append( Sphere(V3(-3,1.5+1,-10), 1, marble1))
rtx.scene.append( Sphere(V3(0,1.5+1,-10), 1, marble3))
rtx.scene.append( Sphere(V3(3,1.5+1,-10), 1, marble5))

# Row 2
rtx.scene.append( Sphere(V3(-3,-1.5+1,-10), 1, marble2))
rtx.scene.append( Sphere(V3(0,-1.5+1,-10), 1, marble4))
rtx.scene.append( Sphere(V3(3,-1.5+1,-10), 1, marble6))


rtx.glRender()

rtx.glFinish("output.bmp")