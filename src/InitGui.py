import FreeCADGui
from .discordPresence import runExtension

def Initialize():
    runExtension()

FreeCADGui.addApplicationStartHandler(Initialize)