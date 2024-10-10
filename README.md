#ModelForge

ModelForge is an ongoing project aimed at building a simple and efficient image classification model training application using Flask, TensorFlow, and Keras. The application allows users to upload images, and it uses those images to train a binary classification model in real-time.

This project is being developed in phases, with each feature and functionality being implemented incrementally.

Current Status
Basic Flask Web App: ✅
Set up the basic Flask server to handle image uploads via a form.
Created the index.html page with a file upload form.
Image Upload Handling: ✅
Users can upload images through the form and those images are saved in the uploads/ directory.
Model Training: ✅ (in progress)
The app trains a binary classification model using TensorFlow on uploaded images.
Images are automatically categorized based on folder structure.
Currently, it handles basic training functionality using ImageDataGenerator and saves the trained model as trained_model.h5.
Upcoming Features
1. Improved Data Handling:
 Organize images in directories based on categories (e.g., class_0, class_1).
 Add support for multi-class classification.
2. Enhanced User Interface:
 Implement a status dashboard to show training progress and model performance.
 Add a results page to view the performance metrics of the trained model (accuracy, loss, etc.).
3. Model Evaluation:
 Implement an evaluation page where users can upload new images to test the trained model.
 Provide predictions and confidence scores for uploaded test images.
4. Optimization:
 Incorporate data augmentation and preprocessing techniques for better model performance.
 Optimize model architecture to handle more complex datasets.
5. Documentation and Tutorials:
 Create documentation on how to set up the app locally.
 Write a step-by-step tutorial on how to use the app for beginners in machine learning.
Installation
1. Clone the repository: git clone https://github.com/ABS-14/ModelForge.git
cd ModelForge
2. Set up a virtual environment (optional but recommended): python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the necessary dependencies: pip install -r requirements.txt

#####################################################

Roadmap
This project is still under active development. The following improvements are planned for future releases:

• Support for multi-class classification.
• Image preprocessing and augmentation for better model performance.
• Enhanced UI/UX for better user experience.
• Model evaluation features to predict new images.
• Performance optimization and testing with larger datasets
