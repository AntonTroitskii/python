import csv
from importlib import resources

import matplotlib.pyplot as plt

class _Population:
    def __init__(self):
        """Read the population file"""
        self.data = {}
        self.variant = "Medium"

        print(f"Reading population data for {self.variant} scenario")
        with resources.open_text(
            "_04_csv_file_read", "WPP2019_TotalPopulationBySex.csv"
        ) as fid:
            rows = csv.DictReader(fid)

            # Read data, filter the correct variant
            for row in rows:
                if int(row["LocID"]) >= 900 or row["Variant"] != self.variant:
                    continue

                country = self.data.setdefault(row["Location"], {})
                population = float(row["PopTotal"]) * 1000
                country[int(row["Time"])] = round(population)

    def get_country(self, country):
        """Get population data for one country"""
        data = self.data[country]
        years, population = zip(*data.items())
        return years, population

    def plot_country(self, country):
        """Plot data for one country, population in millions"""
        years, population = self.get_country(country)
        plt.plot(years, [p / 1e6 for p in population], label=country)

    def order_countries(self, year):
        """Sort countries by population in decreasing order"""
        countries = {c: self.data[c][year] for c in self.data}
        return sorted(countries, key=lambda c: countries[c], reverse=True)

# Instantiate the Singleton
data = _Population()

for country in data.order_countries(2050)[:5]:
    data.plot_country(country)

plt.legend()
plt.xlabel("Year")
plt.ylabel("Population [Millions]")
plt.title("UN Population Projections")
plt.show()