from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    meeting_rooms = []

    for start, end in intervals:
        if not meeting_rooms:
            meeting_rooms.append(end)
        else:
            if start >= meeting_rooms[0]:
                meeting_rooms[0] = end
            else:
                meeting_rooms.append(end)
            meeting_rooms.sort()

    return len(meeting_rooms)


print(minMeetingRooms([[5,8],[6,8]]))