import matplotlib.pyplot as plt

def plotting(user_dict):

    path = "../front-end/static/"
    names = []
    values = []
    details = ["None", "Due date", "Description", "Both"]
    details_values = [0,0,0,0]
    done = ["Done", "Not done"]
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


    # fig, axs = plt.subplots(2,2)
    # fig.tight_layout(w_pad = 8, h_pad = 8)

    # axs[0,0].bar(names, values)
    # axs[0,0].set_yticks(list(range(0,10,1)))
    # axs[0,0].set_xlabel("Username")
    # axs[0,0].set_ylabel("Active tasks")
    # axs[0,0].set_title("Number of active tasks per user")

    # axs[0,1].hist(values, bins=8)
    # axs[0,1].set_yticks(list(range(0,6,1)))
    # axs[0,1].set_xticks(list(range(0,8,1)))
    # axs[0,1].set_xlabel("Active tasks")
    # axs[0,1].set_ylabel("Number of users")
    # axs[0,1].set_title("Number of users having certain number of active tasks")
    

    # axs[1,0].pie(done_values, labels = done, autopct="%.0f%%")
    # axs[1,0].set_title("Done active tasks")

    # axs[1,1].pie(details_values, labels = details, autopct="%.0f%%")
    # axs[1,1].set_title("Different levels of description")

    # plt.savefig(path + "graphs.png")
        
    plt.bar(names, values)
    plt.yticks(list(range(0,10,1)))
    plt.xlabel("Username")
    plt.ylabel("Active tasks")
    plt.title("Number of active tasks per user")
    plt.savefig(path + "bar.png")
    plt.clf()

    plt.hist(values)
    plt.yticks(list(range(0,6,1)))
    plt.xticks(list(range(0,8,1)))
    plt.xlabel("Active tasks")
    plt.ylabel("Number of users")
    plt.title("Number of users having certain number of active tasks")
    plt.savefig(path + "hist.png")
    plt.clf()

    plt.pie(done_values, labels = done, autopct="%.0f%%")
    plt.title("Done active tasks")
    plt.savefig(path + "pie_done.png")
    plt.clf()

    plt.pie(details_values, labels = details, autopct="%.0f%%")
    plt.title("Different levels of description")
    plt.savefig(path + "pie_details.png")