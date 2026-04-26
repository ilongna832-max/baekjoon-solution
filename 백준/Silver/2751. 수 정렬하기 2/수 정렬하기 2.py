import sys
input=sys.stdin.readline
answer=[int(input()) for _ in range(int(input()))]
answer.sort()
sys.stdout.write('\n'.join(map(str,answer))+'\n')