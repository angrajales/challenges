import sys
import http.client
import json
import time

def get_values_from_external_source(source_host = ''):
    conn = http.client.HTTPSConnection(source_host, 443, timeout=10)
    conn.request('GET', '/')
    res = conn.getresponse()
    dict_json = json.loads(res.read())
    return dict_json['values']

def solve(values, total_inches):
    count = {}
    results = []
    for value in values:
        h_inchs = float(value['h_in'])
        complete_name = " ".join([value['first_name'], value['last_name']])
        if (total_inches - h_inchs) in count:
            for single_value in count[(total_inches - h_inchs)]:
                results.append((complete_name, single_value))
        if h_inchs in count:
            count[h_inchs].append(complete_name)
        else:
            count[h_inchs] = [complete_name]
    return results

def solve_problem(values = {}, total_inches = 0):
    results = solve(values, total_inches)
    if len(results) == 0:
        print("No matches found")
    else:
        for match in results:
            print(match[0], match[1])

if __name__ == "__main__":
    SOURCE_HOST = 'mach-eight.uc.r.appspot.com'
    args = sys.argv
    if len(args) != 2:
        raise ValueError("Please execute the command in the following way: ./main.py <total_inches>")
    total_inches = float(args[1])
    values = get_values_from_external_source(SOURCE_HOST)
    solve_problem(values, total_inches)