# [Design Underground System] https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.cid = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cid[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ss, st = self.cid[id]
        if (ss, stationName) in self.time:
            self.time[(ss, stationName)].append(t - st)
        else:
            self.time[(ss, stationName)] = [t - st]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.time[(startStation, endStation)]) / len(self.time[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
