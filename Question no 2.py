def min_shots(heights):
    max_height = -1
    shots = 0

    for height in heights:
        if height > max_height:
            shots += 1
            max_height = height

    return shots - 1

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        heights = list(map(int, input().split()))
        result = min_shots(heights)
        print(result)

if __name__ == "__main__":
    main()