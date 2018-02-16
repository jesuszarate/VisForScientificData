from paraview.simple import *

# create a new 'XML Image Data Reader'
a2dvti = XMLImageDataReader(FileName=['/Users/jesuszarate/SchoolSemesters/Spring2018/CS6635-DataVis/Assignment2/data02/2d.vti'])
a2dvti.PointArrayStatus = ['Scalars_']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get color transfer function/color map for 'Scalars_'
scalars_LUT = GetColorTransferFunction('Scalars_')

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = GetOpacityTransferFunction('Scalars_')

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
a2dvtiDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=a2dvti)

# set active source
SetActiveSource(warpByScalar1)

# show data in view
warpByScalar1Display = Show(warpByScalar1, renderView1)

warpByScalar1Display.ScaleFactor = 409.6


# show color bar/color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

Hide(a2dvti, renderView1)
