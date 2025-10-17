#Páginas
pages = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]

#Quadros memória
frame_count = 8
frames = []

last_page = pages[-1]

#FIFO
for page in pages:
    if page not in frames:
        if len(frames) < frame_count:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)

#Estado final dos quadros
print("Quadros finais:", frames)

#Diz em qual quadro ficou a última página inserida.
index_last_page = frames.index(last_page) if last_page in frames else None
print("A última página está no quadro:", index_last_page)
