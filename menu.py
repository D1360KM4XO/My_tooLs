
# to add Favorites use this:
# nuke.addFavoriteDir("name", "folder")
#e.g.

	# preset for importing stuff
	#
	# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#      IF GIZMOS ARE IMPLEMENTED LOCALLY
	#      USE COPY TO GROUP IN THE NODE TAB
	#      OF THE GIZMO TO AVOID ERRORS WHILE
	#      RENDERING ON THE FARM  PLEASE !!!
	# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#
	#

# WRITE YOUR CODE HERE #

#### BBOX B PIPE>>>
nuke.knobDefault('Merge2.bbox', 'B')

#### MIX VALUE ON MERGE NODE>>>
nuke.knobDefault('Merge2.label','Mix [knob mix]')


#### MIX VALUE ON MERGE NODE>>>
#### nuke.knobDefault('Merge2.label','[knob lifetimeStart]-[knob lifetimeEnd]')



#### BLUR SIZE AND VALUE>>>
nuke.knobDefault("Blur.size", "2")
nuke.knobDefault("Blur.label", "<center><b>[value size] px")
### nuke.knobDefault("Blur.label", "[knob lifetimeStart]-[knob lifetimeEnd]")

#### METADATA ON READ NODE>>>
nuke.knobDefault("Read.label", "[metadata input/width] x [metadata input/height]\nFrame Rage: [value first] - [value last]\nColorspace: [value colorspace]")

#### SHUFFLE NODE LABEL>>>
nuke.knobDefault("Shuffle2.label", "<font size='6'><b>[knob in1]")

#### ROTO NO CLIP>>>
nuke.knobDefault("Roto.cliptype", "no clip")
nuke.knobDefault("RotoPaint.cliptype", "no clip")

#### MULTIPLY VALUE>>>
nuke.knobDefault("Multiply.label", "[knob value]")

#### LAYERCONTACT NAMES>>>
# nuke.knobDefault("LayerContactSheet.showLayerNames", "[knob value]")
nuke.addOnCreate(lambda: nuke.thisNode()['showLayerNames'].setValue(True) if nuke.thisNode().Class() == 'LayerContactSheet' else None, nodeClass='LayerContactSheet')

#### SWITCH LABEL INPUT>>>>
nuke.knobDefault("Switch.label", "[value which]")


#### VIEWER SIZE AND COLOUR>>>>
nuke.knobDefault("Viewer.label", "_")
nuke.addOnCreate(lambda: [nuke.thisNode()['tile_color'].setValue(0xFF39FF14), nuke.thisNode()['note_font_size'].setValue(50)] if nuke.thisNode().Class() == 'Viewer' else None, nodeClass='Viewer')


#### KEEP RGB AND LABEL>>>>
# Define a function that modifies the Remove node on creation
#def onRemoveNodeCreated():
#    node = nuke.thisNode()
#    if node.Class() == 'Remove':
#        node['operation'].setValue('keep')
#        node['channels'].setValue('rgb')

# Add the function to the node creation callback
#nuke.addOnUserCreate(onRemoveNodeCreated, nodeClass='Remove')


# Register the function to be called when a node is created
#nuke.addOnCreate(onRemoveNodeCreated, nodeClass='Remove')


# Set the default label for the Remove node
#nuke.knobDefault("Remove.label", "[knob channels]")


#### REFORMAT NODE LABEL>>>
#nuke.knobDefault("Reformat.label", "[knob filter]")


#### OCIOCOLORSPACE NODE LABEL>>>
nuke.knobDefault("OCIOColorSpace.label", "<center><b>[value in_colorspace]\n[value out_colorspace]")





# Example of how you might add this to a menu
# nuke.menu('Nuke').addCommand('Scripts/Kill All Viewers', killViewers)
