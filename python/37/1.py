# Воспроизведение мультимедиа
#
# Создайте два класса:
#
# AudioFileMixin — требует наличие поля audio_tracks (список треков).
# Метод play_audio() выводит:
#
# Воспроизведение аудио для <НазваниеКласса>:
#
# <название трека>
#
# <название трека>
#
# VideoFileMixin — требует наличие поля video_files (список видео).
# Метод play_video() выводит:
#
# Воспроизведение видео для <НазваниеКласса>:
#
# <название видео>
#
# <название видео>
#
# Если нужное поле отсутствует — выбрасывайте AttributeError.
#
# Устройства
#
# Создайте два класса:
#
# MediaPlayer — поддерживает только аудио. Принимает список треков.
#
# Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
#
# Проверьте работу классов, вызвав методы воспроизведения.
#
# Данные:
#
# tracks = ["track1.mp3", "track2.mp3"]
#
# movies = ["movie.mp4", "trailer.mov"]
#
#
# Пример вывода:
#
# Воспроизведение аудио для MediaPlayer:
#
# track1.mp3
#
# track2.mp3
#
# Воспроизведение аудио для Laptop:
#
# track1.mp3
#
# track2.mp3
#
# Воспроизведение видео для Laptop:
#
# movie.mp4
#
# trailer.mov


class AudioFileMixin:
    """Добавляет объекту возможность воспроизводить список аудиотреков."""

    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError(
                f"{type(self).__name__} не содержит поля audio_tracks"
            )

        print(f"Воспроизведение аудио для {type(self).__name__}:")
        for track in self.audio_tracks:
            print(track)


class VideoFileMixin:
    """Добавляет объекту возможность воспроизводить список видео."""

    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError(
                f"{type(self).__name__} не содержит поля video_files"
            )

        print(f"Воспроизведение видео для {type(self).__name__}:")
        for video in self.video_files:
            print(video)


class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = list(audio_tracks)


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = list(audio_tracks)
        self.video_files = list(video_files)


if __name__ == "__main__":
    tracks = ["track1.mp3", "track2.mp3"]
    movies = ["movie.mp4", "trailer.mov"]

    player = MediaPlayer(tracks)
    laptop = Laptop(tracks, movies)

    player.play_audio()
    laptop.play_audio()
    laptop.play_video()
