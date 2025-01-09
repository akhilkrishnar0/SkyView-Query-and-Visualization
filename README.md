# SkyView-Query-and-Visualization
This project provides a Python script for querying astronomical surveys from the SkyView service and visualizing the images in a dynamic grid layout. The script utilizes Astroquery to fetch images from multiple surveys, then displays them with various normalization techniques using matplotlib. The user can specify the target celestial position (e.g., a galaxy or star), and the script will query multiple surveys and plot them in a grid format.

Features
Query SkyView: Query multiple surveys for a given celestial position (e.g., galaxy or coordinates).
Grid Layout: Automatically determine the number of rows and columns for the plot based on the number of images.
Normalization: Use different normalization methods (e.g., Logarithmic Normalization or Sqrt Normalization) for better visualization of astronomical images with varying intensities.
Customizable: Adjust the grid layout size with a pixel_size parameter and choose from a variety of surveys.
Color Mapping: Display images using grayscale with color bar for intensity reference.
Requirements
astroquery: For querying the SkyView service and retrieving survey images.
matplotlib: For plotting the images in a grid layout.
numpy: For any necessary numerical operations (e.g., array manipulations).
Installation
To get started, you'll need to install the following dependencies:
