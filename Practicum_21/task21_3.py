class Track:
    def __init__(self, title, duration, artist, year):
        self._title = title
        self._duration = duration
        self._artist = artist
        self._year = year

        self._is_playing = False
        self._is_paused = False

    def get_title(self):
        return self._title

    def get_duration(self):
        return self._duration

    def get_artist(self):
        return self._artist

    def get_year(self):
        return self._year

    def play(self):
        self._is_playing = True
        self._is_paused = False

    def pause(self):
        if self._is_playing:
            self._is_paused = True
            self._is_playing = False

    def stop(self):
        self._is_playing = False
        self._is_paused = False

    def __str__(self):
        status = "stopped"
        if self._is_playing:
            status = "playing"
        elif self._is_paused:
            status = "paused"

        return f"{self._artist} - {self._title} ({self._year}, {self._duration} sec) [{status}]"
    

class Album:
    def __init__(self, name, artist, year):
        self._name = name
        self._artist = artist
        self._year = year
        self._tracks = []

    def add_track(self, track: Track):
        self._tracks.append(track)

    def remove_track(self, title):
        for t in self._tracks:
            if t.get_title() == title:
                self._tracks.remove(t)
                return True
        return False

    def play_all(self):
        for t in self._tracks:
            t.play()

    def stop_all(self):
        for t in self._tracks:
            t.stop()

    def get_tracks(self):
        return self._tracks

    def __str__(self):
        result = f"Album: {self._name} ({self._year})\n"
        result += f"Artist: {self._artist}\n"
        result += "Tracks:\n"
        for t in self._tracks:
            result += "  " + str(t) + "\n"
        return result