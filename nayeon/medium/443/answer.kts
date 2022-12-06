package medium.`443`

class Solution {
    /*
    * compress method 는 아래 제한을 만족하지 못하므로 통과할 수 없음.
    * You must write an algorithm that uses only constant extra space.
    * */
    fun compress(chars: CharArray): Int {
        if (chars.size == 1) return 1

        println("test: ${chars.toList().groupingBy { it }.eachCount()}")
        val set = chars.toList().groupingBy { it }.eachCount()
        return set.size +  set.values.map { it.toString()}.count()
    }

    fun compress2(chars: CharArray): Int {
        var idx = 0
        val answer = mutableListOf<Char>()
        while (idx < chars.size) {
            var count = 1
            while (idx < chars.size -1
                && chars[idx] == chars[idx + 1]) {
                println("$idx, ${chars[idx]} , $count")
                idx++
                count++
            }
            answer.add(chars[idx])
            if(count > 1) answer.add(count.toString().count().digitToChar())

            println(answer.toString())
            idx++
        }

        return answer.size
    }
}

fun main() {
    val q = charArrayOf('a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c')
    val answer = Solution().compress2(q)
    println("answer: $answer")
}

main()
