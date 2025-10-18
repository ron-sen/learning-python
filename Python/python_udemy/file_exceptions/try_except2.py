
def art_accessories(canvas):
    try:
        print(f"Canvas size {canvas} ...")
        if canvas == "unknown":
            raise ValueError("Canavs size not possible")
    except ValueError as e:
        print("Error: " , e)
    else:
        print(f"size is { canvas}")
    finally:
        print("Whihch type of colors you need ?")

art_accessories("20cm")
art_accessories("unknown")                         