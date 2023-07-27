# Merge-PDFs
This repository contains a Python script that can be used to merge multiple PDF files into a single PDF file.

Requirements  

        Python 3  
        PyPDF2 module  
Usage   
1. Clone the repository to your local machine.  
2. Install the PyPDF2 module by running the following command in your terminal:  

        pip install PyPDF2

3. Run the merge_pdfs.py script by passing the number of PDF files you want to merge as an argument.     
For example, to merge 2 PDF files, you would run the following command:  
python merge_pdfs.py 2  


4. The script will prompt you to enter the name of each PDF file that you want to merge.
5. The script will then merge the PDF files and create a new PDF file called `Merged.pdf`.

## Example

The following example shows how to merge two PDF files called `file1.pdf` and `file2.pdf`:  

python merge_pdfs.py 2  

Enter the PDF file name: file1.pdf  
Enter the PDF file name: file2.pdf  

Merged.pdf created successfully!  

