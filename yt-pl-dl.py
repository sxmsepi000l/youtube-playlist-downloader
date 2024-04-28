from pytube import Playlist

print('WELCOME TO PLAYLIST DOWNLOADER DEVELOPED BY - www.github.com/sxmsepi000l')

def download_playlist(url):
    # Initialize the playlist object
    playlist = Playlist(url)

    # Print playlist title
    print("Downloading playlist:", playlist.title)

    # Iterate over each video in the playlist
    for video in playlist.videos:
        # Print video title
        print("Downloading:", video.title)
        
        # Download the video in the highest resolution with both video and audio
        try:
            video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            print("Downloaded successfully!")
        except Exception as e:
            print("Error downloading video:", e)

if __name__ == "__main__":
    # URL of the YouTube playlist
    playlist_url = "Your Link Here"

    # Call the function to download the playlist
    download_playlist(playlist_url)
