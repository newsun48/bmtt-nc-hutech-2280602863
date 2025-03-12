class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        # Loại bỏ các ký tự trùng lặp trong key và chỉ giữ lại chữ cái A-Z (bỏ qua 'J')
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
        matrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không có 'J' trong bảng Playfair

        for char in key:
            if char not in matrix:
                matrix.append(char)

        for char in alphabet:
            if char not in matrix:
                matrix.append(char)

        # Tạo bảng 5x5
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        # Tìm vị trí của một ký tự trong bảng Playfair
        for i, row in enumerate(matrix):
            if letter in row:
                return i, row.index(letter)
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
        # Làm sạch văn bản (chỉ giữ chữ cái A-Z, thay 'J' bằng 'I')
        plain_text = plain_text.replace("J", "I").upper()

        # Chia plaintext thành cặp chữ cái
        i = 0
        prepared_text = []
        while i < len(plain_text):
            if i + 1 < len(plain_text) and plain_text[i] == plain_text[i + 1]:
                prepared_text.append(plain_text[i] + 'X')  # Thêm 'X' nếu có chữ cái trùng
                i += 1
            else:
                prepared_text.append(plain_text[i:i + 2])
                i += 2

        cipher_text = ""
        for pair in prepared_text:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Nếu cùng hàng, dịch sang phải
                cipher_text += matrix[row1][(col1 + 1) % 5]
                cipher_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Nếu cùng cột, dịch xuống dưới
                cipher_text += matrix[(row1 + 1) % 5][col1]
                cipher_text += matrix[(row2 + 1) % 5][col2]
            else:
                # Nếu không cùng hàng và cột, đổi chéo
                cipher_text += matrix[row1][col2]
                cipher_text += matrix[row2][col1]

        return cipher_text

    def playfair_decrypt(self, cipher_text, matrix):
        # Làm sạch ciphertext (thay 'J' bằng 'I')
        cipher_text = cipher_text.replace("J", "I").upper()

        # Chia ciphertext thành cặp chữ cái
        i = 0
        prepared_text = []
        while i < len(cipher_text):
            prepared_text.append(cipher_text[i:i + 2])
            i += 2

        plain_text = ""
        for pair in prepared_text:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Nếu cùng hàng, dịch sang trái
                plain_text += matrix[row1][(col1 - 1) % 5]
                plain_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Nếu cùng cột, dịch lên trên
                plain_text += matrix[(row1 - 1) % 5][col1]
                plain_text += matrix[(row2 - 1) % 5][col2]
            else:
                # Nếu không cùng hàng và cột, đổi chéo
                plain_text += matrix[row1][col2]
                plain_text += matrix[row2][col1]

        return plain_text
