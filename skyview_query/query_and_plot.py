# skyview_query/query_and_plot.py

import matplotlib.pyplot as plt
from astroquery.skyview import SkyView
import math
from matplotlib.colors import LogNorm

def query_and_plot(position, surveys, pixel_size=5):
    """
    Query SkyView for multiple surveys and plot them in a dynamic grid layout with LogNorm normalization.

    Parameters:
    - position: str, target position (e.g., "M51" or "00h42m44.3s +41d16m08s")
    - surveys: list, list of surveys to query
    - pixel_size: int, pixel size for the subplot (default is 5) 
    """
    # Query SkyView for the images of the given position and surveys
    images = SkyView.get_images(position=position, survey=surveys)

    # Calculate number of rows and columns based on the number of surveys
    total_images = len(surveys)
    n_cols = math.ceil(math.sqrt(total_images))  # Number of columns
    n_rows = math.ceil(total_images / n_cols)   # Number of rows

    # Create a figure with the specified grid layout
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols * pixel_size, n_rows * pixel_size))

    # Flatten the axes to easily iterate over
    axes = axes.flatten()

    # Plot each image in the grid
    for i, ax in enumerate(axes):
        if i < total_images:  # Only plot the images we have
            # Get the image data
            img_data = images[i][0].data

            # Apply logarithmic normalization using LogNorm
            norm = LogNorm(vmin=img_data.min(), vmax=img_data.max())

            # Display the image in the corresponding subplot with normalized scaling
            im = ax.imshow(img_data, cmap='gray', origin='lower', aspect='auto', norm=norm)
            
            # Set title to the survey name
            ax.set_title(surveys[i])
            ax.axis('off')  # Turn off axis labels for better visualization

            # Add color bar
            fig.colorbar(im, ax=ax, orientation='vertical')

        else:
            ax.axis('off')  # Hide unused axes

    # Adjust layout for better spacing
    plt.tight_layout()
    plt.show()
