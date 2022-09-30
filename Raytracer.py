from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales
brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)

glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType= TRANSPARENT)
diamond = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 2.417, matType= TRANSPARENT)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)


rtx = Raytracer(width, height)
rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))

rtx.scene.append(Plane(position = (0, -10, 0), normal = (0, 1, 0), material = brick))
rtx.scene.append(Plane(position = (-20, 0, 0), normal = (1, 0, 0), material = stone))
# rtx.scene.append(Plane(position = (15, 30, -15), normal = (-1, -1, -1), material = mirror))

rtx.glRender()

rtx.glFinish("output.bmp")