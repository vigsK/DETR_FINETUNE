"""
Example script showing how to use the fixed plot_utils module.

Replace your code block 33 with this approach:
"""

from util.plot_utils import plot_logs
from pathlib import Path

# Your log directory path
log_directory = Path('your_log_directory_path_here')  # Update this with your actual path

# Fields of interest
fields_of_interest = (
    'loss',
    'mAP',
)

# Call the fixed plot_logs function
plot_logs(log_directory, fields_of_interest)
