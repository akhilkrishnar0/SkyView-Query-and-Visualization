# SkyView Query and Visualization

This project provides a Python script for querying astronomical surveys from the **SkyView** service and visualizing the images in a dynamic grid layout. The script utilizes **Astroquery** to fetch images from multiple surveys, then displays them with various normalization techniques using **matplotlib**. The user can specify the target celestial position (e.g., a galaxy or star), and the script will query multiple surveys and plot them in a grid format.

## Features

- **Query SkyView**: Query multiple surveys for a given celestial position (e.g., galaxy or coordinates).
- **Grid Layout**: Automatically determine the number of rows and columns for the plot based on the number of images.
- **Normalization**: Use different normalization methods (e.g., Logarithmic Normalization or Sqrt Normalization) for better visualization of astronomical images with varying intensities.
- **Customizable**: Adjust the grid layout size with a `pixel_size` parameter and choose from a variety of surveys.
- **Color Mapping**: Display images using grayscale with color bar for intensity reference.

## Requirements

- `astroquery`: For querying the SkyView service and retrieving survey images.
- `matplotlib`: For plotting the images in a grid layout.
- `numpy`: For any necessary numerical operations (e.g., array manipulations).

### Installation

To get started, you'll need to install the following dependencies:

```bash
pip install astroquery
pip install matplotlib
```

## Usage

You can use the `query_and_plot` function to query a given celestial position and display images from multiple surveys in a grid layout.

### Example

```python
from astroquery.skyview import SkyView

# Define the target position (e.g., a galaxy or coordinates)
position = "M51"

# List of surveys to query (e.g., GALEX, DSS2, WISE, etc.)
surveys = ["GALEX Near UV", "DSS2 Red", "2MASS-J", "WISE 3.4"]

# Call the query_and_plot function
query_and_plot(position, surveys, pixel_size=5)
```

### Parameters

- `position` (str): The target celestial position (e.g., "M51" for a galaxy, or coordinates like "00h42m44.3s +41d16m08s").
- `surveys` (list): A list of surveys to query (e.g., `["GALEX Near UV", "DSS2 Red", "2MASS-J"]`).
- `pixel_size` (int): The pixel size (in inches) for each subplot. Adjust this to control the size of the final plot (default is `500`).

### Normalization Options

The script supports different normalization techniques:

- **Logarithmic Normalization**: Best for images with a wide range of intensities. Enhances the contrast in the lower intensity regions.
- **Square Root Normalization**: Ideal for images with moderate intensity variations. Enhances contrast while retaining details in brighter regions.

By default, the code uses **LogNorm** for visualization. You can adjust the normalization method within the code if needed.

## Example Output

The output will be a grid layout of images from different surveys, each showing the queried position. The images will be normalized for better visualization with a color bar representing intensity.

## Contribution

Contributions are welcome! Feel free to fork the repository, create issues, and submit pull requests for improvements or bug fixes. 

---

### Acknowledgements

- **Astroquery**: For enabling access to astronomical data from SkyView and other services.
- **matplotlib**: For creating the visualization of the survey images in a customizable grid layout.


