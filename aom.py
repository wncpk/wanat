import customtkinter
import random

app = customtkinter.CTk()
app.title('สุ่มของกิน')
app.geometry('400x300')

#ข้อความแสดงผล
label = customtkinter.CTkLabel(app, text='ถ้าคุณไม่รู้จะกินอะไร', fg_color='transparent', font=('Aria', 25))
label.pack(pady=(20, 0))

#ข้อความแสดคำตอบ
answer_text =customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria', 25))
answer_label .pack(pady=(20, 0))

#กล่องรับข้อความ input
entry = customtkinter.CTkEntry(app, placeholder_text='ใส่คำถาม')
entry.pack(pady=(15, 0))

#ปุ่มกด
def button_event():
   List_Trashtalk = ['ข้าวมันไก่', 'ก๋วยเตี๋ยว', 'ข้าวผัด', 'มาม่า', 'ไม่ต้องแดก']
   persent = {
      '1':0.5,
      '2':0.5,
      '3':0.5,
      '4':0.5,
      '5':3.0
   }
   answer_Word = random.choices(List_Trashtalk, weights =  persent.values(),k=1)[0]
   answer_text.set(answer_Word)

   print(answer_Word)

button = customtkinter.CTkButton(app, text='กดเลยจ้า', command=button_event)
button.pack(pady=(20, 0))

app.mainloop()