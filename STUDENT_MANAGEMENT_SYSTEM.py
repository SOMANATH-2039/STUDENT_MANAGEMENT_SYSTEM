from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class students:
	def __init__(self,root):
		self.root=root
		self.root.title('STUDENT MNGT SYS')
		self.root.geometry('1000x1000+0+0')
		
		title=Label(self.root,text='STUDENT MANAGEMENT SYSTEM',font=('arial',40,'bold'),bg='#FFFFFF',fg='red')
		title.pack(side=TOP,fill=X)
		
		#=====ALL VARIABLES=====
		
		self.roll_no_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.gender_var=StringVar()
		self.contact_var=StringVar()
		self.dob_var=StringVar()
		self.search_by=StringVar()
		self.search_txt=StringVar()
		
		#========FRAME1=========
		
		FRAME1=Frame(self.root,bd=4, relief= RIDGE,bg='crimson')
		
		FRAME1.place(x=20,y=100,width=900, height= 500)
		
		m_frame=Label(FRAME1,text='MANAGE STUDENTS',font=('arial',7,'bold'),bg='yellow',fg='red')
		
		m_frame.grid(row=0,columnspan=2,padx=10)
		
		name=Label(FRAME1,text='NAME   *',font=('arial',5,'bold'),bg='crimson',fg='white')
		
		name.grid(row=2,column=0,padx=10,pady=20,sticky='w')
		
		name_entry=Entry(FRAME1,bd=4,font=('arial',5,'bold'),textvariable=self.name_var,relief=GROOVE,bg='powder blue')
		
		name_entry.grid(row=2,column=1,padx=10,pady=20,sticky='w')
		
		roll_no=Label(FRAME1,text='ROLL NO    *',font=('arial',5,'bold'),bg='crimson',fg='white')
		
		roll_no.grid(row=1,column=0,padx=10,pady=20,sticky='w')
		
		roll_entry=Entry(FRAME1,bd=4,font=('arial',5,'bold'),textvariable=self.roll_no_var,relief=GROOVE)
		
		roll_entry.grid(row=1,column=1,padx=10,pady=20,sticky='w')
		
		email=Label(FRAME1,text='E-MAIL',font=('arial',5,'bold'),bg='crimson',fg='white')
		
		email.grid(row=3,column=0,padx=10,pady=20,sticky='w')
		
		email_entry=Entry(FRAME1,bd=4,font=('arial',5,'bold'),textvariable=self.email_var,relief=GROOVE)
		
		email_entry.grid(row=3,column=1,padx=10,pady=20,sticky='w')
		
		mobile_no=Label(FRAME1,text='MOBILE NO   *',font=('arial',5,'bold'),bg='crimson',fg='white')
		
		mobile_no.grid(row=4,column=0,padx=10,pady=20,sticky='w')
		
		mobile_no_entry=Entry(FRAME1,bd=4,font=('arial',5,'bold'),textvariable=self.contact_var,relief=GROOVE)
		
		mobile_no_entry.grid(row=4,column=1,padx=10,pady=20,sticky='w')
		
		gender=Label(FRAME1,text='GENDER     *',font=('arial',5,'bold'),bg='crimson',fg='white')
		
		gender.grid(row=6,column=0,padx=10,pady=20,sticky='w')
		
		combo_search=ttk.Combobox(FRAME1,width=12,font=('arial',8,'bold'),textvariable=self.gender_var,state='readonly')
		combo_search['values']=('MALE','FEMALE','OTHERS')
		combo_search.grid(row=6,column=1)
		
		dob=Label(FRAME1,text='D_O_B   *',font=('arial',5,'bold'),bg='crimson',fg='white')
		
		dob.grid(row=5,column=0,padx=10,pady=20,sticky='w')
		
		dob_entry=Entry(FRAME1,bd=4,font=('arial',5,'bold'),textvariable=self.dob_var,relief=GROOVE)
		
		dob_entry.grid(row=5,column=1,padx=10,pady=20,sticky='w')
		
		address=Label(FRAME1,text="ADDRESS  * ",font=('arial',5,'bold'),bg='crimson',fg='white')
		
		address.grid(row=7,column=0,padx=10,pady=10,sticky='w')
		
		self.address_entry=Text(FRAME1,bd=4,height=2,width=20,font=('arial',5,'bold'),relief=GROOVE)
		
		self.address_entry.grid(row=7,column=1,padx=10,pady=20,sticky='w')
		
		#=======BUTTON_FRAME=======
		
		BTN_FRAME=Frame(FRAME1,bd=4, relief= RIDGE,bg='crimson')
		
		BTN_FRAME.place(x=10,y=400,width=500, height= 80)
		
		add_btn=Button(BTN_FRAME,text='ADD',width=15,height=3,font=('Elephant',9,'bold'),bg='white',command=self.add_student)
		
		add_btn.grid(row=0,column=0,padx=10,pady=5)
		
		update_btn=Button(BTN_FRAME,text='UPDATE',width=15,height=5,font=('arial',6,'bold'),command=self.update_data,bg='white')
		
		update_btn.grid(row=0,column=1,padx=10,pady=5)
		
		delete_btn=Button(BTN_FRAME,text='DELETE',width=15,height=5,font=('arial',6,'bold'),command=self.delete_data,bg='white')
		
		delete_btn.grid(row=0,column=2,padx=10,pady=5)
		
		clear_btn=Button(BTN_FRAME,text='CLEAR',width=15,height=5,font=('arial',6,'bold'),command=self.clear,bg='white')
		
		clear_btn.grid(row=0,column=3,padx=0,pady=5)
		
		#-----------------FRAME2--------------
		
		FRAME2=Frame(self.root,bd=4, relief= RIDGE,bg='crimson')
		
		FRAME2.place(x=10,y=960,width=1050, height= 800)
		
		search_by=Label(FRAME2,text='SEARCH_BY',font=('arial',4,'bold'),bg='yellow',fg='red')
		
		search_by.grid(row=0,columnspan=1,padx=5)
		
		combo_search_by=ttk.Combobox(FRAME2,width=12,font=('arial',5,'bold'),textvariable=self.search_by,state='readonly',)
		
		combo_search_by['values']=('ROLL_NO','CONTACT')
		
		combo_search_by.grid(row=0,column=1)
		
		search_entry=Entry(FRAME2,bd=4,font=('arial',5,'bold'),textvariable=self.search_txt,relief=GROOVE)
		
		search_entry.grid(row=0,column=2,padx=10,pady=20,sticky='w')
		
		search_btn1=Button(FRAME2,text='SEARCH',width=4,height=1,font=('arial',3,'bold'),command=self.search_data,bg='white')
		
		search_btn1.grid(row=0,column=3,padx=5,pady=5)
		
		showall_btn=Button(FRAME2,text='SHOW_ALL',width=3,height=0,font=('arial',3,'bold'),command=self.fetch_data,bg='white')
		
		showall_btn.grid(row=0,column=4,padx=5,pady=5)
		
		#------------TABLE_FRAME-----------
		
		table_frame=Frame(FRAME2,bd=4,relief=RIDGE,bg='red')
		
		table_frame.place(x=10,y=80,height=700,width=1020)
		
		scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
		
		scroll_y=Scrollbar(table_frame,orient=VERTICAL)
		
		self.student_table=ttk.Treeview(table_frame,columns=('roll_no','name','email','gender','mobile_no','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		
		scroll_x.config(command=self.student_table.xview)
		
		scroll_y.config(command=self.student_table.yview)
		
		self.student_table.heading('roll_no',text='ROLL_NO')
		
		self.student_table.heading('name',text='NAME')
		
		self.student_table.heading('email',text='E_MAIL')
		
		self.student_table.heading('mobile_no',text='CONTACT')
		
		self.student_table.heading('dob',text='D_O_B')
		
		self.student_table.heading('gender',text='GENDER')
		
		self.student_table.heading('address',text='ADDRESS')
		
		self.student_table['show']='headings'
		
		self.student_table.column('roll_no',width=200)
		
		self.student_table.column('name',width=500)
		
		self.student_table.column('email',width=800)
		
		self.student_table.column('gender',width=250)
		
		self.student_table.column('mobile_no',width=400)
		
		self.student_table.column('dob',width=300)
		
		self.student_table.column('address',width=600)
		
		self.student_table.pack(fill=BOTH,expand=1)
		
		self.student_table.bind('<ButtonRelease-1>',self.get_cursor)
		self.fetch_data()

#==========ADDING_FUNCTION=======	
	def add_student(self):
		if self.roll_no_var.get()=='' or self.name_var.get()=='' or self.contact_var.get()=='' or self.dob_var.get()=='' or self.gender_var.get()=='' or self.address_entry=='':
			messagebox.showerror('ERROR','* MARKED FIELD ARE MANDOTORY')
		else:
			mycon=mysql.connector.connect(host='localhost',user='root',password='Sindhuja@16212025',database='PROJECTS')
			cursor=mycon.cursor()
			cursor.execute('insert into STUDENT_MGNT VALUES (%s,%s,%s,%s,%s,%s,%s)',(self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.address_entry.get('1.0',END)))
			mycon.commit()
			self.fetch_data()
			self.clear()
			mycon.close()
			messagebox.showinfo('SUCCESS','DATA ENTERED SUCCESSFULLY')
		
#=========DATA_DISPLAYING_FUNCTION=========		
	def fetch_data(self):
		mycon=mysql.connector.connect(host='localhost',user='root',password='Sindhuja@16212025',database='PROJECTS')
		
		cursor=mycon.cursor()
		
		cursor.execute('select * from STUDENT_MGNT')
		rows=cursor.fetchall()
		
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,values=row)
			mycon.commit()
		mycon.close()
		
#=====CLEAR_FUNCTION======
		
	def clear(self):
		
		self.roll_no_var.set('')
		self.name_var.set('')
		self.email_var.set('')
		self.gender_var.set('')
		self.contact_var.set('')
		self.dob_var.set('')
		self.address_entry.delete('1.0',END)
	
	def get_cursor(self,event):
		cursor_row=self.student_table.focus()
		contents=self.student_table.item(cursor_row)
		row=contents['values']
		
		self.roll_no_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.contact_var.set(row[4])
		self.dob_var.set(row[5])
		self.address_entry.delete('1.0',END)
		self.address_entry.insert(END,row[6])
		
#========UPDATE_FUNCTION=========			
	def update_data(self):
		
		mycon=mysql.connector.connect(host='localhost',user='root',password='your_DB_password',database='your_DB_name')
		
		cursor=mycon.cursor()
		
		cursor.execute('update STUDENT_MGNT set name=%s,e_mail=%s,gender=%s,contact=%s,d_o_b=%s,address=%s where roll_no=%s',(
		self.name_var.get(),
		self.email_var.get(),
		self.gender_var.get(),
		self.contact_var.get(),
		self.dob_var.get(),
		self.address_entry.get('1.0',END),
		self.roll_no_var.get()
		))
		
		mycon.commit()
		self.fetch_data()
		self.clear()
		mycon.close()
		
#========DELETE_FUNCTION=======
	
	def delete_data(self):
		
		mycon=mysql.connector.connect(host='localhost',user='root',password='your_DB_password',database='your_DB_name')
		
		cursor=mycon.cursor()
		
		cursor.execute('delete from STUDENT_MGNT where roll_no=%s'
		%self.roll_no_var.get())
		mycon.commit()
		mycon.close()
		self.fetch_data()
		self.clear()
	
#=======SEARCH_FUNCTION=========

	def search_data(self):
		
		mycon=mysql.connector.connect(host='localhost',user='root@localhost',password='your_DB_password',database='your_DB_name')
		
		cursor=mycon.cursor()
		
		cursor.execute("select * from STUDENT_MGNT where "+str(self.search_by.get())+'='+str(self.search_txt.get()))
		rows=cursor.fetchall()
		
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,values=row)
			mycon.commit()
		mycon.close()
		
root=Tk()
ob=students(root)
root.mainloop()	
