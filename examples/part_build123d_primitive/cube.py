import build123d as bd

with bd.BuildPart() as result:
    bd.Box(5, 5, 5)

if "show_object" in locals():
    # show_object(result.part.solid(), name="art")
    show_object(result.part.solid().wrapped, name="art")
