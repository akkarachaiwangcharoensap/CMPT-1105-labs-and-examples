def getMyCourseInfo (courseNumber):
    rooms = {
            'CS101': 3004,
            'CS102': 4501,
            'CS103': 6755,
            'NT110': 1244,
            'CM241': 1411
    }

    instructors = {
            'CS101': 'Haynes',
            'CS102': 'Alvarado',
            'CS103': 'Rich',
            'NT110': 'Burke',
            'CM241': 'Lee'
    }

    times = {
            'CS101': '8:00 a.m',
            'CS102': '9:00 a.m',
            'CS103': '10:00 a.m',
            'NT110': '11:00 a.m',
            'CM241': '1:00 p.m'
    }

    return 'You selected: ' + str(courseNumber) + '\n' + 'Room: ' + str(rooms[courseNumber])+ '\n' + 'Instructor: ' + str(instructors[courseNumber]) + '\n' + 'Time: ' + times[courseNumber] + '\n'

courseNumber = input("Please enter a course number")

print(getMyCourseInfo(courseNumber))
