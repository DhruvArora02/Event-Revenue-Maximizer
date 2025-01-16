import matplotlib.pyplot as plt

def visualize_schedule(events, solution):
    """
    Visualize the schedule of events.
    """
    fig, ax = plt.subplots()
    for i, event in enumerate(events):
        ax.plot([event[0], event[1]], [i + 1, i + 1], 'r-', label='Excluded' if i == 0 else "")
    for i, event in enumerate(solution):
        ax.plot([event[0], event[1]], [i + 1, i + 1], 'g-', label='Selected' if i == 0 else "")
    ax.set_yticks(range(1, len(events) + 1))
    ax.set_yticklabels([f"Event {i + 1}" for i in range(len(events))])
    ax.set_xlabel("Time")
    ax.set_title("Event Scheduling")
    ax.legend(loc='upper right')
    plt.show()
