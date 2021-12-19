from tkinter import *
import heapq
from collections import Counter
from collections import namedtuple
from tkinter import ttk

window = Tk()
window.title('Huffman')
window.geometry('300x115-600-300')
window.config(bg='#EBEBEB')
window.resizable(False, False)


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, num):
        self.left.walk(code, num + "0")
        self.right.walk(code, num + "1")


class Leaf(namedtuple("Leaf", ["symbol"])):
    def walk(self, code, num):
        code[self.symbol] = num or "0"


def encode(text):
        huffman = []
        for smb, frequency in Counter(text).items():
            huffman.append(((frequency, len(smb), Leaf(smb))))
        heapq.heapify(huffman)
        count = len(huffman)
        while len(huffman) > 1:
            frequency1, count1, left = heapq.heappop(huffman)
            frequency2, count2, right = heapq.heappop(huffman)
            if frequency1 == frequency2 and count2 > len(s):
                x = right
                right = left
                left = x
            heapq.heappush(huffman, (frequency1 + frequency2, count, Node(left, right)))
            count += 1
        code = {}
        if huffman:
            [(frequency, count, root)] = huffman
            root.walk(code, "")
        return code


def decode(entry_decode, code):
    global enc_smb
    dec_text = []
    enc_smb = ""
    enc_smb = ""
    for smb in entry_decode:
        enc_smb += smb
        for dec_smb in code:
            if code.get(dec_smb) == enc_smb:
                dec_text.append(dec_smb)
                enc_smb = ""
                break
    return "".join(dec_text)


def clicked_decode():
    mes_decode = Tk()
    mes_decode.title('Huffman')
    mes_decode.config(bg='#EBEBEB')
    entry_decode = decode_entry.get()
    dcd = decode(entry_decode, code)
    if len(enc_smb) > 0:
        mes_decode.geometry('600x100+450+150')
        for i in reversed(enc_smb):
            if i == entry_decode[-1]:
                entry_decode = entry_decode[:-1]
        dcd_label = Label(mes_decode, text=f'{entry_decode} => {dcd}', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
        dcd_label.pack()
        miss_label = Label(mes_decode, text=f'"{enc_smb}" - error!!!', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
        miss_label.pack()
    else:
        mes_decode.geometry('600x50+450+150')
        for i in reversed(enc_smb):
            if i == entry_decode[-1]:
                entry_decode = entry_decode[:-1]
        dcd_label = Label(mes_decode, text=f'{entry_decode} --> {dcd}', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
        dcd_label.pack()


def main():
    mes_code = Tk()
    mes_code.title('Huffman')
    mes_code.geometry('1000x600+300+100')
    mes_code.config(bg='#EBEBEB')
    frame_table = Frame(mes_code, width=800, height=180, bg='#EBEBEB')
    frame_table2 = Frame(mes_code, width=800, height=360, bg='#EBEBEB')
    frame_change = Frame(mes_code, width=800, height=120, bg='#EBEBEB')
    frame_table.place(relx=0, rely=0, relwidth=1, relheight=0.3)
    frame_table2.place(relx=0, rely=0.3, relwidth=1, relheight=0.5)
    frame_change.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
    text = input.replace(" ", "")
    global s
    s = ""
    for i in text:
        if i not in s:
            s += i
    b = ''
    for i in range(len(text)):
        b += bin(ord(text[i]))
    b = b.replace("b", "")
    size_label = Label(frame_table, text=f'Размер текста до кодирования:', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
    size_label.pack()
    s1_label = Label(frame_table, text=f'{b}', font=('Times New Roman', 8), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
    s1_label.pack()
    global code
    code = encode(text)
    encoded = "".join(code[smb] for smb in text)
    letter = []
    binary = []
    for smb in sorted(code):
        letter.extend(smb)
        binary.append(code[smb])
    general = []
    for i in range(len(letter)):
        for j in range(len(binary)):
            if letter.index(letter[i]) == binary.index(binary[j]):
                general.append([letter[i], binary[j]])
    tbl = ttk.Treeview(frame_table2, show='headings')
    head = ['Буква', 'Биты']
    tbl['columns'] = head
    for header in head:
        tbl.heading(header, text=header, anchor='center')
        tbl.column(header, anchor='center')
    for i in general:
        tbl.insert('', 'end', values=i)
    scroll_pane = ttk.Scrollbar(frame_table2, command=tbl.yview)
    tbl.configure(yscrollcommand=scroll_pane.set)
    scroll_pane.pack(side=RIGHT, fill=Y)
    size_after_label = Label(frame_table, text=f'Размер текста после кодирования:', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
    size_after_label.pack()
    s2_label = Label(frame_table, text=f'{encoded}', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12, bg='#EBEBEB')
    s2_label.pack()
    tbl.pack(expand=YES, fill=BOTH)
    global decode_entry
    decode_entry = Entry(frame_change, bg='#fff', fg='#444', font=('Times New Roman', 12))
    decode_entry.place(relx=0.3, rely=0.25, width=400)
    decode_btn = Button(frame_change, text='Декодировать', command=clicked_decode, bg='#EBEBEB')
    decode_btn.place(relx=0.45, rely=0.6)


def clicked():
    global input
    input = input_entry.get()
    window.destroy()
    main()


input_label = Label(window, text='Введите текст', font=('Times New Roman', 14), justify=CENTER, padx=10, pady=12)
input_label.pack()
input_entry = Entry(window, bg='#fff', fg='#444', font=('Times New Roman', 12))
input_entry.pack()
encoded_btn = Button(window, text='Закодировать', command=clicked)
encoded_btn.pack(padx=10, pady=8)
window.mainloop()