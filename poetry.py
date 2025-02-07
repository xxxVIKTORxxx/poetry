import random

# Cosmic Symphony of Rhythmic Mutation
# A Pythonic ode to poetic evolution, shaped by the rhythm of stars

# Expanded poetic pool of celestial whispers
phrases = [
    "Starlight fades", "Nebulae breathe", "Planets turn", "Galaxies dream", 
    "Comets write ancient scripts", "Silence reigns", "Echoes linger", 
    "Moonlight dances", "Black holes weep", "Solar winds hum", 
    "Dust drifts timelessly", "Meteor showers spark", "Eons pass silently", 
    "Stars cradle secrets", "Void echoes softly", "Night's canvas glows", 
    "Auroras paint skies", "Cosmos whispers tales", "Darkness listens patiently", 
    "Constellations pulse", "Satellites wander", "Light bends gracefully", 
    "Galactic tides shift", "Gravity serenades", "Time twists endlessly", 
    "Celestial choirs sing", "Meteor trails gleam", "Timeless echoes rise", 
    "Night veils unfold", "Galaxies spin eternally", "Wisdom dances in orbits", 
    "Comets leave whispers", "Nebulae sketch dreams", "Distant voices hum", 
    "Ecliptic songs emerge", "Cosmic riddles remain", "Solar arcs gleam", 
    "Space blossoms endlessly", "Galactic hearts beat", "Shadows carve light"
]

# Cosmic rhythm for two-line stanzas, ensuring an 8-line output
line_structure = [2, 2, 2, 2]  # Simplified to ensure consistent rhythm with 8-line output

# The heavens mutate their own verse to satisfy rhythmic needs
def mutate_for_rhythm(poem_lines):
    mutated_poem = []
    used_phrases = set()
    for i, line in enumerate(poem_lines):
        words = line.split()
        target_length = line_structure[i % len(line_structure)]
        if len(words) != target_length:  # If rhythm needs correction
            available_phrases = [phrase for phrase in phrases if phrase not in used_phrases]
            if len(available_phrases) < target_length:
                available_phrases = phrases  # Reset if pool is too small
            chosen_phrases = random.sample(available_phrases, target_length)
            line = " ".join(chosen_phrases)
            used_phrases.update(chosen_phrases)
        else:
            # Word mutation logic: replace words with random choices from related phrases
            words_to_mutate = random.sample(words, min(1, len(words)))
            for word in words_to_mutate:
                replacement_phrase = random.choice([phrase for phrase in phrases if phrase not in used_phrases])
                replacement_word = replacement_phrase.split()[0]
                line = line.replace(word, replacement_word, 1)
                used_phrases.add(replacement_phrase)
        mutated_poem.append(line)
    return mutated_poem

# The heavens write their own verse
def generate_verse():
    poem_lines = []
    used_phrases = set()
    for line_length in line_structure * 2:  # Generate 8 lines for poetic rhythm
        available_phrases = [phrase for phrase in phrases if phrase not in used_phrases]
        if len(available_phrases) < line_length:
            available_phrases = phrases  # Reset if pool is too small
        line = " ".join(random.sample(available_phrases, line_length))
        used_phrases.update(line.split())
        poem_lines.append(line)
    return poem_lines

# Call forth poetic stars, mutate for rhythm
def celestial_lament():
    print("Whispered by the cosmos:\n")
    poem_lines = generate_verse()
    mutated_poem = mutate_for_rhythm(poem_lines)
    for line in mutated_poem:
        print(line)
    print("\n~*~ End of cosmic verse ~*~")

# Begin the celestial symphony
celestial_lament()
