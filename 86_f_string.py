def demo():
    track = "Perfect"
    artist = "ed sheeran"
    album = "divide"
    download = 1234567
    print(f"tract name = {track}, artist = {artist}, download = {download:,}")   # string interpolation
    print("tract name = {}, artist = {}".format(track, artist))


if __name__ == '__main__':
    demo()
