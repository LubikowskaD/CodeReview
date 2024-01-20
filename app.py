from tkinter import *
import difflib
import webbrowser
import os

#file path
main_folder = os.path.abspath(os.getcwd())

#tkinter class - dialog window
root = Tk()
root.title('code review')   #title
root.iconbitmap("C:\\Users\\domin\\Downloads\\myIcon.ico")  #path to image of logo
root.geometry("825x750")   #size of window
root.resizable(False, False)

#box 1
frame1 = Frame(root)
frame1.pack(side="left", pady=10, padx=10) # padding - adding free space between elements
frame1.place(x=10,y=50)

#label 1
label1 = Label(frame1, text="Original code:")
label1.grid(row=0, column=0)

#text widget in box1
text_widget1 = Text(frame1, width=30, height=10, font = ("Helvetica", 16))
text_widget1.grid(row=1, column=0)



#box 2
frame2 = Frame(root)
frame2.pack(side="left", pady=10, padx=10)
frame2.place(x=450,y=50)

#label 2
label2 = Label(frame2, text="Code updated:")
label2.grid(row=0, column=0)

#text widget in box 2
text_widget2 = Text(frame2, width=30, height=10, font = ("Helvetica", 16)) #how the window looks like
text_widget2.grid(row=1, column=0) #changes the position of the label



#box 3 - results
frame3 = Frame(root)
frame3.pack(side="left", pady=10, padx=10)
frame3.place(x=230,y= 420)

#label 3
label3 = Label(frame3, text="differences")
label3.grid(row=0, column=0)

#text widget in box 3
text_widget3 = Text(frame3, width=30, height=10, font = ("Helvetica", 16))
text_widget3.grid(row=1, column=0)



#function that compares and displays differences
def compare_and_display():
    text1 = text_widget1.get(1.0, END)
    text2 = text_widget2.get(1.0, END)

    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    #finds lines that are in text_widget1 but not in text_widget2
    diff_lines1 = [line for line in lines1 if line not in lines2]

    #finds lines that are in text_widget2 but not in text_widget1
    diff_lines2 = [line for line in lines2 if line not in lines1]

    #displays the result in text_widget3
    text_widget3.delete(1.0, END)

    for line in diff_lines1:
        text_widget3.insert(END, f'Line from Original code: {line}\n')

    for line in diff_lines2:
        text_widget3.insert(END, f'Line from Code updated: {line}\n')



#function that clears boxes 1 and 2
def clear_text():
    text_widget1.delete(1.0, END)
    text_widget2.delete(1.0, END)
    text_widget3.delete(1.0, END)



#function that generates a html report with comparison results
def gen_report():
    text1 = text_widget1.get(1.0, END)
    text2 = text_widget2.get(1.0, END)
    show_pre = 'show_pre'
    show_post = 'show_post'
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()    #four arguments required in HTMLdiff function
    difference = difflib.HtmlDiff(wrapcolumn = 80).make_file(lines1, lines2, show_pre, show_post)   #wrapcolumn estimates 80 characters in each line
    difference_report = open(main_folder+"/show_comparison.html","w+")
    difference_report.write(difference)   # writes down the differences to the difference report
    difference_report.close()
    webbrowser.open('file://'+main_folder+'/show_comparison.html')



#"Compare and display" button
Comparison = Button(root, text="Compare and display", command=compare_and_display)
Comparison.pack(side="bottom", pady=10, padx=10)
Comparison.place(x=350,y= 350)


# "Clear both boxes" button
clear_both_button = Button(root, text="Clear Both Boxes", command=clear_text)
clear_both_button.pack(side="bottom", pady=10, padx=10)
clear_both_button.place(x=360,y= 380)


#"Generate report" button
generate_full_report = Button(root, text="Generate Report", command=gen_report)
generate_full_report.pack(side="bottom", pady=10, padx=10)
generate_full_report.place(x=360,y= 700)



root.mainloop() #execution of all
