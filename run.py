import dblayer

db = dblayer.DBLayer("test.sqlite")

for n in range(1,12):
    w = dblayer.Widget(float(n))
    db.insert_widget(w)

print db.average_length()
print db.probability(9.0)
