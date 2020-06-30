from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    p = prerequisites

    if not p:
        return True

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

    return len(sorted_courses) == numCourses
