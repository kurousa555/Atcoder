import statistics

N = int(input())
polls = [input() for _ in range(N)]
mode = statistics.mode(polls)

print(mode)

# from collections import defaultdict
# N = int(input())
# polls = defaultdict(list)
# for _ in range(N):
#     S = input()
#     polls[S].append(1)

# for poll in polls.keys():
#     polls[poll] = len(polls[poll])

# max_poll = max(polls.values())
# # print(max_poll)

# new_poll = [poll for poll in polls if polls[poll]==max_poll]
# new_poll.sort()
# for poll in new_poll:
#     print(poll)

