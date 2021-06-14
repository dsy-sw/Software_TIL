package game

class Player{
    var name = "mardrigal"      // 맴버 변수는 반드시 초기화가 돼야함
        get() = field.capitalize()
        set(value) {
            field = value.trim()
        }
    fun castFireball(numFireballs: Int=2) =
        println("한 덩어리의 파이어볼이 나타난다. (x$numFireballs)")
}