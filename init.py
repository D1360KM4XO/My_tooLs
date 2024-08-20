import nuke
import os

def add_tools_to_menu(menu, folder_path):
    # Iterate through each item in the given folder
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)

        if os.path.isdir(item_path):  # If the item is a directory, create a submenu
            sub_menu = menu.addMenu(item_name)
            add_tools_to_menu(sub_menu, item_path)  # Recursively add items from the subdirectory

        elif item_name.endswith(".gizmo"):  # Add gizmo files to the current menu or submenu
            gizmo_name = os.path.splitext(item_name)[0]
            menu.addCommand(gizmo_name, lambda g=item_path: nuke.nodePaste(g))

        elif item_name.endswith(".nk"):  # Add toolset files to the current menu or submenu
            toolset_name = os.path.splitext(item_name)[0]
            menu.addCommand(toolset_name, lambda t=item_path: nuke.nodePaste(t))

def add_dc_tools_menu():
    # Define the base path relative to the user's home directory
    base_path = os.path.expanduser("~/.nuke/DC_tools")
    icons_path = os.path.join(base_path, "icons")

    # Create the main DC Tools menu
    toolbar = nuke.toolbar("Nodes")
    dc_tools_menu = toolbar.addMenu("DC Tools", icon=os.path.join(icons_path, "DC_tools.png"))

    # Add tools from the base directory (DC_tools)
    add_tools_to_menu(dc_tools_menu, base_path)

# Defer adding the DC Tools menu until after Nuke has initialized all other menus
nuke.addOnCreate(add_dc_tools_menu, nodeClass='Root')





###############

###############

###############

###############

###############



nuke.pluginAddPath("stamps")

nuke.pluginAddPath('pixelfudger3')


nuke.pluginAddPath("NukeSurvivalToolkit")



