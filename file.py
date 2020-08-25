import csv


def make_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow([*jobs[0].keys()])
    for job in jobs:
        writer.writerow([*job.values()])
