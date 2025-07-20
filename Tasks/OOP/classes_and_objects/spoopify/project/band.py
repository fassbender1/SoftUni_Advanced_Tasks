from project.album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    # def remove_album(self, album_name: str) -> str:
    #     if Album.published:
    #         return f"Album has been published. It cannot be removed."
    #     if album_name not in Band.albums:
    #         return f"Album {album_name} is not found."
    #     Band.albums.remove(album_name)
    #     return f"Album {album_name} has been removed."
    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self) -> str:
        result = f"Band {self.name}\n"
        second_part = "\n".join(album.details() for album in self.albums)
        return result + second_part
    # def details(self):
    #     result = [f"Band {self.name}"]
    #     for album in self.albums:
    #         result.append(album.details())
    #     return "\n".join(result)

