import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# signal = [0.434269,0.449724,0.447024,0.439791,0.428057] # Sample data of 5 values . Just comment the line if you are having a data file .
data = pd.read_csv(File_Path) # Use pd.read_csv(filepath) if file is of format .csv and use pd.read_excel(filepath) if file is of format .xlsx   
# inside above bracket enter the file path and use read command accordingly as mentioned in above line and make sure that file is present in same directory or add path accordingly .
signal = data[Column_Name] # Inside square brackets we need to enter the name of the column in inverted commas where our required data of IMU is present .
sampling_frequency = 2000 # Set the sampling frequency as per your test data .
N = len(signal)

freqs = []
freq_step = sampling_frequency / N
for i in range(N):
    freqs.append(i * freq_step)

dft_result = []
for k in range(N):
    sum_complex = 0
    for n in range(N):
        angle = -2j * np.pi * k * n / N
        sum_complex += signal[n] * np.exp(angle)
    dft_result.append(sum_complex)
# Below 2 lines are for converting the Real Part obtained by DFT formula into dB  
mag = np.abs(np.real(dft_result))
scaled_magnitude = 10 * np.log10(mag)

# Below is the code for plotting the graph 
plt.figure(figsize=(10, 8)) # Declares the size of graph(10 by 8 inches)
plt.plot(freqs, scaled_magnitude, label='Real Part')  # 'label' parameter defines the name that will be displayed on the graph 
plt.title('DFT Analysis (Real Part)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('DFT Result (Real Part)')
plt.grid(True)
plt.legend()
plt.show()
