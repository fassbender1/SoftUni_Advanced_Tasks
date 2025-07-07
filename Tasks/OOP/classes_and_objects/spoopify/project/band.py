from project import album
from project.album import Album


class Band:
    albums = []
    def __init__(self, name: str):
        self.name = name

    def add_album(self, album: Album) -> str:
        if album.name in Band.albums:
            return f"Band {self.name} already has {album.name} in their library."
        Band.albums.append(album.name)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        if album.published:
            return f"Album has been published. It cannot be removed."
        if album_name not in Band.albums:
            return f"Album {album_name} is not found."
        Band.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self) -> str:
        result = f"Band {self.name}\n"
        second_part = Album.details()
        return result + second_part

    # def details(self):
    #     result = [f"Band {self.name}"]
    #     for album in self.albums:
    #         result.append(Album.details())
    #     return "\n".join(result)

