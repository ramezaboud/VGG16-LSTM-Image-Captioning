# Image Captioning App 🖼️✍️

An end-to-end Machine Learning web application that automatically generates descriptive text (captions) for any uploaded image.

## Overview
This project uses a deep learning architecture inspired by an Encoder-Decoder model to perform image captioning:
1. **Encoder (VGG16):** A pre-trained CNN model is used to extract rich visual features from the uploaded image.
2. **Decoder (LSTM/RNN):** A sequential model that takes the extracted image features and generates a descriptive natural language text sequence dynamically.
3. **User Interface (Streamlit):** A clean and simple UI that allows users to easily upload images and view the generated captions in real-time.

---

## 🛠️ Installation & Setup

To run this project locally, it is highly recommended to use `conda` based on the provided `environment.yml` to recreate the exact environment without version conflicts.

1. **Clone the repository:**
   ```bash
   git clone <YOUR-REPOSITORY-URL>
   cd "image captioning"
   ```

2. **Create the Conda environment:**
   This command will install Python and all required libraries (e.g., TensorFlow, Streamlit, Keras, etc.).
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment:**
   ```bash
   conda activate myenv
   ```

---

## 🚀 How to Run the App

1. Ensure you have the `working/` folder containing your trained model weights (`best_model.h5`) and the tokenizer features (`features.pkl`) within the project structure:
   ```
   📁 image captioning
   ├── 📄 app.py
   ├── 📄 environment.yml
   ├── 📄 cls-project-image-captioning.ipynb
   └── 📁 working
       ├── 📄 best_model.h5
       └── 📄 features.pkl
   ```

2. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to `http://localhost:8501`. Upload an image (`.jpg`, `.jpeg`, or `.png`) and the model will predict its caption in seconds!

---

## 📸 Demo
*(Note for the developer: Replace the text below with actual images or a GIF)*

Upload a screenshot of the UI running and displaying a generated text here:
`![App Demo GIF/Image Placeholder](URL-to-your-GIF/Image)`

---

## 📊 Dataset Reference
The model was trained using the well-known [Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k). *Because of its large size, the `flickr8k` images folder is excluded from this repository. If you plan to test or rerun the training notebook (`cls-project-image-captioning.ipynb`), you can download it from Kaggle and place it in the project root.*
