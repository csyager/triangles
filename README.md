# Triangles
This python script uses matplotlib and Qt to create a GUI that simulates a simple math trick.  Starting with a triangle and a point inside of it, if you repeatedly move half the distance to a randomly-selected vertice and plot a point, you will approach a fractal pattern of infinitely repeating triangles.  To illustrate this, this script creates a canvas with three vertices and an internal point on the screen.  Click the screen to move the dot around to any starting position.  Click the `Plot point` button to plot a point half the distance from the starting point to a randomly-chosen vertice.  Click `Plot 100 points` to repeat this operation 100 times.  Do that a few times and you should see the fractal pattern start to emerge.

## Installation and Usage
```
git clone https://github.com/csyager/triangles.git
```

There are three simulations in this repo.  The first shows the Chaos Game with four vertices, any of which can be chosen as the next vertex:  
```
python3 random_squares.py
```

The second shows the Chaos Game with four vertices, but the same vertex cannot be chosen as the next vertex twice consecutively:  
```
python3 squares.py
```

The last simulation shows the Chaos Game with three vertices, where any vertex can be chosen at each round:  
```
python3 triangles.py
```
