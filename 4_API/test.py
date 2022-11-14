from flask  import Flask

app=Flask('JAGAN')

@app.route('/h')
def home():
    return 'HELLO WORLD'
    
@app.route('/w')
def ARE():
    return 'HOW ARE YOU'   
    
app.run(debug=True)