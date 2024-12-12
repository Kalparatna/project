from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import google.generativeai as genai
from django.conf import settings
from dotenv import load_dotenv
import os
import time
from django.urls import reverse

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MCQ_STORAGE = {}

def generate_mcqs(topic, num_questions, retries=3):
    prompt = (
        f"Generate {num_questions} multiple-choice questions (MCQs) on the topic '{topic}'. "
        "Each question should have four options, with one correct answer, formatted as follows:\n"
        "{\n"
        "  \"questions\": [\n"
        "    {\n"
        "      \"question\": \"Question text\",\n"
        "      \"options\": [\"Option 1\", \"Option 2\", \"Option 3\", \"Option 4\"],\n"
        "      \"correct_answer\": \"Option 1\"\n"
        "    }\n"
        "  ]\n"
        "}."
    )
    
    model = genai.GenerativeModel('gemini-pro')
    
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            mcqs = json.loads(response.text)
            return mcqs['questions']
        
        except json.JSONDecodeError as e:
            print("Error parsing JSON response:", e)
        
        except Exception as e:
            print("An error occurred:", e)

        time.sleep(2)
    
    return None

def quiz_home(request):
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        return render(request, 'error.html', {"error": "API key not configured correctly."})

    if request.method == 'POST':
        topic = request.POST.get('topic')
        num_questions = int(request.POST.get('num_questions')) 

        if topic:
            questions = generate_mcqs(topic, num_questions)
            if not questions:
                return render(request, 'error.html', {"error": "Failed to generate MCQs."})

            print("Generated Questions:", questions)

            topic_id = len(MCQ_STORAGE) + 1
            MCQ_STORAGE[topic_id] = {
                "topic": topic,
                "questions": questions,
            }

            messages.success(request, 'MCQs generated successfully! Now take the quiz.')
            return redirect(reverse('quiz_start', args=[topic_id]))
            
    return render(request, 'index.html')

def quiz_start(request, topic_id):
    topic_id = int(topic_id)
    topic_data = MCQ_STORAGE.get(topic_id)
    if not topic_data:
        return render(request, 'error.html', {"error": "Topic not found."})
    return render(request, 'start_quiz.html', {'topic': topic_data['topic'], 'topic_id': topic_id})

def take_quiz(request, topic_id):
    topic_id = int(topic_id)
    topic_data = MCQ_STORAGE.get(topic_id)
    if not topic_data:
        return render(request, 'error.html', {"error": "Topic not found."})

    questions = topic_data["questions"]

    if request.method == 'POST':
        score = 0
        total_questions = len(questions)

        for index, question in enumerate(questions, start=1):
            selected_answer = request.POST.get(f'mcq_{index}')
            if selected_answer == question["correct_answer"]:
                score += 1

        messages.success(request, f'You scored {score} out of {total_questions}!')
        return render(request, 'quiz_results.html', {
            'topic': topic_data['topic'],
            'questions': questions,
            'score': score,
            'total_questions': total_questions
        })
    
    return render(request, 'quiz_form.html', {
        'topic': topic_data['topic'],
        'questions': questions,
        'topic_id': topic_id,
    })
