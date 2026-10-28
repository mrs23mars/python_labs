from src.lab04.io_txt_csv import read_text, write_csv

txt = read_text("data/samples/a.txt")
print(txt)

write_csv(
    [("test", 3), ("hello", 5)],
    "data/out/check.csv",
    header=("word", "count")
)