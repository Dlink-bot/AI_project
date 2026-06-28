"""A simple movie recommendation system based on a favorite genre."""

from typing import Dict, List, Optional

MOVIES_BY_GENRE: Dict[str, List[str]] = {
    "action": [
        "Mad Max: Fury Road",
        "John Wick",
        "The Dark Knight",
        "Mission: Impossible - Fallout",
    ],
    "comedy": [
        "Knives Out",
        "The Grand Budapest Hotel",
        "Superbad",
        "Palm Springs",
    ],
    "drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "Whiplash",
        "Moonlight",
    ],
    "science fiction": [
        "Interstellar",
        "Blade Runner 2049",
        "Arrival",
        "The Matrix",
    ],
    "horror": [
        "Get Out",
        "The Conjuring",
        "Hereditary",
        "A Quiet Place",
    ],
    "romance": [
        "La La Land",
        "The Notebook",
        "Before Sunset",
        "Crazy, Stupid, Love.",
    ],
    "thriller": [
        "Se7en",
        "Gone Girl",
        "Prisoners",
        "No Country for Old Men",
    ],
    "fantasy": [
        "The Lord of the Rings: The Fellowship of the Ring",
        "Harry Potter and the Sorcerer's Stone",
        "Spirited Away",
        "Pan's Labyrinth",
    ],
    "animation": [
        "Spider-Man: Into the Spider-Verse",
        "Coco",
        "Toy Story",
        "How to Train Your Dragon",
    ],
}

GENRE_ALIASES: Dict[str, str] = {
    "sci-fi": "science fiction",
    "scifi": "science fiction",
    "sf": "science fiction",
    "rom-com": "romance",
    "romcom": "romance",
    "thriller": "thriller",
}


def normalize_genre(genre: str) -> str:
    """Normalize a genre name so user input is handled consistently."""
    cleaned = genre.strip().lower()
    return GENRE_ALIASES.get(cleaned, cleaned)


def recommend_movies(favorite_genre: str, limit: int = 5) -> Optional[List[str]]:
    """Return a list of movie recommendations for the requested genre."""
    genre = normalize_genre(favorite_genre)

    if genre in MOVIES_BY_GENRE:
        return MOVIES_BY_GENRE[genre][:limit]

    for known_genre in MOVIES_BY_GENRE:
        if genre in known_genre or known_genre in genre:
            return MOVIES_BY_GENRE[known_genre][:limit]

    return None


def main() -> None:
    """Run the interactive recommendation system."""
    print("Movie Recommendation System")
    print("Enter your favorite genre to get movie suggestions.")
    favorite_genre = input("Favorite genre: ").strip()

    recommendations = recommend_movies(favorite_genre)

    if recommendations:
        print(f"\nRecommended movies for '{favorite_genre.title()}':")
        for index, movie in enumerate(recommendations, start=1):
            print(f"{index}. {movie}")
    else:
        print("No recommendations found for that genre yet.")


if __name__ == "__main__":
    main()
