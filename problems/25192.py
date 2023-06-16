import sys
input = sys.stdin.readline

chatting = set()
count = 0

N = int(input())
for i in range(N):
    chat = input().rstrip()
    if chat == 'ENTER':
        if chatting:
            count += len(chatting)
            chatting = set()
    else:
        chatting.add(chat)
if chatting:
    count += len(chatting)

print(count)