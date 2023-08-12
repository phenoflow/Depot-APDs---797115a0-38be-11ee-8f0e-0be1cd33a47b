# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2023.

import sys, csv, re

codes = [{"code":"53586020","system":"multilex"},{"code":"58509020","system":"multilex"},{"code":"63123020","system":"multilex"},{"code":"65842020","system":"multilex"},{"code":"89970020","system":"multilex"},{"code":"89974020","system":"multilex"},{"code":"91981020","system":"multilex"},{"code":"91987020","system":"multilex"},{"code":"92204020","system":"multilex"},{"code":"92210020","system":"multilex"},{"code":"92212020","system":"multilex"},{"code":"92216020","system":"multilex"},{"code":"99841020","system":"multilex"},{"code":"99847020","system":"multilex"},{"code":"99849020","system":"multilex"},{"code":"99855020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depot-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depot-apds-150mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depot-apds-150mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depot-apds-150mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
