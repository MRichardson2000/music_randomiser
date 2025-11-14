🎧 Album Selector
A personal music randomiser built to break me out of my comfort zone.

🚀 Why I Built This
I love music — but I tend to default to the same comfort bands and albums (Lorna Shore :D). So I built a tool that removes the element of choice and lets randomness guide my listening. It’s a fun way to rediscover forgotten tracks and explore my library with fresh ears as well as work on a very fun project that keeps me deeply interested.

I exported my Apple Music library as an XML file and used it as the foundation for this project. I’d never worked with XML before, so this was a great excuse to learn something new while building something I’d actually use. 

To use you need to open apple music on a mac device - click file - library - export to xml and then save it. This is where it pulls the data from. I've got multiple devices so I made the decision to upload my xml file to github so I can make improvements on other devices if I feel like it. Otherwise I would've hidden it but it's up to you. 

🛠️ What It Does
This tool reads your Apple Music XML library and offers:

🎲 random_album() — Pick random albums from your entire library

🎲 random_artist() — Pick random artists

🎲 random_single() — Pick random single

🎲 random_2025_album() — Pick albums released in 2025

🎲 random_2026_album() — Pick albums released in 2026

🔥 view_highest_skipped_songs() — Show songs you’ve skipped more than 5 times (maybe it's time I let them go?)

🔥 view_last_played_date() — Show last play date of chosen song or album for analysis

📦 Project Structure
Code
main.py              # Entry point — runs the randomisers and skip analysis
src/
├── config.py        # Path to your XML library file
├── randomiser.py    # Functions for random selection
└── services.py      # XML parsing and data extraction
🧪 Sample Output
bash
['Mercenary', 'I Hope We Make It Out of This Alive', 'In Medias Res']


🎉 Final Thoughts
This started as a small idea and turned into something surprisingly useful. I’m already using it to pick albums for my walks — and I’m excited to keep improving it. The final step for this is to implement some pytests to ensure it works well long term as I intend to utilise this for the forseeable future to add some spontanouity to my life. I have a habit of defaulting to old habits and likes so I really like randomisers