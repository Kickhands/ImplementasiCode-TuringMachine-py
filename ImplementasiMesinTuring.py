class TuringMachine:
    def __init__(self, tape, start_state, accept_state, reject_state, transition_table):
        # Inisialisasi mesin Turing dengan pita, status awal, status diterima, status ditolak, dan tabel instruksi
        self.tape = list(tape)  # Mengubah input pita menjadi list simbol
        self.head = 0  # Kepala mulai berada di awal pita (indeks 0)
        self.state = start_state  # Status awal mesin Turing
        self.accept_state = accept_state  # Status jika string diterima
        self.reject_state = reject_state  # Status jika string ditolak
        self.transition_table = transition_table  # Tabel instruksi yang berisi aturan transisi

    def step(self):
        """Melakukan satu langkah eksekusi mesin Turing."""
        current_symbol = self.tape[self.head]  # Membaca simbol yang ada di posisi kepala
        if (self.state, current_symbol) in self.transition_table:
            # Jika ada aturan transisi untuk kombinasi status dan simbol yang dibaca
            new_state, new_symbol, move_direction = self.transition_table[(self.state, current_symbol)]
            # Menulis simbol baru pada pita sesuai aturan transisi
            self.tape[self.head] = new_symbol
            # Memperbarui status mesin dengan status baru
            self.state = new_state
            # Menggerakkan kepala sesuai arah yang ditentukan (kiri atau kanan)
            if move_direction == "L":
                self.head -= 1  # Jika arah kiri, bergerak satu posisi ke kiri
            elif move_direction == "R":
                self.head += 1  # Jika arah kanan, bergerak satu posisi ke kanan
            return True
        else:
            # Jika tidak ada aturan transisi untuk kondisi saat ini, mesin berhenti dan menolak input
            return False

    def run(self):
        """Menjalankan mesin Turing hingga mencapai status diterima atau ditolak."""
        while self.state != self.accept_state and self.state != self.reject_state:
            # Terus lakukan langkah sampai mencapai status diterima atau ditolak
            if not self.step():
                break  # Jika tidak ada langkah yang dapat dilakukan, berhenti
        return self.state == self.accept_state  # Mengembalikan True jika string diterima, False jika ditolak


# Tabel instruksi untuk bahasa a^n b^n
transition_table = {
    ('start', 'a'): ('find_b', 'X', 'R'),  # Jika membaca 'a', tandai dengan 'X' dan pindah ke status find_b
    ('find_b', 'b'): ('check_end', 'Y', 'L'),  # Jika membaca 'b', tandai dengan 'Y' dan pindah ke status check_end
    ('check_end', 'a'): ('find_b', 'X', 'R'),  # Kembali ke find_b untuk mencari pasangan 'b' selanjutnya
    ('check_end', 'Y'): ('accept', 'Y', 'R'),  # Jika menemukan 'Y' (akhir dari pita), terima string
    ('find_b', 'Y'): ('find_b', 'Y', 'R'),  # Lewati simbol 'Y' jika ditemukan
    ('find_b', 'X'): ('find_b', 'X', 'R'),  # Lewati simbol 'X' jika ditemukan
    ('start', 'Y'): ('start', 'Y', 'R'),  # Lewati simbol 'Y' yang ada di pita
    ('start', ' '): ('accept', ' ', 'R'),  # Jika menemukan blank space (akhir pita), terima string
}

# Contoh input string "aabb"
tm = TuringMachine(tape="aabb", start_state="start", accept_state="accept", reject_state="reject", transition_table=transition_table)

# Menjalankan mesin Turing dan memeriksa apakah string diterima
result = tm.run()

if result:
    print("String diterima")  # Jika mesin Turing menerima string, tampilkan pesan diterima
else:
    print("String ditolak")  # Jika mesin Turing menolak string, tampilkan pesan ditolak
