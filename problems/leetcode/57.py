class Solution:
    def insert(self, intervals, newInterval):
        n = newInterval

        ui = []

        for i, interval in enumerate(intervals):
            if (n[1] < interval[0]):
                ui.append(n)
                return ui + intervals[i:]
            elif (n[0] > interval[1]):
                ui.append(interval)

            else:
                n = [min(interval[0], n[0]), max(interval[1], n[1])]

        ui.append(n)
        return ui