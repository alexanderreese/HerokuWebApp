# HerokuWebApp

Website: https://ajreese1-finalproject-0c860333516f.herokuapp.com/ 
Project Repo: https://github.com/alexanderreese/HerokuWebApp 

## 1. Introduction
This report outlines the process of deploying a TensorFlow Convolutional Neural Network (CNN) model, trained on the MNIST dataset, using Heroku as a platform. The deployment includes a web interface for user interaction, allowing users to draw a digit and receive a prediction from the model.
## 2. Dataset Selection & Model Training
### 2.1 Dataset Description
The MNIST dataset, a standard in machine learning, was used for training the model. It comprises 70,000 grayscale images of handwritten digits (0-9), each of size 28x28 pixels. The dataset is divided into 60,000 training images and 10,000 testing images.
### 2.2 Model Training and Serialization
A CNN was designed and trained using TensorFlow. The architecture included convolutional layers, pooling layers, and fully connected layers, optimized for recognizing handwritten digits. After training, the model achieved a high accuracy of +99% on the test set. It was then serialized using TensorFlow's save_model function, allowing for later use in prediction.
## 3. Deployment Preparation
### 3.1 Selection of Deployment Tool/Platform
Heroku, a cloud platform as a service, was chosen for deployment due to its ease of use, scalability, and support for various programming languages and frameworks, including Flask for Python and TensorFlow.
### 3.2 Web/API Endpoint Development
A Flask web application was developed as an interface for the model. The application features a drawing canvas where users can draw a digit. JavaScript functions capture the canvas content and send it to a Flask endpoint.
## 4. Deployment and Testing
### 4.1 Deployment Process
The Flask application, along with the trained model, was deployed to Heroku. Heroku provided a way to deploy a webpage stored on a GitHub repository. A connection from Heroku to a personal GitHub repository was established using the Heroku web interface. Necessary configurations, including Procfile, requirements.txt, and runtime.txt, were then set up in the repository to facilitate the deployment process on Heroku's servers. 
### 4.2 Testing Methodology
Testing was conducted to ensure that the deployed application correctly receives user input, processes it, and returns the predicted digit. Various digits were drawn on the canvas and submitted for prediction.
### 4.3 Test Results and Observations
The application successfully predicted most of the handwritten digits. However, the accuracy was lower compared to the original test set, possibly due to differences in digit styles or issues with image preprocessing. More user’s personal digit styles are likely needed to improve the model for general use. 
## 5. Reflection
### 5.1 Challenges and Solutions
•	Model Size and Loading Time: The initial loading time was high due to the model's size. This was mitigated by optimizing the model and ensuring efficient loading in the Flask app by not loading the entire TensorFlow library.
•	Image Preprocessing: Ensuring the drawn image matched the MNIST format (28x28 grayscale) was challenging. This was resolved by implementing methods from the Pillow library. 
### 5.2 Lessons Learned
•	Importance of data preprocessing in model deployment.
•	What is required for a TensorFlow model to deploy on the web.
## 6. Conclusion
The project demonstrated the effective deployment of a TensorFlow CNN model using Heroku. It highlighted the importance of data preprocessing, model optimization, and the practical considerations of deploying machine learning models in a real-world application. Despite some challenges, the project was a valuable learning experience in applying machine learning models in practical scenarios.
