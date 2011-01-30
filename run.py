import dblayer

db = dblayer.DBLayer("test.sqlite")

for n in range(1,11) + [12]:
    w = dblayer.Widget(float(n))
    db.insert_widget(w)

print db.average_length()
