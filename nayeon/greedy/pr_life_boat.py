def solution(people, limit):
    answer = 0
    people.sort()

    start_index = 0
    last_index = len(people) - 1

    while start_index < last_index:
        if people[last_index] + people[start_index] <= limit:
            start_index += 1
            answer += 1
        last_index -= 1

    return len(people) - answer



print(solution([70, 80, 50], 100))
