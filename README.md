# OO code using turtle graphics

### What I've Done
- Implemented a Python program using object-oriented programming principles.
- Created two classes: `Polygon` for drawing regular polygons and `EmbeddedPolygon` for drawing nested shapes.
- Developed a `Run` class to manage user inputs and generate random attributes for shapes (size, color, orientation, location).
- Added functionality to draw nine different art styles based on user input, utilizing the `turtle` graphics module.
- Successfully generated screenshots for each of the nine art styles.

### Issues Encountered
- **Random Attribute Assignment**: Faced challenges with ensuring unique attributes for each shape. Fixed by properly calling the `randat()` method before each shape draw.
- **Turtle Performance**: Drawing large numbers of shapes slowed down the rendering. Improved speed using `turtle.tracer(0)` for faster screen updates. (I used Chatgpt to help with this by using `turtle.update()`)
