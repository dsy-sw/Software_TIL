open class TownSquare : Room("Town Square") {
    private val bellSound = "댕댕"
    override  val dangerLevel = super.dangerLevel -3
    override fun load() = "당신의 참여를 주민들이 다 함께 환영합니다." +
            ringBell()
   private fun ringBell() = "당신의 도착을 알립니다. $bellSound"
}

fun printRoomInfo(room: Room) {
    println(room.description())
    println(room.load())
}

fun main() {
    // TownSquatr 클래스를 상속하여 자식 정의. 그리고 인스턴스를 생성해서 리턴
    // 중요도 ***
    val test = object: TownSquare() {
        override fun load() = "새로운 로드입니다."
    }
    println(test.load())
    println(test.description())
}