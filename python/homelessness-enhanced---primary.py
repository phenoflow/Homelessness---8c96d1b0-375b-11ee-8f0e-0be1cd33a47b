# Nanjo, A.,Banerjee A., 2023.

import sys, csv, re

codes = [{"code":"9k6..00","system":"readv2"},{"code":"9k60.00","system":"readv2"},{"code":"67112","system":"med"},{"code":"96605","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('homelessness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["homelessness-enhanced---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["homelessness-enhanced---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["homelessness-enhanced---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
