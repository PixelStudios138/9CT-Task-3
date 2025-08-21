# Year 9 CT Task 3

## Phase 1
### Question
My question for this project is: "What is the most popular Australian rock album, and who has the most albums?"

### Hypothesis
#### Back In Black is the most poplar Australian rock album, but Jimmy Barnes has the most albums

---

My hypothesis is: "Back In Black is the most popular Australian rock album, but Jimmy Barnes has the most albums". This stems from the fact that Back In Black is considered one of the most influential albums of all time, while Jimmy Barnes has been releasing albums non stop since 1984.

### Mind Map

![Mind Map of question possibilities](/Images/mindmap.png "Mind Map of Choices")  

### Functional And Non-Functional Requirements
Functional Requirements:  
- Successfully create and load the dataset
- Clean any missing data and convert any wrong entries into the right datatype
- Should be visualised in a Matplotlib chart (unless dataset is being viewed)
- Charts should be saved when viewed

Non Functional Requirements:  
- User Interface should be simple and easy to use
- UI should function well
- UI should try to be in an app, but text based can be used if necessary
- System should correctly display errors to users
- System should have a error system and display the right errors.

### Use Case
Actor: User

Goal: To access and interact with existing data through the program’s user interface.

Preconditions:

The dataset (`Album Streams.csv`) has already been preloaded into the system by a programmer.

The user has access to the system interface.

Main Flow:

User opens the program and is presented with an text based interface. It opens to a menu with some options.

User selects one of the following options by writing the respective number:  
a. View top 10 albums by total streams and every artist's total streams  
b. View pie chart of % of total albums by each artist  
c. View each album by an artist's streams  
d. View full dataset  
e. Quit the program  

System performs the requested action and outputs to user.

Postconditions:

User has viewed the data.

Any new charts are saved by the system.

Data and charts remains available for further queries or analysis.

## Phase 2
### Current Information
I can access data directly from Spotify, which I intend to do for this assessment. For the purpose of keeping the dataset a decent size and unbiased, I am going to be looking at the following artists: AC/DC, The Screaming Jets, Cold Chisel, Jimmy Barnes, Ian Moss, Noiseworks, Icehouse, The Angels, Midnight Oil, Rose Tattoo, INXS, Australian Crawl, and The Choirboys. I can access data for total streams on songs and albums, and use that to form my dataset.

### Data Dictionary

|Field         |Data Type |Format For Display | Description                         | Example   | Validation                                       |
|--------------|----------|-------------------|-------------------------------------|-----------|--------------------------------------------------|
|Album         |object    |XX..XX             |Name of the album                    |Hysteria   |Can be any amount of characters, including numbers|
|Artist        |object    |XX..XX             |Name of the artist who made the album|Def Leppard|Can be any amount of characters, including numbers|
|Total Streams |int64     |NNN                |Total number of streams of the album |123456789  |Must be a whole number, not seperated by commas   |
|Artist Streams|int64     |NNN                |Total number of streams of the artist|987654321  |Must be a whole number, not seperated by commas   |

## Phase 4
### Analysis
From my findings, I can conclude that Back In Black is the most popular Australian rock album, and Jimmy Barnes does have the most albums of the 13 artists analysed. When looking at the top 10 albums, Back In Black is at the top with 4.75 billion total streams. AC/DC also hold the second and third spot with Highway To Hell and The Razor's edge respectively. When looking at the share of albums per artist, Jimmy Barnes holds the top spot with 15.4% of the 130 albums in the dataset, as he has 21 albums. This aligns perfectly with my hypothesis. After multiple runs of the code, it returns the same result multiple times, proving its accuracy.

### Peer Analysis  
**Peer 1 - Benji**  
Plus: Very effective to visualise the sales of individual albums. Uses multiple graphs to show different pieces of data. Interface gives clean and efficient user experience.  
Minus: No error handling if you do not enter a valid artist, the program quits instead. Artists are not ordered by sales (minor)  
Implication: The program is very good when you enter knowing exactly what data you hope to get, e.g. wanting to know how much Cold Chisel sold. Visualising with multiple graphs is very helpful to understand scale as well, however the case sensitivity can make it difficult to navigate individual artists if you are not well versed in music. Overall extremely solid work.

Mine for him:  
Plus: User interface is smooth and provides a nice, friendly user experience. Graphs are visualised well, and it is easy to view the data for a certain period of time (e.g 1991-2002)  
Minus: Only uses 1 graph which becomes a bit clunky when the whole time period is seen.  
Implication: The program makes it easy to view data on batting-friendly and bowling-friendly periods in cricket, especially in different periods (e.g. whether Mark Waugh played in a bowling or batting-friendly period). Graph for whole dataset does get a bit clunky. Overall a really good effort  

**Peer 2 - Sidd**  
Plus: Clean UI, well structured, interactive, good graphs  
Minus: Limited data when viewing raw datasets and nav UI gets long and clunky after a while  
Implication: Leads to a lack of transparency and an overpowering of UX

Mine For Him:  
Plus: User interface is smooth and provides a friendly user experience. The usage of an app makes it easier to navigate. The graphs are laid out well and easy to understand  
Minus: When navigating between different sections, it shut and opened different apps, which was a slight pain. There was no way to go back to the home page on the data visualisation though, so the app had to be forced to quit. When that happened, the program didn't stop running  
Implication: Program functions well and provides a mostly smooth way of viewing the data. The few bumps caused by the application interface are annoying at times, but not enough to ruin the UX. Overall a really good program  

**Peer 3 - Minh**  
Plus - The code is very simple and straightforward to understand and works the way it should be  
Minus - I don't see anything wrong with the code but you can clean up the repo to keep only the code, csv, the markdown and essential files only  
Implication - There is a quit option  

Mine for him:  
Plus: Charts are well defined and clearly relevant data. Multiple charts help to show the data better. Saving figures works  
Minus: Error handling isn't the best, and the code doesn't loop, so the program has to be restarted after each selection  
Implication: Program works quite well, and the UI functions well. The UX is brought down by the forced restarts if all charts want to be viewed. Overall a pretty good effort  

### Evaluations
**Requirements Outline**  
I believe my code successful in most areas of functional and non-functional requirements. The dataset is loaded in every case, and is cleaned, converting the entries in the `Total Streams` and `Artist Streams` column into integers, as they are initially loaded as comma seperated strings. All data requested (except for the whole dataset) is viewed in matplotlib charts, and they are all saved as images. The user interface is simple to use and functions well, however it is in a text-based format when I initially aimed for an app based. The system does not have an error system like I aimed, and I noticed that wrong inputs just simply work.

**Peer Feedback**  
My assessment holds up pretty well from peer feedback. A friend from another Computer Tech class, Benji, praised the user interface and experience, wide rang of graphs, and visualisation. He did say that the error handling does let me down, and that it could be better if artists were organised by streams like albums (when viewing the first graph). Minh also praised the UI and UX, and couldn't find anything with the code. He did mention that the project could be organised a bit better, which I do agree with. Sidd also praised the structure, and the UI and UX. He felt that the dataset was a bit limited, and that the UI gets clunky if used for too long, which is quite true. Having to manually enter the data, it does feel limited, but I feel that I analysed well enough to make up for it.

**Project Management**  
I managed my project pretty well. For the code, it was well managed, I tried to mitigate as many bugs I could find. I had all functions for my code in the `data_module.py` script, and the rest (which was just UI) was in the `main.py` script. I organised it well, having images of the mind map and graphs saved in the `Images` folder. However, time management wasn't the best, as I initially wanted to collect my own data, but my form wasn't released, so I lost a week waiting for that. However, I think my project was managed pretty well.

**Data And Security**  
The data is accurate, as I got it from 2 sources, Spotify and `kworb.net`. It is valid, as it does measure exactly what it needs to. The 2 sources help reduce its bias, but it is somewhat biased as I only focused on 13 artists instead of the hundreds that there are. The data is accurate of 1/8/2025, as that's the last time I updated the dataset, so any streams after that date aren't counted. The security does not need updating, and the UX could be more accessible if it was in app format rather than the text based format I ended up using.

## Conclusion
My project is extremely successful in providing a user friendly way to view data on Australian rock albums. This markdown file has successfully documented the entire process of making this, from intial conception to evaluation. I have poured my heart and soul into this, and I hope it pays off. Thank you for your time.
