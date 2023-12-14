import PySimpleGUI as sg
import ffmpeg
import os

def video2audio(input_path, output_path):
    video = ffmpeg.input(input_path)
    audio = ffmpeg.output(video, output_path, y="-y")
    ffmpeg.run(audio)

def check_and_convert(video_path, audio_path):
    if os.path.exists(audio_path):
        confirm = sg.popup_yes_no(f"The file '{audio_path}' already exists. Do you want to overwrite it?")
        if confirm == "No":
            return
    video2audio(video_path, audio_path)
    sg.popup(f"Conversion completed. Audio saved to {audio_path}")

video_column = [
    [
        sg.Text("Video"),
        sg.In(size=(25, 1), enable_events=True, key="-VIDEO-"),
        sg.FileBrowse(),
    ]
]

layout = [
    [sg.Column(video_column)],
    [sg.Button("video2audio")],
]

window = sg.Window("video2audio", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "video2audio":
        video_path = values["-VIDEO-"]
        if video_path:
            base_path, _ = os.path.splitext(video_path)
            audio_path = base_path + ".mp3"
            check_and_convert(video_path, audio_path)

window.close()
