import nuke
from nkss import nuke_start_screen

menu = nuke.menu("Nuke").findItem("Edit")
menu.addCommand("Nuke Start Screen", nuke_start_screen.show_start_screen)