# Central Perk

There are a lot of FRIENDS fans out there who wish they could have little more of FRIENDS. This project aims are generating texts from the older dialogues of the show using tensorflow. I aim at launching it as a standalone webapp where user can generate new scripts on their device using tensorflow.js 

## Installation

Currently this repo need tensorflow and it is written in Python. Install latest tesnorflow first using:
```bash
pip install tensorflow
```

## Usage

- Title Generation: You can generate new titles of the show using the generateTitles.py file which uses the pretrained model. You can retrain the model as well. It still needs some fine tuning.
- Dialogues Generation: This is not yet implemented but it is supposed to take a character name as parameter and their first word and generate new texts based on their older ones. I'll be adding this in the upcoming weeks.

## Milestones

- [x] Scrape transcripts and separate titles and dialogues.
- [x] Generate titles
- [ ] Remove unknown alphabets from title
- [ ] Generate texts for each character
- [ ] Convert for tensorflow.js
- [ ] Deploy as a React app


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Notice
The dialogues and episode titles may be subject to copyright by the writers Marta Kauffman & David Crane or the production hous. I have downloaded and processed the transcripts from this [repository](https://github.com/puneeth019/FRIENDS).
