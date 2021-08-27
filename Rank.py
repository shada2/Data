import xlrd # to read xlsx
import csv
xlsx_file = "torank2.xlsx"



def main():
    # load xlsx
    print ("Loading XLSX file:", xlsx_file)
    workbook = xlrd.open_workbook(xlsx_file)
    worksheet_1 = workbook.sheet_by_index(0)

    header_list=[]
    general_dict={}
    print ("Generating headers and dataset")
    # build header list and general dicctionary
    for x in range(worksheet_1.nrows):
        if x <= 4:
            header_list.append(worksheet_1.row_values(x))
        else:
            temp_list = worksheet_1.row_values(x)
            del temp_list[0]
            general_dict[worksheet_1.row_values(x)[0]] = temp_list

    print ("Sorting elements")
    sorted_elements = sort_elements(header_list,general_dict)
    build_csv(header_list,sorted_elements)

def build_csv(header_list,sorted_elements):
    new_dict={}
    max_leng=len(sorted_elements[0])
    counter=0
    while counter <= max_leng-1:
        main_data=[]
        for x in range(len(sorted_elements)):
            descripcion=sorted_elements[x][counter][0]
            value=sorted_elements[x][counter][1]
            main_data.append(descripcion)
            main_data.append(value)
            main_data.append("")

        new_dict[counter]=main_data
        counter+=1
        main_data=[]

    #build header
    new_header=[]
    for elem in header_list:
        temp_subheader=[]
        for x in range(len(elem)):
            if x == 0:
                temp_subheader.append(elem[x])
            else:
                temp_subheader.append(elem[x])
                temp_subheader.append("")
                temp_subheader.append("")

        new_header.append(temp_subheader)

    #Name	Ead (KBT)
    sub_header=[]
    for x in range(len(new_header[0])):
        sub_header.append("Name")
        sub_header.append("Ead (KBT)")
        sub_header.append("")

    sub_header=sub_header[0:len(new_header[0])-1]
    # generate csv
    with open("output.csv", 'w', newline='', encoding='utf-8') as f:
        write = csv.writer(f)
        for elem in new_header:
            write.writerow(elem)
        write.writerow(sub_header)
        for key, value in new_dict.items():
            write.writerow(value)
    print ("File output.csv generated")

def sort_elements(list_to_sort,general_dict):
    main_list=[]
    for x in range(len(list_to_sort[0])-1):
        tempt_dict={}
        counter=0
        for key, value in general_dict.items():
            tempt_dict[key] = value[x]
            counter+=1

        sorted_tuples = sorted(tempt_dict.items(), key=lambda item: item[1])
        main_list.append(sorted_tuples)

    return main_list

if __name__ == '__main__':
    main()
