Album Selector: 
A personal music randomiser built to break me out of my comfort zone.

Why I Built This: 
I love music - but I tend to default to the same comfort bands and albums (Lorna Shore :D). So I built a tool that removes the element of choice and lets randomness guide my listening. It's a fun way to rediscover forgotten tracks and explore my library with fresh ears as well as work on a very fun project that keeps me deeply interested.

I exported my Apple Music library as an XML file and used it as the foundation for this project. 

To use you need to open apple music on a mac device - click file - library - export to xml and then save it. This is where it pulls the data from. I've got multiple devices so I made the decision to upload my xml file to github so I can make improvements on other devices if I feel like it. Otherwise I would've hidden it but it's up to you. #

I have built this program to work with the IOS app "carnets" which is why it's kinda bad code. It needs to work easily with a mobile keyboard so I've designed it to work so i call the same function everytime then just pass in the number for the function I want to call. 

I have also written my library to a database as well in case I decide to expand this later. 

Sample Output: 
['Mercenary', 'I Hope We Make It Out of This Alive', 'In Medias Res']
