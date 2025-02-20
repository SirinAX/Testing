def print_right_triangle(height):
    for i in range(1, height + 1):
        # Mencetak bintang
        for j in range(i):
            print("*", end="")
        
        # Pindah ke baris berikutnya
        print()

def main():
    try:
        height = int(input("Masukkan tinggi segitiga: "))
        if height < 1:
            print("Tinggi segitiga harus berupa integer positif.")
        else:
            print_right_triangle(height)
    except ValueError:
        print("Harap masukkan integer yang valid.")

if __name__ == "__main__":
    main()
