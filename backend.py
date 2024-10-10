from flask import Flask, request, render_template,  jsonify
import os
from tensorflow import keras 
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route
@app.route('/')
def home():
    return render_template('index.html')
# Handle favicon.ico requests to prevent 404 errors
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Train model route
@app.route('/train', methods=['POST'])
def train():
    if 'files[]' not in request.files:
        return jsonify({'message': 'No files part'})

    files = request.files.getlist('files[]')
    if len(files) == 0:
        return jsonify({'message': 'No files received'})
    
    print(f"Received {len(files)} files")

    # Save uploaded files
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            print(f"Saved file: {file_path}")  # Check if files are saved

    # Train the model with the uploaded images
    message = train_model(app.config['UPLOAD_FOLDER'])

    return jsonify({'message': message})

# Model training function
def train_model(data_directory):
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    # Generate training data
    train_generator = datagen.flow_from_directory(
        data_directory,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary',
        subset='training')  # Using 80% of data for training

    # Generate validation data
    validation_generator = datagen.flow_from_directory(
        data_directory,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary',
        subset='validation')  # Using 20% of data for validation

    # CNN model architecture
    model = keras.models.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Conv2D(128, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Conv2D(128, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Flatten(),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    model.fit(train_generator, validation_data=validation_generator, epochs=10)

    # Save the trained model
    model.save('trained_model.h5')

    return 'Model trained and saved!'

if __name__ == '__main__':
    app.run(debug=True)

