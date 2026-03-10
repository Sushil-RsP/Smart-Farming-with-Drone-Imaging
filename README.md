# Smart Farming with Drone Imaging 🌾📡

This project is a smart farming solution that leverages drone-captured imagery and machine learning to analyze vegetation health using NDVI (Normalized Difference Vegetation Index) and image segmentation. It provides a simple web interface built with Flask for farmers, agronomists, and researchers.

---   

## 🚀 Features

- 📥 Upload drone images via web interface
- 🌿 Calculate NDVI from simulated NIR and Red channels
- 🧠 Segment crop health regions using a dummy U-Net model
- 🌈 Visualize NDVI heatmaps and segmentation overlays
- 📊 Display field health statistics (mean NDVI, healthy crop area, etc.)
- 🖼️ Clean, responsive UI with custom background and styles

---

## 🛠️ Technologies Used

- Python 3.12
- Flask
- OpenCV
- NumPy
- Matplotlib
- HTML5 + CSS3

---


## 📁 Folder Structure

Smart-Farming-with-Drone-Imaging/
├── app.py # Main Flask application
├── ndvi_calculator.py # NDVI computation and preprocessing
├── segmenter.py # Dummy U-Net style segmentation
├── visualizer.py # Visualization and field statistics
├── static/
│ ├── uploads/ # Uploaded drone images
│ ├── outputs/ # Processed images (NDVI, masks, overlays)
│ └── bg/ # Background assets
└── templates/
├── index_with_bg.html # Upload interface
└── result_with_bg.html # Results display


---

## Run the Flask app:
 - python app.py
   
