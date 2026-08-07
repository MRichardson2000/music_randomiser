Album Selector: 
A personal music randomiser built to break me out of my comfort zone.

Why I Built This: 
I love music - but I tend to default to the same comfort bands and albums (Lorna Shore :D). So I built a tool that removes the element of choice and lets randomness guide my listening. It's a fun way to rediscover forgotten tracks and explore my library with fresh ears as well as work on a very fun project that keeps me deeply interested.

I exported my Apple Music library as an XML file and used it as the foundation for this project. 

I use this for two situations:
1. I use Carnets on my phone to run it as a jupyter notebook so I can randomise my selections whilst I'm out and about. So I have everything in app.py. No imports except the XML file
2. I also have a database to store my full library and i'm not sure which direction i'm going at the moment but for Carnets I have to use plist to read from the xml but on my laptop I'm going to utilise postgresql instead. 

To use you need to open apple music on a mac device - click file - library - export to xml and then save it. This is where it pulls the data from. I've got multiple devices so I made the decision to upload my xml file to github so I can make improvements on other devices if I feel like it. Otherwise I would've hidden it but it's up to you. 

Sample Output: 
['PSYCHOFRAME']
