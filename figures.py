from mathLib import *
from math import *

WHITE = (1,1,1)
BLACK = (0,0,0)

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2


class Intersect(object):
    def __init__(self, distance, point, normal, texcoords, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texcoords = texcoords
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE, spec = 1.0, ior = 1.0, texture = None, matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        self.ior = ior
        self.texture = texture
        self.matType = matType


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = subtractVList(self.center, orig)
        tca = dotProduct(L, dir)
        d = (norm(L) ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        P = addVectors(orig, [t0*dir[0], t0*dir[1], t0*dir[2]])
        normal = subtractVList(P, self.center)
        normal = normV(normal)

        u = 1 - ((atan2(normal[2], normal[0])) / (2 * pi) + 0.5)
        v = acos(-1*normal[1]) / pi

        uvs = (u, v)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         texcoords = uvs,
                         sceneObj = self)

class Plane(object):
    def __init__(self, position, normal, material):
        self.position = position
        self.normal = normV(normal)
        self.material = material

    def ray_intersect(self, orig, dir):
        # Distancia = (( planePos - origRayo) o normal) / (direccionRayo o normal)
        denom = dotProduct(dir, self.normal)

        if abs(denom) > 0.0001:
            num = dotProduct(subtractVList(self.position, orig), self.normal) 
            t = num / denom

            if t > 0:
                # P = O + t*D
                P = addVectors(orig, [t * dir[0], t * dir[1], t * dir[2]])
                return Intersect(distance = t,
                                 point = P,
                                 normal = self.normal,
                                 texcoords = None, # Para aplicar las uvs en todo el plano habria que repetir lq textura 
                                                   # una y otra vez en el plano
                                 sceneObj = self)

        return None


