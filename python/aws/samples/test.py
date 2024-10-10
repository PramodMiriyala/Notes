query = ("['ap-south-1b']", "['i-016a0b5ae17607811']")
if __name__ == '__main__':
    region_list = query[0].strip("'[]'").split(",")
    id_list = query[1].strip("'[]'").split(",")
    for region in region_list:
        for index in id_list:
            print(f"{region}:{index}")