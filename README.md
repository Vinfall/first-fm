## Intro

A Python script using [pylast](https://github.com/pylast/pylast) to perform Last.FM (or other compatible API like Libre.FM) initialization for your local music library, therefore *First*.FM.

## Usage

### TL;DR

1. Get your Last.fm API key [here](https://www.last.fm/api/account/create)
2. Copy `.env.local.example` to `.env.local` and replace the content with your credentials
3. Put `tracks.txt` in the same directory
4. Run the sciript
5. Done

### Detailed Instruction

```sh
git clone https://github.com/Vinfall/First-FM
cd First-FM
# If you prefer a virtual Python envrionment
# virtualenv venv
# source ./venv/bin/activate
pip install -r requirements.txt
cp .env.local.example .env.local

# Modify .env.local aoocrdingly
vim .env.local

# Put `tracks.txt` in the same directory of `first-fm.py`
mv /some/where/tracks.txt ./tracks.txt

python first-fm.py
```

### `tracks.txt` Format

The script would do some sanitization but it's advised to make the file clean in the first place, at least every line follows the format of `Artist - Title`.

Or check [`tracks.txt.example`](tracks.txt.example):

```
Artist - Title

Adele - Rolling in the Deep
Ayumi - 華暦
fripSide - LEVEL5-judgelight-
```

## [License](LICENSE)

Licensed under BSD 3-Clause.
