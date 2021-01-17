# finetuned
Hack the North 2020++ project!

A web app that edits photos to match the mood and lyrics of a song.

## Demo

## Getting Started
### Prerequisites
This project was built using Python3, which can be installed [here](https://www.python.org/downloads/). 

### Installation
1. Clone [this repository](https://github.com/ryli123/finetuned) onto your local device
2. The files `spotify.py` and `genius.py` both require API keys. 
3. A Spotify API key can be acquired at [this link](https://developer.spotify.com/documentation/web-api/quick-start/). Copy both the client_id and secret into `cid = ''
secret=''`, respectively, in `spotify.py`
4. An API token for Genius can be acquired pursuant to these [instructions](https://docs.genius.com/#/getting-started-h1). This should be copied into `API_TOKEN = ''` in `genius.py`
5. A token is also needed for Microsoft Azure. More information can be found [here](https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/). The subscription key and endpoint should replace `subscription_key = ""` and `endpoint = ""` in `genius.py`

### Deployment 
1. Run `python server.py` from command line in the main folder.
2. The web app should open locally at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
A user may choose to explore the home page briefly. To upload photos, they can either navigate from the home page or using the Navbar to get to [http://127.0.0.1:5000/start](http://127.0.0.1:5000/start). Following this, the user follows through a fairly self-explanatory procedure of selecting a song before viewing how the photos are edited accordingly.

### Known Bugs
Due to some caching issues, when the same image is loaded in multiple times to be viewed properly on screen in their edited form.

### Future Steps
Some immediate next steps we could take involve making a more user-friendly interface for users to download their edited photos, as well as further working through the details of the tuning algorithm.

Long term, AI could have play a potential role in the photo-editing process. Currently, the coefficients used in photo-editing are hand-picked; however, with more sample data, it is possible that neural networks could make the process more consistent.


## Built With
-  [Flask] (https://flask.palletsprojects.com/en/1.1.x/) - Web Framework
-  [Bootstrap Navbar] (https://getbootstrap.com/docs/4.0/components/navbar/) - Bootstrap components
-  [Jinja] (https://jinja.palletsprojects.com/en/2.11.x/) - Web Template Engine

## Acknowledgements
Inspiration was drawn from:
-  [Osvaldas Valutis](https://tympanus.net/codrops/2015/09/15/styling-customizing-file-inputs-smart-way/) and his form input styling
