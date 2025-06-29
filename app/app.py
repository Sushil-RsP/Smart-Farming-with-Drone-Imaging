
from flask import Flask, render_template, request, redirect
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from ndvi_calculator import preprocess_image, calculate_ndvi
from segmenter import dummy_unet_segmentation
from visualizer import overlay_segmentation, compute_field_statistics
import matplotlib.pyplot as plt

UPLOAD_FOLDER = 'static/uploads' 
OUTPUT_FOLDER = 'static/outputs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_visual(name, array, cmap='viridis'):
    plt.imshow(array, cmap=cmap)
    plt.axis('off')
    save_path = os.path.join(OUTPUT_FOLDER, name)
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    return save_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Load and process
        image = cv2.imread(filepath)
        image = cv2.resize(image, (256, 256))
        preprocessed = preprocess_image(image)
        red_channel = preprocessed[:, :, 2]
        nir_channel = red_channel + 0.2 
        ndvi = calculate_ndvi(nir_channel, red_channel)
        segmented = dummy_unet_segmentation(ndvi)
        overlay = overlay_segmentation((preprocessed * 255).astype('uint8'), segmented)
        stats = compute_field_statistics(ndvi, segmented)

        # Save outputs
        ndvi_path = save_visual('ndvi_map.png', ndvi, cmap='RdYlGn')
        seg_path = save_visual('seg_map.png', segmented, cmap='Accent')
        overlay_path = os.path.join(app.config['OUTPUT_FOLDER'], 'overlay.png')
        cv2.imwrite(overlay_path, overlay)

        return render_template('result_with_bg.html',
                               ndvi_path=ndvi_path,
                               seg_path=seg_path,
                               overlay_path=overlay_path,
                               stats=stats,
                               uploaded_image=filepath)
    return render_template('index_with_bg.html')

if __name__ == '__main__':
    app.run(debug=True)

# python app.py