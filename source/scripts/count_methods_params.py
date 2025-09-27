import os
import csv
import json

subjects_res = os.listdir("../generated/")
subjects_dev = os.listdir("../../results/RQ2/Developer-Provided-Spec/")

excluded = ('gravitee', 'ocvn')

results = {}

csv_name = "results/endpoint_params.csv"


# respector-generated
for subject in subjects_res:
    if subject.startswith(excluded):
        continue
    with open(f"../generated/{subject}", 'r') as f:
        s = json.load(f)
    count_params_res = 0
    for path, methods in s["paths"].items():
        for method, details in methods.items():
            if "parameters" not in details:
                continue
            count_params_res += len(details["parameters"])
    subject_name = subject.split(".")[0]
    results.setdefault(subject_name, {})["count_params_res"] = count_params_res
    # print(f"{subject_name} params: {count_params_res}")

# dev
count_os = 0
for subject in subjects_dev:
    if subject.startswith(excluded):
        continue
    with open(f"../../results/RQ2/Developer-Provided-Spec/{subject}", 'r') as f:
        s = json.load(f)
        
    count_params_dev = 0

    for path, methods in s["paths"].items():
        for method, details in methods.items():
            if "parameters" not in details:
                continue
            count_params_dev += len(details["parameters"])

    subject_name = subject.split("-")[0].split(".")[0]

    if subject.startswith("ohsome"):
        count_os += count_params_dev
        results.setdefault(subject_name, {})["count_params_dev"] = count_os
    else:
        results.setdefault(subject_name, {})["count_params_dev"] = count_params_dev


with open(csv_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["subject_name", "count_params_res", "count_params_dev"])
    for subject, counts in results.items():
        writer.writerow([
            subject,
            counts.get("count_params_res", 0),
            counts.get("count_params_dev", 0)
        ])
  
print(f"Result saved in {csv_name}")
