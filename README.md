# Triangles
This python script uses matplotlib and Qt to create a GUI that simulates a simple math trick.  Starting with a triangle and a point inside of it, if you repeatedly move half the distance to a randomly-selected vertice and plot a point, you will approach a fractal pattern of infinitely repeating triangles.  To illustrate this, this script creates a canvas with three vertices and an internal point on the screen.  Click the screen to move the dot around to any starting position.  Click the `Plot point` button to plot a point half the distance from the starting point to a randomly-chosen vertice.  Click `Plot 100 points` to repeat this operation 100 times.  Do that a few times and you should see the fractal pattern start to emerge.