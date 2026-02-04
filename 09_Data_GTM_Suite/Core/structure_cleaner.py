import pandas as pd

class StructureCleaner:
    def __init__(self, dataframe):
        self.df = dataframe

    def remove_duplicates(self, subset_col=None):
        initial = len(self.df)
        self.df = self.df.drop_duplicates(subset=subset_col)
        print(f"🧹 [DCE] Duplicados eliminados: {initial - len(self.df)}")
        return self.df