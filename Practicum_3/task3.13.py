N = int(input())
C = int(input())
record_num = int(input())

records_per_page = N * C
page_num = (record_num - 1) // records_per_page + 1
column_num = ((record_num - 1) // N) % C + 1
row_number_in_column = (record_num - 1) % N + 1

print(f'страница {page_num} столбец {column_num} строка {row_number_in_column}')