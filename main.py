from flask import Flask, send_from_directory
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/videos')
def list_videos():
    """
    Returns all the list of videos inside `videos` folder.
    """
    video_dir = os.path.join(os.getcwd(), 'videos')
    videos = [f for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f))]
    return '<br>'.join(videos)


@app.route('/videos/<path:path>')
def get_video(path):
    # Access video like: "http://localhost:5000/videos/myvideo.mp4"
    return send_from_directory('videos', path)

if __name__ == '__main__':
    app.run(debug=True)
