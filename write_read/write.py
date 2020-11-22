def create_write_to_file(result):
    f = open("output.out", "w+")
    f.write(str(result))
    f.close()