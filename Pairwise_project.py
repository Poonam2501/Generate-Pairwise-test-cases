import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import pandas as pd
import threading
import itertools
from itertools import cycle,islice
import pandastable as pdt
from pandastable import *
import random

class test:
        def __init__(self,root):
            self.root = root
            self.root.geometry("1350x700+0+0")
            self.root.title("COMBINATORIAL TESTING WINDOW")

            self.frame1 = tk.Frame(self.root,bg="white")
            self.frame1.place(x=60,y=60,width=1250,height=600)

            # ===================Parameter Name=================

            s_name = tk.Label(self.frame1,text="System Parameter :",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=20)

            p_name = tk.Label(self.frame1,text="Parameter Name",font=("times new roman",20),bg="white",fg="black").place(x=400,y=20)
            self.txt_pname = tk.Entry(self.frame1,font=("arial",15),bg="lightgray")
            self.txt_pname.place(x=400,y=60,width=250)

            self.btn_paraName = tk.Button(self.frame1,text="Save parameter name",cursor="hand2",font=("times new roman",15),command=self.save_name,padx=5).place(x=700,y=60)

            #=====================Parameter Value(1)===============

            p_val = tk.Label(self.frame1,text="Parameter Values :",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=150)

            self.txt_pval = tk.Entry(self.frame1,font=("times new roman",17),bg="lightgray")
            self.txt_pval.place(x=400,y=150,width=250)        

            self.btn_add = tk.Button(self.frame1,text="add value",cursor="hand2",font=("times new roman",15),command=self.add_value,padx=5).place(x=700,y=150)

            #=====================Parameter Value(2)===============

            self.box_val = tk.Text(self.frame1,height=15,width=20,bg="lightgray")
            self.box_val.place(x=850,y=150,width=250)

            #=====================Save=============================

            self.btn_save = tk.Button(self.frame1,text="Save",cursor="hand2",font=("times new roman",15),command=self.final_save,padx=10).place(x=400,y=350)

            #=====================Combobox=========================

            stren_lbl = tk.Label(self.frame1,text=" Testing  Strength  :",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=455)

            self.cmb_text = ttk.Combobox(self.frame1,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_text['values'] = ("select",1,2)
            self.cmb_text.place(x=400,y=465,width=250)
            self.cmb_text.current(0)

            # ========final==================

            self.btn_generate = tk.Button(self.frame1,text="Generate Test Cases",cursor="hand2",font=("times new roman",15),command = self.generate,padx=10).place(x=400,y=550)
            self.btn_cancel = tk.Button(self.frame1,text="Cancel",cursor="hand2",font=("times new roman",15),padx=10,command=self.cancel  ).place(x=650,y=550)
            self.btn_close = tk.Button(self.frame1,text="Close",cursor="hand2",font=("times new roman",15),padx=10,command = self.close_window).place(x=800,y=550)
    
            # ===============================
            self.max = 0
            self.max2 = 0
            self.maxE = 0
            self.max2E = 0
            self.count = 0
            self.list1 = [ ]
            self.list_val = []
            self.max_key = ' '
            self.max2_key = ' '
            self.max_keyE = ' '
            self.max2_keyE = ' '
            # ===============================

        #===============parameter===================

        def save_name(self,list1 = []):
            self.list1 = list1
            if self.txt_pname.get() == '':
                messagebox.showinfo("Invalid parameter","Please enter valid parameter name",parent=self.root)
            else:
                self.list1.append(self.txt_pname.get())
            
            #print(self.list1)

        #================values======================

        def add_value(self,dict_value = []):
            
            if self.txt_pval.get() ==  '':
                messagebox.showinfo("Invalid parameter value","Please enter valid parameter value",parent=self.root)
            else:
                self.box_val.insert(END,self.txt_pval.get() + '\n')
                self.dict_value = dict_value
                self.dict_value.append(self.txt_pval.get())
                self.count = self.count + 1
                #self.save_para()
                self.txt_pval.delete(0,END)   

        #============parameter with values==========

        def final_save(self,dict={}):
            self.dict = dict
            n = self.count 
            name = self.txt_pname.get()
            value = self.dict_value[-n:]
            #counter + 1
            self.dict[name] = value
            #print(self.dict)

            self.dict_doublicate = self.dict.copy()

            self.count = 0
            self.txt_pname.delete(0,END)
            self.txt_pval.delete(0,END)
            self.box_val.delete("1.0",END)

        #=============max no. of value================

        def max_val(self):
            #============key with max no. of values================
            for key,value in self.dict.items():
                length = len(value)

                if self.max < length:
                    self.max = length
                    self.max_key = key
                    
            #=============key with second max no. of values=========
            for key,value in self.dict.items():
                length = len(value)

                if (length <= self.max and length > self.max2 and key != self.max_key):
                    self.max2 = length
                    self.max2_key = key

                elif (length <= self.max and length == self.max2 and key != self.max_key):
                    pass
            
            return

        def max_val_eachChoice(self):
            
            for key,value in self.dict_doublicate.items():
                length1 = len(value)

                if self.maxE < length1:
                    self.maxE = length1
                    self.max_keyE = key
                    

            for key,value in self.dict_doublicate.items():
                length1 = len(value)

                if (length1 <= self.maxE and length1 >= self.max2E and key != self.max_keyE):
                    self.max2E = length1
                    self.max2_keyE = key

            
            return

        #==============Sort Dictionary===================
        def sortDict(self):
            #n = 0
            m = 0
            self.combi_list = []
            self.sortedDict = {}
            #========sorted dict=========================
            for k in sorted(self.dict, key=lambda k: len(self.dict[k]), reverse=True):
                self.sortedDict.update( {k:self.dict[k]} )

            #print("Sorted Dict :",self.sortedDict,"\n")
            
            list_values = list(self.sortedDict.values())
            single_list_values = list(itertools.chain.from_iterable(list_values))
            #print(list_values)
            #print(single_list_values,"\n")
            len1 = len(single_list_values)

            #=========list of all pairwise combinations=============
            for i in list_values:
                if i != list_values[len(list_values)-1]:
                    m = m + len(i)
                    #n = len(i)
                    for j in i:
                    
                        trial = single_list_values[m:len1+1]
                        self.combi_list.append(list((j,k) for k in trial))
                        
            #print("List of all pairwise combinations :",list(itertools.chain.from_iterable(self.combi_list)),"\n")

        #==============Difference=======================
        def diff(self):
            self.sortDict()
            self.max_val()
            total_pairs = self.max * self.max2
            val_list = [0] * total_pairs
            
            self.final_dict = {}
            for key,value in self.sortedDict.items():
                if key == self.max_key:
                    self.final_dict.update({key : list(itertools.chain.from_iterable(itertools.repeat(x,self.max2) for x in value))})
                    #print(self.final_dict)

                if key == self.max2_key:
                    self.final_dict.update({key : list(islice(cycle(self.sortedDict[key]),total_pairs))})
                    #print(self.final_dict)

                if key != self.max_key and key != self.max2_key:
                    lnth = len(value)
                    i = 0
                    for val in value:
                        val_list[i] = val
                        i = i + 1
                    self.final_dict[key] = val_list
                    val_list = [0] * total_pairs
                    #print(self.final_dict)

            self.combi_list_2 = [(i,j) for i in self.sortedDict[self.max_key] for j in self.sortedDict[self.max2_key]]
            #print("Combination of first 2 parameters :",self.combi_list_2,"\n")

            self.li_diff1 = list(set(tuple(list(itertools.chain.from_iterable(self.combi_list)))) - set(tuple(self.combi_list_2)))
            #print("Difference :",self.li_diff1,"\n")

            self.li_diff = []
            for k,v in self.sortedDict.items():
                for pair in self.li_diff1:
                    if pair[0] in v:
                        self.li_diff.append(pair)

            #print("Final list of difference : ",self.li_diff,"\n")


        #================Check combinations and insert values=======================

        def diff_final(self):
            
            #============insert combinations in dict================
            for p in self.li_diff:
                for key,value in self.final_dict.items():
                    if p[0] in value:
                        self.val_in = []
                        
                        for i in range(0,len(value)):
                            if value[i] == p[0]: 
                                self.val_in.append(i)
                       

                        #print(self.val_in)

                        for indx in self.val_in:
                            for key,value in self.final_dict.items():
                            
                                #lst = self.final_dict[key]
                                if p[1] in value and value[indx] == p[1]:
                                    break
                                

                                elif p[1] in value and value[indx] == 0:
                                    value[indx]=p[1]
                                    self.final_dict[key] = value
                                    break
                            
                                
                                elif p[1] in value and value[indx] != p[1]:
                                    for ind in self.val_in:
                                        if ind != indx and value[ind] == value[indx]:
                                            value[ind] = p[1]
                                            break

                                        elif ind != indx and value[ind] == 0:
                                            value[ind] = p[1]
                                            break

                            break 
                #print(self.final_dict)

        #==============Final dict========================      
            
        def fill(self):
            tp = self.max * self.max2

            for key,value in self.final_dict.items():
                for i in range(tp):
                    if value[i] == 0:
                        li = self.sortedDict[key]
                        value[i] = random.choice(li)  
                    
                    

        
        #==============Each choice testing===============

        def each_choice(self):
            self.max_val_eachChoice()
            
                
            for key,value in self.dict_doublicate.items():
                m = len(value)

                if m == self.maxE:
                    self.dict_doublicate[key] = value
                elif m < self.maxE:
                    self.dict_doublicate[key] = list(islice(cycle(self.dict_doublicate[key]),self.maxE))
                    

            self.df1 = pd.DataFrame({ key : pd.Series(value) for key,value in self.dict_doublicate.items() })
            
            try:
                self.OpenNew_window()
                self.table = pt = Table(self.frame, dataframe=self.df1,showtoolbar=True,showstatusbar=True)
            except AttributeError as error:
                print(error)
            
            try:
                pt.show()
            except AttributeError as error:
                print(error)
                print("Error occured!!")
                   

        #===============Pairwise Testing=============

        def pairwise(self):
            self.combi_list_2 = []
            #self.l = []
            self.max_val()
            self.sortDict()
            total_pairs = self.max * self.max2

            self.combi_list_2 = [(i,j) for i in self.sortedDict[self.max_key] for j in self.sortedDict[self.max2_key]]

            self.diff()
            self.diff_final()
            self.fill()
            
            #print(self.combi_list)
            #print(self.combi_list_2)

            
            try:
                self.df = pd.DataFrame({ key : pd.Series(value) for key,value in self.final_dict.items() })
            except AttributeError:
                print("Occured!!!")

            try:
                self.OpenNew_window()
                self.table = pt = Table(self.frame, dataframe=self.df,showtoolbar=True,showstatusbar=True)
            except AttributeError as error:
                print(error)
            
            try:
                pt.show()
            except AttributeError as error:
                print(error)
                print("Error occured!!")
    

        #==================Display window============

        def OpenNew_window(self):
            self.newWindow = Toplevel(self.root)
            self.newWindow.title("New window")
            self.newWindow.geometry("900x500+0+0")

            self.frame = Frame(self.newWindow)
            self.frame.pack(fill='both', expand=True)

        #==================Generate test case===========

        def generate(self):
            if self.cmb_text.get() == "select":
                messagebox.showerror("Invalid strength","Please enter valid testing strength",parent=self.root)
                
            elif self.cmb_text.get() == "1":
                threading.Thread(target=self.each_choice).start()

            elif self.cmb_text.get() == "2":
                threading.Thread(target=self.pairwise).start()

        #===============cancel data======================

        def cancel(self):
            self.txt_pname.delete(0,END)
            self.txt_pval.delete(0,END)
            self.box_val.delete("1.0",END)
            self.dict.clear()
            self.dict_doublicate.clear()

        #===============close window======================
        
        def close_window(self):
            self.root.destroy()

root = Tk()
obj=test(root)
root.mainloop()