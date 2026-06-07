import os
import PyPDF2
from PyPDF2 import PdfMerger

# ==========================================
# ১. একাধিক PDF মার্জ (Merge) বা একত্রীকরণ করা
# ==========================================

# যে PDF গুলো জোড়া দিবি সেগুলোর লিস্ট
all_pdfs = ["Spoken English Day-01.pdf", "Spoken English Day-02.pdf"]
merged_filename = "SE Day-01 & 02.pdf"

our_merger = PdfMerger()

for pdf in all_pdfs:
    our_merger.append(pdf)

# মার্জ হওয়া নতুন ফাইলটি সেভ করা
our_merger.write(merged_filename)
our_merger.close()

print(f"সফলভাবে মার্জ হয়েছে: {merged_filename}")


# ==========================================
# ২. PDF থেকে নির্দিষ্ট পেজ বাদ দেওয়া (Remove Pages)
# ==========================================

input_file = "SE Day-01 & 02.pdf"
output_file = "SE Day-01 & 02 (Modified).pdf"

# ⚠️ মনে রাখবি: PDF এর পেজ ইনডেক্স ০ (Zero) থেকে শুরু হয়।
# যেমন: ৯ম ও ১০ম পেজ বাদ দিতে চাইলে ইনডেক্স হবে ৮ এবং ৯।
pages_to_remove = [8, 9] 

# নোট: তুই যদি মাত্র ১টি পেজ বাদ দিতে চাস (যেমন ৩ নম্বর পেজ, ইনডেক্স ২), 
# তাহলে নিচের লাইনটি আনকমেন্ট করিস এবং loops এর কন্ডিশন 'if i != page_to_remove:' করে দিস।
# page_to_remove = 2

# মূল PDF টি রিড করা এবং নতুন ফাইল রাইট করার প্রস্তুতি
with open(input_file, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()
    
    # লুপ চালিয়ে নির্দিষ্ট পেজগুলো বাদ দিয়ে বাকিগুলো নতুন ফাইলে যোগ করা
    for i in range(len(reader.pages)):
        if i not in pages_to_remove:
            writer.add_page(reader.pages[i])
            
    # ফাইনাল মডিফাইড PDF টি রাইট করা
    with open(output_file, 'wb') as output_pdf:
        writer.write(output_pdf)

print(f"কাজ শেষ! পেজ বাদ দেওয়া নতুন PDF: {output_file}")


# ==========================================
# ৩. পুরানো বা অন্তর্বর্তীকালীন ফাইল ডিলিট করা (ঐচ্ছিক)
# ==========================================
# তুই যদি চাস মডিফাইড ফাইলটি তৈরি হওয়ার পর মাঝখানের মার্জ হওয়া ফাইলটি ডিলিট হয়ে যাক,
# তাহলে নিচের লাইনটি আনকমেন্ট (# মুছে দেওয়া) করে দিতে পারিস।

# if os.path.exists(input_file):
#     os.remove(input_file)
#     print(f"🗑️ পুরানো ফাইলটি ডিলিট করা হয়েছে: {input_file}")