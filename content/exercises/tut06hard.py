words = """The sun is shining brightly in the clear blue sky. The sun is warm on my
skin, and the sun is making everything feel alive. The birds are
singing their sweet songs, and the birds are flying high in the sky.
The trees are swaying gently in the breeze, and the trees are providing
shade from the sun. The world is a beautiful place, and the world is
full of wonder. The sun is setting slowly, casting a warm glow over the
landscape. The sun is shining down on us, and the sun is making
everything feel happy. The birds are singing their sweet melodies, and
the birds are chirping loudly. The trees are swaying gently, and the
trees are rustling softly.
"""

#%%
words = words.lower().split()
print(words[:5])
print(words[-5:])

#%%
counts = {}

#%%
for word in words:
    word = word.strip('!?"\',.;.')
    counts[word] += 1

#%%

for word in words:
    word = word.strip('!?"\',.;.')
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

#%%
print(counts)

#%%
for word, count in counts.items():
    print(word, ": ", count, sep="")
