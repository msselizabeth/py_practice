import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle(vert, ax):
    triangle = patches.Polygon(vert, fill=False, edgecolor='red')
    ax.add_patch(triangle)
    
draw_triangle([[0,0], [0.5, 0.75]])