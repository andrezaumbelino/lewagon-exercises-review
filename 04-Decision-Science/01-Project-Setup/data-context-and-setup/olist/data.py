import os
import pandas as pd


class Olist:

    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities

        base_path = os.path.dirname(__file__)
        csv_path = os.path.join(base_path, "..","data", "csv")

        file_names = []
        for f in os.listdir(csv_path):
            if f.endswith(".csv"):
                file_names.append(f)

        key_names = []
        for file in file_names:
            name = file.replace("_dataset.csv", "")  # Remover sufixo "_dataset.csv"
            name = name.replace(".csv", "")  # Remover sufixo ".csv" (caso exista)
            name = name.replace("olist_", "")  # Remover prefixo "olist_"
            key_names.append(name)

        data = {}

        for name, file in zip(key_names, file_names):
            data[name] = pd.read_csv(os.path.join(csv_path, file))

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
