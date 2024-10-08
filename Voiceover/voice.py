import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.7)  # Volume 0-1\


engine.say("The old clockmaker lived alone in a cottage on the edge of town. Every day, he meticulously repaired broken clocks, breathing life back into lost time. One morning, a young girl entered his shop, carrying an old, dusty pocket watch. My grandfather's, she said softly, her eyes wide with hope. Can you make it tick again? The clockmaker examined the watch, its hands frozen in the past. He nodded, and for hours he worked in silence, surrounded by the rhythmic ticking of other clocks. Finally, he handed the watch back to the girl, its hands now moving smoothly, as if time itself had been awakened. The girl beamed, her smile as bright as the morning sun. Thank you, she whispered, clutching the watch tightly. As she left, the clockmaker returned to his bench, his heart warmed by her joy. He glanced at the many clocks on the wall, feeling, perhaps for the first time, that his work did more than repair gears. It brought memories back to life.")
engine.runAndWait()



# for voice in voices:
#    print(f"THE VOICE : {voice}", "\n" + voice.id)
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()