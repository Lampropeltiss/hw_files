def join_files(file_names):
    sorted_file_list = sort_files(file_names)
    with open('result_file.txt', 'w', encoding='utf-8') as result_file:
        for file_name, length in sorted_file_list:
            print(file_name, file=result_file)
            print(str(length), file=result_file)
            with open(file_name, 'r', encoding='utf-8') as file:
                result_file.writelines(file.readlines())
                result_file.write('\n')


def sort_files(file_names):
    file_lengths = {}
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
            file_lengths.update({file_name: len(data)})
    return sorted(file_lengths.items(), key=lambda item: item[1])


file_list = ['1.txt', '2.txt', '3.txt']
join_files(file_list)
