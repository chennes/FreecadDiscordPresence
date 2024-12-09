__title__ = 'Discord Presence'
__author__ = 'Tzur Soffer'
import FreeCAD
import FreeCADGui

from discordPresence import runExtension

def Initialize():
    print("Started Discord Presence")
    runExtension()

FreeCADGui.addApplicationStartHandler(Initialize)
