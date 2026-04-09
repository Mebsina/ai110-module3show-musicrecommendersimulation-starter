"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import argparse
from tabulate import tabulate
from src.recommender import load_songs, recommend_songs, MODES

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=list(MODES.keys()), default="genre")
    args = parser.parse_args()

    songs = load_songs("data/songs.csv")

    for profile in PROFILES:
        print(f"\n=== {profile['name']} | mode: {args.mode} ===\n")
        recommendations = recommend_songs(profile, songs, k=5, mode=args.mode)
        rows = []
        for i, (song, score, explanation) in enumerate(recommendations):
            rows.append([i + 1, song["title"], song["artist"], f"{score:.2f}", explanation])
        print(tabulate(rows, headers=["#", "Title", "Artist", "Score", "Reasons"], tablefmt="rounded_outline"))
        print()


if __name__ == "__main__":
    main()
