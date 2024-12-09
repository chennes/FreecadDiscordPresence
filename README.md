# FreeCAD Discord Rich Presence Extension

This extension integrates Discord Rich Presence with FreeCAD, allowing users to display their current FreeCAD activity (such as the active workbench and file being edited) directly in Discord.

## Features
- Displays the current workbench in use within FreeCAD.
- Shows the name of the file currently being edited.
- Updates every 5 seconds to reflect real-time changes in FreeCAD.
- Automatically starts and stops when FreeCAD is running.

## Requirements
- **FreeCAD**: Version 0.19 or higher.
- **PySide2**: Qt bindings for Python used by FreeCAD for GUI.
- **pypresence**: Python library to manage Discord Rich Presence.

You can install the required library with the following:

```bash
pip install pypresence
```

## Installation
1. Download/Clone the repository: You can clone or download this project to your local machine.

2. Place the script in the Mod folder of freecad.
    - On Linux it is usually /usr/share/freecad/Mod/
    - On Windows it is usually C:\Program Files\FreeCAD\Mod\
    - On macOS it is usually /Applications/FreeCAD/Mod/