from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range
from pydub.scipy_effects import eq

# from OpenAITTS import get_voice
from GoogleTTS import get_voice
from gpt import get_script

from datetime import datetime

# Get the script for today's show
talks = get_script()

# talks = [
#     {
#       "topic": "Introduction",
#       "content": "Good evening, ladies and gentlemen, boys and girls, and welcome to another enchanting episode of Tales of Time! I am your trusty narrator, Benny, here to whisk you away on a journey through the annals of history. Tonight, we have a lineup of fascinating tales to share with you. We'll explore groundbreaking historical events, celebrate monumental cultural milestones, and dive into some quirky and delightful anecdotes from our cherished listeners. So, sit back, relax, and let the magic of storytelling transport you to times gone by."
#     },
#     {
#       "topic": "Historical Events",
#       "content": "Tonight, we shall delve into a day that marked a turning point in the world of science and innovation. On this very day, many moons ago, a brilliant mind graced our world with an invention that forever changed the course of human knowledge. Yes, dear listeners, we are talking about the remarkable discovery of penicillin by Sir Alexander Fleming in 1928! Picture this: it's a chilly September morning in London. Dr. Fleming, a humble bacteriologist at St. Mary's Hospital, is sorting through a clutter of petri dishes filled with colonies of Staphylococcus bacteria. Suddenly, something extraordinary catches his eye. One of the dishes, left uncovered by a fortuitous mistake, reveals a moldy spot, clear and devoid of bacteria. Curious and intrigued, Fleming observes that this mold, later identified as Penicillium notatum, has created a bacteria-free zone. Eureka! A moment of serendipity, where a mere accident paved the way for the world's first antibiotic. Penicillin's discovery marked the dawn of a new era in medicine, transforming how we combat bacterial infections. No longer were we at the mercy of deadly diseases like pneumonia, syphilis, and gangrene. With penicillin, lives were saved, and medical science leaped forward with newfound hope and vigor. Imagine a world without this wonder drug, where a simple cut could spell doom, where infections ran rampant without a cure. Fleming's penicillin ushered in an age of antibiotics, revolutionizing healthcare and giving us the power to fight back against the invisible enemies of our bodies. So, my dear friends, as we marvel at the miracles of modern medicine, let us tip our hats to Sir Alexander Fleming and his accidental genius. For it is on this very day that he gifted humanity with the elixir of life, a beacon of hope in our darkest hours. And with that, we conclude our first tale of the evening, a testament to the boundless possibilities of human curiosity and chance discoveries. Stay tuned, for our journey through time has only just begun!"
#     },
#     {
#       "topic": "Cultural Milestones",
#       "content": "Today, we celebrate a monumental moment in the world of cinema. It was on this very day in 1977 that a film unlike any other graced the silver screen, forever altering the landscape of science fiction and adventure. Yes, dear audience, I'm talking about the legendary 'Star Wars'! Picture the scene: the year is 1977, and the world is about to witness the birth of a cinematic phenomenon. Directed by the visionary George Lucas, 'Star Wars: Episode IV – A New Hope' burst onto the screen, captivating audiences with its epic tale of a galaxy far, far away. The film transported viewers to a universe teeming with interstellar battles, valiant heroes, and formidable villains. At the heart of this saga was a young farm boy named Luke Skywalker, who, along with Princess Leia, Han Solo, and a host of unforgettable characters, embarked on a quest to defeat the evil Galactic Empire. The film's groundbreaking special effects, masterful storytelling, and John Williams' iconic score captured the imagination of millions, igniting a passion for the stars that continues to burn brightly to this day. 'Star Wars' was more than just a movie; it was a cultural milestone that transcended generations. Fans from all walks of life found themselves united in their love for this epic space opera. The film spawned a franchise that includes sequels, prequels, spin-offs, television series, books, comics, and a vast array of merchandise. But what truly set 'Star Wars' apart was its ability to inspire. It sparked the imaginations of countless individuals, driving them to explore new frontiers in filmmaking, storytelling, and even space exploration. It reminded us that even in a vast and uncertain universe, hope and courage can lead to extraordinary adventures. As we reflect on this iconic moment, let us remember the magic of 'Star Wars' and its impact on our cultural tapestry. Whether you're a die-hard fan or a newcomer to the saga, the force of 'Star Wars' lives on, reminding us that the power of storytelling knows no bounds. And now, dear friends, as we leave the stars behind and return to our earthly abode, prepare yourselves for our final tale of the evening. A tale filled with quirks and peculiarities, sent in by you, our beloved audience."
#     },
#     {
#       "topic": "Anecdotes and Stories",
#       "content": "Today, we have a fascinating story sent in by one of our listeners, Emily from Boston. Emily writes to us about an unusual competition that took place in the quaint town of Bunol, Spain, many years ago. It was on this very day, in 1945, that the first 'La Tomatina' festival began, and oh, what a spectacle it was! Imagine this: a warm summer day in Bunol, where the streets are abuzz with excitement. The townsfolk have gathered for the annual parade, but little did they know that this year's celebration would take a wildly unexpected turn. A group of young men, brimming with mischief, decided to join the parade with a twist – they carried with them baskets of ripe tomatoes. As the parade wound its way through the town, one of the young men, in a fit of playful exuberance, tossed a tomato at a nearby participant. What followed was sheer chaos and hilarity! The tomato hit its mark, and soon, others joined in, hurling tomatoes left and right. The air was filled with laughter and the splatter of juicy tomatoes, as the town erupted into an impromptu food fight. The sheer joy and spontaneity of the moment captivated everyone, turning the parade into a riotous celebration of camaraderie and fun. Over the years, this spontaneous act of tomato-throwing evolved into an annual tradition known as 'La Tomatina.' Each year, on the last Wednesday of August, thousands of people from around the world gather in Bunol to partake in this exuberant tomato fight. The streets run red with tomato juice as participants gleefully hurl tomatoes at one another, reveling in the sheer delight of the messy spectacle. 'La Tomatina' has become a symbol of joy, unity, and the simple pleasure of letting loose and having fun. It's a reminder that sometimes, the most memorable moments in life come from the unplanned and the unexpected. So, dear listeners, as we wrap up tonight's journey through time, let us take a leaf out of Bunol's book and embrace the joy of spontaneity. Whether it's a playful tomato fight or a spontaneous act of kindness, it's these moments that color our lives and make history truly come alive."
#     },
#     {
#       "topic": "Outro",
#       "content": "Thank you for joining me, Benny, on this delightful adventure through the pages of time. As we reflect on the stories of the past, let us carry their lessons and joys into our present and future. Remember, history is not just a series of dates and events, but a tapestry of human experiences, woven together by our shared curiosity and wonder. Until we meet again, keep your hearts light and your spirits high. Good night, and may your dreams be filled with wonder!"
#     }
#   ]

# merge the content for intro and first event and merge the outro with the last event
intro = talks[0]["content"]
outro = talks[-1]["content"]

filenames = []

for i, talk in enumerate(talks[1:len(talks)-1]):
    if i == 0:
        text = intro + talk["content"]
    elif i == len(talks)-3:
        text = talk["content"] + outro
    else:
        text = talk["content"]
    filenames.append(get_voice(f"output{i+1}.mp3", text))

back = AudioSegment.from_file("backtrack.mp3", "mp3")
back = normalize(back)
back = compress_dynamic_range(back, release=5000)

# Load the audio files
# filenames = ["./templates/26-05/output1.mp3", "./templates/26-05/output2.mp3", "./templates/26-05/output3.mp3"]
audioList = [AudioSegment.from_file(f, "mp3") for f in filenames]

# Combine the audio files and eq the back track to music to make room for the voice

combined = AudioSegment.empty()
combined += AudioSegment.silent(duration=5000)
backpointer = 5000
musicLen = 10 * 60 * 1000
fadeDuration = 3000
downdB = -12
for audio in audioList:
    # print(length)
    result = normalize(audio)
    result = result.low_pass_filter(4000)
    result = result.high_pass_filter(500)
    result = result + 8
    combined += result
    length = len(combined)
    combined += AudioSegment.silent(duration=musicLen)

    back = back.fade(to_gain = downdB, start = backpointer-fadeDuration, duration = fadeDuration)
    back = back.fade(to_gain = 12, start = length, duration = fadeDuration)
    backpointer = len(combined)

combined += AudioSegment.silent(duration=5000)

# Combine the distorted audio with the backtrack
final_audio = combined.overlay(back)

# Apply fade in and fade out effects
final_audio = final_audio.fade_in(3000).fade_out(3000)

# get todays date
today = datetime.now().strftime("%d-%m")

# Export the modified audio
final_audio.export(f"../templates/{today}/final_audio_test.mp3", format="mp3")