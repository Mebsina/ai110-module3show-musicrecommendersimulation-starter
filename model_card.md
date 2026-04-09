# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

**SongFinder 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
	- It suggests the top 5 songs from a 20-song catalog that best match a user's stated taste profile.

- What assumptions does it make about the user  
	- It assumes the user can describe their preferences explicitly: a favorite genre, a favorite mood, a target energy level, and whether they prefer acoustic sounds.

- Is this for real users or classroom exploration  
	- Classroom exploration only.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
	- Genre, mood, energy, and acousticness.

- What user preferences are considered  
	- Favorite genre, favorite mood, target energy, and `likes_acoustic`.

- How does the model turn those into a score  
	- Each song gets points for matching the user's genre and mood, with weights that vary by ranking mode. Then it loses points based on how far its energy is from the user's target. Finally it gains a small bonus based on how acoustic or produced it sounds relative to the user's preference.

- What changes did you make from the starter logic  
	- The starter had empty stubs. I added `score_song` as a separate function that returns both a numeric score and a list of reasons, then wired it into `recommend_songs` for ranking.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
	- 20 songs.

- What genres or moods are represented  
	- Genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, r&b, classical, country, metal, edm, folk, blues, reggae, soul. 
    - Moods: happy, chill, intense, relaxed, moody, focused, energetic, romantic, peaceful, nostalgic, angry, melancholic, sad.

- Did you add or remove data  
	- I added 10 songs to the original 10 to cover genres and moods that were missing.

- Are there parts of musical taste missing in the dataset  
	- Yes. Lyrics, language, cultural context, and tempo preference are not captured. The catalog is also fictional so it does not reflect real listening patterns.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
	- Users with clear, common preferences like chill lofi or intense workout music get strongly differentiated results.

- Any patterns you think your scoring captures correctly  
	- Genre and mood together cleanly separate songs that feel very different, like chill lofi vs intense rock, without any overlap in the top results.

- Cases where the recommendations matched your intuition  
	- The chill lofi profile returned Library Rain and Midnight Coding at the top, which was exactly what I expected.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
	- Valence, danceability, and tempo are stored in the CSV but never used in scoring.

- Genres or moods that are underrepresented  
	- Lofi has three songs while metal, blues, and reggae each have one. A user with a rare genre preference has fewer candidates to rank from.

- Cases where the system overfits to one preference  
	- The genre bonus is large enough that a song in the wrong genre will almost never outrank one in the right genre, even if every other feature is a better match.

- Ways the scoring might unintentionally favor some users  
	- Users who prefer popular or well-represented genres like lofi or pop will consistently get more relevant options than users who prefer underrepresented genres.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
	- Four profiles: Chill Lofi Listener, High-Energy EDM Listener, Hip-Hop Fan, and Acoustic Folk Listener.

- What you looked for in the recommendations  
	- Whether songs with both genre and mood matches ranked clearly above songs with only one match, and whether the top result for each profile was the obvious correct pick.

- What surprised you  
	- The Acoustic Folk and Hip-Hop profiles exposed the catalog imbalance clearly. Each has only one matching genre song, so the gap between rank 1 (score ~3.9) and rank 2 (score ~0.4) was huge. The EDM and Lofi profiles had more candidates and produced more meaningful top-5 lists.
	- Coffee Shop Stories (jazz, relaxed) appeared in the Chill Lofi top 5 despite matching neither genre nor mood, purely because its energy and acousticness were close to the profile.

- Any simple tests or comparisons you ran  
	- Ran all four profiles across all three modes. The EDM profile preferred Drop Zone with a near-perfect energy match. The Hip-Hop profile preferred Block Party for the same reason. Both had the other as their second pick because the shared energetic mood was enough for a mood bonus even without a genre match.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
	- Add valence to distinguish happy from sad songs within the same genre and mood label.

- Better ways to explain recommendations  
	- Show a per-feature breakdown visually instead of a comma-separated string.

- Improving diversity among the top results  
	- Add a rule that limits how many songs from the same genre can appear in the top K.

- Handling more complex user tastes  
	- Support a range for energy instead of a single target value, so a user can say they want something between 0.3 and 0.5.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
	- That they are fundamentally a scoring and ranking problem. The interesting part is deciding what to score and how much weight to give each signal.

- Something unexpected or interesting you discovered  
	- The genre weight alone drove most of the ranking. Even with energy and acousticness in the formula, genre almost always decided the top half of the list.

- How this changed the way you think about music recommendation apps  
	- Real apps like Spotify are doing something structurally similar but with implicit signals from millions of users instead of one person filling out a profile. The content-based layer I built is just one piece of a much larger system.

---

## 10. Personal Reflection: Engineering Process

- What was your biggest learning moment during this project?
	- Separating `score_song` from `recommend_songs`. Before that distinction, I thought of recommendation as one big step. Realizing that scoring one song and ranking a list are two different problems made the whole system easier to reason about and test.

- How did using AI tools help you, and when did you need to double-check them?
	- AI helped generate the expanded song catalog quickly and draft explanations for the README and model card. I needed to double-check the feature values to make sure they were internally consistent, for example that high-energy songs also had low acousticness, because the generated numbers were not always coherent on their own.

- What surprised you about how simple algorithms can still feel like recommendations?
	- The output of the chill lofi profile felt genuinely correct even though the logic is just addition and subtraction. The genre and mood weights alone were enough to make the top results feel intentional, not random. It made it clear that a well-chosen scoring rule matters more than algorithmic complexity.

- What would you try next if you extended this project?
	- Add more songs per genre so underrepresented genres like folk and hip-hop produce a meaningful top 5 instead of one strong match followed by near-zero scores. Also add a diversity rule so the same genre cannot fill all five spots.

---

## 11. Optional Extensions

- Challenge 2: Multiple Scoring Modes
	- Added three ranking strategies selectable via a `--mode` CLI flag: 
		- `genre` weights genre match highest
		- `mood` weights mood match highest
		- `energy` applies a heavier penalty for energy distance. 
	- Each mode uses the same scoring components but different weights defined in a `MODES` dict. Switching modes visibly changes the ranking order, most notably in profiles where genre and mood point to different songs.

- Challenge 4: Visual Summary Table
	- Results are displayed using `tabulate` with `rounded_outline` formatting. Each profile produces a bordered table showing rank, title, artist, score, and the full reason breakdown per song. This makes the scoring transparent and easy to read at a glance.
