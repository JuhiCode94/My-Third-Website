from django.shortcuts import render
import random
from datetime import datetime
from django.contrib import messages
from .models import Contact

# Create your views here.

def welcome(request):
    """
    Renders the welcome page.
    """
    return render(request, "welcome.html")
    # Uncomment the line below to return plain text instead of a rendered template
    # return HttpResponse("this is homepage")

def result(request):
    """
    Handles the result page for the typing test.
    Compares the original text and the user's typed text, highlights errors,
    calculates statistics (accuracy and words per minute), and displays them.
    """

    # Retrieve the original text and user-typed text from the request
    original_text = request.GET.get('original_text', '')
    user_text = request.GET.get('user_text', '')

    original_words = original_text.split()
    user_words = user_text.split()

    # Highlight incorrect words
    def highlight_text(words, comparison_words, is_original):
        """
        Highlights correct and incorrect words by wrapping them in <span> tags.
        """
        highlighted = []
        for index, word in enumerate(words):
            if index < len(comparison_words):
                if word != comparison_words[index]:
                    highlighted.append(f'<span class="incorrect-word">{word}</span>')
                else:
                    highlighted.append(f'<span class="correct-word">{word}</span>')
            else:
                # If the word count exceeds the comparison, append without highlighting
                if is_original:
                    highlighted.append(word)
                else:
                    highlighted.append(f'<span class="correct-word">{word}</span>')
        return ' '.join(highlighted)

    # Highlight the original and user texts with appropriate tags
    highlighted_original = highlight_text(original_words[:len(user_words)], user_words, True)
    highlighted_user = highlight_text(user_words, original_words[:len(user_words)], False)

    # Calculate the number of correct and incorrect words
    correct_words_count = sum(1 for i, word in enumerate(user_words) if i < len(original_words) and word == original_words[i])
    incorrect_words_count = sum(1 for i, word in enumerate(user_words) if i < len(original_words) and word != original_words[i])

    # Calculate accuracy and words per minute (WPM)
    accuracy = (correct_words_count / len(user_words)) * 100 if user_words else 0
    wpm = len(user_words)  # Simplified for example; calculate properly based on time.

    # Context dictionary for rendering the result page
    context = {
        'original_text': highlighted_original,
        'user_text': highlighted_user,
        'words_typed': len(user_words),
        'correct_words': correct_words_count,
        'incorrect_words': incorrect_words_count,
        'accuracy': accuracy,
        'wpm': wpm
    }

    # Render the result.html template with the context
    return render(request, 'result.html', context)

def home(request):
    """
    Renders the home page.
    """
    return render(request, "home.html")
    # Uncomment the line below to return plain text instead of a rendered template
    # return HttpResponse("this is homepage")

def about(request):
    """
    Renders the about page.
    """
    return render(request, "about.html")
    # Uncomment the line below to return plain text instead of a rendered template
    # return HttpResponse("this is homepage")  

def contact(request):
    """
    Handles the contact form submission.
    Saves the contact details to the database and displays appropriate messages.
    """
    if request.method == "POST":
        # Retrieve form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Check if all fields are filled before saving
        if name and email and message:
            # Create a new Contact object and save it to the database
            contact = Contact(name=name, email=email, message=message, timestamp=datetime.today())
            contact.save()
            # Display a success message
            messages.success(request, 'Your message has been sent successfully!')
        else:
            # Display error message if any fields are missing
            messages.error(request, 'Please fill out all fields.') 
      
    # Render the contact.html template
    return render(request, "contact.html")
    # Uncomment the line below to return plain text instead of a rendered template
    # return HttpResponse("this is contact page")     

def english_typing(request, section=None, difficulty=None):
    """
    Renders the English typing test page with different sections and difficulties.
    Generates buttons for the user to start different typing tests.
    """
    buttons = {}
    
    # Generate buttons for word-based typing tests based on difficulty
    if section == 'words':
        if difficulty == 'easy':
            buttons = {
                'Easy Words Test 1': '/typing_test?test=easy_words_1',
                'Easy Words Test 2': '/typing_test?test=easy_words_2'
            }
        elif difficulty == 'moderate':
            buttons = {
                'Moderate Words Test': '/typing_test?test=moderate_words'
            }
        elif difficulty == 'difficult':
            buttons = {
                'Difficult Words Test': '/typing_test?test=difficult_words'
            }

    # Generate buttons for paragraph-based typing tests based on difficulty
    elif section == 'paragraph':
        if difficulty == 'easy':
            buttons = {
                'Easy Paragraph Test': '/typing_test?test=easy_paragraph'
            }
        elif difficulty == 'moderate':
            buttons = {
                'Moderate Paragraph Test': '/typing_test?test=moderate_paragraph'
            }
        elif difficulty == 'difficult':
            buttons = {
                'Difficult Paragraph Test': '/typing_test?test=difficult_paragraph'
            }

    # Render the english_typing.html template with the section, difficulty, and buttons context
    return render(request, 'english_typing.html', {
        'section': section,
        'difficulty': difficulty,
        'buttons': buttons
    })

def typing_test(request):
    # Fetch test_type from the query parameters (determines which word list to display)
    test_type = request.GET.get('test', '')

    # Define word lists for different difficulty levels
    word_lists = {
        # List of easy words (easy_words_1)
        'easy_words_1': ['table', 'old', 'apple', 'car', 'loud', 'make', 'run', 'jump', 'radio', 'bread', 'arm', 'bite', 'cloud', 
                         'kiss', 'bat', 'fill', 'drop', 'seat', 'song', 'dance', 'fork', 'game', 'quick', 'sing', 'light', 'swim',
                         'tree', 'box', 'strong', 'bad', 'laugh', 'run', 'jump', 'nail', 'pig', 'horse', 'moon', 'land', 'stop', 'press',
                         'slow', 'funny', 'pink', 'cry', 'book', 'pen', 'tree', 'deep', 'happy', 'fire', 'poor', 'walk', 'green', 'roof',
                         'laugh', 'cold', 'city', 'bitter', 'dark', 'dream', 'touch', 'branch', 'hand', 'star', 'fast', 'jump', 'car', 'clear',
                         'coin', 'race', 'day', 'always', 'find', 'rise', 'book', 'park', 'art', 'hour', 'six', 'noisy', 'rain', 'empty',
                         'art', 'best', 'party', 'around', 'land', 'fox', 'apple', 'sure', 'fish', 'dark', 'heavy', 'eat', 'change', 'hole',
                         'car', 'press', 'near', 'team', 'wind', 'fox', 'dog', 'tree', 'table', 'spin', 'head', 'ready', 'box', 'follow',
                         'goat', 'city', 'moon', 'push', 'safe', 'time', 'bright', 'fall', 'moon', 'river', 'cloud', 'sun', 'quick', 'family',
                         'feel', 'fall', 'table', 'friend', 'forest', 'write', 'deep', 'bird', 'paint', 'wish', 'head', 'day', 'green',
                         'year', 'pepper', 'safe', 'dark', 'snow', 'shape', 'window', 'black', 'chance', 'mix', 'press', 'jump', 'hard',
                         'soon', 'eat', 'fix', 'fine', 'letter', 'full', 'mix', 'good', 'cat', 'poor', 'dream', 'laugh', 'party', 'remember',
                         'run', 'soon', 'row', 'coffee', 'see', 'carry', 'teach', 'night', 'sudden', 'next', 'fast', 'moment', 'name', 'bank',
                         'dust', 'glue', 'eat', 'ring', 'fish', 'pool', 'stop', 'short', 'life', 'cloud', 'reach', 'path', 'win', 'push', 'bag',
                         'table', 'yes', 'green', 'catch', 'coach', 'cold', 'south', 'best', 'rule', 'new', 'class', 'way', 'dog', 'outside',
                         'force', 'true', 'round', 'travel', 'tall', 'path', 'win', 'bubble', 'mix', 'plate', 'hit', 'read', 'perfect', 'cook',
                         'fast', 'pig', 'hope', 'school', 'rush', 'pick', 'shake', 'send', 'book', 'trip', 'quiet', 'leaf', 'river', 'try',
                         'tree', 'house', 'term', 'wish', 'lucky', 'point', 'dream', 'cold', 'chain', 'share', 'long', 'down', 'ball', 'second',
                         'story', 'wet', 'aim', 'dream', 'word', 'edge', 'sink', 'neck', 'dog', 'goat', 'team', 'fall', 'walk', 'change', 'dress',
                         'jump', 'deep', 'new', 'coin', 'cold', 'price', 'mark', 'cold', 'love'],

        # List of easy words (easy_words_2)
        'easy_words_2': ['slow', 'funny', 'pink', 'cry', 'book', 'pen', 'tree', 'deep', 'happy', 'fire', 'poor', 'walk', 'green', 'roof',
                 'quiet', 'frog', 'north', 'bread', 'mouse', 'chair', 'white', 'yellow', 'gift', 'plate', 'noise', 'clean', 'flower',
                 'sharp', 'match', 'simple', 'giant', 'tiny', 'safe', 'talk', 'clock', 'smile', 'visit', 'bright', 'circle', 'plant', 
                 'garden', 'clear', 'lion', 'ocean', 'water', 'think', 'shine', 'bridge', 'key', 'summer', 'winter', 'laugh', 'open', 
                 'ready', 'field', 'paper', 'movie', 'room', 'jump', 'throw', 'carry', 'touch', 'space', 'friend', 'crowd', 'song', 
                 'animal', 'chase', 'happy', 'warm', 'voice', 'stone', 'hurry', 'orange', 'train', 'guess', 'strong', 'quick', 'soft',
                 'pencil', 'drink', 'climb', 'hotel', 'night', 'child', 'shadow', 'storm', 'place', 'stairs', 'dance', 'glass', 'begin',
                 'morning', 'pocket', 'market', 'shine', 'start', 'picture', 'light', 'sweet', 'candle', 'strong', 'driver', 'honey',
                 'round', 'shirt', 'fun', 'clean', 'river', 'speak', 'dinner', 'road', 'sharp', 'cool', 'think', 'brush', 'store', 
                 'letter', 'doctor', 'middle', 'finish', 'animal', 'clay', 'leaf', 'loud', 'alone', 'calm', 'draw', 'block', 'watch',
                 'basket', 'metal', 'forest', 'music', 'laugh', 'fresh', 'pillow', 'police', 'world', 'lamp', 'rope', 'shell', 'small',
                 'silver', 'banana', 'giant', 'puzzle', 'berry', 'cheese', 'piano', 'button', 'story', 'monkey', 'garden', 'bubble',
                 'noisy', 'secret', 'blanket', 'cookie', 'window', 'orange', 'rabbit', 'strong', 'stone', 'circle', 'donkey', 'skate',
                 'zebra', 'spoon', 'island', 'lunch', 'bottom', 'travel', 'branch', 'tiger', 'handle', 'ribbon', 'letter', 'bottle',
                 'moment', 'grape', 'purple', 'wallet', 'forest', 'train', 'butter', 'donut', 'cactus', 'pirate', 'copper', 'sailor',
                 'ladder', 'mango', 'bucket', 'pencil', 'camera', 'summer', 'dolphin', 'clown', 'breeze', 'castle', 'arrow', 'jungle',
                 'waffle', 'rattle', 'cherry', 'silver', 'flame', 'tunnel', 'packet', 'soccer', 'yellow', 'kitten', 'wallet', 'rocket',
                 'subway', 'cousin', 'forest', 'cotton', 'market', 'toffee', 'biscuit', 'dragon', 'pencil', 'temple', 'puppy', 'helmet',
                 'sunny', 'guitar', 'butter', 'turtle', 'window', 'tablet', 'spring', 'castle', 'purple', 'dragon', 'hunger', 'little',
                 'market', 'cotton', 'breeze', 'blouse', 'forest', 'travel', 'window', 'island', 'market', 'castle', 'jungle', 'packet',
                 'button', 'rabbit', 'cotton', 'ladder', 'forest'],

        # List of moderate difficulty words
        'moderate_words': ['serene', 'delicate', 'intricate', 'canvas', 'horizon', 'gather', 'subtle', 'balance', 'vibrant', 'mystery', 'reflect', 
                           'gentle', 'embrace', 'patience', 'gradual', 'explore', 'curious', 'harmony', 'subtle', 'evolve', 'woven', 'progress', 
                           'genuine', 'vibrant', 'pursuit', 'clarity', 'quiet', 'fragment', 'unravel', 'steady', 'dynamic', 'vivid', 'unravel', 
                           'patience', 'resilient', 'sincere', 'whisper', 'gentle', 'evolving', 'quiet', 'balance', 'spectrum', 'intricate', 'curious', 
                           'deliberate', 'radiant', 'mindful', 'subtle', 'pursuit', 'challenge', 'embrace', 'tender', 'meticulous', 'radiant', 'wander', 
                           'delicate', 'transparent', 'steady', 'genuine', 'resilient', 'fragment', 'clarity', 'journey', 'thoughtful', 'humble', 
                           'steady', 'flourish', 'delicate', 'whisper', 'humble', 'vibrant', 'steady', 'harmonious', 'resilient', 'patience', 'careful', 
                           'luminous', 'subtle', 'curious', 'unravel', 'intricate', 'vivid', 'transient', 'steady', 'transparent', 'resolve', 'balanced', 
                           'transparent', 'gradual', 'tender', 'clarity', 'intricate', 'fragment', 'steady', 'elusive', 'subtle', 'mindful', 'serene', 
                           'whisper', 'mindful', 'graceful', 'curious', 'balance', 'mysterious', 'humble', 'steady', 'gentle', 'exploration', 'clarity', 
                           'resilient', 'humble', 'radiant', 'whisper', 'explore', 'journey', 'mindful', 'steady', 'elusive', 'patience', 'thoughtful', 
                           'quiet', 'subtle', 'vibrant', 'steadfast', 'gentle', 'balanced', 'clarity', 'curious', 'luminous', 'fragment', 'unfolding', 
                           'subtle', 'progress', 'intricate', 'steady', 'pursuit', 'mindful', 'quiet', 'delicate', 'balanced', 'whisper', 'translucent', 
                           'transient', 'peaceful', 'genuine', 'vibrant', 'resilient', 'subtle', 'harmony', 'luminous', 'steady', 'subtle', 'fragment', 
                           'delicate', 'mindful', 'pursuit', 'patience', 'serene', 'steady', 'evolving', 'thoughtful', 'gentle', 'balance', 'curiosity', 
                           'resilient', 'steady', 'dynamic', 'fragment'],

        # List of difficult words
        'difficult_words': ['ephemeral', 'enigmatic', 'juxtaposition', 'convoluted', 'tenebrous', 'serendipity', 'obfuscate', 'ineffable', 'transitory', 
                            'paradoxical', 'labyrinthine', 'visceral', 'perspicacious', 'esoteric', 'quixotic', 'recondite', 'sanguine', 'juxtapose', 
                            'verisimilitude', 'anachronistic', 'inexorable', 'diaphanous', 'acquiesce', 'ethereal', 'incongruous', 'mellifluous', 
                            'vicarious', 'ineffable', 'enigmatic', 'transcendental', 'ephemeral', 'precipitous', 'prosaic', 'nebulous', 'indomitable', 
                            'sycophantic', 'ubiquitous', 'tenacity', 'dialectical', 'catharsis', 'seraphic', 'dissonance', 'disparate', 'luminescent', 
                            'vicarious', 'ambivalence', 'prevaricate', 'discombobulate', 'incongruent', 'labyrinthine', 'tumultuous', 'dichotomy', 
                            'incandescent', 'acrimonious', 'quixotic', 'transcendence', 'paradox', 'exude', 'clandestine', 'obfuscation', 'profound', 
                            'enigmatic', 'ethereal', 'premonition', 'precarious', 'inconsequential', 'recondite', 'cryptic', 'mutable', 'nebulous', 
                            'reverberate', 'salubrious', 'esoteric', 'ineffable', 'juxtaposition', 'malleable', 'phantasmagoric', 'ethereal', 'juxtapose', 
                            'inscrutable', 'alacrity', 'insidious', 'ethereal', 'ephemeral', 'ineffable', 'transcendental', 'labyrinthine', 'quixotic', 
                            'vicarious', 'juxtaposition', 'transient', 'perennial', 'ambivalence', 'resonant', 'elusive', 'conflagration', 'esoteric', 
                            'dichotomy', 'sycophantic', 'incongruity', 'veracity', 'ruminate', 'ephemeral', 'nuanced', 'paradigm', 'volatile', 'labyrinthine', 
                            'inscrutable', 'phantasmal', 'juxtaposition', 'perennial', 'reverberate', 'enigmatic', 'dynamic', 'inscrutable', 'perspicuous', 
                            'diaphanous', 'inscrutable', 'symbiotic', 'ambivalence', 'labyrinthine', 'fragmentary', 'precipitate', 'infinitesimal', 
                            'anomalous', 'quixotic', 'disquietude', 'nebulous', 'ephemeral', 'paradoxical', 'insidious', 'phantasmagoric', 'juxtapose', 
                            'volatile', 'incomprehensible', 'enigmatic', 'quixotic', 'transcendental', 'ephemeral', 'vacillate', 'recondite', 'seraphic', 
                            'vicarious', 'transient', 'fragmented', 'kaleidoscope', 'ineffable', 'tumultuous', 'diaphanous', 'insidious', 'recondite', 
                            'magnanimous', 'nebulous', 'anachronistic', 'mellifluous', 'reverberate', 'precarious', 'symbiotic', 'esoteric', 'cryptic', 
                            'periphery', 'volatile', 'symbiosis', 'enigmatic', 'recondite', 'discombobulate', 'perspicuous', 'ambiguous', 'phantasmagoric', 
                            'transient', 'incongruous', 'ephemeral', 'tumultuous', 'dynamic', 'ethereal', 'surreal', 'perennial', 'juxtapose', 'cryptic', 
                            'vicarious', 'reverberate', 'ephemeral', 'phantasmal'],

        'easy_paragraph': ['''It was a bright and sunny morning when Sarah and her little brother Jack decided to spend the day at the park. The sky was clear, and the sun was shining brightly, making everything look fresh and colorful. Sarah, who was nine years old, loved going to the park. She enjoyed the green grass, the tall trees, and the flowers that bloomed all around. Jack, who was six, was always excited to play and explore. Today was no different.
        
                            “Are you ready, Jack?” Sarah asked as she put on her sneakers. Jack nodded and grabbed his small red ball.
                            
                            The park wasn’t too far from their house. They walked there together, holding hands and talking along the way. Sarah told Jack about the fun things they could do at the park. “We can play on the swings, go down the slide, and maybe even have a picnic!” she said. Jack smiled, excited about all the fun they would have.
                            
                            When they arrived at the park, they saw many people there. Some were walking dogs, others were playing basketball, and a few families were having picnics under the trees. Sarah and Jack ran towards the playground, where they found their favorite swing set. They took turns pushing each other high into the sky, laughing and shouting with joy.
                            
                            After swinging for a while, they decided to play with the red ball. They kicked it back and forth, running around and laughing as they chased it across the grassy field. As the sun began to set, they sat on the grass, enjoying a snack Sarah had packed in her backpack: peanut butter sandwiches and apple slices.
                            
                            “This was the best day ever!” Jack said with a big grin on his face. Sarah agreed, happy to have spent such a wonderful day with her little brother. They knew they would remember this day for a long time.'''
                            ],

        'moderate_paragraph': ['''Liam and Ava were best friends who lived in a small town surrounded by woods, rivers, and fields. They had been friends for as long as they could remember. Both loved the outdoors, and every day after school, they would run out into the woods, exploring new places and discovering hidden paths. Their favorite part of the day was when they went on adventures together. They didn’t need a map because they always seemed to find something new, whether it was an old tree with branches that seemed to reach for the sky or a quiet spot by the river where the water sparkled under the sun.

                                One sunny afternoon, Liam and Ava decided to take a different route through the woods. They had been on many adventures before, but today, they wanted to explore a part of the forest that no one had ever talked about. It was the farthest they had gone, and both of them felt excited about the possibility of discovering something amazing.

                                "Do you think we’ll find something special today?" Ava asked as they walked through the thick grass.

                                Liam looked up at the sky, his eyes squinting as he thought. "Maybe we’ll find a hidden cave or a secret garden," he said, his voice filled with excitement.

                                The two friends walked deeper into the woods, their feet crunching on the dry leaves that covered the ground. The trees were tall, and the air was thick with the smell of pine and damp earth. Ava and Liam had been in these woods so many times, but today felt different. There was a sense of mystery, like the trees themselves were watching them as they passed.

                                After walking for a while, they came across a small clearing. In the middle of the clearing, there was a large rock with moss growing on it. The rock was flat and smooth, making it seem almost like a table. Ava ran over to the rock and touched it. "It feels cool," she said, brushing her fingers across the moss.

                                Liam stood a few steps behind her, scanning the area. "I think we should climb that rock," he suggested.

                                Ava grinned. "Let’s do it!"

                                The rock wasn’t too tall, but it was a little slippery with the moss. Ava climbed first, using her hands to pull herself up. She reached the top and looked down at Liam. "It’s great up here!" she shouted. "You can see the whole forest from here!"

                                Liam followed her, his feet slipping a little, but he managed to reach the top. He sat beside Ava, both of them looking out over the woods. From up high, the trees looked like a giant green sea, with only a few gaps between them. The sun was starting to set, casting an orange glow over everything.

                                "This place is amazing," Liam said, his eyes wide with wonder.

                                Ava nodded. "It feels like we’re in the middle of nowhere. Just us and the woods."

                                The two friends stayed on the rock for a while, talking about everything and nothing. They made plans for the summer, talking about the things they wanted to do, like camping by the river or hiking to the highest hill in the woods. As the sun began to set, they realized it was time to head back home.

                                "Let’s go," Liam said, standing up and brushing the dirt off his pants. "It’s getting late."

                                Ava stood up, but as she turned to leave, something caught her eye. Near the edge of the clearing, there was a small bush with bright red berries. The berries looked unusual, not like anything they had seen before. Ava stepped closer to the bush, and Liam followed her.

                                "Do you think these are safe to eat?" Ava asked, eyeing the berries carefully.

                                Liam bent down and examined them. "I don’t know. They look a little strange, but I’ve never seen anything like them."

                                They both took a step back. They had been taught never to eat anything they found in the woods unless they were sure it was safe. "Let’s leave them alone," Liam suggested.

                                Ava agreed, and the two friends turned to leave the clearing. But as they did, something strange happened. The ground beneath their feet started to rumble, and the trees around them shook. The sound of a distant roar echoed through the woods. Both of them froze, their eyes wide with fear.

                                "What was that?" Ava whispered, gripping Liam’s arm.

                                Liam was just as scared, but he tried to stay calm. "I don’t know, but we need to get out of here."

                                They turned and ran, not looking back. The trees seemed to close in around them as they made their way through the woods. They could still hear the rumbling noise, getting louder with each step. It sounded like something huge was moving through the forest, and it was getting closer.

                                The two friends didn’t stop running until they reached the edge of the woods, where they could see their town in the distance. They slowed down, out of breath and shaking. "What was that?" Ava gasped, still trying to catch her breath.

                                Liam shook his head. "I don’t know. I’ve never heard anything like that before."

                                The sun had set completely, and the sky was darkening. The town lights twinkled in the distance, but neither of them wanted to go back into the woods that night. They decided to take the long way home, staying on the paved road and avoiding the forest.

                                The next day, Liam and Ava told their families about what had happened. They described the rumbling sound and the strange roar they had heard. At first, everyone thought it was just an animal, but no one had ever heard such a sound before. It was the kind of mystery that made people talk, but no one had any answers.

                                Days passed, and the two friends couldn’t stop thinking about the adventure they had. They returned to the clearing to look for any signs of what happened, but the strange sound had not returned. The berries were still there, but they decided not to go near them. They couldn’t shake the feeling that something strange had happened in the woods that day.

                                Even though they didn’t know what had caused the noise, Liam and Ava agreed that their adventure in the woods was something they would never forget. The woods were full of surprises, and they both knew that they had only begun to scratch the surface of the mysteries hidden there.

                                And so, the two friends kept exploring, but they never went back to that clearing again. They still had many more adventures ahead of them, and who knew what they would discover next?'''],



        'difficult_paragraph': ['''In the heart of a distant kingdom, nestled between towering mountains, there lay an enchanted forest. Its vast expanse was unlike any ordinary woodland. This forest was a world of wonder and mystery, where the trees whispered ancient secrets, the streams sang gentle lullabies, and the very earth seemed to hum with magic. The forest was known to all, but few had ventured deeply into its depths. Most people who lived near the forest would only walk on its outskirts, carefully avoiding the shadowy paths that led further in.

                                The forest had a reputation for being both beautiful and dangerous. Legends spoke of hidden treasures, creatures with extraordinary powers, and portals to other realms. Many had tried to explore its depths, but none had returned with clear answers about what lay within. Most of the explorers came back with stories of strange happenings—of flickering lights, whispering voices, and the sense that they were being watched by eyes that never blinked.

                                It was in this mysterious forest that a young girl named Elara lived. She had grown up in a small village at the forest’s edge, surrounded by tales of magic and wonder. Elara was no ordinary girl. While most children were content to play and run through the village, Elara found herself drawn to the forest, its allure irresistible. From the moment she could walk, she wandered into the woods, marveling at the beauty of the flowers, the sparkle of the dew on the leaves, and the peace that seemed to radiate from the place. The older villagers often cautioned her, telling her to stay close to home, to avoid the dangers that lay beyond the familiar paths. But Elara was different. She felt a deep connection to the forest, as if it were calling her to discover its secrets.

                                One autumn evening, as the sun dipped below the horizon, Elara decided that she would venture deeper into the forest than ever before. She had heard whispers of a hidden glade, a place where the trees grew so tall and close that their branches formed a canopy of leaves that seemed to shimmer with a magical light. It was said that those who found the glade would be granted a wish—an impossible wish, one that could change the course of their life forever.

                                With determination in her heart, Elara packed a small bag with food and water, and set off into the forest. The air was crisp, filled with the scent of pine and earth. As she walked deeper into the woods, the familiar sounds of the village faded away. The chirping of birds and the rustling of leaves were replaced by an eerie silence, broken only by the occasional hoot of an owl or the rustle of a distant creature moving through the underbrush.

                                The trees around her grew taller, their trunks thick and gnarled, twisted by years of age and the mysterious forces that dwelled within the forest. Strange, luminous mushrooms grew at the base of some of the trees, casting a soft, eerie glow on the forest floor. As Elara ventured further, she began to feel an odd sensation, as if the very air around her was charged with energy. It was as though the forest was alive, its ancient magic stirring in the air, watching her every move.

                                After several hours of walking, Elara reached a clearing. At the center of the clearing stood a massive tree, its bark a deep shade of silver, and its roots spread out like the arms of a giant. The tree seemed to shimmer in the twilight, as if it were not entirely of this world. Elara approached it cautiously, her heart pounding with anticipation. She had heard stories of this tree, known to the villagers as the "Heartwood." It was said that the tree held the key to the enchanted glade, but only those with pure intentions could find it.

                                As she stood before the tree, Elara noticed a faint glow beneath its roots. Kneeling down, she pushed aside the moss and leaves, revealing a small, hidden entrance. The opening was narrow, just big enough for her to slip through. Without hesitation, Elara crawled into the passageway, her heart racing with excitement. The path twisted and turned, leading her deeper underground. The air grew cooler, and the scent of earth and stone filled her senses. Finally, after what seemed like an eternity, the passage opened up into a vast cavern.

                                In the center of the cavern was a pool of water, its surface perfectly still, reflecting the glow of the Heartwood tree above. The water shimmered with an otherworldly light, casting a soft, ethereal glow around the cavern. Elara approached the water cautiously, her reflection rippling on its surface. As she gazed into the pool, she saw something strange—a figure, barely visible, standing just beneath the water's surface. It was a woman, her face obscured by flowing hair, but her eyes—deep, knowing eyes—stared up at Elara.

                                Suddenly, the figure spoke, her voice soft but clear. "Elara, you have come seeking your wish. But the path you seek is not an easy one. The forest holds many secrets, and not all are meant to be uncovered."

                                Elara stepped back, startled by the voice. "Who are you?" she asked, her voice trembling.

                                "I am the Guardian of the Glade," the figure replied. "I watch over those who seek the Heartwood, and I protect the wishes that lie within the forest. To gain your wish, you must first prove your worth."

                                Elara felt a surge of determination. "I am ready," she said boldly. "I will do whatever it takes."

                                The Guardian's eyes seemed to glow brighter as she smiled. "Then you must face the trials of the forest. Only by overcoming the challenges set before you can you earn your wish. But remember, the forest is not kind to those who seek power for selfish reasons. If your heart is pure, you will succeed. If not, the forest will reject you."

                                With that, the figure disappeared beneath the water, leaving Elara standing alone in the cavern. The forest had always been a place of wonder, but now it was a place of challenge—a place where only those with true courage and integrity could claim their desires.

                                Determined to prove herself, Elara stood tall. She knew that the forest was more than just a place of magic. It was a realm of lessons—lessons of wisdom, humility, and strength. With these thoughts in her mind, Elara took her first step toward the trials that awaited her, ready to face whatever challenges the enchanted forest had in store.'''],
    }

    # Get the word list based on test_type
    word_list = word_lists.get(test_type, [])

    # Shuffle the word list
    random.shuffle(word_list)

    # If the "Start New Test" button is clicked, shuffle the words
    if request.method == 'POST':
        random.shuffle(word_list)

    # Define the range of minutes for the timer
    minute_range = range(1, 31)

    return render(request, 'typing_test.html', {
        'word_list': word_list,
        'test_type': test_type,
        'minute_range': minute_range,
    })