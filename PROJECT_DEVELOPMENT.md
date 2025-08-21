# Year 9 CT Task 3

## Phase 1
### Question
My question for this project is: "What is the most popular Australian rock album, and who has the most albums?"

### Hypothesis
#### Back In Black is the most poplar Australian rock album, but Jimmy Barnes has the most albums

---

My hypothesis is: "Back In Black is the most popular Australian rock album, but Jimmy Barnes has the most albums". This stems from the fact that Back In Black is considered one of the most influential albums of all time, while Jimmy Barnes has been releasing albums non stop since 1984.

### Functional And Non-Functional Requirements
Functional Requirements:  
- Successfully create and load the dataset
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

The dataset has already been preloaded into the system by a programmer.

The user has access to the system interface.

Main Flow:

User opens the program and is presented with an app. It opens to a menu with some options.

User selects one of the following options:
a. View top 10 albums by total streams and every artist's total streams
b. View pie chart of % of total albums by each artist
c. View each album by an artist's streams
d. View full dataset
e. Quit the program

System performs the requested action and outputs to user.

Postconditions:

User has viewed and/or interacted with the data.

Any valid updates are saved by the system.

Data remains available for further queries or analysis.

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
Peer 1 -

Peer 2 - 

Peer 3 - 

