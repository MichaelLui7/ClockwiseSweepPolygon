import numpy as np
import sympy as sp
from Connected_Graph_2nd import Vertices,ClockScan

def get_expression_from(vertices):
    t = sp.symbols('t')
    function_list = []

    # For every pair of consecutive vertices, create a parametric equation
    for i in range(len(vertices)):
        x0, y0 = vertices[i]
        x1, y1 = vertices[i + 1]
        
        # Parametric equation for the line segment between the two vertices
        x_t = x0 * (1 - t) + x1 * t
        y_t = y0 * (1 - t) + y1 * t

        # Add the parametric equations to the list
        function_list.append((x_t, y_t))

    # Add the last segment connecting the last and first vertices to form a closed loop(This is not an optimal attempt)
    x0, y0 = vertices[-1]
    x1, y1 = vertices[0]
    x_t = x0 * (1 - t) + x1 * t
    y_t = y0 * (1 - t) + y1 * t
    function_list.append((x_t, y_t))

    return function_list


if __name__ == "__main__":
    # Create an instance of Vertices and get the vertices
    vertices_obj = Vertices()
    vertices = vertices_obj.vertices
    
    # Get the expressions for the line segments
    function_list = get_expression_from(vertices)
    
    # Print the expressions for demonstration purposes
    for i, (x_t, y_t) in enumerate(function_list):
        print(f"Line Segment {i}: x(t) = {x_t}, y(t) = {y_t}")