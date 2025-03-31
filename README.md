## Overview
This repository provides generalized code for analyzing time series data using various techniques, including Fast Fourier Transform (FFT), Discrete Fourier Transform (DFT), and Dynamic Time Warping (DTW). The primary dataset consists of time series data from an Inertial Measurement Unit (IMU), and the analysis methods are tailored for processing and extracting meaningful patterns and insights from the sensor data.

The project aims to provide a flexible framework for applying these time series analysis techniques to IMU data, which can be adapted for a range of different applications such as sensor data analysis, motion tracking, and anomaly detection.

## Features
- **FFT (Fast Fourier Transform):** Efficient algorithm to compute the Discrete Fourier Transform (DFT) of a time series, enabling frequency domain analysis.
- **DFT (Discrete Fourier Transform):** Provides an understanding of the frequency components in the time series data.
- **DTW (Dynamic Time Warping):** A method for measuring similarity between two time series that may vary in speed.
- **Generalized Code:** The code is written in a modular fashion to allow for easy customization and extension for other datasets or use cases.

## Installation Guide
This section provides detailed steps for setting up your environment and installing the required libraries to run the time series analysis project.

### Clone the Repository
```bash
git clone https://github.com/Karanveer69/Data-Analysis-Using-FFT-DFT-and-DTW.git
```

### Setting Up a Virtual Environment
It's a good practice to use a virtual environment to isolate your project's dependencies and avoid conflicts with other Python projects on your system.

Using `venv` (Standard Library), create a Virtual Environment. Open a terminal and navigate to the project directory, then run:
```bash
python3 -m venv venv
```
This will create a folder named `venv` that contains the isolated environment.

### Activate the Virtual Environment
#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```
After activation, your terminal prompt should change to indicate you're working inside the virtual environment.

### Change Directory
Run the following command in your terminal:
```bash
cd Data-Analysis-Using-FFT-DFT-and-DTW
```

### Install Dependencies
Once your virtual environment is set up and activated, install the required dependencies for the project:
```bash
pip install numpy matplotlib pandas dtaidistance
```

### Verify Installation (Optional)
After installation is complete, you can verify that all the libraries are installed by running the following Python commands:
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dtw
```
If no errors appear, the installation was successful.

