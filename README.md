# 🖼️ Image Captioning Model

# Image Captioning App 

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00.svg)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000.svg)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-VGG16-green.svg)
![NLP](https://img.shields.io/badge/NLP-LSTM-blue.svg)

This project implements an **Image Captioning** system using deep learning techniques. The model generates descriptive textual captions for images by combining visual feature extraction and sequential text generation.

---

## 🏗️ Model Architecture

The architecture utilizes an **Encoder-Decoder** approach to fuse image and text features:

* **Encoder:** A pre-trained **CNN (VGG16)** is used to extract 4096-dimensional feature vectors from input images. Dense layers are then applied to process these features.
* **Decoder:** An **LSTM** sequence model is used for caption generation, utilizing an embedding layer for text input and dense layers for output prediction.
* **Optimization:** Compiled using Categorical Crossentropy loss and the Adam optimizer.

---

## 📝 Dataset

This project uses the [Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k).

| Detail | Value |
|---|---|
| Total Images | ~8,091 |
| Total Captions | ~40,455 (~5 per image) |
| Source | Kaggle |

> **Note:** Due to size constraints, the raw dataset is **not included** in this repository. You can download it from [Google Drive](https://drive.google.com/drive/folders/1ByljBwnVCczz99eG74T3yEPDQWBGs--O) or from [Kaggle](https://www.kaggle.com/datasets/adityajn105/flickr8k). Place it in the project root as `flickr8k/`.

---

## 🏷️ Key Features

* Image-Text fusion with Encoder-Decoder (VGG16 + LSTM).
* NLP preprocessing with NLTK (stopword removal, tokenization).
* Batch-wise data generator for memory efficiency.
* BLEU score evaluation (BLEU-1 ≈ 0.55, BLEU-2 ≈ 0.33).
* Interactive **Streamlit** web app for real-time inference.

---

## � Example Output

| Input Image | Generated Caption |
|:---:|:---:|
| ![Example Output](https://github.com/user-attachments/assets/4af38267-7db8-48a2-befd-af82a1db85d5) | *"little girl pigtails fingerpaints"* |

---

## 🛠️ Installation & Setup

It is recommended to use `conda` based on the provided `environment.yml`.

1. **Clone the repository:**
   ```bash
   git clone <YOUR-REPOSITORY-URL>
   cd "image captioning"
   ```

2. **Create the Conda environment:**
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment:**
   ```bash
   conda activate myenv
   ```

---

## 🚀 How to Run the App

1. Ensure you have the `working/` folder containing your trained model weights and tokenizer:
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

3. Open your browser at `http://localhost:8501`, upload an image, and the model will generate a caption!

---

## � Activity Diagram

📄 [View Activity Diagram (PDF)](activite.pdf)

---

## � License

This project is open-source and available under the MIT License.
