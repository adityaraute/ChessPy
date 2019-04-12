import tkinter
root = tkinter.Tk()
root.geometry('770x800')
root.title("Chess")
photo1 = tkinter.PhotoImage(file="king.png")
mlist=[]
for i in range (8):
	row=[]
	for j in range (8):
		element='b'+str(i)+str(j)
		row.append(element)
	mlist.append(row)
for i in range (8):
	for j in range (8):
		if i%2 == 0 and j%2 == 0 or i%2 == 1 and j%2 == 1 :
			col='black'
		else:
			col='white'
		mlist[i][j]=tkinter.Button(root,state='normal',height=6,width=12,bg=col,activebackground=col)
		mlist[i][j].grid(row=i,column=j)
mlist[0][3].configure(image=photo1,height=90,width=90)
mlist[0][0].configure(state='disabled')
root.mainloop()
