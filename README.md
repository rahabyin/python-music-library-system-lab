# Music Library System

## Overview
A Python class-based music library system that tracks individual songs and provides global analytics.

## Features
- Song Creation with name, artist, genre
- Global tracking of total songs, unique artists, unique genres
- Analytics: songs per genre and per artist

## Class Structure

### Instance Properties
- `name`: Song title
- `artist`: Performing artist
- `genre`: Music genre

### Class Attributes
- `count`: Total songs created
- `genres`: List of unique genres
- `artists`: List of unique artists
- `genre_count`: Dictionary of songs per genre
- `artist_count`: Dictionary of songs per artist

### Class Methods
| Method | Purpose |
|--------|---------|
| `add_song_to_count()` | Increments total count |
| `add_to_genres(genre)` | Adds unique genre |
| `add_to_artists(artist)` | Adds unique artist |
| `add_to_genre_count(genre)` | Updates genre count |
| `add_to_artist_count(artist)` | Updates artist count |

## Setup
```bash
pipenv install
pipenv shell
python3 test_song.py

## Usage
from song import Song
song = Song("99 Problems", "Jay Z", "Rap")
print(Song.count)  # 1
print(Song.genres)  # ['Rap']

## Concepts Used
Classes and Objects
Constructors (__init__)
self keyword
Class attributes and methods (@classmethod, cls)
Lists and Dictionaries
in / not in operators
Conditional statements


---

## Step 8: Commit Your Changes

```bash
# Check what files changed
git status

# Add all files to staging
git add .

# Commit with descriptive message
git commit -m "Add Song class with global tracking and tests"

# Verify commit was made
git log --oneline

# Push your feature branch to GitHub
git push origin song-class

# Verify on GitHub that the branch appears