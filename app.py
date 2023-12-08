from flask import Flask, render_template, request
import os
from PIL import Image
import base64
import io
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the model when the app starts
model = None
try:
    model_path = os.path.join('mysite', 'my_model.keras')
    model = load_model('my_model.h5')
except Exception as e:
    print(f"Error loading the model: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    # Get data URL from the request
    data_url = request.form['imgData']
    # Extract the base64 encoded image data
    image_data = base64.b64decode(data_url.split(',')[1])
    # Convert to PIL Image
    img = Image.open(io.BytesIO(image_data))
    # Resize to 28x28
    img = img.resize((28, 28))
    # Convert to grayscale
    img = img.convert('L')

    # Preprocess the image
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255  # Normalize the image
    img_array = img_array.reshape(-1, 28, 28, 1)   # Reshape for the model

    # Predict the class
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    print(f'Predicted class: {predicted_class[0]}')
    return f'Predicted class: {predicted_class[0]}'



if __name__ == '__main__':
    app.run(debug=True)
