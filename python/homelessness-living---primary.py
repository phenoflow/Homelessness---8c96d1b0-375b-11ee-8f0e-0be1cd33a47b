# Nanjo, A.,Banerjee A., 2023.

import sys, csv, re

codes = [{"code":"13F9.00","system":"readv2"},{"code":"13FA.00","system":"readv2"},{"code":"13FL.00","system":"readv2"},{"code":"13FW.00","system":"readv2"},{"code":"31951","system":"med"},{"code":"34506","system":"med"},{"code":"35716","system":"med"},{"code":"70848","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('homelessness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["homelessness-living---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["homelessness-living---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["homelessness-living---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
