from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    p = prerequisites

    if not p:
        return [i for i in range(numCourses)]

    graph = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}

    for parent, child in p:
        graph[parent].append(child)
        in_degree[child] += 1

    queue = []

    for key, val in in_degree.items():
        if val == 0:
            queue.append(key)

    sorted_courses = []

    while queue:
        course = queue.pop(0)
        sorted_courses.append(course)

        for child in graph[course]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    if len(sorted_courses) == numCourses:
        return sorted_courses[::-1]
    else:
        return []