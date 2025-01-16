from scheduler import WeightedIntervalScheduling
from visualization import visualize_schedule


if __name__ == "__main__":
    events = [
        (1, 3, 50),
        (2, 5, 20),
        (4, 6, 100),
        (6, 7, 200),
        (5, 8, 150),
        (8, 9, 250)
    ]

    scheduler = WeightedIntervalScheduling(events)

    max_revenue = scheduler.compute_max_revenue()

    selected_events = scheduler.find_solution()

    print(f"Maximum Revenue: {max_revenue}")
    print("Selected Events:")
    for event in selected_events:
        print(f"Start: {event[0]}, End: {event[1]}, Revenue: {event[2]}")

    visualize_schedule(events, selected_events)
