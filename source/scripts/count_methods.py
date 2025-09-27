import os
import csv
import json

subjects_res = os.listdir("../generated/")
subjects_dev = os.listdir("../../results/RQ2/Developer-Provided-Spec/")

results = {}

csv_name = "results/endpoint_methods.csv"


# respector-generated
for subject in subjects_res:
  with open(f"../generated/{subject}", 'r') as f:
    s = json.load(f)
  count_res = 0
  for path in s["paths"].keys():
    amt = len(s["paths"][path])
    count_res = count_res + amt
  subject_name = subject.split(".")[0]
  results.setdefault(subject_name, {})["count_res"] = count_res

count_os = 0

# dev
for subject in subjects_dev:
  with open(f"../../results/RQ2/Developer-Provided-Spec/{subject}", 'r') as f:
    s = json.load(f)
  count_dev = 0
  for path in s["paths"].keys():
    amt = len(s["paths"][path])
    if subject.startswith("ohsome"):
      count_os = count_os + amt
    else:
      count_dev = count_dev + amt
  subject_name = subject.split("-")[0].split(".")[0]
  if subject.startswith("ohsome"):
    results.setdefault("ohsome", {})["count_dev"] = count_os   
  else:
    results.setdefault(subject_name, {})["count_dev"] = count_dev

with open(csv_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["subject_name", "count_res", "count_dev"])
    for subject, counts in results.items():
        writer.writerow([
            subject,
            counts.get("count_res", 0),
            counts.get("count_dev", 0)
        ])
  
print(f"Result saved in {csv_name}")
