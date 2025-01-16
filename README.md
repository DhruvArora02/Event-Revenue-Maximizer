# Event-Revenue-Maximizer

__Project Overview__ -

This project implements the Weighted Interval Scheduling algorithm to solve the problem of maximizing revenue from a schedule of events. Each event has a start time, end time, and associated revenue. The system selects non-overlapping events to maximize the total revenue.

This solution is widely applicable in domains such as event planning, job scheduling, and resource allocation.

__Key Features__ -
- Input a list of events with start time, end time, and revenue.
- Compute the maximum revenue by selecting non-overlapping events.
- Visualize the selected events on a timeline.
- Efficient implementation using dynamic programming and binary search.

__Technologies Used__ -
- **Programming Language:** Python
- **Libraries:**
  - `matplotlib` for visualizations
  - `tkinter` for a simple GUI (optional)
  - `numpy` for optimized computations

__How It Works__ -
1. **Data Input:** Accepts a list of events with their details.
2. **Sorting:** Sorts the events based on their end times.
3. **Dynamic Programming:** 
   - Computes the maximum revenue for each event by including or excluding it.
   - Uses binary search to find the last non-conflicting event for optimal performance.
4. **Output:** Displays the selected events and total revenue.
5. **Visualization:** Shows the timeline of events for better understanding.

