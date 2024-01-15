#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reference
# https://github.com/pylast/pylast/blob/main/tests/test_pylast.py
# https://code.input.sh/-/snippets/2

import os
import pylast
import re
import time

_TRACK_FILE = "tracks.txt"
# Block word list
_TO_REPLACE = [
    " \(合唱版\)",
    " \(双语版\)",
    " \(钢琴版\)",
    " \(国\)",
    " \(粤语版\)",
    " \(TV.*?[Vv]er(sion)?(\.)?\)",
    # " \(Live\)",
    " \(Clean\)",
    " \(Off Vocal\)",
    " \(Instrumental\)",
]
# Ignore word list
_TO_IGNORE = [
    "纯音乐",
    "Pure Music",
]

def load_secrets():
    # Load screct credentials from local file
    secrets_file = ".env.local"
    if os.path.isfile(secrets_file):
        with open(secrets_file, 'r') as f:
            lines = f.readlines()
            doc = {}
            for line in lines:
                if '=' in line:
                    key, value = line.split(' = ')
                    doc[key.strip()] = value.strip().strip('"')
    else:
        # Load screct credentials from environment variables
        doc = {
            "API_KEY": os.environ.get("PYLAST_API_KEY", "").strip(),
            "API_SECRET": os.environ.get("PYLAST_API_SECRET", "").strip(),
            "username": os.environ.get("PYLAST_USERNAME", "").strip(),
            "password": os.environ.get("PYLAST_PASSWORD", "").strip()
        }
        if not all(doc.values()):
            raise EnvironmentError("Missing environment variables, check .env.local")
    return doc

def read_tracks_file():
    tracks = []
    with open(_TRACK_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # Split using only the first occurrence of ' - '
            artist, title = line.strip().split(' - ', 1)
            track_info = {
                "artist": artist,
                "title": title
            }
            tracks.append(track_info)
    return tracks

secrets = load_secrets()

username = secrets["username"]
password_hash = pylast.md5(secrets["password"])
api_key = secrets["API_KEY"]
api_secret = secrets["API_SECRET"]

network = pylast.LastFMNetwork(
    api_key=api_key,
    api_secret=api_secret,
    username=username,
    password_hash=password_hash,
)

tracks = read_tracks_file()
for track in tracks:
    artist = track["artist"]
    # Replace unexpected trailing abominations
    for keyword in _TO_REPLACE:
        title = re.sub(keyword, "", track["title"])
    # Ignore certain type of tracks
    if artist != "ID" and not any(keyword in title for keyword in _TO_IGNORE):
        last_api_call = network.scrobble(artist, title, int(time.time()))
    print ("Scrobbled: " + artist + " - " + title)
