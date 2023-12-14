#!/bin/sh

if [ -d "venv" ]; then
	true
else
	python -m venv venv
	source venv/bin/activate

	pip install pysimplegui
	pip install ffmpeg-python
fi

source venv/bin/activate
python video2audio.py
