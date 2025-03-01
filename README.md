# ClockwiseSweepPolygon
A little program last year
## Polygon Construction & Analysis Toolkit

A collection of algorithms to construct non-intersecting polygons from 2D points, analyze geometric properties, and generate parametric representations.

### Features

- **Polygon Construction**: Implements a clockwise polar sweep algorithm
- **Randomized Testing**: Generates test coordinates automatically
- **Parametric Expressions**: Experimental line segment equation generation
- **Geometric Analysis**: Finds maximum internal angles in polygons
- **Visualization**: Built-in matplotlib plotting support

### Installation

```bash
## Clone repository with HTTPS
git clone https://github.com/MichaelLui7/ClockwiseSweepPolygon.git
cd ClockwiseSweepPolygon

## Install dependencies (Python 3.6+ required)
pip install -r requirements.txt


## Core Components

### 1. Polygon Construction (Connected_Graph_2nd.py)
Implements a robust algorithm for constructing simple polygons through systematic vertex processing:

- **Vertex Input Handling**: Supports manual coordinate entry or file input (`graph.txt`)
- **Adaptive Clockwise Scanning**: 
  - Utilizes a dynamically calculated centroid within the vertex cloud's bounding box as the polar origin
  - Avoids edge distortion common in fixed-origin approaches (e.g., bottom-left corner bias)
- **Visual Validation**: Integrated matplotlib visualization verifies non-intersecting polygon formation
- **Complexity Management**: O(n log n) sorting efficiency through optimized polar angle calculations
