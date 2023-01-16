def main():
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))
    C = Counter()  # C[x]: 今までxが何回出現したか

    ans = 0
    for j in range(N):
        print(ans,j,C,A[j],C[A[j]])
        ans += j - C[A[j]]  # j=0 から数えているので、今まで見た整数はj個です
        C[A[j]] += 1  # A[j]の出現回数を1増やします
    print(ans)


if __name__ == '__main__':
    main()
