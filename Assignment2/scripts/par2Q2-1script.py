from paraview.simple import *

#read a object to the view
reader = OpenDataFile('/Users/jesuszarate/SchoolSemesters/Spring2018/CS6635-DataVis/Assignment2/data02/2d.vti')
Show()
Render()
ResetCamera()

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

plotOverLine1 = PlotOverLine(Input=reader, 
                            Source='High Resolution Line Source')

plotOverLine1.Source.Point2 = [4096.0, 2048.0, 0.0]

lineChartView1 = CreateView('XYChartView')
layout1.AssignView(2, lineChartView1)

plotOverLine1Display = Show(plotOverLine1, lineChartView1)