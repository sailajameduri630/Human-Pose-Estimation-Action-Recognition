# Human Pose Estimation and Action Recognition in Video

## Project Overview
This project uses deep learning techniques to recognize human actions from video sequences using pose-related features and temporal modeling.

## Features
- Video-based human action recognition
- Deep learning model for action prediction
- Prediction confidence score (if supported by the application)
- Voice output for predicted actions (if supported by the application)
- Streamlit-based user interface

## Technologies Used
- Python
- TensorFlow/Keras
- CNN and LSTM (if implemented in the model)
- Streamlit
- OpenCV

## Project Files
- `App.py` – Main application
- `LRCN_model.h5` – Trained model
- `get_class_from_filename.py` – Class-name utility
- `colab_resave_model.py` – Model conversion/resaving utility
- `requirements.txt` – Python dependencies

## How to Run

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Streamlit application:
   ```bash
   streamlit run App.py
   ```

## Future Improvements
- Real-time action recognition using webcam input
- Support for additional human actions
- Improved model accuracy and robustness
