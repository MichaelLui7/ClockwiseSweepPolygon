import numpy as np
import matplotlib.pyplot as plt
import random

class Vertices:
    def __init__(self):
        self.n = int(input("Number of Vertices: "))
        self.vertices = []
        for i in range(self.n):
            try:
                x = float(input(f'Real part of vertex {i+1}: '))
                y = float(input(f'Imaginary part of vertex {i+1}: '))
                self.vertices.append((x, y))
            except Exception as e:
                print(f"An error occurred: {e}")
        
        self.x_max = max(v[0] for v in self.vertices)
        self.y_max = max(v[1] for v in self.vertices)
        self.x_min = min(v[0] for v in self.vertices)
        self.y_min = min(v[1] for v in self.vertices)

        self.centroid=(
            sum(v[0] for v in self.vertices)/self.n,
            sum(v[1] for v in self.vertcies)/self.n
        )

    def plot_vertices(self):
        # plt.figure(figsize=(8, 8))
        # plt.xlim(self.x_min - 10, self.x_max + 10)
        # plt.ylim(self.y_min - 10, self.y_max + 10)
        # plt.xlabel('Real Part')
        # plt.ylabel('Imaginary Part')
        # plt.title('Vertices on Complex Plane')

        # Plot vertices
        for vertex in self.vertices:
            plt.plot(vertex[0], vertex[1], 'bo')
        plt.figure(1)
        plt.grid(True)
        plt.show()


class RandomPoints:
    def __init__(self, x_max, y_max, x_min, y_min):
        self.x_max = x_max
        self.y_max = y_max
        self.x_min = x_min
        self.y_min = y_min

    def generate_points(self, num_points=100):
        random_points = []
        for _ in range(num_points):
            x = random.uniform(self.x_min, self.x_max)
            y = random.uniform(self.y_min, self.y_max)
            random_points.append((x, y))
        return random_points


class ClockScan:
    @staticmethod
    def scan_clockwise(random_point, vertices):
        sorted_vertices = []

        # Sort vertices based on the angle relative to random_point
        for vertex in vertices:
            # Calculate angle using arctangent (angle in radians)
            angle = np.arctan2(vertex[1] - random_point[1], vertex[0] - random_point[0])

            # Convert angle to degrees and adjust for clockwise sorting
            angle_degrees = np.degrees(angle)
            if angle_degrees < 0:
                angle_degrees += 360

            sorted_vertices.append((angle_degrees, vertex))

        # Sort vertices based on angle (clockwise)
        sorted_vertices.sort(key=lambda x: x[0])

        # Return only the sorted vertices
        return [vertex[1] for vertex in sorted_vertices]

    @staticmethod
    def is_same_hamilton_cycle(list1, list2):
        # Check if two lists are the same up to rotation or reversal
        if sorted(list1) != sorted(list2):
            return False
        
        n = len(list1)
        # Check reversal
        if list1 == list2[::-1]:
            return True
        for i in range(n):
            # Check rotation
            if list1 == list2[i:] + list2[:i]:
                return True
        return False

    @staticmethod
    def choose_correct_one(sorted_lists):
        best_list = None
        max_matches = 0
        for lst in sorted_lists:
            matches = sum(ClockScan.is_same_hamilton_cycle(lst, other) for other in sorted_lists if lst != other)
            if matches > max_matches:
                max_matches = matches
                best_list = lst
        return best_list if max_matches >= 0.7 * (len(sorted_lists) - 1) else None


def connection(points):
    # Assuming points is a list of vertices sorted in a Hamiltonian cycle
    n = len(points)
    # Connect vertices in the order they appear in points
    for i in range(n):
        # Connect each vertex to the next one in the list, and loop back to the first vertex
        plt.plot([points[i][0], points[(i+1) % n][0]], [points[i][1], points[(i+1) % n][1]], 'r-')
        plt.plot(points[i][0], points[i][1], 'bo')
    
    plt.figure(1)
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    # Create vertices
    vertices_obj = Vertices()
    vertices_obj.plot_vertices()

    # Generate random points
    random_points_obj = RandomPoints(vertices_obj.x_max, vertices_obj.y_max, vertices_obj.x_min, vertices_obj.y_min)
    random_points = random_points_obj.generate_points(num_points=min(100, (vertices_obj.n)*2))

    # Example of ClockScan usage
    clock_scan_obj = ClockScan()
    sorted_lists = [clock_scan_obj.scan_clockwise(random_point, vertices_obj.vertices) for random_point in random_points]
    
    # Choose the best list
    best_list = clock_scan_obj.choose_correct_one(sorted_lists)

    # Generates Centroid:
    centroid= vertices_obj.centroid
    
    if best_list:
        print(f"The chosen list is: {best_list}")
        connection(best_list)  # Pass the best_list to the connection function
    else:
        print("No suitable Hamiltonian cycle found.")
        connection(clock_scan_obj.scan_clockwise(centroid,vertices_obj.vertices))  
    print("finished")
