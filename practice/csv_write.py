import csv

with open("st.csv","w",newline='')as f:
    w = csv.writer(f, delimiter=",")
    w.writerrow(["one","two","three"])
    w.writerrow(["four","five","six"])
