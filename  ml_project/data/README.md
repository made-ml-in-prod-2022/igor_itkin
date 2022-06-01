# Data Description
About Dataset
Context
The data is already presented in https://www.kaggle.com/ronitf/heart-disease-uci but there are some descriptions and values that are wrong as discussed in https://www.kaggle.com/ronitf/heart-disease-uci/discussion/105877. So, here is re-processed dataset that was cross-checked with the original data https://archive.ics.uci.edu/ml/datasets/Heart+Disease.

## Content

There are 13 attributes

age: age in years

sex: sex (1 = male; 0 = female)

cp: chest pain type

    -- Value 0: typical angina
    -- Value 1: atypical angina
    -- Value 2: non-anginal pain
    -- Value 3: asymptomatic

trestbps: resting blood pressure (in mm Hg on admission to the hospital)

chol: serum cholestoral in mg/dl

fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

restecg: resting electrocardiographic results
    
    -- Value 0: normal
    -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

thalach: maximum heart rate achieved

exang: exercise induced angina (1 = yes; 0 = no)

oldpeak = ST depression induced by exercise relative to rest

slope:
the slope of the peak exercise ST segment
    
    -- Value 0: upsloping
    -- Value 1: flat
    -- Value 2: downsloping

ca: number of major vessels (0-3) colored by flourosopy

thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

and the label
condition: 0 = no disease, 1 = disease

Acknowledgements
Data posted on Kaggle: https://www.kaggle.com/ronitf/heart-disease-uci
Description of the data above: https://www.kaggle.com/ronitf/heart-disease-uci/discussion/105877
Original data https://archive.ics.uci.edu/ml/datasets/Heart+Disease

Creators:
Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbr

Creators:
Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
Donor: David W. Aha (aha '@' ics.uci.edu) (714) 856-8779

Inspiration
With the attributes described above, can you predict if a patient has heart disease?