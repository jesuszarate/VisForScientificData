from paraview.simple import *

def set_rotation(obj, ren, rot):
    
    SetActiveSource(obj)    
    objDisplay = Show(obj, ren)
    objDisplay.Orientation = [0.0, 0.0, rot]
    objDisplay.PolarAxes.Orientation = [0.0, 0.0, rot]

rot = 0 

for i in range(0, 16):
    ren = Render()
    arr = Arrow()
    shrink = Shrink(Input=arr)
    
    set_rotation(shrink, ren, rot)
    
    extractEdges1 = ExtractEdges(Input=arr)
    set_rotation(extractEdges1, ren, rot)
    
    rot += 22.5
    
RenderAllViews()