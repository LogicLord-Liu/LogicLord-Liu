import json

with open("songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

with open("README.md", "w", encoding="utf-8") as f:
    f.write("## 🎵 Recently Listening (KuGou)\n\n")
    for song in songs:
        f.write(f"- 🎧 {song['title']} - {song['artist']}\n")
