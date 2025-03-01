import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import Connected_Graph_2nd

def get_vertices():
    # Create an instance of Vertices and get the vertices
    vertices_obj = Connected_Graph_2nd.Vertices()
    vertices = vertices_obj.vertices
    return vertices

def get_line_segments(vertices):
    # Generate line segments connecting consecutive vertices
    line_segments = []
    for i in range(len(vertices)):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % len(vertices)]
        line_segments.append([(x0, y0), (x1, y1)])
    return line_segments

def get_points_on_line_segment(segment, num_points):
    # Sample num_points evenly spaced points on the line segment
    x0, y0 = segment[0]
    x1, y1 = segment[1]
    t_values = np.linspace(0, 1, num_points)
    points = [(x0 * (1 - t) + x1 * t, y0 * (1 - t) + y1 * t) for t in t_values]
    return points

def calculate_angle(point_c, point_a, point_b):
    # Calculate the angle ACB at point C
    # Vector AC
    ac_x = point_c[0] - point_a[0]
    ac_y = point_c[1] - point_a[1]
    # Vector BC
    bc_x = point_c[0] - point_b[0]
    bc_y = point_c[1] - point_b[1]
    # Dot product and magnitude of vectors AC and BC
    dot_product = ac_x * bc_x + ac_y * bc_y
    mag_ac = np.sqrt(ac_x**2 + ac_y**2)
    mag_bc = np.sqrt(bc_x**2 + bc_y**2)
    # Cosine of the angle
    cos_angle = dot_product / (mag_ac * mag_bc)
    # Angle in radians
    angle_rad = np.arccos(cos_angle)
    # Convert to degrees
    angle_deg = np.round (np.degrees(angle_rad),7)  
    return angle_deg

def find_max_angle(vertices, point_a, point_b):
    max_angle = 0
    line_segments = get_line_segments(vertices)
    for segment in line_segments:
        points_on_segment = get_points_on_line_segment(segment, 2000 // len(line_segments))
        for point_c in points_on_segment:
            angle = calculate_angle(point_c, point_a, point_b)
            if angle > max_angle:
                max_angle = angle
    return max_angle

# Example usage:
# Define points A and B
point_a = (1, 1)
point_b = (5, 5)

# Get the vertices and find the maximum angle
vertices = get_vertices()
max_angle = find_max_angle(vertices, point_a, point_b)
print("Maximum angle:", max_angle)