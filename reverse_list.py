def sort_by_filesize(dictionary):
    def convert_filesize_to_float(filesize):
        suffixes = {'KB': 1e-6, 'MB': 1e-3, 'GB': 1, 'TB': 1e3, 'PB': 1e6}
        if filesize[-2:] in suffixes:
            return float(filesize[:-2]) * suffixes[filesize[-2:]]
        else:
            return float(filesize)
    
    items = list(dictionary.items())
    items.sort(key=lambda x: convert_filesize_to_float(x[1]), reverse=True)
    return {k: v for k, v in items}

file_size_dict = {"birthday": "3.23TB", "vacation": "5000KB", "wedding": "2PB", "something": "2.3KB", "graduation": "4.5GB", "road_trip": "1.8GB", "family_reunion": "2.7GB"}

ordered_dict = sort_by_filesize(file_size_dict)

for k, v in ordered_dict.items():
    print(k + ": " + v)