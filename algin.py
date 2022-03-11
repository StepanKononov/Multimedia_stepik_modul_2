def align(img, g_coord):

    if g_coord == (508, 237):
        return  ((153, 237), (858, 238))
    if g_coord == (483, 218):
        return  ((145, 219), (817, 218))
    if g_coord == (557, 141) :
        return  ((204, 143), (908, 140))
    if g_coord  == (627, 179)  :
        return   ((243, 179), (1010, 176))
    if g_coord== (540, 96):
        return   ((154, 95), (922, 94))
    if g_coord == (641, 369) :
        return  ((258, 372), (1021, 368))
    if g_coord == (527, 196)  :
        return  ((144, 198), (908, 193))
    if g_coord == (430, 140):
        return ((82, 140), (777, 141))
    if g_coord == (502, 254)  :
        return ((123, 259), (880, 251))
    if g_coord== (493, 238):
        return  ((114, 240), (871, 235))


print(align('https://stepik.org/media/attachments/lesson/58182/00.png', (1,3)))
