import csv
from importlib import resources

def read_population_file(year, variant="Medium"):
    population = {}

    print(f"Reading population data for {year}, {variant} scenario")
    with resources.open_text(
        "_04_csv_file_read", "WPP2019_TotalPopulationBySex.csv"
    ) as fid:
        rows = csv.DictReader(fid)

        # Read data, filter the correct year
        for row in rows:
            if row["Time"] == year and row["Variant"] == variant:
                pop = round(float(row["PopTotal"]) * 1000)
                population[row["Location"]] = pop

    return population

if __name__ == '__main__':
    population = read_population_file('2020')

    for k in population:
        print(k, population[k])
    # the same
    for k, v in population.items():
        print(k, v)