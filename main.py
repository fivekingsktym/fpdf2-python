from fpdf import FPDF

# create FPDF object
# Layout ('P','L') => Portait or Landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
# pdf = FPDF()
pdf = FPDF('P', 'mm', 'Letter')


# Add a page
pdf.add_page()


# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
# pdf.set_font('helvetica', size=12)
pdf.set_font('helvetica', '', 16)
# pdf.set_font('helvetica', 'BIU', 16)

# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
# pdf.cell(text="hello world")
# pdf.cell(40, 10, 'Hello World!', ln=True) # old apporach
pdf.cell(120, 80, 'Hello World!', new_x="LMARGIN", new_y="NEXT", border=True)
# pdf.set_text_color(220,50,50)

pdf.set_font('times', 'U', 12)
pdf.cell(80, 10, 'Good Bye World!')


pdf.output("hello_world.pdf")