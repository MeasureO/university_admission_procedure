import pprint
n = int(input())

with open("applicants.txt", 'r') as f, open("test.txt", 'w') as test:
    lines = [i.strip().split() for i in f.readlines()]
    for item in lines:
        item[0] += ' ' + item[1]
        item.remove(item[1])
    # print(lines)
    lines.sort(key=lambda x: x[0])
    for line in lines:
        print(line, file=test)
applicants = {"Physics": [], "Engineering": [], "Mathematics": [], "Biotech": [], "Chemistry": []}
applied = set()
scores_ind = {"Physics": 1, "Biotech": 2, "Chemistry": 2, "Mathematics": 3, "Engineering": 4}

for j in range(6, 9):
    for faculty in applicants.keys():
        if faculty == "Physics":
            faculty_list = sorted([i for i in lines if i[j] == faculty], key=lambda x: - max((float(x[1]) + float(x[3])) / 2, float(x[5])))
        elif faculty == "Chemistry":
            faculty_list = sorted([i for i in lines if i[j] == faculty], key=lambda x: -max(float(x[2]), float(x[5])))
        elif faculty == "Mathematics":
            faculty_list = sorted([i for i in lines if i[j] == faculty], key=lambda x: -max(float(x[3]), float(x[5])))
        elif faculty == "Engineering":
            faculty_list = sorted([i for i in lines if i[j] == faculty], key=lambda x: -max((float(x[3]) + float(x[4])) / 2, float(x[5])))
        elif faculty == "Biotech":
            faculty_list = sorted([i for i in lines if i[j] == faculty], key=lambda x: -max((float(x[1]) + float(x[2])) / 2, float(x[5])))
        for app in faculty_list:
            if len(applicants[app[j]]) < n and tuple(app) not in applied:
                applicants[app[j]].append(app)
                applied.add(tuple(app))
for faculty in sorted(applicants.keys()):
    # print(faculty)
    with open(f"{faculty.lower()}.txt", 'w') as f:
        print(file=f)
        if faculty == "Mathematics" or faculty == "Chemistry":
            for elem in sorted(applicants[faculty], key=lambda x: (-max(float(x[scores_ind[faculty]]), float(x[5])), x[0])):
                print(elem[0], max(elem[scores_ind[faculty]], elem[5]), file=f)
        elif faculty == "Physics":
            for elem in sorted(applicants[faculty], key=lambda x: (-max((float(x[1]) + float(x[3])) / 2, float(x[5])), x[0])):
                print(elem[0], max((float(elem[1]) + float(elem[3])) / 2, float(elem[5])), file=f)
        elif faculty == "Biotech":
            for elem in sorted(applicants[faculty], key=lambda x: (-max((float(x[1]) + float(x[2])) / 2, float(x[5])), x[0])):
                print(elem[0], max((float(elem[1]) + float(elem[2])) / 2, float(elem[5])), file=f)
        elif faculty == "Engineering":
            for elem in sorted(applicants[faculty], key=lambda x: (-max((float(x[3]) + float(x[4])) / 2, float(x[5])), x[0])):
                print(elem[0], max((float(elem[3]) + float(elem[4])) / 2, float(elem[5])), file=f)

        # for elem in sorted(applicants[faculty], key=lambda x: (-float(x[scores_ind[faculty]]), x[0])):
        #     print(elem[0], elem[scores_ind[faculty]])
    # 1st iteration
    # for faculty in applicants.keys():
    #     faculty_list = sorted([i for i in lines if i[5] == faculty], key=lambda x: -float(x[scores_ind[faculty]]))
    #     for app in faculty_list:
    #         if len(applicants[app[5]]) < n and tuple(app) not in applied:
    #             applicants[app[5]].append(app)
    #             applied.add(tuple(app))
    # # 2nd iteration
    # for faculty in applicants.keys():
    #     faculty_list = sorted([i for i in lines if i[6] == faculty], key=lambda x: -float(x[scores_ind[faculty]]))
    #     for app in faculty_list:
    #         if len(applicants[app[6]]) < n and tuple(app) not in applied:
    #             applicants[app[6]].append(app)
    #             if tuple(app) not in applied:
    #                 applied.add(tuple(app))
    # # 3rd iteration
    # for faculty in applicants.keys():
    #     faculty_list = sorted([i for i in lines if i[7] == faculty], key=lambda x: -float(x[scores_ind[faculty]]))
    #     for app in faculty_list:
    #         if len(applicants[app[7]]) < n and tuple(app) not in applied:
    #             applicants[app[7]].append(app)
    #             if tuple(app) not in applied:
    #                 applied.add(tuple(app))
    # old output
    # for faculty in sorted(applicants.keys()):
    #     print(faculty)
    #     for elem in sorted(applicants[faculty], key=lambda x: (-float(x[scores_ind[faculty]]), x[0])):
    #         print(elem[0], elem[scores_ind[faculty]])

