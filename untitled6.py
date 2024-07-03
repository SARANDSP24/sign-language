import numpy as np

class Shape:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def translate(self, tx, ty):
        """Translates the shape by tx and ty."""
        translation_matrix = np.array([[1, 0, tx],
                                    [0, 1, ty],
                                    [0, 0, 1]])
        for i in range(len(self.vertices)):
            homogeneous_vertex = np.array([self.vertices[i][0], self.vertices[i][1], 1])
            translated_vertex = np.dot(translation_matrix, homogeneous_vertex)
            self.vertices[i] = (translated_vertex[0], translated_vertex[1])

    def rotate(self, angle_degrees, center=(0, 0)):
        """Rotates the shape around a center point by angle_degrees."""
        angle_radians = np.radians(angle_degrees)
        rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians), 0],
                                    [np.sin(angle_radians), np.cos(angle_radians), 0],
                                    [0, 0, 1]])
        for i in range(len(self.vertices)):
            # Translate to origin, rotate, and translate back
            self.vertices[i] = (self.vertices[i][0] - center[0], self.vertices[i][1] - center[1])
            homogeneous_vertex = np.array([self.vertices[i][0], self.vertices[i][1], 1])
            rotated_vertex = np.dot(rotation_matrix, homogeneous_vertex)
            self.vertices[i] = (rotated_vertex[0] + center[0], rotated_vertex[1] + center[1])

    def scale(self, sx, sy, center=(0, 0)):
        """Scales the shape around a center point by sx and sy."""
        scaling_matrix = np.array([[sx, 0, 0],
                                    [0, sy, 0],
                                    [0, 0, 1]])
        for i in range(len(self.vertices)):
            # Translate to origin, scale, and translate back
            self.vertices[i] = (self.vertices[i][0] - center[0], self.vertices[i][1] - center[1])
            homogeneous_vertex = np.array([self.vertices[i][0], self.vertices[i][1], 1])
            scaled_vertex = np.dot(scaling_matrix, homogeneous_vertex)
            self.vertices[i] = (scaled_vertex[0] + center[0], scaled_vertex[1] + center[1])

    def get_primitives(self):
        """Returns the shape's edges as a list of line segments."""
        primitives = []
        for edge in self.edges:
            start_vertex = self.vertices[edge[0]]
            end_vertex = self.vertices[edge[1]]
            primitives.append((start_vertex, end_vertex))
        return primitives

# Example:
# Create a triangle
triangle_vertices = [(2, 1), (5, 4), (1, 4)]
triangle_edges = [(0, 1), (1, 2), (2, 0)]
triangle = Shape(triangle_vertices, triangle_edges)

# Perform transformations
triangle.translate(3, 2)
triangle.rotate(45, center=(5, 5))
triangle.scale(1.5, 0.8, center=(5, 5))

# Get the primitives (line segments)
primitives = triangle.get_primitives()

# Output
print("Transformed Triangle Primitives:")
for primitive in primitives:
    print(f"Line: ({primitive[0][0]}, {primitive[0][1]}) -> ({primitive[1][0]}, {primitive[1][1]})")