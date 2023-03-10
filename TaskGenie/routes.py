from flask import render_template
from TaskGenie import app

@app.route("/")
@app.route("/home")
def home():
    
    from TaskGenie.task import Task    
    from TaskGenie.linked_list import LinkedList
    ll = LinkedList()
    present = Task("Present", "Saturday", "medium", "Going to buy the present at the shop")
    friend1_call = Task("Calling friend", "Today", "high", "Calling friend to wish happy birthday")        
    friend2_call = Task("Calling friend", "Sunday", "low", "Calling friend to ask about the moving")
    friend3_call = Task("Calling friend", "Sunday", "low", "Calling friend to aks how he is going")
    interview = Task("Interview", "Today", "high", "Having phone interview today")     
    shower = Task("Take a Shower", "Today", "high", " ")     

    ll.add_beginning(present)
    ll.add_beginning(friend1_call)
    ll.add_beginning(friend2_call)
    ll.add_beginning(friend3_call)
    ll.add_beginning(interview)
    ll.add_beginning(shower)

    return render_template("home.html", title="Home", tasks=ll)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/add_task")
def add_task():
    pass