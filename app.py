from flask import Flask, jsonify, request
import question_logic
import random

app = Flask(__name__)

# Route to generate assertion and reason questions
@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    data = request.get_json()  # Get data from POST request
    text = data.get('text', '')
    
    # Validate if text is provided
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Generate questions from text
    questions = question_logic.generate_neet_assertion_reason_questions(text)
    
    return jsonify({'questions': questions}), 200


if __name__ == '__main__':
    app.run(debug=True)
