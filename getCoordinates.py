import pandas as pd


class GetCoordinates:
    def __init__(self, path:  str):
        self.dataFrame = pd.read_csv(path)


    def get_coordinates(self):
        coordinate_columns = [x_y for x_y in self.dataFrame.columns if "lat" in x_y or "lon" in x_y]
        coordinates = [(lat, long) for lat, long in self.dataFrame[coordinate_columns].values]
        return coordinates

#
# if __name__ == "__main__":
#     g_coordinates = GetCoordinates("Stops.csv")
#     print(g_coordinates.get_coordinates())