from django.shortcuts import render, render_to_response
# from bokeh.io import show, output_file
from bokeh.models import FactorRange
from bokeh.plotting import figure,output_file,show
from bokeh.models import Range1d

# embed for bokeh 
from bokeh.embed import components

# Create your views here.
def app_page_main(request):
    factors = [
    ("Q1", "jan"), ("Q1", "feb"), ("Q1", "mar"),
    ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
    ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
    ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),
    ]
    p = figure(x_range=FactorRange(*factors), plot_height=300,plot_width=500,
    toolbar_location="below", tools="pan,wheel_zoom,box_zoom,reset,tap")
    x = [ 10, 12, 16, 9, 10, 8, 12, 13, 14, 14, 12, 16 ]
    p.vbar(x=factors, top=x, width=0.9, alpha=0.5)

    p.line(x=["Q1", "Q2", "Q3", "Q4"], y=[12, 9, 13, 14], color="red", line_width=2)

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    
        # create some data
    x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [0, 8, 2, 4, 6, 9, 5, 6, 25, 28, 4, 7]
    x2 = [2, 5, 7, 15, 18, 19, 25, 28, 9, 10, 4]
    y2 = [2, 4, 6, 9, 15, 18, 0, 8, 2, 25, 28]
    x3 = [0, 1, 0, 8, 2, 4, 6, 9, 7, 8, 9]
    y3 = [0, 8, 4, 6, 9, 15, 18, 19, 19, 25, 28]

    # select the tools we want
    TOOLS="pan,wheel_zoom,box_zoom,reset,save"

    # the red and blue graphs will share this data range
    xr1 = Range1d(start=0, end=30)
    yr1 = Range1d(start=0, end=30)

    # only the green will use this data range
    xr2 = Range1d(start=0, end=30)
    yr2 = Range1d(start=0, end=30)

    # build our figures
    p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=500, plot_height=300)
    p1.scatter(x1, y1, size=12, color="red", alpha=0.5)

    p2 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
    p2.scatter(x2, y2, size=12, color="blue", alpha=0.5)

    p3 = figure(x_range=xr2, y_range=yr2, tools=TOOLS, plot_width=300, plot_height=300)
    p3.scatter(x3, y3, size=12, color="green", alpha=0.5)

    # plots can be a single Bokeh Model, a list/tuple, or even a dictionary
    plots = {'Red': p1, 'Blue': p2, 'Green': p3,'yellow':p} 
    script,div = components(p)
    script1,div1= components(p1)



    return render_to_response('app_pages/app_page_main.html',{'script':script,'div':div,'script1':script1,'div1':div1})