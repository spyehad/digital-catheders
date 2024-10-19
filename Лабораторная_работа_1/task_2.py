
disk_mem_in_mb = 1.44 #Mb
disk_mem_in_bites = disk_mem_in_mb * 1024 * 1024
pages = 100
rows = 50
chars = 25
char_mem = 4 # Bites
book_mem_in_bites = pages * rows * chars * char_mem
book_count = int(disk_mem_in_bites / book_mem_in_bites)

print("Количество книг, помещающихся на дискету:", book_count)
