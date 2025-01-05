import spacy
import random

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Important terms (NEET topics)
important_terms = ['photosynthesis', 'mitosis', 'chlorophyll', 'neuron', 'ATP', 'enzyme', 'nucleus', 'sodium', 'potassium', 'lactic acid']

# Function to generate MCQs (Multiple Choice Questions)
def generate_mcq(chunk):
    # Process chunk using spaCy NLP
    doc = nlp(" ".join(chunk))

    # Filter key terms based on NEET topics
    key_terms = [token.text for token in doc if token.text.lower() in important_terms]
    mcq_questions = []

    for key_term in key_terms:
        # Generate question
        question_text = f"What is the primary function of {key_term}?"

        # Generate unambiguous distractors
        distractors = [
            term for term in important_terms 
            if term != key_term and not is_related(key_term, term)
        ]
        random.shuffle(distractors)

        # Ensure there are enough distractors
        if len(distractors) < 3:
            continue  # Skip this question if not enough distractors

        # Prepare MCQ
        options = [key_term] + distractors[:3]
        random.shuffle(options)
        mcq_question = {
            "type": "Multiple Choice",
            "question": question_text,
            "options": options,
            "answer": key_term
        }
        mcq_questions.append(mcq_question)

    return mcq_questions

def is_related(term1, term2):
    """Check if two terms are closely related."""
    # Example logic: Assume related terms are those that co-occur in scientific contexts
    # You can use a semantic similarity function or a predefined relationship dictionary
    related_pairs = [
        ("photosynthesis", "chlorophyll"), 
        ("neuron", "sodium"), 
        ("enzyme", "ATP")
    ]
    return (term1, term2) in related_pairs or (term2, term1) in related_pairs

def generate_neet_mcqs(text):
    # Split text into chunks of 5 to 10 words
    words = text.split()
    chunks = [words[i:i+10] for i in range(0, len(words), 10)]

    all_mcqs = []
    for chunk in chunks:
        if len(chunk) < 5:
            continue
        mcqs = generate_mcq(chunk)
        all_mcqs.extend(mcqs)

    return all_mcqs
