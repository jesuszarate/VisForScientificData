from paraview.simple import *

rot = 0 

for i in range(0, 16):
    ren = Render()
    arr = Arrow()

    arrowDisp = Show(arr, ren)
    arrowDisp.Orientation = [0.0, 0.0, rot]
    arrowDisp.PolarAxes.Orientation = [0.0, 0.0, rot]
    arr.TipResolution = 12
    rot += 22.5   
    
RenderAllViews()