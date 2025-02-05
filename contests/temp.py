def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of clocks
        a = list(map(int, input().split()))  # Initial times of the clocks

        # Find the minimum initial time
        min_a = min(a)
        # Find all indices where the initial time equals the minimum
        min_indices = [i for i in range(n) if a[i] == min_a]

        possible = False
        # Check each candidate pivot clock
        for i in min_indices:
            # Calculate the maximum distance from this pivot to either end
            left_distance = i  # Distance to the leftmost clock
            right_distance = n - 1 - i  # Distance to the rightmost clock
            max_distance = max(left_distance, right_distance)

            # Check if the pivot clock can reset itself in time
            if min_a > max_distance:
                # Now check if all other clocks can be reset in time
                valid = True
                for j in range(n):
                    if a[j] <= abs(j - i):
                        valid = False
                        break
                if valid:
                    possible = True
                    break

        # Output the result for this test case
        print("YES" if possible else "NO")

# Call the solve function
solve()