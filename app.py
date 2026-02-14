"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app)

quotes = [
    "Every day is a fresh start.",
    "You are stronger than you think.",
    "Small steps every day lead to big changes.",
    "Your feelings are valid. Keep going.",
    "Breathe. You are doing the best you can."
]

responses = {
    "greeting": [
        "Hello! I'm here to listen. How are you feeling today?",
        "Hi, I’m glad you reached out. What’s on your mind?",
        "Hey there. How are you doing emotionally right now?"
    ],
    "sad": [
        "I’m sorry you’re feeling down. Want to talk about what’s troubling you?",
        "It’s okay to feel sad sometimes. You’re not alone.",
        "Your feelings are valid. Do you want to share what’s been happening?"
    ],
    "anxious": [
        "Anxiety can feel overwhelming. Let’s try a breathing exercise: Inhale for 4, hold for 4, exhale for 6. Repeat 3 times.",
        "It’s normal to feel anxious. Would you like me to suggest some calming activities?",
        "Try grounding: Look around and name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste."
    ],
    "happy": [
        "That’s wonderful to hear! What’s been going well?",
        "I’m glad you’re feeling good. Celebrate the small wins!",
        "That’s awesome! Want to share what’s making you happy today?"
    ],
    "crisis": [
        "⚠️ I hear that you're going through a very tough time. If you are thinking about suicide, please reach out to a trusted person immediately.",
        "You are not alone. If you are in India, you can call Vandrevala Foundation Helpline: 1860 2662 345 / 1800 2333 330.",
        "If you are elsewhere, please look up your local crisis hotline. You deserve help and care."
    ],
    "breathing": [
        "Let's try a simple breathing exercise: Inhale 4 sec, hold 4 sec, exhale 6 sec. Repeat 3 times.",
        "Take a deep breath in, hold for 4 seconds, and exhale slowly. Repeat this a few times."
    ],
    "meditation": [
        "Try a 5-minute meditation: Sit comfortably, close your eyes, focus on your breath, and let thoughts pass.",
        "Find a quiet place and meditate for a few minutes. Focus on your breathing and relax."
    ],
    "default": [
        "I’m here to listen. Can you tell me more?",
        "That sounds important. Would you like to share more about it?",
        "I understand. I’m here with you."
    ]
}

def classify_message(msg):
    text = msg.lower()
    if re.search(r"\b(hello|hi|hey)\b", text):
        return "greeting"
    elif re.search(r"\b(sad|depressed|down|unhappy)\b", text):
        return "sad"
    elif re.search(r"\b(anxious|nervous|worried|stress)\b", text):
        return "anxious"
    elif re.search(r"\b(happy|good|great|fine)\b", text):
        return "happy"
    elif re.search(r"\b(suicide|end life|kill myself)\b", text):
        return "crisis"
    elif re.search(r"\b(breathing|exercise)\b", text):
        return "breathing"
    elif re.search(r"\b(meditation)\b", text):
        return "meditation"
    elif re.search(r"\b(quote|motivate)\b", text):
        return "quote"
    else:
        return "default"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    if not user_msg.strip():
        return jsonify({"response": "I didn’t catch that. Could you type something?"})

    category = classify_message(user_msg)
    if category == "quote":
        bot_response = random.choice(quotes)
    elif category == "crisis":
        bot_response = " ".join(responses["crisis"])
    else:
        bot_response = random.choice(responses[category])

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app)

# Motivational quotes
quotes = [
    "Every day is a fresh start.",
    "You are stronger than you think.",
    "Small steps every day lead to big changes.",
    "Your feelings are valid. Keep going.",
    "Breathe. You are doing the best you can.",
    "How are you feeling today? Remember, it's okay to not be okay.",
    "Take care of yourself, you deserve peace.",
    "Life isn’t about waiting for the storm to pass, but learning to dance in the rain.",
    "Be proud of how far you’ve come, even if it’s just a small step.",
    "Progress, not perfection, is what matters.",
    "You don’t need to have it all figured out to move forward.",
    "Happiness is found in small moments, cherish them.",
    "You’re not behind in life; you’re on your own unique timeline.",
    "It’s okay to rest. Rest is productive too.",
    "Your voice matters, your feelings matter, YOU matter.",
    "Sometimes the bravest thing you can do is ask for help.",
    "You’ve survived 100% of your worst days. That’s strength.",
    "Don’t compare your journey to others; your path is yours.",
    "Healing isn’t linear, and that’s perfectly okay.",
    "The fact that you’re here means you’re already fighting.",
    "Keep going. Better days are ahead.",
    "Every sunset brings the promise of a new sunrise.",
    "You are not alone. Someone cares about you.",
    "Even the smallest light shines in the darkest night."
]

# --- Responses for categories ---
responses = {
    # --- Mental health (75 approx) ---
    "greeting": ["Hello! How are you feeling today?", "Hi, I’m here to listen.", "Hey there, what’s on your mind?"],
    "sad": ["I’m sorry you’re feeling this way. Want to share more?", "Sadness is natural. You’re not alone."],
    "anxious": ["Let’s do a breathing exercise: Inhale 4, hold 4, exhale 6.", "Anxiety passes. Try grounding with your senses."],
    "happy": ["That’s amazing! What’s making you happy today?", "Happiness is worth celebrating!"],
    "crisis": [
        "⚠️ Please reach out to a trusted person if you’re thinking about suicide.",
        "If you are in India, call Vandrevala Helpline: 1860 2662 345 / 1800 2333 330."
    ],
    "breathing": ["Let’s do a calm breath: Inhale 4 sec, exhale 6 sec.", "Deep breaths help slow stress."],
    "meditation": ["Sit quietly, close eyes, breathe slowly.", "Focus on the present moment and relax."],
    "therapy": ["Therapy is a safe way to process feelings.", "Talking to a professional can help."],
    "lonely": ["Loneliness is tough. Would you like to share more?", "You are not truly alone, I’m here with you."],
    "selfcare": ["Try journaling, rest, or a hobby for self-care.", "Self-care is important. What helps you relax?"],
    "burnout": ["Take breaks. Burnout is a sign to rest.", "Balance matters—don’t overpush yourself."],
    "gratitude": ["Can you list 3 things you’re grateful for?", "Gratitude boosts positivity."],
    "anger": ["It’s okay to feel angry. Want to talk it out?", "Try deep breaths when anger rises."],
    "overthinking": ["Your mind is busy. Try writing your thoughts down.", "Focus on one step at a time."],
    "insomnia": ["Good sleep hygiene helps. Want me to share tips?", "Try calming routines before bed."],
    "confidence": ["Believe in yourself. You’re capable.", "Small wins build confidence."],
    "motivation": ["Motivation comes and goes, but discipline helps.", "You can do this. Start small."],
    "fear": ["Fear is natural. Facing it slowly helps.", "Would you like a calming technique for fear?"],
    "mindfulness": ["Be present: notice your breath, your senses.", "Mindfulness is about awareness, not control."],
    "relapse": ["Relapse doesn’t mean failure. It’s part of recovery.", "Be kind to yourself during setbacks."],
    "healing": ["Healing takes time. You’re making progress.", "Be patient with your journey."],
    "resilience": ["You’ve overcome before, you can again.", "Resilience grows with practice."],
    "relationships": ["Relationships affect our emotions deeply. Want to talk about it?", "It’s okay to set boundaries."],
    "stress": ["Stress is heavy. Try breaks and deep breaths.", "Managing stress in small steps helps."],
    "forgiveness": ["Forgiving doesn’t mean forgetting, it means peace.", "Forgiveness helps you, not just others."],
    "shame": ["Shame is heavy. You are worthy of kindness.", "Talk about it—it helps lighten shame."],
    "guilt": ["We all make mistakes. Learn and move forward.", "Don’t carry guilt forever—it hurts growth."],
    "hope": ["Hope can carry you forward. What gives you hope?", "Even in hard times, hope is real."],
    "patience": ["Patience takes practice. Go step by step.", "Slow progress is still progress."],
    "support": ["Support systems matter. Who do you lean on?", "You deserve support and care."],

    # --- General topics (25) ---
    "weather": ["How’s the weather around you?", "Weather can affect mood. Sunny or rainy?"],
    "sports": ["Sports are fun! Do you follow any?", "Physical activity boosts mood too."],
    "food": ["Food can be comforting. What’s your favorite dish?", "Cooking can be therapeutic."],
    "tech": ["Tech is growing fast! Any gadget you like?", "AI and apps can help with mindfulness too."],
    "news": ["News can be overwhelming. Want to discuss?", "Stay updated, but don’t overload yourself."],
    "music": ["Music heals. What songs help your mood?", "Do you enjoy calming music?"],
    "movies": ["Movies can be relaxing. Any favorites?", "Storytelling helps us escape reality."],
    "travel": ["Travel refreshes the mind. Dream destinations?", "Even short trips can recharge you."],
    "books": ["Books are powerful. Do you enjoy reading?", "Fiction or self-help—both inspire."],
    "hobbies": ["Hobbies give balance. What do you enjoy?", "Creative outlets reduce stress."],

    # --- Extra 50 everyday categories ---
    "study": ["Studying can be stressful. Want tips?", "Take breaks while studying."],
    "exam": ["Exams bring pressure. You’ll do fine!", "Study smart, not just long."],
    "career": ["Career choices are stressful. Want advice?", "It’s okay to explore different paths."],
    "work": ["Work can be draining. Balance matters.", "Don’t forget rest while working."],
    "money": ["Money worries are valid. Budgeting helps.", "Would you like finance stress tips?"],
    "family": ["Family can be supportive but stressful too.", "Want to talk about family matters?"],
    "friendship": ["Friendships shape us. Cherish good ones.", "Tough friendships can drain energy."],
    "school": ["School life is busy. How’s yours?", "Balance school and rest too."],
    "college": ["College is exciting but stressful.", "Want to talk about college life?"],
    "future": ["The future feels uncertain. Step by step helps.", "It’s okay not to have it figured out."],
    "dreams": ["Dreams inspire us. What’s yours?", "Dreams motivate action."],
    "routine": ["Routine creates stability.", "Healthy routines reduce anxiety."],
    "exercise": ["Exercise lifts mood. Do you workout?", "Even walks count as exercise."],
    "pets": ["Pets bring comfort. Do you have one?", "Animals reduce stress too."],
    "nature": ["Nature heals. Have you been outside today?", "Green spaces calm the mind."],
    "art": ["Art is expression. Do you draw or paint?", "Creativity is therapy."],
    "goals": ["Set small goals—they add up.", "What’s one goal you’re working on?"],
    "health": ["Health is wealth. Are you feeling okay?", "Both mental and physical health matter."],
    "time": ["Time feels fast. How do you manage it?", "Time management reduces stress."],
    "internet": ["The internet connects us. How do you use it?", "Take breaks from screens too."],
    "gaming": ["Gaming is fun. Do you play?", "Games can reduce stress, but balance helps."],
    "science": ["Science is fascinating! Any topic you like?", "Curiosity keeps the mind sharp."],
    "space": ["Space is inspiring! Do you like astronomy?", "The universe is vast and beautiful."],
    "philosophy": ["Philosophy makes us think. Do you like it?", "Deep thoughts help perspective."],
    "language": ["Languages connect people. Do you learn any?", "Words shape our thoughts."],
    "culture": ["Culture is rich. Which one inspires you?", "Traditions give belonging."],
    "history": ["History teaches lessons. Any favorite era?", "Learning the past helps the future."],
    "fashion": ["Fashion expresses personality. What’s your style?", "Dressing up can lift mood."],
    "shopping": ["Shopping can be fun! Do you enjoy it?", "Be mindful while spending."],
    "economy": ["The economy affects us all.", "Want to discuss money topics?"],
    "environment": ["The environment needs care. Do you recycle?", "Nature gives us balance."],
    "politics": ["Politics is complex. Want to discuss calmly?", "Different views exist, let’s respect them."],
    "festival": ["Festivals bring joy. Do you celebrate any?", "Traditions connect people."],
    "weekend": ["Weekends are for rest! Plans?", "How do you relax on weekends?"],
    "morning": ["Good morning! How did you sleep?", "Mornings bring new starts."],
    "night": ["Good night! Rest well.", "Sleep is essential for health."],
    "birthday": ["Happy Birthday! Celebrate yourself!", "Birthdays are special days."],
    "holiday": ["Holidays refresh us. Any plans?", "Take time to recharge."],
    "workout": ["Workouts energize. Do you exercise often?", "Fitness helps the mind."],
    "coffee": ["Coffee boosts mornings. Do you like it?", "Tea or coffee—your pick?"],
    "tea": ["Tea calms the mind.", "Do you prefer herbal tea?"],
    "water": ["Stay hydrated. Did you drink water today?", "Water supports brain function."],
    "sleep": ["Sleep restores energy. Did you rest well?", "Good sleep improves mood."],
    "celebration": ["Celebrations lift spirits. Any recent one?", "Enjoy small celebrations too."],
    "love": ["Love heals. Do you want to talk about relationships?", "Love can be both joy and pain."],
    "dating": ["Dating is exciting but confusing.", "Want to talk about dating experiences?"],
    "marriage": ["Marriage changes life. Any thoughts?", "Healthy communication is key."],
    "children": ["Children bring joy but responsibility.", "Parenting is a journey."],
    "aging": ["Aging is natural. Wisdom grows.", "Every age has beauty."],
    "death": ["Death is hard to cope with.", "Grief takes time—be kind to yourself."],

     # --- General Knowledge / Tech / AI / Internet ---
    "ai": [
        "AI stands for Artificial Intelligence—it simulates human intelligence in machines.",
        "AI is used in chatbots, healthcare, self-driving cars, and more."
    ],
    "machine_learning": [
        "Machine Learning is a branch of AI that learns from data.",
        "ML powers recommendations, image recognition, and predictions."
    ],
    "cybersecurity": [
        "Cybersecurity protects systems and data from attacks.",
        "Strong passwords, 2FA, and awareness keep you safe online."
    ],
    "internet": [
        "The internet connects people worldwide through networks.",
        "Be mindful of screen time—balance is key."
    ],
    "social_media": [
        "Social media connects us, but too much can affect mental health.",
        "It’s okay to take breaks from social platforms."
    ],
    "blockchain": [
        "Blockchain is a secure way of recording transactions.",
        "It powers cryptocurrencies like Bitcoin and Ethereum."
    ],
    "cloud": [
        "Cloud computing lets you store data and run apps online.",
        "Examples: Google Drive, AWS, Microsoft Azure."
    ],
    "gk_science": [
        "The Earth revolves around the Sun in 365 days.",
        "Water covers about 71% of Earth’s surface."
    ],
    "gk_space": [
        "The Milky Way is our galaxy.",
        "The Moon affects tides on Earth."
    ],
    "gk_history": [
        "Mahatma Gandhi led India’s independence movement.",
        "The printing press was invented by Johannes Gutenberg."
    ],
    "gk_geography": [
        "Mount Everest is the highest mountain in the world.",
        "The Amazon is the largest rainforest on Earth."
    ],
    #--emotional states------
    "guilt": [
    "Guilt can feel heavy. Talking about it helps.",
    "Remember, mistakes don’t define you.",
    "Forgiveness—especially self-forgiveness—takes time."],
     
     "shame" : [
    "Shame is hard, but you are more than your mistakes.",
    "You deserve compassion, not shame.",
    "Talking about shame can help it lose power."],
     
     "confusion": [
    "It’s okay to feel confused. Let’s slow things down.",
    "Confusion is the first step to clarity.",
    "Would you like to talk through what’s confusing you?"
],  

     "loneliness" : [
    "Loneliness feels painful, but you’re not truly alone., i am with you.",
    "I hear you. Connection matters—want me to suggest ways?, i am with you.",
    "Reaching out to even one person can ease loneliness, i am with you."
],  
     "frustration": [
    "Frustration is normal. Let’s take a pause and reset.",
    "You’re doing your best—progress takes time.",
    "Try a deep breath before continuing."
],  
     "jealousy": [
    "Jealousy can be tough, but it shows what you value.",
    "Instead of comparing, focus on your own path.",
    "It’s okay to admit jealousy—it’s human."
], 
     "hopefulness" : [
    "Hope can give strength in tough times.",
    "Even small hopes matter—what’s giving you hope today?",
    "Hope grows when you focus on little wins."
],
    "resilience": [
    "You’ve overcome challenges before—you’re strong.",
    "Resilience grows every time you keep going.",
    "Even small steps forward show great strength."
],    
    "love": [
    "Love is powerful—cherish it.",
    "You deserve love and kindness.",
    "Affection can heal deep wounds."
],  
     "regret":  [
    "Regret is tough, but it also teaches lessons.",
    "You can’t change the past, but you can change today.",
    "Be kind to yourself—you did the best you could then."
],
    "greeting": [
        "Hello! How are you feeling today?",
        "Hi, I’m here to listen.",
        "Hey there, what’s on your mind?"
    ],
    "happy": [
        "That’s amazing! What’s making you happy today?",
        "Happiness is worth celebrating!"
    ],
    "sad": [
        "I’m sorry you’re feeling this way. Want to share more?",
        "Sadness is natural. You’re not alone."
    ],
    "anxiety": [
        "Let’s do a breathing exercise: Inhale 4, hold 4, exhale 6.",
        "Anxiety passes. Try grounding with your senses."
    ],
    "crisis": [
        "⚠️ Please reach out to a trusted person if you’re thinking about suicide.",
        "If you are in India, call Vandrevala Helpline: 1860 2662 345 / 1800 2333 330."
    ],
    "guilt": [
        "Guilt can feel heavy. Talking about it helps.",
        "Remember, mistakes don’t define you.",
        "Forgiveness—especially self-forgiveness—takes time."
    ],
    "shame": [
        "Shame is hard, but you are more than your mistakes.",
        "You deserve compassion, not shame.",
        "Talking about shame can help it lose power."
    ],
    "confusion": [
        "It’s okay to feel confused. Let’s slow things down.",
        "Confusion is the first step to clarity.",
        "Would you like to talk through what’s confusing you?"
    ],
    "loneliness": [
        "Loneliness feels painful, but you’re not truly alone.",
        "I hear you. Connection matters—want me to suggest ways?",
        "Reaching out to even one person can ease loneliness."
    ],
    "frustration": [
        "Frustration is normal. Let’s take a pause and reset.",
        "You’re doing your best—progress takes time.",
        "Try a deep breath before continuing."
    ],
    "jealousy": [
        "Jealousy can be tough, but it shows what you value.",
        "Instead of comparing, focus on your own path.",
        "It’s okay to admit jealousy—it’s human."
    ],
    "hopefulness": [
        "Hope can give strength in tough times.",
        "Even small hopes matter—what’s giving you hope today?",
        "Hope grows when you focus on little wins."
    ],
    "resilience": [
        "You’ve overcome challenges before—you’re strong.",
        "Resilience grows every time you keep going.",
        "Even small steps forward show great strength."
    ],
    "love": [
        "Love is powerful—cherish it.",
        "You deserve love and kindness.",
        "Affection can heal deep wounds."
    ],
    "regret": [
        "Regret is tough, but it also teaches lessons.",
        "You can’t change the past, but you can change today.",
        "Be kind to yourself—you did the best you could then."
    ],
    "bored": [
        "Feeling bored happens. Want some ideas to pass time?",
        "Maybe try a hobby or listen to music."
    ],
    "relief": [
        "I’m glad you feel relieved. What helped?",
        "Relief is like a deep breath for your mind."
    ],
    "excitement": [
        "Exciting times! What’s making you feel thrilled?",
        "I love your energy! Share more if you like."
    ],
    "anger": [
        "Anger is natural. Want to talk it out?",
        "Try deep breaths when anger rises.",
        "Sometimes writing down feelings helps."
    ],
    "fear": [
        "Fear is natural. Facing it slowly helps.",
        "Would you like a calming technique for fear?"
    ],
    "disgust": [
        "Disgust is a valid feeling. Want to share why?",
        "Understanding the cause can help process it."
    ],
    "surprise": [
        "Surprise! That can be exciting or unsettling.",
        "Do you want to share what surprised you?"
    ],
    "gratitude": [
        "Can you list 3 things you’re grateful for?",
        "Gratitude boosts positivity."
    ],
    "confidence": [
        "Believe in yourself. You’re capable.",
        "Small wins build confidence."
    ],
    "motivation": [
        "Motivation comes and goes, but discipline helps.",
        "You can do this. Start small."
    ],
    "mindfulness": [
        "Be present: notice your breath, your senses.",
        "Mindfulness is about awareness, not control."
    ],
    "overthinking": [
        "Your mind is busy. Try writing your thoughts down.",
        "Focus on one step at a time."
    ],
    "insomnia": [
        "Good sleep hygiene helps. Want me to share tips?",
        "Try calming routines before bed."
    ],
    "selfcare": [
        "Try journaling, rest, or a hobby for self-care.",
        "Self-care is important. What helps you relax?"
    ],
    "burnout": [
        "Take breaks. Burnout is a sign to rest.",
        "Balance matters—don’t overpush yourself."
    ],
    "patience": [
        "Patience takes practice. Go step by step.",
        "Slow progress is still progress."
    ],
    "support": [
        "Support systems matter. Who do you lean on?",
        "You deserve support and care."
    ],
    "hope": [
        "Hope can carry you forward. What gives you hope?",
        "Even in hard times, hope is real."
    ],
    "curiosity": [
        "Curiosity keeps the mind sharp.",
        "Exploring new things is always valuable."
    ],
    "embarrassment": [
        "Embarrassment is normal. Don’t be too hard on yourself.",
        "We all feel embarrassed sometimes."
    ],
    "pride": [
        "Be proud of your achievements, no matter how small.",
        "Celebrating yourself is healthy and important."
    ],
    "jealousy": [
        "Jealousy shows what you value. Let’s explore it gently.",
        "Comparisons don’t define you."
    ],
    "nostalgia": [
        "Nostalgia can be bittersweet. Want to share a memory?",
        "Remembering good times can lift your spirits."
    ],
    "sadness": [
        "It’s okay to feel sad. Talk if you want.",
        "Sadness doesn’t last forever."
    ],
    "lonely": [
        "Feeling lonely is tough. Reaching out helps.",
        "Connection matters. Let’s think of one person you trust."
    ],
    "disappointment": [
        "Disappointments happen. Want to talk about it?",
        "It’s normal to feel upset when things don’t go as expected."
    ],
    "relaxation": [
        "Relaxation is important. Try taking a few deep breaths.",
        "Even a short break can refresh your mind."
    ],
    "peace": [
        "Peace comes from within. Focus on your breath.",
        "Moments of calm are valuable."
    ],
    "optimism": [
        "Optimism helps see the bright side.",
        "Focus on small positive moments today."
    ],
    "pessimism": [
        "It’s okay to feel down sometimes. Thoughts can be adjusted gently.",
        "Even small positive actions can help lift mood."
    ],

    #study related
     "quantum physics": ["Quantum physics studies matter and energy at atomic levels.",
                          "Do you want to learn about superposition or entanglement?"],
    "classical physics": ["Classical physics explains macroscopic phenomena like motion and force.", "Newton’s laws are a fundamental part of classical physics."],
    "mechanics": ["Mechanics deals with motion, forces, and energy.", "It’s foundational for engineering and physics."],
    "thermodynamics": ["Thermodynamics studies heat, work, and energy transfer.", "It helps us understand engines and refrigeration."],
    "electromagnetism": ["Electromagnetism studies electric and magnetic fields.", "It powers modern electronics and communication."],
    "optics": ["Optics studies light and its behavior.", "It explains lenses, mirrors, and optical instruments."],
    "relativity": ["Relativity deals with space, time, and gravity.", "Einstein’s theory revolutionized physics."],
    "mathematics": ["Mathematics is the language of the universe.", "Do you want to discuss algebra, calculus, or statistics?"],
    "algebra": ["Algebra uses symbols and equations to solve problems.", "It’s useful in math, physics, and computer science."],
    "geometry": ["Geometry studies shapes, sizes, and spaces.", "It’s essential for design, architecture, and engineering."],
    "trigonometry": ["Trigonometry focuses on triangles and angles.", "It’s widely used in physics, engineering, and navigation."],
    "calculus": ["Calculus studies change and motion.", "It’s critical for science, engineering, and economics."],
    "probability": ["Probability measures the likelihood of events.", "It’s applied in statistics, AI, and finance."],
    "statistics": ["Statistics collects, analyzes, and interprets data.", "It helps make informed decisions from data."],
    "computer_science": ["Computer Science studies algorithms, programming, and software.", "Do you want to know about programming languages or AI?"],
    "programming": ["Programming is writing instructions for computers.", "Languages like Python, Java, and C++ are common."],
    "algorithms": ["Algorithms solve problems step by step.", "Sorting and searching are classic examples."],
    "data_structures": ["Data structures organize data efficiently.", "Lists, trees, and graphs are key examples."],
    "machine_learning": ["Machine Learning lets computers learn from data.", "It powers recommendations, image recognition, and predictions."],
    "artificial_intelligence": ["AI simulates human intelligence in machines.", "Applications include chatbots, self-driving cars, and healthcare."],
    "deep_learning": ["Deep Learning uses neural networks with many layers.", "It’s used in AI image and speech recognition."],
    "neural_networks": ["Neural networks are inspired by the human brain.", "They help in pattern recognition and predictions."],
    "biology": ["Biology studies life and living organisms.", "Do you want to learn about cells, genetics, or ecosystems?"],
    "genetics": ["Genetics studies heredity and DNA.", "It explains how traits are passed down."],
    "microbiology": ["Microbiology studies microorganisms.", "It’s important for medicine and environment."],
    "anatomy": ["Anatomy studies the structure of organisms.", "It’s fundamental in medicine and biology."],
    "physiology": ["Physiology studies how organisms function.", "It explains body systems and processes."],
    "chemistry": ["Chemistry studies matter and reactions.", "It’s key for medicine, materials, and energy."],
    "organic_chemistry": ["Organic chemistry studies carbon-based compounds.", "It’s used in drugs, plastics, and fuels."],
    "inorganic_chemistry": ["Inorganic chemistry studies non-carbon compounds.", "It’s important for metals, minerals, and catalysis."],
    "biochemistry": ["Biochemistry studies chemical processes in living things.", "It connects biology and chemistry."],
    "environmental_science": ["Environmental science studies ecosystems and human impact.", "It’s vital for sustainability."],
    "history": ["History helps us learn from the past.", "Do you want to know about ancient civilizations or modern events?"],
    "ancient_civilizations": ["Ancient civilizations shaped culture and society.", "Examples: Egypt, Mesopotamia, Indus Valley."],
    "world_war_1": ["World War I lasted from 1914 to 1918.", "It involved many nations and changed global politics."],
    "world_war_2": ["World War II lasted from 1939 to 1945.", "It had massive impact on world history."],
    "modern_history": ["Modern history studies the last few centuries.", "It helps understand current global issues."],
    "literature": ["Literature explores human experiences through writing.", "Do you enjoy novels, poems, or plays?"],
    "poetry": ["Poetry expresses emotions through words.", "Reading poetry can inspire and comfort."],
    "novels": ["Novels tell long, fictional stories.", "They can improve empathy and imagination."],
    "plays": ["Plays are meant to be performed.", "They teach about drama, dialogue, and culture."],
    "languages": ["Languages connect people and cultures.", "Learning new languages broadens your perspective."],
    "linguistics": ["Linguistics is the scientific study of language.", "It explores grammar, syntax, and meaning."],
    "philosophy": ["Philosophy explores fundamental questions about life.", "It encourages critical thinking and reasoning."],
    "psychology": ["Psychology studies the mind and behavior.", "It helps understand emotions and actions."],
    "sociology": ["Sociology studies society and social behavior.", "It explains cultures, communities, and trends."],
    "economics": ["Economics studies production, distribution, and consumption.", "It helps understand markets and policies."],
    "political_science": ["Political science studies governments and policies.", "It explains power, law, and society."],
    "astronomy": ["Astronomy studies stars, planets, and the universe.", "Telescopes help us explore outer space."],
    "space_science": ["Space science explores planets, galaxies, and space phenomena.", "It includes astrophysics and cosmology."],




    # --- Default ---
    "default": ["I don't understand what you're saying. Can you please elaborate it with simple words?"]
}

# --- Keyword mapping ---
keywords = {}
for cat in responses.keys():
    if cat == "default":
        continue
    keywords[cat] = [cat]  # each category at least matches its own name


# --- Keywords with Synonyms & Variations ---
# --- Keywords with Synonyms & Variations ---
keywords = {
    # --- Greetings / Mood ---
    "greeting": ["hello", "hi", "hey", "good morning", "good evening", "how are you"],
    "sad": ["sad", "unhappy", "depressed", "cry", "low", "down", "heartbroken"],
    "anxious": ["anxious", "worried", "nervous", "panic", "stress", "tension"],
    "happy": ["happy", "joyful", "great", "awesome", "good", "fantastic", "smile"],
    "crisis": ["suicide", "end life", "kill myself", "hopeless", "self harm", "give up"],
    "breathing": ["breathing", "inhale", "exhale", "relaxation exercise", "deep breath"],
    "meditation": ["meditation", "mindful", "calm", "relaxation", "yoga"],
    "therapy": ["therapy", "counseling", "counsellor", "therapist", "psychologist"],
    "lonely": ["lonely", "alone", "isolated", "no friends", "abandoned"],
    "selfcare": ["selfcare", "take care", "relax", "pamper", "me time"],
    "burnout": ["burnout", "exhausted", "tired", "drained", "overworked"],
    "gratitude": ["gratitude", "thankful", "blessed", "appreciate"],
    "anger": ["anger", "angry", "mad", "frustrated", "irritated"],
    "overthinking": ["overthinking", "thinking too much", "looping thoughts"],
    "insomnia": ["insomnia", "can't sleep", "awake", "sleep problem"],
    "confidence": ["confidence", "self esteem", "belief", "proud"],
    "motivation": ["motivation", "inspire", "energy", "drive"],
    "fear": ["fear", "scared", "afraid", "terrified", "phobia"],
    "mindfulness": ["mindfulness", "awareness", "present moment"],
    "relapse": ["relapse", "fall back", "slip up", "start again"],
    "healing": ["healing", "recover", "recovery", "cure"],
    "resilience": ["resilience", "strong", "bounce back", "courage"],
    "relationships": ["relationships", "partner", "friend", "connection", "bond"],
    "stress": ["stress", "pressure", "load", "tense"],
    "forgiveness": ["forgive", "forgiveness", "let go", "apology"],
    "shame": ["shame", "embarrassed", "humiliated"],
    "guilt": ["guilt", "regret", "remorse"],
    "hope": ["hope", "faith", "optimism"],
    "patience": ["patience", "waiting", "slow", "calm"],
    "support": ["support", "help", "backing", "assistance"],
    "greeting": ["hello", "hi", "hey", "good morning", "good evening", "how are you"],
    "happy": ["happy", "joyful", "great", "awesome", "good", "fantastic", "smile", "feeling good"],
    "sad": ["sad", "unhappy", "depressed", "cry", "low", "down", "heartbroken", "not okay", "not fine"],
    "anxious": ["anxious", "worried", "nervous", "panic", "stress", "scared", "restless"],
    "crisis": ["suicide", "end life", "kill myself", "hopeless", "self harm", "can't go on"],
    "guilt": ["guilt", "guilty", "regret", "ashamed", "my fault", "blame myself"],
    "shame": ["shame", "ashamed", "embarrassed", "humiliated", "worthless"],
    "confusion": ["confused", "uncertain", "unsure", "don’t know", "lost", "doubt"],
    "loneliness": ["lonely", "alone", "nobody", "isolated", "ignored", "friendless"],
    "frustration": ["frustrated", "annoyed", "irritated", "fed up", "stuck"],
    "jealousy": ["jealous", "envious", "compare", "envy", "wish I had"],
    "hopefulness": ["hopeful", "optimistic", "bright future", "faith", "looking forward"],
    "resilience": ["resilient", "bounce back", "strong", "survivor", "tough"],
    "love": ["love", "affection", "caring", "compassion", "fondness", "like you"],
    "regret": ["regret", "wish I hadn’t", "if only", "I shouldn’t have", "my mistake"],
    "bored": ["bored", "nothing to do", "dull", "boredom", "listless"],
    "fear": ["fear", "scared", "afraid", "frightened", "terrified"],
    "anger": ["anger", "angry", "mad", "furious", "irritated"],
    "pride": ["pride", "proud", "satisfied", "accomplished"],
    "curiosity": ["curious", "interested", "wonder", "inquisitive"],
    "embarrassment": ["embarrassed", "awkward", "humiliated", "shy"],
    "nostalgia": ["nostalgic", "memory", "remember", "past", "old times"],
    "disappointment": ["disappointed", "let down", "sad about", "unhappy with"],
    "relaxation": ["relax", "calm", "chill", "peaceful", "rest"],
    "peace": ["peaceful", "calm", "serene", "quiet", "tranquil"],
    "optimism": ["optimistic", "positive", "hopeful", "bright"],
    "pessimism": ["pessimistic", "negative", "hopeless", "downbeat"],

    # --- General topics ---
    "weather": ["weather", "rain", "sunny", "cloudy", "storm"],
    "sports": ["sports", "game", "football", "cricket", "basketball"],
    "food": ["food", "eat", "dish", "meal", "snack"],
    "tech": ["tech", "technology", "gadget", "device"],
    "news": ["news", "headlines", "current affairs"],
    "music": ["music", "song", "band", "instrument", "sing"],
    "movies": ["movie", "film", "cinema", "series", "hollywood"],
    "travel": ["travel", "trip", "journey", "tour"],
    "books": ["book", "novel", "reading", "author"],
    "hobbies": ["hobby", "interest", "pastime", "free time"],

    # --- Everyday topics ---
    "study": ["study", "learn", "revision", "reading"],
    "exam": ["exam", "test", "quiz"],
    "career": ["career", "job", "profession", "work life"],
    "work": ["work", "office", "task", "job"],
    "money": ["money", "finance", "salary", "budget"],
    "family": ["family", "parents", "siblings", "relatives"],
    "friendship": ["friendship", "friends", "buddy", "bestie"],
    "school": ["school", "class", "teacher", "homework"],
    "college": ["college", "university", "campus"],
    "future": ["future", "tomorrow", "later", "ahead"],
    "dreams": ["dreams", "goals", "ambition", "aspiration"],
    "routine": ["routine", "habit", "schedule"],
    "exercise": ["exercise", "workout", "fitness", "gym"],
    "pets": ["pet", "dog", "cat", "animal"],
    "nature": ["nature", "forest", "mountain", "river"],
    "art": ["art", "drawing", "painting", "sketch"],
    "goals": ["goal", "target", "aim", "objective"],
    "health": ["health", "doctor", "illness", "wellbeing"],
    "time": ["time", "clock", "hours", "minutes"],
    "internet": ["internet", "web", "online", "network"],
    "gaming": ["game", "gaming", "console", "playstation", "xbox"],
    "science": ["science", "biology", "physics", "chemistry"],
    "space": ["space", "nasa", "mars", "moon", "galaxy"],
    "philosophy": ["philosophy", "wisdom", "deep thought"],
    "language": ["language", "english", "spanish", "hindi"],
    "culture": ["culture", "tradition", "customs", "heritage"],
    "history": ["history", "past", "ancient", "king", "gandhi"],
    "fashion": ["fashion", "clothes", "style", "dress"],
    "shopping": ["shopping", "buy", "mall", "store"],
    "economy": ["economy", "finance", "market", "inflation"],
    "environment": ["environment", "climate", "global warming"],
    "politics": ["politics", "election", "government"],
    "festival": ["festival", "holiday", "celebration"],
    "weekend": ["weekend", "saturday", "sunday"],
    "morning": ["morning", "sunrise", "dawn"],
    "night": ["night", "evening", "midnight"],
    "birthday": ["birthday", "bday", "cake", "party"],
    "holiday": ["holiday", "vacation", "trip"],
    "workout": ["workout", "exercise", "gym"],
    "coffee": ["coffee", "cappuccino", "latte"],
    "tea": ["tea", "chai", "green tea"],
    "water": ["water", "drink", "hydrate"],
    "sleep": ["sleep", "nap", "rest", "dream"],
    "celebration": ["celebration", "party", "event"],
    "love": ["love", "relationship", "crush", "romance"],
    "dating": ["dating", "date", "boyfriend", "girlfriend"],
    "marriage": ["marriage", "wedding", "husband", "wife"],
    "children": ["children", "kids", "child", "baby"],
    "aging": ["aging", "old", "elderly", "senior"],
    "death": ["death", "loss", "grief", "passed away"],

    # --- Tech / AI / Knowledge ---
    "ai": ["ai", "artificial intelligence", "robots", "automation"],
    "machine_learning": ["machine learning", "ml", "training models", "data learning"],
    "cybersecurity": ["cybersecurity", "cyber attack", "hacking", "online safety"],
    "social_media": ["social media", "facebook", "instagram", "twitter", "tiktok"],
    "blockchain": ["blockchain", "crypto", "bitcoin", "ethereum"],
    "cloud": ["cloud", "aws", "azure", "google cloud", "cloud storage"],
    "gk_science": ["science fact", "earth", "sun", "physics"],
    "gk_space": ["space fact", "stars", "universe", "astronomy"],
    "gk_history": ["history fact", "freedom", "revolution"],
    "gk_geography": ["geography", "mountain", "river", "country", "continent"],
    
    #study relate
    "quantum_physics": ["quantum physics", "quantum mechanics", "superposition", "entanglement"],
    "classical_physics": ["classical physics", "newton", "motion", "forces"],
    "mechanics": ["mechanics", "motion", "force", "energy"],
    "thermodynamics": ["thermodynamics", "heat", "temperature", "entropy"],
    "electromagnetism": ["electromagnetism", "electricity", "magnetism", "fields"],
    "optics": ["optics", "light", "lenses", "mirrors"],
    "relativity": ["relativity", "einstein", "special relativity", "general relativity"],
    "mathematics": ["math", "mathematics", "numbers", "algebra", "calculus"],
    "algebra": ["algebra", "equation", "variables", "polynomial"],
    "geometry": ["geometry", "shapes", "angles", "triangle", "circle"],
    "trigonometry": ["trigonometry", "sine", "cosine", "tangent", "angles"],
    "calculus": ["calculus", "derivative", "integral", "limits", "differentiation"],
    "probability": ["probability", "chance", "likelihood", "statistics"],
    "statistics": ["statistics", "mean", "median", "variance", "data"],
    "computer_science": ["computer science", "computing", "algorithm", "programming"],
    "programming": ["programming", "coding", "python", "java", "c++"],
    "algorithms": ["algorithm", "sort", "search", "pathfinding"],
    "data_structures": ["data structure", "array", "list", "tree", "graph"],
    "machine_learning": ["machine learning", "ml", "training", "data model"],
    "artificial_intelligence": ["ai", "artificial intelligence", "robots", "automation"],
    "deep_learning": ["deep learning", "neural network", "cnn", "rnn"],
    "neural_networks": ["neural network", "nodes", "layers", "weights"],
    "biology": ["biology", "life", "cells", "organism"],
    "genetics": ["genetics", "dna", "heredity", "traits"],
    "microbiology": ["microbiology", "bacteria", "virus", "microbe"],
    "anatomy": ["anatomy", "body", "organs", "structure"],
    "physiology": ["physiology", "function", "systems", "processes"],
    "chemistry": ["chemistry", "reaction", "compound", "element"],
    "organic_chemistry": ["organic chemistry", "carbon", "molecules", "compounds"],
    "inorganic_chemistry": ["inorganic chemistry", "metals", "minerals", "salts"],
    "biochemistry": ["biochemistry", "enzymes", "proteins", "metabolism"],
    "environmental_science": ["environment", "ecology", "sustainability", "ecosystem"],
    "history": ["history", "past", "events", "civilization"],
    "ancient_civilizations": ["ancient civilization", "egypt", "rome", "mesopotamia"],
    "world_war_1": ["world war 1", "ww1", "1914", "1918"],
    "world_war_2": ["world war 2", "ww2", "1939", "1945"],
    "modern_history": ["modern history", "20th century", "21st century", "contemporary history"],
    "literature": ["literature", "novel", "poem", "story"],
    "poetry": ["poetry", "verse", "rhyme", "poem"],
    "novels": ["novel", "fiction", "author", "story"],
    "plays": ["play", "drama", "theater", "performance"],
    "languages": ["language", "linguistics", "communication", "words"],
    "linguistics": ["linguistics", "grammar", "syntax", "phonetics"],
    "philosophy": ["philosophy", "ethics", "logic", "mind"],
    "psychology": ["psychology", "mind", "behavior", "cognition"],
    "sociology": ["sociology", "society", "community", "culture"],
    "economics": ["economics", "market", "finance", "trade"],
    "political_science": ["political science", "government", "law", "policy"],
    "astronomy": ["astronomy", "stars", "planets", "universe"],
    "space_science": ["space science", "space", "cosmos", "astrophysics"],

    # --- Motivational trigger ---
    "quote": ["quote", "motivate", "inspire", "encourage"]
}

# --- Classifier ---
def classify_message(msg):
    text = msg.lower()
    for category, words in keywords.items():
        for w in words:
            if re.search(rf"\b{w}\b", text):
                return category
    return "default"


# --- Chat API ---
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    if not user_msg.strip():
        return jsonify({"response": "I didn’t catch that. Could you type something?"})

    category = classify_message(user_msg)
    if category == "quote":
        bot_response = random.choice(quotes)
    else:
        bot_response = random.choice(responses.get(category, responses["default"]))

    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True)