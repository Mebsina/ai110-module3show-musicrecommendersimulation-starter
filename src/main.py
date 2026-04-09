"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


PROFILES = [
    {
        "name": "Chill Lofi Listener",
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.38,
        "likes_acoustic": True,
    },
    {
        "name": "High-Energy EDM Listener",
        "genre": "edm",
        "mood": "energetic",
        "energy": 0.95,
        "likes_acoustic": False,
    },
    {
        "name": "Hip-Hop Fan",
        "genre": "hip-hop",
        "mood": "energetic",
        "energy": 0.78,
        "likes_acoustic": False,
    },
    {
        "name": "Acoustic Folk Listener",
        "genre": "folk",
        "mood": "melancholic",
        "energy": 0.31,
        "likes_acoustic": True,
    },
]


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile in PROFILES:
        print(f"\n=== {profile['name']} ===\n")
        recommendations = recommend_songs(profile, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
