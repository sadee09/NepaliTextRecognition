# Nepali Text Recognition Chatbot

A Flask-based web application that provides an intelligent chatbot interface for Kathmandu Engineering College (KEC). The chatbot uses deep learning (TensorFlow/Keras) to understand and respond to user queries in Nepali language, providing information about the college, programs, faculty, admission procedures, and more.

## Features

- **Nepali Language Support**: Understands and responds to queries in Nepali language
- **Interactive Web Interface**: Modern, user-friendly chat interface
- **Deep Learning Model**: Uses TensorFlow/Keras neural network for intent classification
- **College Information**: Provides comprehensive information about:
  - College location and contact details
  - Academic programs and departments
  - Faculty information
  - Admission requirements and procedures
  - Fee structure and scholarship schemes
  - Extracurricular activities and clubs
  - Hostel facilities

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: TensorFlow/Keras
- **NLP**: Tokenization and sequence padding, NLTK
- **Data Processing**: NumPy, pandas, scikit-learn (LabelEncoder)
- **Visualization**: Matplotlib (for model development)
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **Data Storage**: JSON files for responses and college data

## Project Structure

```
NepaliTextRecognition/
├── app.py                          # Main Flask application
├── templates/
│   └── chat.html                   # Chat interface template
├── static/
│   ├── style.css                   # Styling for the chat interface
│   ├── kec.jpg                     # College logo/avatar
│   └── user.jpg                    # User avatar
├── chat_model_final/               # Trained TensorFlow model (final version)
├── tokenizer_final.pickle          # Text tokenizer for preprocessing
├── label_encoder_final.pickle      # Label encoder for intent classification
├── updated_response_data.json      # Response data for different intents
├── updated_college_data.json       # College information data
├── Chatbot.ipynb                   # Jupyter notebook for model training/development
├── Chatbot_v2.ipynb                # Alternative model version
└── kec_model.ipynb                 # KEC-specific model notebook
```


## Configuration

Before running the application, update the file paths in `app.py` to match your system:

```python
DATA_PATH = 'path/to/updated_response_data.json'
MODEL_PATH = 'path/to/chat_model_final'
TOKENIZER_PATH = 'path/to/tokenizer_final.pickle'
LABEL_ENCODER_PATH = 'path/to/label_encoder_final.pickle'
```

**Note**: Currently, the paths in `app.py` are set to absolute paths. Update them to relative paths or your local paths.

## Usage

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Start chatting**: Type your questions in Nepali or English, and the chatbot will respond with relevant information about KEC.

## How It Works

1. **User Input**: The user types a message in the chat interface
2. **Preprocessing**: The input text is tokenized and padded to a fixed length (MAX_LEN = 20)
3. **Prediction**: The trained neural network model predicts the intent class
4. **Response Selection**: If confidence is above 0.7, the corresponding response is retrieved from the response data
5. **Error Handling**: If confidence is below 0.7, an error message is returned asking the user to rephrase

## Model Details

- **Architecture**: Deep learning model using TensorFlow/Keras
- **Input**: Tokenized and padded text sequences (max length: 20)
- **Output**: Intent classification with confidence threshold of 0.7
- **Training**: Model was trained on Nepali text data for college-related queries

## Development

The project includes Jupyter notebooks for model development and experimentation:
- `Chatbot.ipynb`: Initial model development
- `Chatbot_v2.ipynb`: Improved model version
- `kec_model.ipynb`: KEC-specific model training

