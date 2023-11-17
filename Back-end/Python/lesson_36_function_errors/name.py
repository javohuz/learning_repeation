

def fullname(name , lastname):
    return f'{name} {lastname}'.title()

def fullname_with_sharf(name,lastname ,otasini_ismi):
    return f'{name} {lastname} {otasini_ismi}'.title()

def getArea(r,pi=3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def getPerimeter(r,pi=3.14159):
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2*pi*r
