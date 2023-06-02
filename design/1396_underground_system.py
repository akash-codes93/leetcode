class Trip:

    def __init__(self, _id, s_station, starttime, e_station =None, endtime=None):

        self.id = _id
        self.s_station = s_station
        self.starttime = starttime

        self.e_station = e_station
        self.endtime = endtime

class StationAverage:
    def __init__(self, total_time, size):
        self.total_time = total_time
        self.size = size


class UndergroundSystem:

    def __init__(self):
        self.trip_map = {}
        self.average_distance_map = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trip_map[id] = Trip(
            id, stationName, t
        )

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        node = self.trip_map[id]
        node.e_station = stationName
        node.endtime = t

        if node.s_station not in self.average_distance_map:
            self.average_distance_map[node.s_station] = {
                node.e_station: StationAverage((node.endtime - node.starttime), 1)
            }
        else:
            average_distance_map = self.average_distance_map[node.s_station]
            if node.e_station not in average_distance_map:
                average_distance_map.update({
                    node.e_station: StationAverage((node.endtime - node.starttime), 1)
                })
            else:
                destination = average_distance_map[node.e_station]
                destination.total_time += (node.endtime - node.starttime)
                destination.size += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        node = self.average_distance_map[startStation][endStation]
        return node.total_time/ node.size



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)