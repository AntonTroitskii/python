import re
from pathlib import Path
from ge_ct_protocol_name import ANATOMY_PATTERN

EXAM_DOSE_SETTINGS = 'Exam Dose Settings'
SCAN_SETTINGS = 'Scan Settings'

SERIES_AXIAL = r'^Series \d+,Axial'
SERIES_SCAN_SETTINGS = r'^Series \d+ Group \d+ Scan Settings'
SERIES_RECON_SETTINGS = r'^Series \d+ Group \d+ Recon \d Settings'

SERIES = 'series'
ID = 'id'
TYPE = 'type'
RECON = 'recons'

PROTOCOL_NAME = ANATOMY_PATTERN


def read_params_in_line(line):
    if line[-1] == ',':
        res = line[:-1].split(sep=',')
    else:
        res = line.split(sep=',')

    return res


def save_protocols_names(file_path, exams: dict):
    lines = []
    for name in exams.keys():
        lines.append(name)

    with open(file_path, 'w', encoding='utf8') as output_file:
        output_file.writelines('\n'.join(lines))


def read_exams(protocols_path):
    with open(protocols_path, 'r') as file:
        lines = file.readlines()

    exams = {}

    for i in range(0, len(lines)):

        line = lines[i]

        if bool(re.match(PROTOCOL_NAME, line)):

            name = line
            name = name.strip('\n')
            exams[name] = {}
            exams[name][SERIES] = []
        else:
            if EXAM_DOSE_SETTINGS in line:
                i += 1
                line = lines[i]
                param = read_params_in_line(line)

                i += 1
                line = lines[i]
                vals = read_params_in_line(line)

                exams[name][EXAM_DOSE_SETTINGS] = dict(zip(param, vals))
                i += 1

            if bool(re.match(SERIES_AXIAL, line)):
                line = lines[i]
                param_series = read_params_in_line(line)

                if param_series[1] == 'Axial':
                    series_item = {}
                    series_item[ID] = param_series[0]
                    series_item[TYPE] = param_series[1]
                    series_item[RECON] = []
                    exams[name][SERIES].append(series_item)

                    i += 1

            if bool(re.match(SERIES_SCAN_SETTINGS, line)):
                i += 1
                line = lines[i]
                param = read_params_in_line(line)

                i += 1
                line = lines[i]
                vals = read_params_in_line(line)

                series_item[SCAN_SETTINGS] = dict(zip(param, vals))

            if bool(re.match(SERIES_RECON_SETTINGS, line)):
                i += 1
                line = lines[i]
                param = read_params_in_line(line)

                i += 1
                line = lines[i]
                vals = read_params_in_line(line)

                series_item[RECON].append(dict(zip(param, vals)))

    return exams
