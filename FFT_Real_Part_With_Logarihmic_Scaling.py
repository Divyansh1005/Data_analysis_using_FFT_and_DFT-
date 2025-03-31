import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(File_Path) # Use pd.read_csv(filepath) if file is of format .csv and use pd.read_excel(filepath) if file is of format .xlsx   
# inside above bracket enter the file path and use read command accordingly as mentioned in above line and make sure that file is present in same directory or add path accordingly .
signal = data[Column_Name] # Inside square brackets we need to enter the name of the column in inverted commas where our required data of IMU is present .
sampling_frequency = 2000 # Set the sampling frequency as per your test data .
N = len(signal)


# Compute the amplitude
fft_result = np.fft.fft(signal)
# Compute the frequencies
freqs = np.fft.fftfreq(len(signal), 1/sampling_frequency)


# Logarithmic scaling
magnitude = abs(np.real(fft_result))
scaled_magnitude = 10 * np.log10(magnitude)


# Plotting the graph
plt.figure(figsize=(10,8)) # Declares the size of graph(10 by 8 inches)
plt.plot(freqs[0:len(freqs)//2], fft_result[0:len(freqs)//2])  
plt.title('Real Part by FFT Analysis Using Logarithmic Scaling (Shifted)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)  # Display grid for easier study
plt.show()