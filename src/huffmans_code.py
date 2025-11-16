import heapq
from collections import Counter

class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq

class Huffman:

    def __init__(self):
        self.codes = {}
        self.reversing = {}
    
    def build_frequency_dict(self, text):
        return Counter(text)
    
    def build_heap(self, frequency):
        heap = []
        for char, freq in frequency.items():
            node = TreeNode(char, freq)
            heapq.heappush(heap, node)
        return heap

    def build_tree(self, heap):
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            merged = TreeNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(heap, merged)

        if heap:
            return heap[0]
        
        return None

    def assigment(self, root, code):
        if root is None:
            return
        
        if root.char is not None:
            self.codes[root.char] = code
            self.reversing[code] = root.char
            return

        self.assigment(root.left, code + '0')
        self.assigment(root.left, code + '1')

    def building(self, root):
        self.codes = {}
        self.reverse = {}
        if root:
            self.assigment(root, '')
        
    def get_encoded(self, text):
        encoded = ''
        for char in text:
            encoded += self.codes[char]
        return encoded

    def filling(self, encoded):
        fill = 8 - len(encoded) % 8
        for i in range(fill):
            encoded += '0'

        return encoded
    
    def get_byte(self, fill_text):
        b = bytearray()
        for i in range(0, len(fill_text), 8):
            byte = fill_text[i:i+8]
            b.append(int(byte, 2))
        return b
    
    def compress(self, text):
        frequency = self.frequency_dict(text)
        heap = self.build_heap(frequency)
        root = self.build_tree(heap)
        self.assigment(root)

        encoded_text = self.get_encoded(text)
        filling_text = self.filling(encoded_text)
        byte_array = self.get_byte(filling_text)

        return bytes(byte_array)

    def remove_filled(self, filling_text):
        fill_info = filling_text[:8]
        fill = int(fill_info, 2)

        filling_text = filling_text[:8]
        if fill > 0:
            encoded_text = filling_text[:-fill]
        else:
            encoded_text = filling_text

        return encoded_text

    def decode(self, encoded_text):
        current_code = ''
        decoded_text = ''

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reversing:
                char = self.reversing[current_code]
                decoded_text += char
                current_code = ''

        return decoded_text

    def decompress(self, compressed_text):
        bit_string = ''
        for byte in compressed_text:
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits

        encoded_text = self.remove_filled(bit_string)
        decompressed = self.decode(encoded_text)

        return decompressed

