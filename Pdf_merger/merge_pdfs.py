import PyPDF2

pdfs = int(input("how many pdf you want to merge: "))

merger = PyPDF2.PdfMerger()

for i in range(pdfs):
    pdf = input("Enter the pdf file name: ")
    merger.append(pdf)
    
merger.write("Merged.pdf")

print("Merged.pdf created successfully!")