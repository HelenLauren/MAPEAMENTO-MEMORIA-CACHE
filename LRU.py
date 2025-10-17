#Páginas
pages = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]

#Quadros
frame_count = 8
frames = []

last_page = pages[-1]

#LRU
for page in pages:
    if page in frames:
        #se a página já está nos quadros, atualizamos sua posição (mais recentemente usada)
        frames.remove(page)
        frames.append(page)
    else:
        if len(frames) < frame_count:
            frames.append(page)
        else:
            #remove a página menos recentemente usada (primeira da lista)
            frames.pop(0)
            frames.append(page)

#Estado final dos quadros
print("Quadros finais:", frames)


#Diz em qual quadro ficou a última página inserida.
index_last_page = frames.index(last_page) if last_page in frames else None
print("A última página está no quadro:", index_last_page + 1)
