def mru(pages, frame_count):
    frames = []
    last_page = pages[-1]
    
    for page in pages:
        if page in frames:
            frames.remove(page)  #atualiza para mais recentemente usada
            frames.append(page)
        else:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                #remove a página mais recentemente usada (última da lista)
                frames.pop(-1)
                frames.append(page)
                
    index_last_page = frames.index(last_page) if last_page in frames else None
    print("Quadros finais:", frames)
    print("A última página está no quadro:", index_last_page + 1, "\n")


#Sequências exemplo:
sequences = [
    [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7],
    [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11],
    [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
]

frame_count = 8

#MRU em cada sequência
for i, pages in enumerate(sequences, 1):
    print(f"===== Sequência {i} =====")
    mru(pages, frame_count)