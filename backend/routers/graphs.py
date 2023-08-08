import matplotlib.pyplot as plt
from .models import Task_Pydantic, TaskIn_Pydantic, User_Pydantic, Tasks, Users

def plotting(user_dict):

    names = []
    values = []
    details = ["none", "date", "description", "both"]
    details_values = [0,0,0,0]
    done = ["done", "not done"]
    done_values = [0,0]
    for user in user_dict:
        names.append(user)
        values.append(len(user_dict[user]))
        for task in user_dict[user]:
            if task.is_done:
                done_values[0] += 1
            else:
                done_values[1] += 1
            
            if(task.due_date and task.description):
                details_values[3] += 1
            elif(task.description):
                details_values[2] += 1
            elif(task.due_date):
                details_values[1] += 1
            else:
                details_values[0] += 1

        
    plt.bar(names, values)
    plt.savefig("bar.png")
    plt.clf()

    plt.hist(values)
    plt.savefig("hist.png")
    plt.clf()

    plt.pie(done_values, labels = done)
    plt.savefig("pie_done.png")
    plt.clf()

    plt.pie(details_values, labels = details)
    plt.savefig("pie_details.png")