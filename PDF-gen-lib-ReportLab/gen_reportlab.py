from reportlab.platypus import SimpleDocTemplate # Using pip3 install reportlab
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# Protip never name your script with the name of your library name meaning don't name it libray-name.py

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

report = SimpleDocTemplate("/home/zero/Python/PDF-gen-lib-ReportLab/report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])

# Now let's add data's into the report

table_data = []

for k, v in fruit.items():
  table_data.append([k, v]) # Appending the key value pairs of fruit dictionaries to the table_data list
  
  #print(table_data)
  
report_table = Table(data=table_data) # Using the table method assigning the table data to the data parameter

report.build([report_title, report_table])

# Now let's assign colours to our table

table_style = [('GRID', (0,0), (-1,-1), 1, colors.blue)] 

# Allingning the table 

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# Again building the PDF 
report.build([report_title, report_table])

# Adding fraphics to the table
# Sizing the pie chart 

report_pie = Pie(width=3, height=3) # type: ignore size is in the inch

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

# print(report_pie.data)
# output: [2, 5, 8, 3, 1, 1, 13]
# print(report_pie.labels)
# output: ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

report_chart = Drawing()
report_chart.add(report_pie)

# Again building the report with the chart

report.build([report_title, report_table, report_chart])