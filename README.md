# Parkinson's Disease Detection

## Overview
-This project aims to develop a machine learning model for the early detection of Parkinson's disease using various features extracted from patient data. Early diagnosis is crucial for effective treatment and management of the disease.
## Problem Statement
-Parkinson's disease is a progressive neurodegenerative disorder that affects movement. This project focuses on creating a predictive model to identify Parkinson's disease based on voice recordings and other clinical features, enabling timely intervention.
## Dataset

- The datset includes :

- **name**: The name or identifier of the patient in the dataset.

- **MDVP:Fo(Hz)**: The fundamental frequency (Fo) in Hertz, which measures the pitch of the voice.

- **MDVP:Fhi(Hz)**: The highest frequency (Fhi) in Hertz, representing the maximum pitch during voice recording.

- **MDVP:Flo(Hz)**: The lowest frequency (Flo) in Hertz, representing the minimum pitch during voice recording.

- **MDVP:Jitter(%)**: Jitter percentage, which quantifies the frequency variation from cycle to cycle in a voice signal. It is an indicator of voice stability.

- **MDVP:Jitter(Abs)**: Absolute jitter value, representing the average absolute difference between consecutive periods of the voice signal.

- **MDVP:RAP**: Relative Average Perturbation, a measure of voice irregularity calculated over three cycles of the voice signal.

- **MDVP:PPQ**: Pitch Perturbation Quotient, a measure of periodicity in the voice signal, assessing pitch stability over a longer duration.

- **Jitter:DDP**: Difference of Differences of Periods, another measure of voice stability that evaluates variations in the lengths of cycles.

- **MDVP:Shimmer**: Amplitude variation in the voice signal, indicating how much the intensity of the voice changes from one cycle to the next.

- **MDVP:Shimmer(dB)**: Shimmer measured in decibels, a logarithmic representation of amplitude variation.

- **Shimmer:APQ3**: Amplitude Perturbation Quotient (APQ) calculated over a short window, assessing short-term amplitude variations.

- **Shimmer:APQ5**: Similar to APQ3 but calculated over a longer duration, providing insight into amplitude stability over time.

- **MDVP:APQ**: A general measure of amplitude perturbation, representing overall stability in voice amplitude.

- **Shimmer:DDA**: Double Dissimilarity Amplitude, a measure of amplitude perturbation that considers variations across multiple cycles.

- **NHR**: Noise to Harmonics Ratio, which quantifies the amount of noise in the voice relative to its harmonic components.

- **HNR**: Harmonics to Noise Ratio, indicating the relative strength of harmonics compared to noise in the voice signal.

- **status**: The classification status of the patient, indicating whether they have Parkinson's disease (1) or not (0).

- **RPDE**: Recurrence Period Density Entropy, a measure of the complexity of the voice signal that helps differentiate between normal and pathological voices.

- **DFA**: Detrended Fluctuation Analysis, a method used to analyze the fractal-like properties of the voice signal, assessing its variability.

- **spread1**: A measure related to the distribution of data points, typically used to assess the spread of features in voice analysis.

- **spread2**: Another measure of distribution related to the analysis of voice signal characteristics.

- **D2**: A measure of complexity in the voice signal, often associated with non-linear dynamics in speech patterns.

- **PPE**: Pitch Period Entropy, quantifying the irregularity of pitch periods in the voice signal, helping to assess voice stability.

These features are essential for analyzing voice characteristics that may indicate the presence of Parkinson's disease, allowing for early detection and intervention.

## Web App
- A web application has been created using Streamlit to provide a user-friendly interface for detecting Parkinson's disease. The app allows users to:

#### Input Data: Users can enter specific data points related to voice recordings and patient characteristics.
#### View Predictions: After entering the data, users can submit the input to receive a prediction indicating whether the person is likely to have Parkinson's disease.

## License
-This project is licensed under the MIT License - see the LICENSE file for details.
