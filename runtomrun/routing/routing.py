import geopy
import geopy.distance
import math
# in meters
RESOLUTION = 300
RESOLUTION_DISTANCE = geopy.distance.geodesic(meters=RESOLUTION)

NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270
COMPASS = (NORTH, EAST, SOUTH, WEST)


class Routes:

    def __init__(self, lat: float, lng: float, length: int) -> None:
        self.lat = lat
        self.lng = lng
        self.length = length
        self.start = geopy.Point(lat, lng)
        self.points_n = math.floor(self.length / RESOLUTION)

    def get(self):
        routes = []
        # routes += self.__route_circle()
        routes += self.__route_square()
        # routes += self.__route_line()
        #routes += self.__route_triangle()
        return routes


    def __route_circle(self):
        r = self.length / (2 * math.pi)
        r_distance = geopy.distance.geodesic(meters=r)
        angle_d = 360 / self.points_n

        routes = []
        for direction in COMPASS:
            center = r_distance.destination(point=self.start, bearing=direction)

            points = []
            for i in range(0, self.points_n):
                p = r_distance.destination(point=center, bearing=angle_d*i)
                points.append((p.latitude, p.longitude))
            routes.append(points)

        return routes

    def __route_square(self):
        a = self.length / 4
        a_points = math.floor(self.points_n / 4)
        result = []
        last = self.start
        compass_array = [[NORTH, EAST, SOUTH, WEST],
                         [NORTH, WEST, SOUTH, EAST],
                         [SOUTH, WEST, NORTH, EAST],
                         [SOUTH, EAST, NORTH, WEST]]
        for direction in compass_array:
            points = []
            for destination in direction:
                for i in range(1, a_points):
                    p = RESOLUTION_DISTANCE.destination(point=last, bearing=destination)
                    points.append((p.latitude, p.longitude))
                    last = p
            result.append(points)

        return result

    def __route_line(self):
        line = self.length/2
        a_points = math.floor(self.points_n/2)
        compass_array = [[NORTH, SOUTH],
                         [WEST,EAST],
                         [SOUTH,NORTH],
                         [EAST,WEST]]
        result = []
        last = self.start
        for direction in compass_array:
            points = []
            for destination in direction:
                for i in range(1, a_points):
                    p = RESOLUTION_DISTANCE.destination(point=last, bearing=destination)
                    points.append((p.latitude, p.longitude))
                    last = p
                result.append(points)

        return result

    def __route_triangle(self):
        a = self.length/3
        a_points = math.floor(self.points_n/3)
        compass_array_triangle = [[30, 150, 270],
                                  [330,210,90],
                                  [270, 150, 30],
                                  [90, 210, 330]]
        result = []
        last = self.start
        for direction in compass_array_triangle:
            points = []
            for destination in direction:
                for i in range(1, a_points):
                    p = RESOLUTION_DISTANCE.destination(point=last, bearing=destination)
                    points.append((p.latitude, p.longitude))
                    last = p
                result.append(points)

        return result


def pr(routes: list):
    for r in routes:
        for p in r:
            print(str(p[0]) + "\t" + str(p[1]))
        print("\n\n")


def generate_route(length, lat, lng):
    length = 5000
    lat = 52.403596
    lng = 16.950054
    result = Routes(lat, lng, length).get()
    # result to tablica która leci do mnie
    return result
