### How to compute nx, ny for a custom resolution

#### Step 1: Convert your desired resolution (in km) to degrees
Choose the desired horizontal and vertical resolution, for example 2 km.
At ≈ 46°N (latitude of central Europe):
- 1° latitude ≈ 111.2 km
- 1° longitude ≈ 111.2 × cos(46°) ≈ 77.2 km

Now, convert your chosen resolution into degrees. In our case of 2 km horizontal and vertical resolution we get:
- Δx ≈ 2 / 77.2 ≈ 0.026°
- Δy ≈ 2 / 111.2 ≈ 0.018°

The vertical resolution of 2 km corresponds to 0.018° and the horizontal resolution of 2 km corresponds to 0.026°.

---

#### Step 2: Compute the number of grid points

Use the bounding box of the ICON-CH1/2-EPS domain:

- x<sub>min</sub> = −0.817, x<sub>max</sub> = 18.183
- y<sub>min</sub> = 41.183, y<sub>max</sub> = 51.183

Then compute the number of grid points.

- $n_x = \frac{x_{\text{max}} - x_{\text{min}}}{\Delta x} + 1$
- $n_y = \frac{y_{\text{max}} - y_{\text{min}}}{\Delta y} + 1$

For our example of 2 km resolution we get:
- $n_x ≈ 732$
- $n_y ≈ 557$
