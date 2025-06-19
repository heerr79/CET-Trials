from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
        'name': user.get_full_name() or user.username,
    }
    return render(request, 'profile.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def subjects(request):
    # Your view logic goes here
    return render(request, 'subjects.html')

def syllabus(request):
    # Your view logic goes here
    return render(request, 'syllabus.html')

def about(request):
    # Your view logic goes here
    return render(request, 'about.html')

def pcm(request):
    # Your view logic goes here
    return render(request, 'pcm.html')

def pcb(request):
    # Your view logic goes here
    return render(request, 'pcb.html')

def pcmc1(request):
    # Your view logic goes here
    return render(request, 'pcmc1.html')

def pcmp1(request):
    # Your view logic goes here
    return render(request, 'pcmp1.html')

def result(request):
    correct = request.GET.get('correct', 0)  # Default to 0 if not provided
    wrong = request.GET.get('wrong', 0)  # Default to 0 if not provided
    context = {
        'correct': correct,
        'wrong': wrong,
    }
    # Your view logic goes here
    return render(request, 'result.html', context)

def result1(request):
    correct = request.GET.get('correct', 0)  # Default to 0 if not provided
    wrong = request.GET.get('wrong', 0)  # Default to 0 if not provided
    context = {
        'correct': correct,
        'wrong': wrong,
    }
    # Your view logic goes here
    return render(request, 'result1.html')

def result2(request):
    correct = request.GET.get('correct', 0)  # Default to 0 if not provided
    wrong = request.GET.get('wrong', 0)  # Default to 0 if not provided
    context = {
        'correct': correct,
        'wrong': wrong,
    }
    # Your view logic goes here
    return render(request, 'result2.html')

def instruction1(request):
    # Your view logic goes here
    return render(request, 'instruction1.html')

def instruction2(request):
    # Your view logic goes here
    return render(request, 'instruction2.html')

def pcmm1(request):
    # Your view logic goes here
    return render(request, 'pcmm1.html')

def pcbp1(request):
    # Your view logic goes here
    return render(request, 'pcbp1.html')

def resultp1(request):
    correct = request.GET.get('correct', 0)  # Default to 0 if not provided
    wrong = request.GET.get('wrong', 0)  # Default to 0 if not provided
    context = {
        'correct': correct,
        'wrong': wrong,
    }
    # Your view logic goes here
    return render(request, 'resultp1.html')

def pcbc1(request):
    # Your view logic goes here
    return render(request, 'pcbc1.html')

def resultc1(request):
    correct = request.GET.get('correct', 0)  # Default to 0 if not provided
    wrong = request.GET.get('wrong', 0)  # Default to 0 if not provided
    context = {
        'correct': correct,
        'wrong': wrong,
    }
    # Your view logic goes here
    return render(request, 'resultc1.html')

def pcbb1(request):
    # Your view logic goes here
    return render(request, 'pcbb1.html')

def resultb1(request):
    correct = request.GET.get('correct', 0)  # Default to 0 if not provided
    wrong = request.GET.get('wrong', 0)  # Default to 0 if not provided
    context = {
        'correct': correct,
        'wrong': wrong,
    }
    # Your view logic goes here
    return render(request, 'resultb1.html')

# AI Exam Generation Functions
def generate_questions_with_gemini(subject, difficulty, question_count, topics=None):
    """
    Generate questions based on MHTCET syllabus
    """
    
    # MHTCET Syllabus Topics
    syllabus_topics = {
        'physics': {
            'class11': [
                'Motion in a plane', 'Laws of motion', 'Thermal properties of matter', 
                'Sound', 'Optics', 'Electrostatics', 'Semiconductor'
            ],
            'class12': [
                'Circular motion', 'Rotational motion', 'Oscillations', 'Gravitation',
                'Elasticity', 'Electrostatics', 'Wave Motion', 'Magnetism',
                'Surface Tension', 'Wave Theory of Light', 'Stationary Waves',
                'Kinetic Theory of Gases and Radiation', 'Interference and Diffraction',
                'Current Electricity', 'Magnetic Effects of Electric Current',
                'Electromagnetic Inductions', 'Electrons and Photons',
                'Atoms, Molecules and Nuclei', 'Semiconductors', 'Communication Systems'
            ]
        },
        'chemistry': {
            'class11': [
                'Some basic concepts of Chemistry', 'Structure of atoms', 'Chemical bonding',
                'Redox reactions', 'Elements of groups 1 and 2', 'States of matter (Gaseous and Liquids)',
                'Adsorption and colloids (Surface Chemistry)', 'Hydrocarbons',
                'Basic principles of organic chemistry'
            ],
            'class12': [
                'Solid State', 'Chemical Thermodynamics and Energetic', 'Electrochemistry',
                'General Principles and Processes of Isolation', 'Solutions and Colligative Properties',
                'p-Block elements', 'Group 15 elements', 'd and f Block Elements',
                'Chemical Kinetics', 'Coordination Compounds', 'Halogen Derivatives of Alkanes (and arenes)',
                'Aldehydes, Ketones and Carboxylic Acids', 'Organic Compounds Containing Nitrogen',
                'Alcohols, Phenols and Ether Alcohol', 'Polymers', 'Chemistry in Everyday Life',
                'Biomolecules Carbohydrates'
            ]
        },
        'mathematics': {
            'class11': [
                'Trigonometry II', 'Straight lines', 'Circles', 'Measures of dispersion',
                'Probability', 'Complex numbers', 'Permutations and combinations',
                'Functions', 'Limits', 'Continuity'
            ],
            'class12': [
                'Mathematical Logic Statements', 'Matrices', 'Pair of Straight Lines',
                'Circle', 'Line', 'Conics', 'Trigonometric Functions', 'Vectors',
                'Three Dimensional Geometry', 'Plane', 'Linear Programming Problems',
                'Continuity', 'Applications of Derivatives', 'Integration',
                'Differentiation', 'Applications of Definite Integral',
                'Differential Equation', 'Probability Distribution', 'Statistics',
                'Bernoulli Trials and Binomial Distribution'
            ]
        },
        'biology': {
            'class11': [
                'Biomolecules', 'Respiration and energy transfer', 'Human Nutrition',
                'Excretion and osmoregulation'
            ],
            'class12': [
                'Origin and the Evolution of Life', 'Chromosomal Basis of Inheritance',
                'Genetic Engineering and Genomics', 'Human Health and Diseases',
                'Animal Husbandry', 'Circulation', 'Excretion and osmoregulation',
                'Control and Co-ordination', 'Human Reproduction', 'Organisms and Environment-II',
                'Genetic Basis of Inheritance', 'Gene its nature, expression, and regulation',
                'Biotechnology Process and Application', 'Enhancement in Food Production',
                'Microbes in Human Welfare', 'Photosynthesis', 'Respiration',
                'Reproduction in Plants', 'Organisms and Environment'
            ]
        }
    }
    
    # Subject mapping
    subjects_map = {
        'pcm': ['physics', 'chemistry', 'mathematics'],
        'pcb': ['physics', 'chemistry', 'biology']
    }
    
    subjects = subjects_map.get(subject, ['physics', 'chemistry', 'mathematics'])
    
    questions = []
    
    for i in range(int(question_count)):
        subject_name = random.choice(subjects)
        class_level = random.choice(['class11', 'class12'])
        topic = random.choice(syllabus_topics[subject_name][class_level])
        
        # Generate questions based on actual syllabus topics
        if subject_name == 'physics':
            if topic == 'Motion in a plane':
                question_text = f"In motion in a plane, what is the angle between velocity and acceleration vectors in uniform circular motion?"
                options = ["0°", "45°", "90°", "180°"]
                correct_answer = 2  # 90°
            elif topic == 'Laws of motion':
                question_text = f"According to Newton's third law of motion, if a body A exerts a force F on body B, then body B exerts:"
                options = ["No force on A", "Force F on A in the same direction", "Force F on A in the opposite direction", "Force 2F on A"]
                correct_answer = 2  # Force F on A in the opposite direction
            elif topic == 'Electrostatics':
                question_text = f"The electric field intensity at a point due to a point charge is:"
                options = ["Inversely proportional to distance", "Inversely proportional to square of distance", "Directly proportional to distance", "Directly proportional to square of distance"]
                correct_answer = 1  # Inversely proportional to square of distance
            elif topic == 'Current Electricity':
                question_text = f"The resistance of a wire is R. If its length is doubled and radius is halved, the new resistance will be:"
                options = ["R/2", "R", "2R", "4R"]
                correct_answer = 3  # 4R
            elif topic == 'Wave Motion':
                question_text = f"The speed of sound in air depends on:"
                options = ["Amplitude", "Frequency", "Temperature", "Wavelength"]
                correct_answer = 2  # Temperature
            else:
                question_text = f"Which of the following is related to {topic}?"
                options = [
                    f"Principle of {topic}",
                    f"Application of {topic}",
                    f"Formula for {topic}",
                    f"Unit of {topic}"
                ]
                correct_answer = random.randint(0, 3)
        
        elif subject_name == 'chemistry':
            if topic == 'Chemical bonding':
                question_text = f"In {topic}, which type of bond is formed by sharing of electrons?"
                options = ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"]
                correct_answer = 1  # Covalent bond
            elif topic == 'Redox reactions':
                question_text = f"In {topic}, oxidation involves:"
                options = ["Loss of electrons", "Gain of electrons", "Loss of protons", "Gain of protons"]
                correct_answer = 0  # Loss of electrons
            elif topic == 'Electrochemistry':
                question_text = f"In {topic}, the standard electrode potential is measured with respect to:"
                options = ["Zinc electrode", "Copper electrode", "Standard hydrogen electrode", "Calomel electrode"]
                correct_answer = 2  # Standard hydrogen electrode
            elif topic == 'Chemical Kinetics':
                question_text = f"In {topic}, the rate of reaction depends on:"
                options = ["Temperature only", "Concentration only", "Both temperature and concentration", "Neither temperature nor concentration"]
                correct_answer = 2  # Both temperature and concentration
            elif topic == 'Organic Compounds Containing Nitrogen':
                question_text = f"Which functional group is characteristic of {topic}?"
                options = ["-OH", "-NH₂", "-COOH", "-CHO"]
                correct_answer = 1  # -NH₂
            else:
                question_text = f"Which concept is fundamental to {topic}?"
                options = [
                    f"Atomic structure in {topic}",
                    f"Molecular interactions in {topic}",
                    f"Chemical equilibrium in {topic}",
                    f"Reaction mechanisms in {topic}"
                ]
                correct_answer = random.randint(0, 3)
        
        elif subject_name == 'mathematics':
            if topic == 'Trigonometry II':
                question_text = f"In {topic}, what is the value of sin²θ + cos²θ?"
                options = ["0", "1", "2", "sin(2θ)"]
                correct_answer = 1  # 1
            elif topic == 'Straight lines':
                question_text = f"In {topic}, the slope of a line perpendicular to y = 2x + 3 is:"
                options = ["2", "1/2", "-1/2", "-2"]
                correct_answer = 2  # -1/2
            elif topic == 'Integration':
                question_text = f"In {topic}, ∫x²dx equals:"
                options = ["x³/3 + C", "x²/2 + C", "x³ + C", "2x + C"]
                correct_answer = 0  # x³/3 + C
            elif topic == 'Probability':
                question_text = f"In {topic}, the probability of an impossible event is:"
                options = ["0", "1", "0.5", "Undefined"]
                correct_answer = 0  # 0
            elif topic == 'Matrices':
                question_text = f"In {topic}, the determinant of a 2×2 matrix [a b; c d] is:"
                options = ["ad + bc", "ad - bc", "ab + cd", "ab - cd"]
                correct_answer = 1  # ad - bc
            else:
                question_text = f"Which mathematical concept is essential in {topic}?"
                options = [
                    f"Algebraic methods in {topic}",
                    f"Geometric principles in {topic}",
                    f"Analytical techniques in {topic}",
                    f"Computational methods in {topic}"
                ]
                correct_answer = random.randint(0, 3)
        
        else:  # biology
            if topic == 'Biomolecules':
                question_text = f"In {topic}, which is the most abundant organic compound in living cells?"
                options = ["Proteins", "Carbohydrates", "Lipids", "Nucleic acids"]
                correct_answer = 1  # Carbohydrates
            elif topic == 'Human Reproduction':
                question_text = f"In {topic}, fertilization typically occurs in:"
                options = ["Ovary", "Uterus", "Fallopian tube", "Vagina"]
                correct_answer = 2  # Fallopian tube
            elif topic == 'Photosynthesis':
                question_text = f"In {topic}, the light reaction occurs in:"
                options = ["Stroma", "Thylakoid membrane", "Mitochondria", "Cytoplasm"]
                correct_answer = 1  # Thylakoid membrane
            elif topic == 'Genetic Engineering and Genomics':
                question_text = f"In {topic}, restriction enzymes are used to:"
                options = ["Cut DNA at specific sites", "Join DNA fragments", "Amplify DNA", "Sequence DNA"]
                correct_answer = 0  # Cut DNA at specific sites
            elif topic == 'Human Health and Diseases':
                question_text = f"In {topic}, which is a vector-borne disease?"
                options = ["Tuberculosis", "Malaria", "Diabetes", "Hypertension"]
                correct_answer = 1  # Malaria
            else:
                question_text = f"Which biological process is central to {topic}?"
                options = [
                    f"Cellular processes in {topic}",
                    f"Molecular mechanisms in {topic}",
                    f"Organismal interactions in {topic}",
                    f"Evolutionary aspects of {topic}"
                ]
                correct_answer = random.randint(0, 3)
        
        # Shuffle options while keeping track of correct answer
        correct_option = options[correct_answer]
        random.shuffle(options)
        new_correct_index = options.index(correct_option)
        
        questions.append({
            'id': i + 1,
            'question': question_text,
            'options': options,
            'correct_answer': new_correct_index,
            'subject': subject_name.title(),
            'difficulty': difficulty,
            'topic': topic,
            'class_level': class_level
        })
    
    return questions

@login_required(login_url='login')
def generate_ai_exam(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        difficulty = request.POST.get('difficulty')
        question_count = request.POST.get('question_count')
        time_limit = request.POST.get('time_limit')
        topics = request.POST.get('topics', '')
        
        # Generate questions using Gemini API (mock implementation)
        questions = generate_questions_with_gemini(subject, difficulty, question_count, topics)
        
        # Store exam data in session for now (in production, use database)
        exam_data = {
            'id': random.randint(1000, 9999),
            'subject': subject,
            'difficulty': difficulty,
            'question_count': question_count,
            'time_limit': time_limit,
            'topics': topics,
            'questions': questions,
            'created_at': datetime.now().isoformat(),
            'status': 'active'
        }
        
        request.session['current_exam'] = exam_data
        
        return redirect('take_ai_exam', exam_id=exam_data['id'])
    
    return redirect('subjects')

@login_required(login_url='login')
def take_ai_exam(request, exam_id):
    exam_data = request.session.get('current_exam')
    
    if not exam_data or exam_data['id'] != exam_id:
        return redirect('subjects')
    
    context = {
        'exam': exam_data,
        'questions': exam_data['questions']
    }
    
    return render(request, 'ai_exam.html', context)

@login_required(login_url='login')
def start_practice(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        topic = request.POST.get('topic')
        question_count = request.POST.get('question_count')
        
        # Generate practice questions
        questions = generate_questions_with_gemini('pcm' if subject in ['physics', 'chemistry', 'mathematics'] else 'pcb', 'medium', question_count, topic)
        
        # Filter questions by subject
        filtered_questions = [q for q in questions if q['subject'].lower() == subject.lower()]
        
        # Store practice session data
        session_data = {
            'id': random.randint(1000, 9999),
            'subject': subject,
            'topic': topic,
            'question_count': question_count,
            'questions': filtered_questions,
            'created_at': datetime.now().isoformat(),
            'mode': 'practice'
        }
        
        request.session['current_practice'] = session_data
        
        return redirect('practice_session', session_id=session_data['id'])
    
    return redirect('subjects')

@login_required(login_url='login')
def practice_session(request, session_id):
    session_data = request.session.get('current_practice')
    
    if not session_data or session_data['id'] != session_id:
        return redirect('subjects')
    
    context = {
        'session': session_data,
        'questions': session_data['questions']
    }
    
    return render(request, 'practice_session.html', context)
