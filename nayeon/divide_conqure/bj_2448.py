import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
stars = [[' '] * 2 * n for _ in range(n)]


def recur(x, y, z):
    if z == 3:
        stars[x][y] = '*'
        stars[x + 1][y - (z // 2)] = '*'
        stars[x + 1][y + (z // 2)] = '*'
        for k in range(-2, 3):
            stars[x + 2][y + k] = '*'
    else:
        nz = z // 2
        recur(x, y, nz)
        recur(x + nz, y - nz, nz)
        recur(x + nz, y + nz, nz)


recur(0, (2 * n - 1) // 2, n)

for s in stars:
    # print("".join(map(str, s)))
    print("".join(s))

"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
첫째 줄에 N이 주어진다. N은 항상 3×2^k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)
24

                       *
                      * *
                     *****
                    *     *
                   * *   * *
                  ***** *****
                 *           *
                * *         * *
               *****       *****
              *     *     *     *
             * *   * *   * *   * *
            ***** ***** ***** *****
           *                       *
          * *                     * *
         *****                   *****
        *     *                 *     *
       * *   * *               * *   * *
      ***** *****             ***** *****
     *           *           *           *
    * *         * *         * *         * *
   *****       *****       *****       *****
  *     *     *     *     *     *     *     *
 * *   * *   * *   * *   * *   * *   * *   * *
***** ***** ***** ***** ***** ***** ***** *****
"""
